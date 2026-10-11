---
name: retro
description: Run a retrospective on an agent session in this repo and suggest improvements to the agents' working environment (instructions, checks, skills, information access). User-invoked.
disable-model-invocation: true
---

The owner has asked for a **retrospective**. You are suggesting improvements to the agents' **environment** so future sessions go better. You are not re-doing the work or grading the opportunity.

## Steps

1. Read the primary sources for the session the owner names: the conversation, the issue and its comments, the PR, its commits and review comments. If no session is named, use the current one.

2. Look for candidates in these categories:

- **Navigation**: did the agent struggle to find the right file, issue or record? Would a one-line pointer in `AGENTS.md` or an opportunity file fix it? _Use when_ finding information took a long time.
- **Automated checks**: is there a mistake a deterministic check could catch (a missing pipeline row, an opportunity file with empty scores, skill copies out of sync, broken links)? Read the existing checks in `.github/workflows/` and `scripts/` first: a check that exists but isn't wired up is the finding, not a reinvention. Prefer building a check over writing a rule. _Use when_ the agent made a mistake a script could have caught.
- **Review rules**: did cross-review between Claude and Codex miss something it should have caught? Mechanical problems get a check; judgement calls get a line in `AGENTS.md`. _Use when_ a reviewer missed a mistake.
- **Instruction size and no-ops**: `AGENTS.md` loads into every session for both agents. Look for lines that don't change behaviour, duplicate `BRIEF.md`, or belong in a skill instead. _Use when_ instructions are long or were ignored.
- **Coordination**: did Claude and Codex collide (same files, same issue, conflicting edits), or did a handoff lose context? _Use when_ work was duplicated or redone.
- **Owner time**: did the session ask the owner for something an agent could have looked up, or bundle decisions poorly? The owner has about two hours a day. _Use when_ the owner was asked more than needed.
- **Tool economy**: were there expensive or repeated tool calls that a script or skill would make cheap? _Use when_ the session made many similar calls.
- **Information access**: was a crucial piece of information unavailable (marketplace data, a product's logs, an account's state)? Note which access would help and that granting it needs the owner's approval. _Use when_ the agent had to guess.

3. Present the candidates to the owner in order of severity, each with: what happened, the proposed change, and the file it would touch.

Only make changes the owner picks. Changes to `AGENTS.md` or these skills need the other agent's review, per `AGENTS.md`.
