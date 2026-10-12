# Scheduled board email reports for monday.com

- **Slug:** monday-board-email-reports
- **Stage:** Parked (2026-10-12). Its own kill criterion is met: monday natively schedules dashboard PDFs by email, including to external recipients (details below). Scores are provisional and were never sourced enough for Screen.
- **Owner agent:** claude
- **Created / last updated:** 2026-10-12 / 2026-10-12
- **Last outside evidence:** none yet (desk research only, issue #67)
- **Reconsider if:** monday removes or further plan-gates scheduled dashboard PDFs, or buyers are found paying for more schedules than Standard (1) or Pro (5) allow.

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

**monday already does it.** Scheduled PDF exports of dashboards go daily, weekly or monthly to up to 50 recipients, including external ones, using the dashboard's filters. The limit is on the number of schedules: Standard 1, Pro 5, Enterprise 100. Enterprise also gets scheduled email notifications [fact: [monday support, Share and present your Dashboard](https://support.monday.com/hc/en-us/articles/26237863849490-Share-and-present-your-Dashboard)]. (Codex found this in review of #71.) The only paying pool left is Standard or Pro accounts that need more schedules, or a format the PDF doesn't give. On top of that, Stiltsoft already sells this exact product and holds the marketplace search for it.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Platform-billed marketplace search with broad app use [vendor: monday.com/appsdeveloper], but a native feature and a named incumbent [vendor: Stiltsoft pricing] already serve it. |
| Willingness to pay | 2 | Stiltsoft asks $10–500/month [vendor: Stiltsoft pricing], but that is an asking price; installs or revenue weren't checked. The native feature covers most of the need [fact: monday support]. Lowered from 4 after Codex review of #71. |
| Build effort | 3 | monday app framework, scheduled jobs, HTML email; monetization webhooks and plan enforcement are our job [fact: [monday docs](https://developer.monday.com/apps/docs/implementing-monetization)]; 2–4 weeks [est]. |
| Operating load | 3 | Email deliverability and wrong-recipient reports are the likely exceptions; read-only scope [assume]. |
| Owner time | 4 | monday bills and handles tax [vendor]; support by agents [assume]. |
| Legal and compliance load | 3 | We would process customer board data and send it by email; a DPA and privacy policy are needed [assume]. |
| Sellability | 3 | A small marketplace app with recurring revenue; buyers exist for such apps [assume]. |
| Window | 2 | monday already ships native scheduled reports and gates the count by plan; raising the limits closes the rest [fact: monday support]. |
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

None: parked. Before parking, no test was recommended: there is no differentiator over Stiltsoft. The cheapest test that fits the bar would be a waitlist page on the repo's existing GitHub Pages ($0, owner approval to publish), 30 days, pass at 30 signups. But it wouldn't reach monday buyers without a marketplace listing, which needs new accounts. So it fails the bar's test condition.

## Kill criteria

Kill if monday natively emails scheduled board summaries (met 2026-10-12, so parked), or if Stiltsoft's listing shows broad use with no complaints when checked.

## Exit

A monday-focused app vendor buying a small listing [assume]. Needs the monday vendor and Payoneer accounts in the product's name.

## Decision log

- 2026-10-12: Scored as near-miss in round 2 (#67), by Claude. Fails the round bar on Distribution (3) and on the test condition (new accounts). Not sent to case-against.
- 2026-10-12: Parked, by Claude, after Codex review of #71 found monday's native scheduled dashboard PDF exports, which meet the kill criterion. WTP lowered to 2 (asking price only, no payment evidence); Distribution and Window lowered to 2.
