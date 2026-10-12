# Scheduled board email reports for monday.com

- **Slug:** monday-board-email-reports
- **Stage:** Signal (near-miss on Distribution, 3 vs the round's bar of 4; its demand test also needs new approval-gated accounts). Scores are provisional: Build effort, Operating load, Owner time, Legal, Sellability and Window rest on assumptions, so the Screen gate isn't met.
- **Owner agent:** claude
- **Created / last updated:** 2026-10-12 / 2026-10-12
- **Last outside evidence:** none yet (desk research only, issue #67)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption, **[title]** search-result title only. Pages checked 2026-10-12.

## The idea in two sentences

A monday.com app that emails a scheduled, filtered digest of a board (overdue items, items changed this week, status counts) to people inside or outside the account, such as clients or managers without seats. Buyers are small teams on monday that report to someone who doesn't log in.

## Signal

Lens: paid apps with published prices. Found while checking what Atlassian vendors have ported to monday.

## Customers and distribution

- **Buyers:** monday account admins on small teams [assume]. Today: Stiltsoft's app, or copy-paste and screenshots [assume].
- **Route without ads:** monday's apps marketplace search. 49% of monday accounts have installed at least one app [vendor: [monday.com/appsdeveloper](https://monday.com/appsdeveloper)]. monday bills, takes 0% until $200K lifetime revenue, then 15% [vendor: same page].
- **Named paid competitor:** Stiltsoft **Board Email Reports**, 14-day trial, then $10/month (5 seats), $70 (50), $110 (100), $500 (unlimited); yearly saves up to 15% [vendor: [Stiltsoft docs](https://docs.stiltsoft.com/ber/latest/pricing-203725208.html), undated, © 2026]. Stiltsoft is an established Atlassian vendor [assume]. Install and review counts not checked this round.
- **Complaints about the competitor:** none looked for (budget).

## Scopes

Reading boards to build a report needs monday's `boards:read` scope [assume, scope name not checked]; sending email needs an outbound mail service. Read-only scope keeps the security load lower than a backup or sync app, but reports leave monday by email, sometimes to people outside the customer's account [assume].

## Strongest reason it fails

Stiltsoft already sells exactly this, priced per seat bucket, and it holds the marketplace search for it. Nothing found says its customers are unhappy, and we didn't check monday's own features: if monday's dashboards or automations can already email a board summary, the paying pool is only the people who need more than that. A cheaper clone with no gap to point to doesn't take the search slot.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Platform-billed marketplace search with broad app use [vendor: monday.com/appsdeveloper], but a named incumbent already serves the exact search [vendor: Stiltsoft pricing]. |
| Willingness to pay | 4 | Published price people are asked to pay, $10–500/month, for exactly this [vendor: Stiltsoft pricing]; paid volume unknown. monday apps can reach $5K+ ARR (ProBackup Bronze status) [title: [ProBackup](https://www.probackup.io/blog/probackup-earns-bronze-partner-status-on-the-monday-com-marketplace)]. |
| Build effort | 3 | monday app framework, scheduled jobs, HTML email; monetization webhooks and plan enforcement are our job [fact: [monday docs](https://developer.monday.com/apps/docs/implementing-monetization)]; 2–4 weeks [est]. |
| Operating load | 3 | Email deliverability and wrong-recipient reports are the likely exceptions; read-only scope [assume]. |
| Owner time | 4 | monday bills and handles tax [vendor]; support by agents [assume]. |
| Legal and compliance load | 3 | We would process customer board data and send it by email; a DPA and privacy policy are needed [assume]. |
| Sellability | 3 | A small marketplace app with recurring revenue; buyers exist for such apps [assume]. |
| Window | 3 | Stable category; monday could add native scheduled reports [assume]. |
| Cost | 4 | Hosting plus a transactional-email plan, under $20/month at launch [est]; no marketplace fee before $200K [vendor]. |

Disqualifiers checked: none. Not employer-related; no regulated data unless a customer puts it in a board [assume].

## Economics (estimates, not forecasts)

- Price: match Stiltsoft's seat buckets, about $10–110/month [est].
- Running cost at launch: under $20/month [est].
- Payment: monday is merchant; 0% cut until $200K lifetime; monthly Payoneer payout [vendor/fact].
- $1k/month owner cash: about 30–50 accounts at an average $25–35/month [est].

## Owner tasks that remain

Approve a monday developer account, a Payoneer account and vendor registration, and the marketplace submission (all approval-gated). Approve an email-sending service.

## Validation plan

No test recommended yet: there is no differentiator over Stiltsoft. The cheapest test that fits the bar would be a waitlist page on the repo's existing GitHub Pages ($0, owner approval to publish), 30 days, pass at 30 signups. But it wouldn't reach monday buyers without a marketplace listing, which needs new accounts. So it fails the bar's test condition.

## Kill criteria

Kill if monday natively emails scheduled board summaries, or if Stiltsoft's listing shows broad use with no complaints when checked.

## Exit

A monday-focused app vendor buying a small listing [assume]. Needs the monday vendor and Payoneer accounts in the product's name.

## Decision log

- 2026-10-12: Scored as near-miss in round 2 (#67), by Claude. Fails the round bar on Distribution (3) and on the test condition (new accounts). Not sent to case-against.
