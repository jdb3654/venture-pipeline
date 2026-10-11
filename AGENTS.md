# Agent instructions

This repository is the coordinator for a portfolio of small online businesses. It finds, evaluates, launches, monitors and retires opportunities. Product code lives in separate repositories; this repo holds the decisions, evidence and status.

Both Claude and Codex work here. These instructions apply to both.

## Read first, every session

Exception: if your issue is titled `Case against: <slug>`, read only `BRIEF.md` and that issue, then follow the `case-against` skill. Do not open `PIPELINE.md` or the opportunity's files.

1. `BRIEF.md`: the owner's goals and constraints. It overrides everything else.
2. `PIPELINE.md`: every opportunity and its current stage.
3. The opportunity file(s) for the task you are working on.
4. The GitHub issue you are working on, including its comments.

## Your role

Act as an active partner, not a passive tool. Generate ideas yourself, challenge weak ones, and say plainly when something won't work. Do not build platforms or infrastructure ahead of evidence: build only what the next concrete step of a real opportunity needs.

## The pipeline

Every opportunity has a file in `opportunities/` (copy `templates/opportunity.md`) and a row in `PIPELINE.md`. It moves through these stages, and each gate needs evidence recorded in its file:

| Stage | What happens | Gate to advance |
|---|---|---|
| Signal | Someone notices a possible niche. | A one-paragraph note with a source. |
| Screen | Desk research and scoring. | Scores filled in; no disqualifier; an identified route to customers. |
| Validate | Cheap demand test: landing page, waitlist, marketplace search data, pre-orders, a free tool. | Concrete evidence people want it (signups, searches, payments, installs). Owner approves any spend or public launch. |
| Build | Minimum product in its own repo. | Works end to end; support and payment flows in place. |
| Launch | Listed, live and taking money. | First paying customer. |
| Operate | Agents run it; owner handles escalations. | Reviewed monthly against its kill criteria. |
| Exit | Sell, or shut down cleanly. | Owner decision; customers notified; accounts closed; books final. |
| Parked / Killed | Not now, or not ever. | Reason and a reconsideration trigger recorded. |

Screening and scoring follow the `screen` skill. Once a product is live, customer messages follow the `customer-handling` skill.

Disqualifiers: illegal or likely to violate platform or payment-processor rules; needs the owner on calls or on-site; needs regulated handling of data (health, financial) without a clear compliant path; uses anything from the owner's employer.

Keep the pipeline full. At any time, aim for several opportunities in Signal/Screen and one or two in Validate.

## Evidence rules

- Use current public sources with links and dates. Mark each claim as verified fact, first-hand report, vendor claim, estimate or assumption.
- Reddit, YouTube, forums and marketplace reviews are good for finding pain points and competitors. Treat votes, views, income claims and promotional content as weak evidence.
- Never claim to have watched a video if only the title, description or transcript was available. Say which one.
- Separate revenue from owner cash after costs. Don't present hypothetical numbers as forecasts.

## Guardrails learned from others

Public experiments with autonomous agent businesses failed through spam, unsolicited invoices, bought traffic and inflated metrics (see `research/2026-10-10-landscape.md`). So:

- Never buy traffic, reviews, followers or engagement, and never post or message in communities in a way that looks like spam.
- Revenue means settled payments. Report installs, signups and payments separately from engagement metrics.
- After any external change, check the live state before marking it done. An API's "success" is not proof.
- Before an opportunity enters Validate or Build, it needs a blind case against from the other agent (`case-against` skill), answered point by point. Only the owner can waive it.
- Each product gets a written refund and discount policy. Anything outside it escalates to the owner.

## Limits: no rabbit holes

