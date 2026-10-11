# Owner access reviews for small Microsoft 365 tenants

- **Slug:** m365-owner-access-reviews
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #58)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A quarterly review for tenants under 100 seats: each Team or group owner gets a short email listing the guests and external sharing links on what they own, marks keep or remove with a reason, and the admin gets a removal list and a dated evidence log. Sold per tenant to the admin of a Business Premium tenant, or to the MSP that runs it.

## Signal

Lens: admin chores small tenants do by hand.

- Many SMB guest lists are years stale: old project guests, finished contractors, former accountants [report: [CIAOPS, 2026-06-03](https://blog.ciaops.com/2026/06/03/most-smb-tenants-have-a-guest-graveyard/)].
- Microsoft's Access Reviews need Entra ID P2 or ID Governance, which Business Premium doesn't include [report: same CIAOPS post].
- Since June 2025, reviewing guests with ID Governance features is metered at **$0.75 per active guest per month** through an Azure subscription, about $3 per guest a year for quarterly reviews [report: [Office 365 for IT Pros, 2025-07-29](https://office365itpros.com/2025/07/29/entra-id-governance-levies-charges/amp/)].

## Customers and distribution

- **Buyers:** admins of 10–100-seat tenants with guests in Teams; MSPs selling "governance with a paper trail" [report: CIAOPS].
- **Today:** nothing, a script, Microsoft's metered guest reviews with an Azure subscription, or a mid-market tool [assume].
- **Route without ads:** search for "guest access review" and "inactive guests"; MSP communities; AppSource after Partner Center.
- **Competitors:** Syskit Point includes owner access reviews only in its Governance plan at **$36/user/year, minimum 100 users** ($3,600/year floor); Management plan $12/user/year, also 100-user minimum [vendor: [Syskit pricing](https://www.syskit.com/products/point/pricing/)]. CIPP (free self-hosted, €99/month hosted) is the default MSP console [vendor: [CyberDrain](https://cyberdrain.com/pricing/)]; whether it does owner reviews was not checked [assume it lists guests].

## Graph permissions (admin consent required)

Read: `User.Read.All`, `Group.Read.All`, `AuditLog.Read.All` (guest last sign-in; Entra P1 [assume]), `Sites.Read.All` (sharing links: broad, reads all site metadata), `Mail.Send` (owner emails; avoidable by sending from our own domain). Write (`User.ReadWrite.All`, `GroupMember.ReadWrite.All`) left out of v1: the admin removes from our list. `Sites.Read.All` is the security-load driver.

## Strongest reason it fails

For guest-only reviews, Microsoft's own metered price is small: a tenant with 60 guests pays about $180 a year [est from the $3/guest/year figure]. Our product only wins where the admin won't attach an Azure subscription, or wants member and sharing-link reviews too (member reviews need P2 per reviewed user). That's a narrow wedge, and CIPP may already cover the guest list for MSPs.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Search and MSP communities; marketplace needs Partner Center [fact: [verification](https://learn.microsoft.com/en-nz/partner-center/enroll/understand-the-verification-process)]. |
| Willingness to pay | 3 | Microsoft charges for the same reviews [report: Office 365 for IT Pros]; Syskit sells them from $3,600/year [vendor]. No sub-100-seat sales evidence. |
| Build effort | 3 | Graph reads, owner emails with signed links, evidence export [est]. |
| Operating load | 2 | Admin consent plus `Sites.Read.All`; owners who don't respond create follow-ups [assume]. |
| Owner time | 4 | Escalations only [assume]. |
| Legal and compliance load | 3 | Holds names and emails of guests and owners; standard privacy terms, no regulated data [assume]. |
| Sellability | 3 | Small governance SaaS, transferable [assume]. |
| Window | 3 | Persists while P2 stays outside Business Premium; closes if Microsoft bundles reviews into Business Premium [assume]. |
| Cost | 4 | Near $0 hosting at low volume plus email sending [est]. |

Disqualifiers checked: none apply.

## Economics (estimates, not forecasts)

- Price: $19/tenant/month flat, up to 100 users [est].
- Running cost at launch: under $10/month [est].
- Payment: MoR, about 5% + $0.50 [assume].
- $100/month of costs: about 6 tenants. $1k/month owner cash: about 60 tenants [est].

## Owner tasks that remain

- One-time: approve accounts; approve publishing.
- Weekly: escalations, under 1 hour [est].

## Validation plan

Free read-only script that lists guests with last sign-in and the groups they're in, plus external sharing links, published alongside the evidence-pack test if both survive (same repository, same 21 days, $0, owner approval to publish). Pass: 5+ organizations ask for the owner-email review. Fail: fewer than 2.

## Kill criteria

Fail on the test, or Microsoft adds access reviews to Business Premium.

## Exit

Fold into the evidence pack if both live; otherwise sell to an M365 governance vendor.

## Decision log

- 2026-10-11: screened by Claude (#58); ranked 2 of 3. Overlaps the evidence pack; consider merging if both pass.
