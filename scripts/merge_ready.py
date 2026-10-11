"""Check whether a PR in this repository is ready to merge.

    python scripts/merge_ready.py <pr>                  report; exit 0 if ready
    python scripts/merge_ready.py <pr> --request        ask Codex to review the latest commit if it hasn't
    python scripts/merge_ready.py <pr> --wait 600       poll every 30s, up to 600s, until ready or failed

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


def unresolved_threads(n):
    """Count unresolved review threads. Claude Code sessions can't use GraphQL
    and have a REST route instead; elsewhere (Codex, a laptop) GraphQL works."""
    try:
        return sum(1 for t in gh("repos/%s/pulls/%d/ccr/review_threads" % (REPO, n))
                   if not t.get("resolved"))
    except (RuntimeError, TypeError):
        owner, name = REPO.split("/")
        query = ("query{repository(owner:\"%s\",name:\"%s\"){pullRequest(number:%d)"
                 "{reviewThreads(first:100){nodes{isResolved}}}}}" % (owner, name, n))
        data = gh("graphql", "POST", {"query": query})
        nodes = data["data"]["repository"]["pullRequest"]["reviewThreads"]["nodes"]
        return sum(1 for t in nodes if not t["isResolved"])


def codex_status(n, head):
    """Return (state, reviewed_commit) from Codex's summary comment, or (None, None)."""
    summaries = [c["body"] for c in gh("repos/%s/issues/%d/comments?per_page=100" % (REPO, n))
                 if c["user"]["login"] == CODEX and SUMMARY in c["body"]]
    if not summaries:
        return None, None
    body = summaries[-1]
    state = "running" if "Running" in body else "completed" if "Completed" in body else "unknown"
    sha = re.search(r"`([0-9a-f]{7,40})`", body)
    return state, sha.group(1) if sha else None


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
    if state is None:
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


def main():
    args = sys.argv[1:]
    if not args or not args[0].isdigit():
        print(__doc__)
        return 2
    n = int(args[0])
    wait = int(args[args.index("--wait") + 1]) if "--wait" in args else 0

    head, state, reviewed, problems, rounds = check(n)
    if "--request" in args and state != "running" and not (reviewed and head.startswith(reviewed)):
        gh("repos/%s/issues/%d/comments" % (REPO, n), "POST", {"body": "@codex review"})
        print("requested Codex review of %s" % head[:7])

    deadline = time.time() + wait
    while problems and time.time() < deadline and all(
            p.startswith(("CI still running", "Codex review still running", "Codex last reviewed",
                          "no Codex review"))
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
