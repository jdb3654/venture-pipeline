# Pre-Copilot oversharing check for small tenants

- **Slug:** m365-oversharing-check
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #58)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A one-off paid scan for small tenants deciding whether to buy Copilot: it lists SharePoint sites and OneDrive files open to "everyone", anonymous and organization-wide links, and broadly shared folders, then gives a fix list ordered by exposure. The buyer is the IT generalist who has to answer "will Copilot show people things they shouldn't see?" before the purchase.

## Signal

Lens: newly possible with AI (Copilot-adjacent gaps for tenants without Copilot licences).

- Microsoft's oversharing tooling, SharePoint Advanced Management (SAM), is included with Copilot licences; standalone it is **$3/user/month**, and there's no sign it is waived for anyone without Copilot [report: [Directions on Microsoft, 2025-07-22](https://www.directionsonmicrosoft.com/its-sharepoint-advanced-management-not-copilot-advanced-management/)].
- Mid-market tools have 100-user minimums (Syskit Point from $12/user/year, 100 users) [vendor: [Syskit](https://www.syskit.com/products/point/pricing/)].

## Customers and distribution

- **Buyers:** 10–100-seat firms considering Copilot. Today: PnP PowerShell scripts, a consultant, or skip the check [assume].
- **Route without ads:** search for "Copilot oversharing" and "Copilot readiness"; AppSource after Partner Center.
- **Competitors:** SAM (above), Syskit, ShareGate, AvePoint [assume for the last two; not checked this round].

## Graph permissions (admin consent required)

`Sites.Read.All` and `Files.Read.All` for sharing and permissions across every site and OneDrive. Flagging sensitive-looking files means reading file names at least, and content for anything better [assume]. This is the highest security load of the three survivors.

## Strongest reason it fails

The moment of need is the Copilot purchase, and buying even one Copilot licence turns SAM on for the tenant by default [report: Directions on Microsoft]. So the free Microsoft tool arrives exactly when the buyer cares, and before that point many small firms won't pay to check. Reading every file's sharing state also makes this the hardest of the three to trust.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Search only until Partner Center exists [fact: [verification](https://learn.microsoft.com/en-nz/partner-center/enroll/understand-the-verification-process)]. |
| Willingness to pay | 2 | SAM at $3/user/month [report] and Syskit [vendor] are adjacent; the free-with-Copilot inclusion undercuts both. |
| Build effort | 3 | Permissions crawl over sites and OneDrives is slow on throttled Graph calls [assume]. |
| Operating load | 2 | Broad file-level permissions; long scans; false positives [assume]. |
| Owner time | 4 | Escalations only [assume]. |
| Legal and compliance load | 2 | Touches file names and possibly content, which may include regulated data in customer tenants [assume]. |
| Sellability | 2 | One-off report with no recurring revenue [est]. |
| Window | 2 | Shrinks as Microsoft bundles SAM features more widely [assume]. |
| Cost | 4 | Near $0 at low volume [est]. |

Disqualifiers checked: we would scan customers' files, which can include health or financial records. Not a disqualifier if we read only sharing metadata and file names and keep nothing; reading content would need a compliant path.

## Economics (estimates, not forecasts)

- Price: $99 per scan up to 100 users [est].
- Running cost at launch: under $10/month [est].
- $1k/month owner cash: about 11 scans a month [est].

## Owner tasks that remain

- One-time: approve accounts and publishing.

## Validation plan

Not worth its own test yet. If the evidence pack's free script draws interest, add one "broadly shared sites" check to it and count requests for the full scan.

## Kill criteria

No requests for a full scan during the evidence-pack test, or Microsoft includes SAM oversharing reports in Business Premium.

## Exit

Fold into the evidence pack; little standalone sale value.

## Decision log

- 2026-10-11: screened by Claude (#58); ranked 3 of 3; no separate test.
