# Scheduled customer statements for QuickBooks Online below Advanced

- **Slug:** qbo-scheduled-statements
- **Stage:** Parked (listing route likely needs Intuit's $300/month Silver tier, above budget; also below the round's bar on Distribution and Willingness to pay)
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #65)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. Pages checked 2026-10-11.

## The idea in two sentences

A QuickBooks Online app that emails customer statements on a schedule (monthly, or when a balance is overdue) for companies on Simple Start, Essentials or Plus, where QuickBooks only offers manual batch statements. Buyers are small B2B firms and their bookkeepers who chase open balances by hand each month.

## Signal

Lens: long-open requests. A QuickBooks moderator said recurring statements are available only in QuickBooks Online Advanced for the US; everyone else creates statements manually (Sales > Customers > Batch actions > Create statements) [report: [QuickBooks Community, 2024-04-27](https://quickbooks.intuit.com/community/reports-87/setup-recurring-statements-178384)]. The thread has one reply and nobody offered to pay.

## Customers and distribution

- **Buyers:** QuickBooks Online Plus and Essentials users with B2B receivables [assume].
- **Today:** manual batch statements; AR suites; upgrading to Advanced [report: Community].
- **Route without ads:** QuickBooks App Store after Intuit's technical and security review [report: [Apideck](https://developers.apideck.com/connectors/quickbooks/docs/application_owner+app_compliance)]. Codex's review of #66 cites Intuit's App Partner Program Guide as making Marketplace listing unavailable on the free Builder tier and available from Silver ($300/month) [report: [Intuit guide via Codex review](https://static.developer.intuit.com/resources/Intuit_App_Partner_Program_Guide.pdf); not opened by Claude, round budget spent]. Without the App Store, the route is search for "QuickBooks automatic statements" only.
- **Named paid competitor:** Paidnice, AR automation for QuickBooks Online and Xero including scheduled statements, from **US$69/month**; 4.9 from 14 reviews; complaints are about bulk edits and learning curve, not statements [vendor: [Capterra](https://www.capterra.ie/software/1032423/paidnice)]. Chaser and Upflow are in the same category [assume, not checked].

## Scopes

`com.intuit.quickbooks.accounting`: read customers, invoices and payments for the whole company file [assume on scope granularity]. Statement generation needs reads (CorePlus, metered above 500,000 calls/month on the free Builder tier) [report: [Apideck, updated 2026-10-06](https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program)]. Whether the API can trigger QuickBooks' own statement emails wasn't checked; if not, we render and send statements ourselves [assume].

## Strongest reason it fails

Statements are one feature inside a crowded AR category, and the people who care enough to pay already buy a suite like Paidnice that does statements plus reminders, late fees and portals. The people left are those who don't care enough to pay $69, and the only demand evidence is a thread with one reply. Sending wrong balances to a customer's customers is an embarrassing, urgent exception.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | App Store listing likely needs Silver at $300/month [report: Codex citing Intuit guide]; without it, search only, against Paidnice and others [vendor]. |
| Willingness to pay | 3 | Paidnice from $69/month bundles it [vendor]; Intuit gates it to Advanced [report]; no one found paying for statements alone. |
| Build effort | 2 | OAuth, statement rendering and email delivery if the API can't send QuickBooks' own; Intuit security review before listing [assume; report]. |
| Operating load | 2 | Full accounting-file read access; outbound email to third parties; balance errors reach customers' customers [assume]. |
| Owner time | 3 | Annual Intuit review and 2-week remediation windows [report: Apideck]. |
| Legal and compliance load | 3 | Financial records of customers' customers; transactional email rules; Intuit terms [assume]. |
| Sellability | 3 | Small recurring app; a bookkeeping-tools buyer might want it [assume]. |
| Window | 3 | Intuit can move the feature down-tier at any time [assume]. |
| Cost | 1 | Builder API tier is $0 within 500,000 reads/month [report: Apideck], but listing likely needs Silver at $300/month [report: Codex citing Intuit guide], above the $50–100/month budget in `BRIEF.md`. |

Disqualifiers checked: financial data, but invoice and payment records under the customer's own authorization through Intuit's reviewed route [assume]; not regulated handling as far as known. Revisit with the CPA consult in `docs/LEGAL-TAX.md`.

## Economics (estimates, not forecasts)

- Price: $15/month per company [est].
- Running cost at launch: under $15/month off-marketplace [est]; about $315/month if listed on Silver [report + est].
- MoR fee about 5% + $0.50 [assume, per #59].
- $1k/month owner cash: about 75 companies [est].

## Owner tasks that remain

Approve an Intuit developer account (payment method on file) and the MoR account (#59); respond to annual Intuit reviews.

## Validation plan

Cheapest test with no new account: a landing page and waitlist for "automatic monthly statements for QuickBooks Plus and Essentials" on the repo's existing GitHub Pages (owner approval to publish; $0), answered where people ask in QuickBooks Community threads only if a reply is genuinely useful (owner approval; not spam). 30 days. Pass: 25 signups. Fail: under 8.

## Kill criteria

Fail the waitlist test, or Intuit makes recurring statements available below Advanced.

## Exit

An AR-automation vendor or bookkeeping-tools company [assume]. Needs its own Intuit developer and MoR accounts.

## Decision log

- 2026-10-11: Screened as near-miss 2 in round 1 (#65), by Claude.
- 2026-10-11: Parked after Codex review of #66: listing likely needs the $300/month Silver tier (above budget), and Legal, Sellability and Window scores rest on assumptions. Reconsider if Intuit opens listing to Builder, or the portfolio budget covers Silver.
