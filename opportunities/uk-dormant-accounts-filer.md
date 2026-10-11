# UK dormant-company accounts filer (after WebFiling closes)

- **Slug:** uk-dormant-accounts-filer
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #56)

Labels: **[fact]** verified on the cited page, **[report]** first-hand report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A self-serve web tool that files dormant-company accounts to Companies House by software, for UK company owners who today use the free WebFiling form and lose it when accounts WebFiling closes. Owners of dormant companies (holding names, paused side businesses, formation-agent customers) pay a small annual fee.

## Signal

Lens: forced deadline, plus our own lens "a free government service is being switched off."

- Companies House WebFiling for annual accounts, and paper accounts, close on 1 April 2028; dormant companies must use commercial software from then. HMRC's free CT600 service already closed on 31 March 2026. [vendor: [TinyTax](https://tinytax.co.uk/guides/companies-house-webfiling-closing), published 2025-12-01, updated 2026-10-11; TinyTax sells such software]. Corroborating headlines from Easy Digital Filing, Xero and Yahoo Finance appeared in search results but were not read.
- Government guidance page exists ([GOV.UK](https://www.gov.uk/guidance/using-software-to-file-your-companys-information)); not read this round, so the 2028 date rests on vendor pages. **Verify on GOV.UK first.**

## Screen gate: ACSP eligibility (unresolved)

Companies House says all agents filing for clients will need to register as an Authorised Corporate Service Provider (ACSP), which requires supervision by a UK anti-money-laundering body; filing as an agent is expected "no earlier than November 2026" [fact: [GOV.UK](https://www.gov.uk/guidance/being-an-authorised-corporate-service-provider), updated 2026-06-19]. The page doesn't say whether self-serve software a director uses to file their own company's accounts counts as an agent. If it does, a US-based owner has no documented route to UK AML supervision, which would make the filing route unusable. **No validation, build or case-against until this is answered** (raised by Codex review on #57).

## Customers and distribution

- **Buyer:** directors of dormant UK companies who file their own accounts today for free. Number of dormant companies: not found this round (a Companies House FOI release on dormant-company penalties exists, [GOV.UK](https://www.gov.uk/government/publications/request-for-statistics-relating-to-dormant-company-penalties), not read). [assume: large, unquantified]
- **Today they use:** free WebFiling; or pay a formation agent, e.g. Rapid Formations at **£49.99 + VAT per year** for a dormant filing [vendor asking price, [Rapid Formations](https://www.rapidformations.co.uk/dormant-company-accounts)]; or accounting software.
- **Route without ads:** search ("file dormant accounts", "WebFiling closed") rising as 2028 nears [assume]; a free "is my company dormant / what's my deadline" checker as a search magnet [assume]. No app marketplace.
- **Competitors:** TinyTax "from £20/year" for micro-entity accounts and CT600 [vendor]; TaxCalc, IRIS, Sage named as software options [vendor, same TinyTax page]; formation agents (above).

## Strongest reason it fails

Price floor and timing. Incumbents already sell micro-entity accounts plus CT600 from £20/year [vendor], and formation agents can bundle dormant filing for their existing customers, so a dormant-only product competes on price near zero. The real switch from free to paid doesn't happen until April 2028, so any 2026 demand test mostly measures people who already pay for convenience. A second gate: developers report Companies House test-credential requests unanswered after 17 and about 40 working days, with a further unanswered follow-up on 2026-10-02 [report: [CH XML forum](https://xmlforum.companieshouse.gov.uk/t/no-response-to-test-account-request-after-17-working-days/1943)]. We can't file anything without those credentials (**approval-gated**).

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Search intent should rise as the free route closes [assume]; no marketplace; formation agents compete for the same queries ([Rapid Formations](https://www.rapidformations.co.uk/dormant-company-accounts)). |
| Willingness to pay | 3 | Paid dormant filing is offered at £49.99 + VAT/yr even while the free route exists, and micro-entity software from £20/yr [vendor asking prices, no sales counts: [Rapid Formations](https://www.rapidformations.co.uk/dormant-company-accounts), [TinyTax](https://tinytax.co.uk/guides/companies-house-webfiling-closing)]. |
| Build effort | 3 | Dormant accounts are the simplest case, but need iXBRL tagging and XML Gateway filing [vendor: TinyTax], plus credential testing ([CH forum](https://xmlforum.companieshouse.gov.uk/t/no-response-to-test-account-request-after-17-working-days/1943)). |
| Operating load | 4 | One filing per company per year; exceptions are rejections, wrong authentication codes, and companies that aren't actually dormant [assume]. Deadline-driven, so bursts. |
| Owner time | 4 | Near zero once live [assume]; rejection spikes near deadlines may need escalation. |
| Legal and compliance load | 2 | Possible ACSP registration with UK AML supervision ([GOV.UK](https://www.gov.uk/guidance/being-an-authorised-corporate-service-provider)). We would hold customers' Companies House authentication codes (a filing credential) and act as presenter; a missed filing triggers a penalty for the customer [assume]. UK filing for a US-based owner needs the CPA consult in `docs/LEGAL-TAX.md`. No regulated personal data. |
| Sellability | 4 | Annual-renewal customer base is easy to transfer to a formation agent or accounting vendor [assume]. |
| Window | 3 | Opens fully April 2028 and closes as incumbents price-match [vendor date: TinyTax]. |
| Cost | 4 | Small web app; filing accounts by software has no Companies House fee [assume, verify]. Well under $50/month. |

Disqualifiers checked: illegal or platform-risky: **unresolved** — ACSP requirement could block the filing route (see Screen gate) / needs owner on calls: no / regulated data: no (company data is public; authentication codes need secure handling) / employer-related: no.

## Economics (estimates, not forecasts)

- Price: about £15–20/year per company [est], undercutting £49.99 agents and matching TinyTax's floor.
- Running cost: about $10/month hosting [est].
- Payments: merchant of record, roughly 5% + $0.50 per sale [assume; Paddle/Lemon Squeezy public pricing, not rechecked]. Net about $21/year per customer at £18.
- Customers needed: about 6 to cover $10/month; about 570 for $1k/month owner cash [est].

## Owner tasks that remain

- Approve requesting Companies House test credentials (contact outside the repo) — once, 10 minutes.
- CPA/legal consult on acting as presenter for UK companies — once, before any sale.
- Approve any public page — once.

## Validation plan

0. **$0, one session, before anything else:** establish from Companies House guidance or the XML/software forums whether a software provider filing for directors must be an ACSP, and whether partnering with an existing ACSP is a workable route. Fail: ACSP required and no partner route; park.
1. **$0, one session:** confirm the 2028 date on GOV.UK and size the market from free Companies House data (count of dormant accounts filed per year). Pass: at least 100,000 dormant filings a year. Fail: below that, park.
2. **$0–£10, 60 days (owner approval to publish):** a one-page "file dormant accounts after WebFiling closes, £18/yr — reserve a place" waitlist plus a free deadline checker. Pass: 25 or more waitlist signups with the price shown. Fail: fewer than 10.

## Kill criteria

Step 1 fails; or step 2 gets fewer than 10 signups in 60 days; or Companies House credentials are still unavailable by 2027-03-31; or ACSP registration is required with no partner route.

## Exit

Sell the customer list and software to a formation agent or small accounting vendor. Needs clean renewal records and no dependence on the owner's identity as presenter.

## Decision log

- 2026-10-11: entered at Screen from discovery round 2 (#56), by Claude. Ranked first of five.
- 2026-10-11: Codex review on #57 raised ACSP registration. Verified the GOV.UK requirement; applicability to self-serve software unknown. Moved to rank 2 behind an ACSP check, by Claude.
