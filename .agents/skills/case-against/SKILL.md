---
name: case-against
description: Blind adversarial review of an opportunity before it enters Validate or Build. Use when an issue titled "Case against: <slug>" is assigned to you, or when you need to request one for an opportunity you own.
---

The other agent attacks an opportunity without seeing the case for it. Two roles: the **owner agent** (owns the opportunity) requests it; the **reviewer** (the other agent) writes it.

## Owner agent: request it

Open an issue titled `Case against: <slug>`, labeled for the other agent (`agent:codex` for a Claude-owned opportunity, and the reverse). Its body is a sanitized excerpt copied verbatim from the opportunity file, and nothing else:

- the **two-sentence idea**;
- the **Customers and distribution** section.

No stage, scores, economics, plan, decision log or argument. The reviewer will see only this and `BRIEF.md`.

If the other agent isn't available, the gate waits. Only the owner can waive it, in a `needs:owner` issue.

## Reviewer: write it

You are the adversary. Your job is to find the reason this fails, not to improve it. A review that finds nothing is a failed review.

**Stay blind.** Read only `BRIEF.md` and the issue (`AGENTS.md` exempts you from the usual startup reading). Do not open `PIPELINE.md`, `opportunities/<slug>.md` or its PRs. If you have worked on this opportunity before, say so on the issue and stop.

**Research** independently, with sources and dates, following the evidence rules in `AGENTS.md`. Look for free substitutes, evidence buyers don't pay, distribution that won't reach them, platform or legal blockers, hidden owner time, and anything in `BRIEF.md` it breaks.

**Budget:** one session, about 10 searches. Stop at the budget even if unfinished, and list what you didn't check.

**Output:** create `opportunities/<slug>-case-against.md` (a new file, so you never open the opportunity file), under 250 words, and open a PR that closes the issue:

```md
# Case against: <slug> (blind review, <agent>, YYYY-MM-DD)

**Verdict:** kill | park | proceed. **Confidence:** low | medium | high.

1. <strongest reason it fails>, with source.
2. <next reason>, with source.
3. <next reason>, with source.

**Cheapest kill test:** <the one test, with its cost and duration, whose failure should end this>.

**Not checked:** <what the budget left out>.
```

## Owner agent: answer it

Under each numbered point, add one line: refuted (with source), accepted, or mitigated (how). "We'll see" is not an answer. Link the file from the opportunity's decision log. The owner reads both sides and decides the stage change.
