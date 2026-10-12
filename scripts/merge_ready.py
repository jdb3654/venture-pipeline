"""Check whether a PR in this repository is ready to merge.

    python scripts/merge_ready.py <pr>                  report; exit 0 if ready
    python scripts/merge_ready.py <pr> --request        ask Codex to review the latest commit if it hasn't
    python scripts/merge_ready.py <pr> --wait 600       poll every 30s, up to 600s, until ready or failed
    python scripts/merge_ready.py <pr> --final          after two Codex rounds: request one last pass
                                                        (waits up to 600s, or --wait); only its new
                                                        P0/P1 findings block. Each lower finding gets
                                                        a follow-up issue, a reply and a resolved thread.

Ready means: PR open and mergeable; CI on the head commit finished green;
Codex finished reviewing the head commit (it does not re-review new pushes
on its own); and no review thread is unresolved. Also reports the number of
Codex review rounds, for the two-round limit in AGENTS.md.

Needs the GitHub CLI (`gh`), authenticated. Standard library only.
"""
import json
import re
import subprocess
import sys
import time
from datetime import datetime

import gh_rest

REPO = "jdb3654/venture-pipeline"
CODEX = "chatgpt-codex-connector[bot]"
SUMMARY = "codex-pull-request-review-summary"


def gh(path, method="GET", fields=None):
    cmd = ["gh", "api", "-X", method, path]
    for key, value in (fields or {}).items():
        cmd += ["-f", "%s=%s" % (key, value)]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        raise RuntimeError(out.stderr.strip() or out.stdout.strip())
    return json.loads(out.stdout) if out.stdout.strip() else None


def review_threads(n):
    """List review threads as {"resolved": bool, "comment_ids": [...]}. Claude Code
    sessions can't use GraphQL and have a REST route instead; elsewhere (Codex,
    a laptop) GraphQL works."""
    try:
        threads = gh("repos/%s/pulls/%d/ccr/review_threads" % (REPO, n))
        return [{"resolved": bool(t.get("resolved")), "comment_ids": t.get("comment_ids", [])}
                for t in threads]
    except (RuntimeError, TypeError):
        owner, name = REPO.split("/")
        query = ("query{repository(owner:\"%s\",name:\"%s\"){pullRequest(number:%d)"
                 "{reviewThreads(first:100){nodes{isResolved comments(first:100)"
                 "{nodes{databaseId}}}}}}}" % (owner, name, n))
        data = gh("graphql", "POST", {"query": query})
        nodes = data["data"]["repository"]["pullRequest"]["reviewThreads"]["nodes"]
        return [{"resolved": t["isResolved"],
                 "comment_ids": [c["databaseId"] for c in t["comments"]["nodes"]]}
                for t in nodes]


def unresolved_threads(n):
    return sum(1 for t in review_threads(n) if not t["resolved"])


def issue_comments(n):
    return gh("repos/%s/issues/%d/comments?per_page=100" % (REPO, n))


def codex_summary(n):
    """Return (state, reviewed_commit, completed_at) from Codex's summary comment.
    Codex edits one summary comment per PR; completed_at is when the latest review finished."""
    bot = [c["body"] for c in issue_comments(n) if c["user"]["login"] == CODEX]
    summaries = [b for b in bot if SUMMARY in b]
    if not summaries:
        if any("create an environment" in b for b in bot):
            return "no-environment", None, None
        return None, None, None
    body = summaries[-1]
    state = "running" if "Running" in body else "completed" if "Completed" in body else "unknown"
    sha = re.search(r"`([0-9a-f]{7,40})`", body)
    done = re.search(r'Completed\*\*\s*<relative-time datetime="([^"]+)"', body)
    return state, sha.group(1) if sha else None, when(done.group(1)) if done else None


def codex_status(n, head):
    """Return (state, reviewed_commit) from Codex's summary comment, or (None, None)."""
    return codex_summary(n)[:2]


