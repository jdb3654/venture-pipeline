# Cyber-insurance evidence pack for small Microsoft 365 tenants

- **Slug:** m365-insurance-evidence-pack
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #58)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A read-only scan of a small Microsoft 365 tenant that produces a dated evidence pack mapped to the questions cyber insurers ask at renewal: MFA coverage (admins included), legacy authentication, number of admins, guest accounts, audit log settings. IT generalists buy one pack per renewal; MSPs buy a per-tenant plan to run it for every client before renewals.

## Signal

Lens: MSPs as buyers / admin chores.

- A consultancy sells the same deliverable as a fixed-price, one-week project: control-to-questionnaire mapping, dated configuration exports, evidence pack, gap plan, **$1,950 per project**, delivered by engineers through time-bound GDAP access [vendor: [o365hq](https://o365hq.com/services/cyber-insurance-readiness-assessment), no page date, © 2026].
- An MSP-focused M365 commentator tells MSPs to sell quarterly governance evidence for cyber insurance and frameworks such as Essential Eight [report: [CIAOPS, 2026-06-03](https://blog.ciaops.com/2026/06/03/most-smb-tenants-have-a-guest-graveyard/)].

## Customers and distribution

- **Buyers:** IT generalists at 10–100-seat firms facing a renewal questionnaire; MSPs with many such clients. Today: screenshots and admin-center exports by hand, or a consultant [assume, consistent with the o365hq offer].
- **Route without ads:** search on "cyber insurance questionnaire Microsoft 365" (the first results page is MSPs, consultants and one tool vendor [fact: search 2026-10-11]); MSP communities; a marketplace listing once Partner Center exists (see `research/2026-10-11-microsoft-ecosystem.md`). No marketplace route is open today.
- **Competitors:** Senserva, an M365 posture tool that markets insurance evidence, lets you register free to scan your own tenant and lists an MSP plan at **$600/month or $6,500/year for up to 50 tenants**, sold through the Microsoft Security Store [vendor: [Senserva](https://senserva.com/cyber-insurance.html)]. Microsoft Secure Score is free in every tenant [assume]. MSP posture platforms (Huntress ISPM and others) appear in 2026 buyer guides [fact: search result title, page not read].

## Graph permissions (all read-only, admin consent required)

`Directory.Read.All`, `Policy.Read.All` (conditional access, security defaults), `UserAuthenticationMethod.Read.All` or `Reports.Read.All` (MFA registration), `AuditLog.Read.All` (sign-in activity; needs Entra P1 in the customer tenant [assume]), `SecurityEvents.Read.All` (Secure Score). Lowest-risk design: delegated permissions while the admin runs it, nothing stored server-side after the pack is generated [assume]. Even so, an admin-consented app reading every user's MFA state is a high-trust request.

## Strongest reason it fails

Senserva already offers a free self-scan and an MSP plan aimed at exactly this, sold through a Microsoft store. Secure Score is free. Insurer questionnaires differ by carrier, so mapping upkeep is ongoing, and if a customer answers "yes" on our evidence and a claim is denied, we are in the story. We have no audience in MSP communities and no marketplace listing.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Search plus MSP communities; marketplace needs Partner Center first [fact: [verification requirements](https://learn.microsoft.com/en-nz/partner-center/enroll/understand-the-verification-process)]. |
| Willingness to pay | 3 | $1,950 consulting projects [vendor: o365hq] and a $600/month MSP plan [vendor: Senserva] show adjacent spend; no sales data. |
| Build effort | 3 | Graph reads plus a questionnaire mapping and PDF output; a few weeks of agent work [est]. |
| Operating load | 2 | Admin consent and broad directory reads; mapping changes as carriers change questions [assume]. |
| Owner time | 4 | Escalations only; no calls needed for a self-serve report [assume]. |
| Legal and compliance load | 2 | Customers attest to insurers using our output; needs clear "evidence, not attestation" terms and careful security-data handling [assume]. |
| Sellability | 3 | Small MSP tools are a known acquisition niche [assume]; transferable if accounts are separate. |
| Window | 3 | Renewal questionnaires recur yearly [assume]; closes if Microsoft adds an insurance view to Secure Score. |
| Cost | 4 | Serverless hosting near $0 at low volume [assume]; MoR fees per sale. |

Disqualifiers checked: not illegal; no calls or on-site work; no health or financial data (security configuration only); nothing from the employer. None apply.

## Economics (estimates, not forecasts)

- Price: $49 per tenant per pack, or $15/tenant/month for MSPs with 5+ tenants [est]. Senserva works out to $12/tenant/month only for an MSP using all 50 tenants; a 10-tenant MSP pays $60 each there. Price is a hypothesis to test.
- Monthly running cost at launch: under $10 [est].
- Payment: merchant of record, about 5% + $0.50 [assume, not rechecked].
- Covering $100/month of costs: about 3 packs or 7 MSP tenants. $1k/month owner cash: roughly 25 single packs a month, or about 75 MSP tenants [est].

## Owner tasks that remain

- One-time: approve accounts (MoR; Partner Center if listing on Microsoft); approve publishing a free script and its README.
- Weekly: escalations, under 1 hour [est].

## Validation plan

Cheapest test: a free, read-only PowerShell script (delegated sign-in, nothing leaves the admin's machine) that prints the five most-asked questionnaire answers with the evidence behind each, published in a public GitHub repository with one honest post in an MSP community. The README offers the full pack and asks interested buyers to reply in a pinned issue with company size and number of tenants.

- Cost: $0. Needs owner approval to publish and to post.
- Duration: 21 days.
- Pass: 5 or more distinct organizations ask for the paid pack. Fail: fewer than 2. Stars and downloads are recorded as engagement, not demand.

## Kill criteria

Fail on the test above, or the case-against finds Senserva's free scan already covers the questionnaire mapping.

## Exit

Sell to an MSP tooling vendor or on Acquire.com/Flippa; keep the script repo, MoR account and support inbox under the product's own name.

## Decision log

- 2026-10-11: screened by Claude (#58); ranked 1 of 3; recommended for case-against.
