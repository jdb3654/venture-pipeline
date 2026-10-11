---
name: case-against
description: Blind adversarial review of an opportunity before it enters Validate or Build. Use when asked for a case against, a red-team or a kill review of an opportunity, or when an issue titled "Case against" is assigned to you.
---

You are the adversary. Your job is to find the reason this opportunity fails, not to improve it. A review that finds nothing is a failed review.

## Stay blind

Read only:

- `BRIEF.md`.
- The **two-sentence idea** and the **Customers and distribution** section of `opportunities/<slug>.md`.

Do not read its scores, signal, economics, validation plan, existing case against or decision log, or any PR discussion. Those carry the author's framing. If you already worked on this opportunity in this session, say so and stop: another agent or a fresh session must do it.

## Do

Research independently, with sources and dates, following the evidence rules in `AGENTS.md`. Look for: free substitutes, evidence buyers don't pay, distribution that won't reach them, platform or legal blockers, hidden owner time, and anything in `BRIEF.md` it breaks.

Budget: one session, at most about 10 searches. Stop at the budget even if unfinished, and say what you didn't check.

## Output

Add this section to the opportunity file, under 250 words, then open a PR:

```md
## Case against (blind review, <agent>, YYYY-MM-DD)

**Verdict:** kill | park | proceed. **Confidence:** low | medium | high.

1. <strongest reason it fails>, with source.
2. <next reason>, with source.
3. <next reason>, with source.

**Cheapest kill test:** <the one test, under $X and Y days, whose failure should end this>.

**Not checked:** <what the budget left out>.
```

## After the review

The opportunity's owner agent answers each numbered point in one line beneath the section: refuted (with source), accepted, or mitigated (how). A point can't be answered with "we'll see". The owner reads both sides and decides the stage change.

## Requesting one

To request a blind review, open an issue titled `Case against: <slug>` labeled for the **other** agent (`agent:codex` for a Claude-owned opportunity, and the reverse). The issue body names the slug only, with no argument for the idea. If the other agent isn't available, a fresh session or a sub-agent that has not seen the opportunity may do it, and the section says which.