def when(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def check(n):
    pr = gh("repos/%s/pulls/%d" % (REPO, n))
    head = pr["head"]["sha"]
    problems = []
    if pr["state"] != "open":
        problems.append("PR is %s" % pr["state"])
    if pr.get("mergeable_state") not in ("clean", "unstable", "has_hooks"):
        problems.append("not mergeable (%s)" % pr.get("mergeable_state"))

    runs = gh("repos/%s/commits/%s/check-runs" % (REPO, head))["check_runs"]
    pending = [r["name"] for r in runs if r["status"] != "completed"]
    failed = [r["name"] for r in runs if r["status"] == "completed"
              and r["conclusion"] not in ("success", "skipped", "neutral")]
    if pending:
        problems.append("CI still running: " + ", ".join(pending))
    if failed:
        problems.append("CI failed: " + ", ".join(failed))

    state, reviewed = codex_status(n, head)
    if state == "no-environment":
        problems.append("Codex can't review: no Codex environment for this repo. "
                        "The owner must create one in Codex settings, then comment @codex review")
    elif state is None:
        problems.append("no Codex review yet")
    elif state == "running":
        problems.append("Codex review still running")
    elif not reviewed or not head.startswith(reviewed):
        problems.append("Codex last reviewed %s, not the head %s (use --request)"
                        % (reviewed, head[:7]))

    threads = unresolved_threads(n)
    if threads:
        problems.append("%d unresolved review thread(s)" % threads)

    rounds = len({r["commit_id"] for r in gh("repos/%s/pulls/%d/reviews?per_page=100" % (REPO, n))
                  if r["user"]["login"] == CODEX})
    return head, state, reviewed, problems, rounds


BLOCKING = ("P0", "P1")
MARKER = "merge_ready --final"


def priority(body):
    m = re.search(r"badge/(P\d)", body or "")
    return m.group(1) if m else None


def finding_title(body):
    first = (body or "").strip().splitlines()[0] if (body or "").strip() else ""
    m = re.search(r"</sub></sub>\s*(.+?)\*\*", first)
    return (m.group(1) if m else re.sub(r"[*<>]", "", first)).strip()[:80] or "Codex finding"


def final_triage(n, head, branch, since):
    """For Codex findings posted since the final request: leave P0/P1 open (blocking); for each
    lower one, open a follow-up issue, reply with its number and resolve the thread.
    Returns the blocking findings as (title, url)."""
    comments = gh("repos/%s/pulls/%d/comments?per_page=100" % (REPO, n))
    by_id = {c["id"]: c for c in comments}
    agent = "agent:codex" if branch.startswith("codex/") else "agent:claude"
    blocking = []
    for t in review_threads(n):
        if t["resolved"] or not t["comment_ids"]:
            continue
        root = by_id.get(t["comment_ids"][0])
        if not root or root["user"]["login"] != CODEX or when(root["created_at"]) < since:
            continue  # not a finding from this pass; the unresolved-thread check covers it
        level = priority(root["body"])
        title = finding_title(root["body"])
        if level in BLOCKING or level is None:
            blocking.append(("%s %s" % (level or "unlabelled", title), root["html_url"]))
            continue
        filed = [by_id[i]["body"] for i in t["comment_ids"][1:]
                 if i in by_id and MARKER in by_id[i]["body"]]
        if not filed:
            issue = gh_rest.issue_create(
                "Follow-up from #%d: %s" % (n, title),
                "Non-blocking %s finding from Codex's final review of #%d (commit `%s`), "
                "moved here by `%s` under the two-round limit in AGENTS.md.\n\n"
                "Finding: %s\n\n> %s" % (level, n, head[:7], MARKER, root["html_url"],
                                          root["body"].strip().replace("\n", "\n> ")),
                [agent])
            gh_rest.pr_reply(n, root["id"], "Not blocking (%s) under the two-round limit. "
                             "Follow-up: #%d (%s)." % (level, issue["number"], MARKER))
            print("filed #%d for %s finding: %s" % (issue["number"], level, title))
        gh_rest.pr_resolve(n, root["id"])
    return blocking


FINAL_TAG = "<!-- merge_ready --final -->"


def final(n, args, wait):
    head, state, reviewed, problems, rounds = check(n)
    if rounds < 2:
        print("--final is for after two Codex review rounds; this PR has %d. "
              "Use --request instead." % rounds)
        return 2
    if state == "no-environment":
        print("NOT READY:\n- " + "\n- ".join(problems))
        return 1
    # A distinct pass: reuse our last request only if it is still pending, or if it
    # already finished on this head (a re-run to re-check); otherwise ask again.
    requests = [c for c in issue_comments(n) if FINAL_TAG in c["body"]]
    since = when(requests[-1]["created_at"]) if requests else None
    state, sha, done_at = codex_summary(n)
    pending = since and (done_at is None or done_at < since)
    finished_here = since and done_at and done_at >= since and sha and head.startswith(sha)
    if not (pending or finished_here):
        settle = time.time() + 600
        while state == "running" and time.time() < settle:  # let an earlier review finish first
            time.sleep(30)
            state, sha, done_at = codex_summary(n)
        c = gh("repos/%s/issues/%d/comments" % (REPO, n), "POST",
               {"body": "@codex review\n\n" + FINAL_TAG})
        since = when(c["created_at"])
        print("requested final Codex review of %s" % head[:7])
    deadline = time.time() + (wait or 600)
    while True:
        state, sha, done_at = codex_summary(n)
        if state == "completed" and done_at and done_at >= since and sha and head.startswith(sha):
            break
        if time.time() >= deadline:
            print("NOT READY:\n- final Codex review of %s not finished; rerun --final" % head[:7])
            return 1
        time.sleep(30)

    branch = gh("repos/%s/pulls/%d" % (REPO, n))["head"]["ref"]
    blocking = final_triage(n, head, branch, since)
    head, state, reviewed, problems, rounds = check(n)
    print("PR #%d at %s; final Codex pass done (--final)" % (n, head[:7]))
    for title, url in blocking:
        print("blocking: %s %s" % (title, url))
    if problems:
        print("NOT READY:\n- " + "\n- ".join(problems))
        return 1
    print("READY to merge")
    return 0


def main():
    args = sys.argv[1:]
    if not args or not args[0].isdigit():
        print(__doc__)
        return 2
    n = int(args[0])
    wait = int(args[args.index("--wait") + 1]) if "--wait" in args else 0
    if "--final" in args:
        return final(n, args, wait)

    head, state, reviewed, problems, rounds = check(n)
    if "--request" in args and state != "running" and not (reviewed and head.startswith(reviewed)):
        gh("repos/%s/issues/%d/comments" % (REPO, n), "POST", {"body": "@codex review"})
        print("requested Codex review of %s" % head[:7])

    deadline = time.time() + wait
    while problems and time.time() < deadline and all(
            p.startswith(("CI still running", "Codex review still running", "Codex last reviewed",
                          "no Codex review", "not mergeable (unknown)", "not mergeable (None)"))
            for p in problems):
        time.sleep(30)
        head, state, reviewed, problems, rounds = check(n)

    print("PR #%d at %s; Codex review rounds with findings: %d (limit 2, AGENTS.md)"
          % (n, head[:7], rounds))
    if problems:
        print("NOT READY:\n- " + "\n- ".join(problems))
        return 1
    print("READY to merge")
    return 0


if __name__ == "__main__":
    sys.exit(main())
