# Venture pipeline

Coordinator for a portfolio of small, legal online businesses run mostly by AI agents (Claude and Codex), with the owner as funder and escalation point. Product code lives in separate repositories.

- [`BRIEF.md`](BRIEF.md): goals and constraints. Start here.
- [`AGENTS.md`](AGENTS.md): how agents work here, including coordination between Claude and Codex.
- [`PIPELINE.md`](PIPELINE.md): every opportunity and its stage.
- [`templates/opportunity.md`](templates/opportunity.md): the evaluation template.
- [`docs/LEGAL-TAX.md`](docs/LEGAL-TAX.md): what to verify before the first sale.

An earlier exploration lives in `jdb3654/independent-business-exploration`. Treat it as reference material, not current direction.

## Starting prompt

Use this to kick off a fresh agent session on the first round of discovery:

> Read BRIEF.md and AGENTS.md. Then generate 15–20 candidate niches that fit the brief, favoring ones with built-in distribution (marketplaces, search, communities) and low support load. Include some that draw on software and systems integration skills and some that don't. Briefly check each against the disqualifiers and drop the ones that fail. Pick the 5 strongest and write a Screen-stage opportunity file for each, with sources. Add all of them to PIPELINE.md, including the dropped ones under Parked/Killed with reasons. Open one PR, and finish with a short summary of which one or two you'd take to Validate and what the cheapest demand test would be.

## Weekly owner review (about 30 minutes)

1. Answer open `needs:owner` issues.
2. Skim `PIPELINE.md` for stage changes.
3. Check spend against the budget in `BRIEF.md`.
4. Approve or kill anything waiting at a gate.