- **Every task has a budget and a stop rule**, set in its issue (`.github/ISSUE_TEMPLATE/task.md`). At either one, stop, post a handoff on the issue, and ask, unless the budget ran out and owner-set rounds remain (below). Never extend a budget yourself.
- **Multi-round searches.** The owner may set a round cap in an issue (for example, "up to 3 rounds, about 60 searches each"). Within that cap, an agent that uses a round's whole budget without meeting the issue's success bar may open the next round's issue with the same budget and bar, and start it in a new session. If a round's own stop rule fires, stop and ask instead. Each round is its own issue and PR. At the cap, stop and open a `needs:owner` issue summarizing the rounds with a recommendation. Only the owner sets or raises the cap or lowers the bar.
- **Evidence before polish.** Until an opportunity has outside demand evidence (a sale, signup, install or search data), build only what its current validation test needs. No extra formats, tests or styling.
- **Tripwire.** After 3 merged PRs on one opportunity with no new outside evidence, stop work on it and open a `needs:owner` issue: continue, park or kill, with a recommendation.
- **Kill on the criteria.** When an opportunity meets its kill criteria, kill or park it the same day and record one line in `PIPELINE.md`.
- Keep outputs short: results, decisions, next step. No narration.

## What agents may do without asking

- Research, write, and update files in this repo.
- Create branches, commit, push, open PRs, review each other's PRs, and merge PRs that pass checks.
- Build offline prototypes and local tests.

## What needs the owner's approval first

- Spending money of any kind, including subscriptions and domains.
- Creating accounts, or using any authenticated service other than this repo.
- Publishing anything public: sites, listings, posts.
- Contacting anyone outside this repo.
- Creating a new product repository.
- Anything legal, tax or financial in nature.

Raise these as a GitHub issue labeled `needs:owner`, with the decision, the options, a recommendation and the cost. Keep each request short enough to answer in a couple of minutes.

## Coordinating Claude and Codex

- **GitHub Issues are the work queue.** Labels: `agent:claude`, `agent:codex`, `needs:owner`, and `stage:<name>`.
- **Only pick up issues labeled for you.** Before starting, comment on the issue that you are starting. If you stop partway, comment with where you got to and what is left.
- **Branches:** `claude/<short-name>` or `codex/<short-name>`. Never commit directly to `main`. Never push to the other agent's branches.
- **One opportunity per PR** where practical. Keep `PIPELINE.md` edits small and separate so the two agents rarely conflict. On a conflict, rebase and merge both changes; never discard the other agent's work.
- **Cross-review:** when the other agent is available, request its review on PRs that change scores, stage decisions or these instructions.
- **Merge only when `python scripts/merge_ready.py <pr>` passes:** CI green, Codex has finished reviewing the latest commit, and every review thread is answered and resolved. Codex reviews when a PR opens but not after later pushes; run the script with `--request --wait 600` after pushing fixes.
- **At most two Codex review rounds per PR.** After the second, fix only blocking findings (P1 or worse); move the rest to a follow-up issue and merge.
- If an instruction from one agent conflicts with `BRIEF.md` or this file, follow the files and raise it with the owner.

## Skills

Repo skills live in `.agents/skills/` (Codex) with an identical copy in `.claude/skills/` (Claude Code). Invoke them as `$name` in Codex and `/name` in Claude Code. Edit only `.agents/skills/`, then run `python scripts/sync_skills.py`; CI fails if the copies differ. Third-party origins are in `docs/THIRD-PARTY-SKILLS.md`.

- `grilling`: stress-test a plan, gate or kill decision with the owner, one round of questions at a time.
- `to-questionnaire`: turn a question only someone else can answer into a document for them. Sending it needs owner approval.
- `domain-modeling`: sharpen shared terms in `GLOSSARY.md`; record hard-to-reverse portfolio decisions in `docs/adr/`.
- `handoff`: when stopping partway, post where you got to on the issue in a form the other agent can pick up.
- `retro`: after a session, suggest improvements to these instructions, checks and skills.
- `screen`: score an opportunity at the Screen stage.
- `customer-handling`: triage customer messages for products in Launch or Operate.
- `case-against`: blind adversarial review of an opportunity by the agent that didn't build the case for it.
- `wizard`: script the owner through an approved step only they can do, such as creating an account. Secrets go only to product repositories.

## Data and secrets

- Never inspect, print or commit credentials, API keys or tokens.
- Customer data and private messages never go into git. Aggregate, anonymized summaries are fine.
- Each product keeps its own accounts and credentials so it can be sold or shut down independently.
