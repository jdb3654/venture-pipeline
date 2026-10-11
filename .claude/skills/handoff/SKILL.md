---
name: handoff
description: Compact the current session into a handoff so another session or the other agent (Claude or Codex) can pick up the work. User-invoked, or use when stopping partway through an issue.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff summarising the current session so a fresh agent can continue the work. The next agent may be Claude or Codex, on a different machine, days later.

## Where it goes

1. **An issue is in play** (the usual case here): post the handoff as a comment on that issue. This is also how `AGENTS.md` asks you to record where you got to when you stop partway. Use `gh issue comment <n> --body-file <file>`, writing the body to a temporary file first so the shell doesn't expand backticks or `$`. If you are handing to the other agent, say so in the comment and leave the label change to the owner unless you were asked to reassign it.
2. **No issue exists:** save it to the OS temporary directory (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows), not the repository, and report the path.

Never commit a handoff to the repository. Its value is short-lived, and the repository and its issues are public.

## What it contains

- **Goal:** what the work is for, in a sentence.
- **State:** done, in progress, and left to do. Name the branch and any open PR.
- **Decisions and open questions:** what was settled and what still needs the owner.
- **Next step:** the single most useful thing to do first.
- **Suggested skills:** which skills the next agent should load, by name (`/grilling` in Claude Code, `$grilling` in Codex).

Do not duplicate what other artifacts already hold (opportunity files, `PIPELINE.md`, ADRs, issues, commits, PRs). Point to them by path or link.

Redact anything sensitive: credentials, account recovery details, customer data, private messages, and anything about the owner's employer or personal finances.

If the user passed arguments, treat them as the focus of the next session and tailor the handoff to it.
