"""GitHub actions through `gh api` REST only, for sessions where gh's
GraphQL-backed commands (issue view/create, pr create) are blocked.

    python scripts/gh_rest.py issue create --title T --body-file F [--label L ...]
    python scripts/gh_rest.py issue comment <n> --body-file F
    python scripts/gh_rest.py pr create --head <branch> --title T --body-file F [--base main]
    python scripts/gh_rest.py pr edit-body <n> --body-file F
    python scripts/gh_rest.py pr reply <n> <comment_id> --body-file F
    python scripts/gh_rest.py pr resolve <n> <comment_id>

--body "text" works anywhere --body-file does. <comment_id> is the review
comment that starts the thread (or any comment in it, for reply). Resolving
uses the Claude Code session route /pulls/<n>/ccr/comments/<id>/resolve and
falls back to GraphQL elsewhere. Needs `gh`, authenticated. Standard library only.
"""
import argparse
import json
import subprocess
import sys

REPO = "jdb3654/venture-pipeline"


def api(path, method="GET", payload=None):
    cmd = ["gh", "api", "-X", method, path]
    if payload is not None:
        cmd += ["--input", "-"]
    out = subprocess.run(cmd, capture_output=True, text=True,
                         input=json.dumps(payload) if payload is not None else None)
    if out.returncode:
        raise RuntimeError(out.stderr.strip() or out.stdout.strip())
    return json.loads(out.stdout) if out.stdout.strip() else None


def issue_create(title, body, labels=()):
    payload = {"title": title, "body": body}
    if labels:
        payload["labels"] = list(labels)
    return api("repos/%s/issues" % REPO, "POST", payload)


def issue_comment(n, body):
    return api("repos/%s/issues/%d/comments" % (REPO, n), "POST", {"body": body})


def pr_create(head, title, body, base="main"):
    return api("repos/%s/pulls" % REPO, "POST",
               {"head": head, "base": base, "title": title, "body": body})


def pr_edit_body(n, body):
    return api("repos/%s/pulls/%d" % (REPO, n), "PATCH", {"body": body})


def pr_reply(n, comment_id, body):
    return api("repos/%s/pulls/%d/comments/%d/replies" % (REPO, n, comment_id), "POST",
               {"body": body})


def pr_resolve(n, comment_id):
    """Resolve the review thread containing comment_id."""
    try:
        return api("repos/%s/pulls/%d/ccr/comments/%d/resolve" % (REPO, n, comment_id), "POST")
    except RuntimeError:
        owner, name = REPO.split("/")
        query = ("query{repository(owner:\"%s\",name:\"%s\"){pullRequest(number:%d)"
                 "{reviewThreads(first:100){nodes{id comments(first:100){nodes{databaseId}}}}}}}"
                 % (owner, name, n))
        threads = api("graphql", "POST", {"query": query})
        nodes = threads["data"]["repository"]["pullRequest"]["reviewThreads"]["nodes"]
        ids = [t["id"] for t in nodes
               if any(c["databaseId"] == comment_id for c in t["comments"]["nodes"])]
        if not ids:
            raise RuntimeError("no review thread contains comment %d" % comment_id)
        mutation = "mutation{resolveReviewThread(input:{threadId:\"%s\"}){thread{isResolved}}}" % ids[0]
        return api("graphql", "POST", {"query": mutation})


def body_of(args):
    if args.body_file:
        with open(args.body_file, encoding="utf-8") as f:
            return f.read()
    return args.body or ""


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    kinds = p.add_subparsers(dest="kind", required=True)

    def with_body(sp, required=True):
        g = sp.add_mutually_exclusive_group(required=required)
        g.add_argument("--body")
        g.add_argument("--body-file")

    issue = kinds.add_parser("issue").add_subparsers(dest="action", required=True)
    sp = issue.add_parser("create")
    sp.add_argument("--title", required=True)
    sp.add_argument("--label", action="append", default=[])
    with_body(sp, required=False)
    sp = issue.add_parser("comment")
    sp.add_argument("n", type=int)
    with_body(sp)

    pr = kinds.add_parser("pr").add_subparsers(dest="action", required=True)
    sp = pr.add_parser("create")
    sp.add_argument("--head", required=True)
    sp.add_argument("--base", default="main")
    sp.add_argument("--title", required=True)
    with_body(sp)
    sp = pr.add_parser("edit-body")
    sp.add_argument("n", type=int)
    with_body(sp)
    sp = pr.add_parser("reply")
    sp.add_argument("n", type=int)
    sp.add_argument("comment_id", type=int)
    with_body(sp)
    sp = pr.add_parser("resolve")
    sp.add_argument("n", type=int)
    sp.add_argument("comment_id", type=int)

    a = p.parse_args()
    try:
        if a.kind == "issue" and a.action == "create":
            r = issue_create(a.title, body_of(a), a.label)
        elif a.kind == "issue":
            r = issue_comment(a.n, body_of(a))
        elif a.action == "create":
            r = pr_create(a.head, a.title, body_of(a), a.base)
        elif a.action == "edit-body":
            r = pr_edit_body(a.n, body_of(a))
        elif a.action == "reply":
            r = pr_reply(a.n, a.comment_id, body_of(a))
        else:
            pr_resolve(a.n, a.comment_id)
            print("resolved thread of comment %d" % a.comment_id)
            return 0
    except RuntimeError as e:
        print("error: %s" % e, file=sys.stderr)
        return 1
    print(r.get("html_url") or r.get("url") or "done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
