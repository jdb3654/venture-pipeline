# Certificate-of-insurance tracker for small contractors and landlords

- **Slug:** small-gc-coi-tracker
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #56)

Labels: **[fact]** verified on the cited page, **[report]** first-hand report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

Small general contractors and property managers forward subcontractors' and vendors' certificates of insurance (ACORD 25 PDFs); an LLM extracts limits, dates and endorsements, checks them against the customer's requirements, and sends renewal reminders before expiry. They pay a low monthly fee instead of a spreadsheet or a $800+/year enterprise tool.

## Signal

Lens: newly possible with AI (reading messy insurance certificates reliably was hard two years ago).

- Established COI tools are priced annually: C2COI $800–2,000, myCOI $1,500–3,000, SmartCompliance $2,000–4,000; CertFocus has a $7,500 minimum [vendor: [Vertikal RMS](https://vertikalrms.com/article/how-much-does-coi-tracking-software-cost-2025-pricing-guide/), 2026-01-24, modified 2026-05-14; Vertikal sells CertFocus, competitor prices unverified].

## Customers and distribution

- **Buyer:** GCs with under 100 subcontractors; property managers with 20–2,000 units [vendor: CertShield's target, [SaaSHub](https://www.saashub.com/certshield-app)].
- **Today they use:** spreadsheets and email [vendor framing, same sources].
- **Route without ads:** search only; no app marketplace identified. Procore and QuickBooks marketplaces not checked (approval-gated to list).
- **Competitors (2026 AI entrants):** CertShield, **$99/month for up to 25 vendors**, human review of uncertain extractions [vendor: [SaaSHub](https://www.saashub.com/certshield-app)]; also BCS, ImageToTable, SiteVetter, Highwire, ExpirationReminder, 1099Policy and RiskWise appeared on the first results page for small-contractor COI searches [fact: search results 2026-10-11; pages not read].

## Strongest reason it fails

Saturation without a distribution edge. At least eight vendors, several launched with AI extraction in 2026, already target this exact small-business segment, and the search results are vendor content marketing. We have no marketplace, no audience and no construction relationships. CertShield's use of human review on uncertain certificates [vendor] suggests full automation isn't reliable yet, and a missed exclusion is a real liability for the customer.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Search only, dominated by vendor blogs [fact: search results 2026-10-11]; no marketplace route found. |
| Willingness to pay | 4 | A paid category with annual contracts from several vendors [vendor: [Vertikal RMS](https://vertikalrms.com/article/how-much-does-coi-tracking-software-cost-2025-pricing-guide/)]; inference that sales exist from the category's age, not from sales data. |
| Build effort | 3 | LLM extraction of ACORD 25, requirement rules, reminder emails, review queue [est]. |
| Operating load | 3 | Extraction errors need review; reminders go to third parties (subs, agents), so bounces and replies arrive [vendor: CertShield's human review, [SaaSHub](https://www.saashub.com/certshield-app)]. |
| Owner time | 4 | Agents can do review; owner only for disputes [assume]. |
| Legal and compliance load | 3 | Interpreting insurance documents; misreads expose the customer; automated email to third parties needs CAN-SPAM care [assume]. No regulated personal data [assume]. |
| Sellability | 4 | Recurring B2B SaaS with low churn is sellable [assume]. |
| Window | 2 | Crowded with 2026 AI entrants [fact: search results]. |
| Cost | 3 | LLM per certificate plus email sending, about $20–40/month at launch [est]. |

Disqualifiers checked: illegal or platform-risky: no / needs owner on calls: no (if strictly self-serve) / regulated data: no / employer-related: no.

## Economics (estimates, not forecasts)

- Price: $39–79/month [est], under CertShield's $99.
- Running cost: about $30/month [est].
- Payments: merchant of record, roughly 5% + $0.50 [assume].
- Customers needed: 1 covers costs; about 25 at $49/month for $1k/month owner cash [est].

## Owner tasks that remain

- Approve a public page and an email-sending account — once.
- Escalations on disputed extractions — occasional, not urgent [assume].

## Validation plan

$0, 30 days, owner approval to publish: a free "upload a certificate, get an expiry and limits check" page with an opt-in for automated tracking at $49/month. Pass: 30 certificates uploaded by distinct visitors and 5 opt-ins. Fail: fewer than 10 uploads.

## Kill criteria

Validation fails, or a case-against finds no distribution route better than search.

## Exit

Sell to an insurance agency, a construction software vendor, or a COI competitor rolling up customers.

## Decision log

- 2026-10-11: entered at Screen from discovery round 2 (#56), by Claude. Ranked third of five.
