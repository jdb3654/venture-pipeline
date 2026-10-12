# SMB marketplaces, round 1: Google Workspace, QuickBooks Online, HubSpot

Issue #65. Researched 2026-10-11 by Claude (file dated for the round). Budget about 60 lookups; used 60 (28 searches, 32 fetches; two fetches timed out, two returned empty pages). The last five checked Codex review findings. $0 spend. No accounts, outreach or publishing.

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. Pages checked 2026-10-11 unless a date is given. Installs, ratings, reviews and votes are engagement, not sales.

## Bottom line

**No candidate meets the "found" bar.** 13 candidates; none scores 4+ on both Distribution and Willingness to pay. Two came closest; after Codex review, one is held at Signal (three scores unsourced) and the other is parked:

| Rank | Candidate | Distribution | WTP | Lowest other | Falls short on |
|---|---|---|---|---|---|
| 1 | [Calendar time reports for client billing](../opportunities/gcal-client-time-reports.md) (Signal) | 3 | 4 | Operating load 2 | Distribution: a 189-review, 5-star incumbent at $12/user/month owns the search, and its reviews show no gap to fix |
| 2 | [Scheduled customer statements for QuickBooks Online below Advanced](../opportunities/qbo-scheduled-statements.md) (Parked) | 2 | 3 | Cost 1 | Both, and listing likely needs Intuit's $300/month Silver tier |

The pattern across all three marketplaces: where a published price exists, a well-reviewed paid app already serves the need; where a gap exists (tier-gated features, missing exports), nobody was found paying for it.

## Route map

### Google Workspace Marketplace

| Item | Finding | Label and source |
|---|---|---|
| How apps are listed | Google Cloud project, OAuth configuration, Marketplace SDK, store listing (website and logo required), then a Marketplace team review for public apps. Public/private choice is permanent. Admin allowlists can block installs. No listing fee mentioned. | [fact: [Google, updated 2026-09-03](https://developers.google.com/workspace/marketplace/how-to-publish)] |
| Who bills | We do. Google offers pricing labels only (Free, Paid with free trial, Paid with free features, Paid). Developers bill through Stripe or similar and gate features with their own licence check. | [fact: labels, [Google Developers Blog, 2021-10-13](https://developers.googleblog.com/app-pricing-update-details-and-editors-choice-now-available-on-google-workspace-marketplace/)]; [vendor: billing, [Mailmeteor, 2022-11-02](https://mailmeteor.com/blog/monetize-google-workspace-addon)]. Not confirmed on a Google page. |
| Platform cut, payout | 0% to Google; payout is whatever our MoR pays. | [assume], follows from the row above |
| Review / certification | Sensitive scopes (Google's own example: reading Calendar events) need brand verification, a justification per scope and a demo video, typically 3–5 business days, no assessment or fee mentioned. Restricted scopes (Gmail, Drive among others) need a CASA security assessment by an approved lab, renewed every 12 months: about $540–1,800 for Tier 2 (TAC Security), $4,500 for Tier 3 (needed for the security badge). 1–4 weeks of lab time; budget a couple of months. | [fact: sensitive, [Google, updated 2026-08-19](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification)]; [report: CASA, [DeepStrike, updated 2026-09-02](https://deepstrike.io/blog/google-casa-security-assessment-2025)]. DeepStrike's list of restricted data includes Calendar; Google's page contradicts it, so Calendar is treated as sensitive. |
| Accounts (all approval-gated) | Google Cloud project under a business Google account; a public website for the listing; MoR (#59). CASA lab contract only if restricted scopes. | as above |

**Cost and lead time:** $0 and a Marketplace review of unstated length for non-sensitive scopes (for example `spreadsheets.currentonly`) [assume on classification]; $0 and 3–5 business days more for sensitive scopes such as Calendar [fact]; plus $540+/year and weeks for restricted Gmail or Drive data [report].

### QuickBooks Online App Store

| Item | Finding | Label and source |
|---|---|---|
| How apps are listed | Production keys require an app assessment questionnaire (also for private apps). Technical review, then security review; critical, high and medium findings fixed before publishing; marketing requirements. Listed apps, and any app over 500 connections, are reviewed yearly; later findings fixed within 2 weeks. | [report: [Apideck connector docs, undated](https://developers.apideck.com/connectors/quickbooks/docs/application_owner+app_compliance)], summarising Intuit's [technical](https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/technical-requirements) and [security](https://developers.intuit.com/app/developer/qbo/docs/go-live/publish-app/security-requirements) requirements (not fetched) |
| Who bills | We do, as far as found: no Intuit app-store billing or revenue share appears in the partner-program coverage. | [assume]; [report: [ChannelE2E, 2025-07-29](https://www.channele2e.com/news/intuit-launches-app-partner-program-with-new-tiers-apis-and-pricing-model-for-developers)] doesn't mention any |
| Developer API fees (the Xero question) | **Yes, but with a free tier.** Intuit App Partner Program since 2025-07-28; fees live since 2025-11-01. Writes ("Core", data-in) free on all tiers. Reads ("CorePlus", data-out) metered: Builder $0/month with 500,000 calls, **blocked** above that; Silver $300/month with 1M then $3.50 per 1,000; Gold $1,700; Platinum $4,500. A payment method must be on file. Unlike Xero, API use alone can stay at $0, but see the listing tier below. | [report: [Apideck, updated 2026-10-06](https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program)]; Intuit's own FAQ didn't render |
| Listing tier | **Listing on the App Store likely needs the Silver tier ($300/month), not the free Builder tier**, per Intuit's App Partner Program Guide as cited in Codex's review of #66. Above the `BRIEF.md` budget, so QuickBooks App Store distribution is effectively closed to us for now. | [report: [Intuit guide via Codex review](https://static.developer.intuit.com/resources/Intuit_App_Partner_Program_Guide.pdf); not opened by Claude, round budget spent] |
| Platform cut, payout | None found. | [assume] |
| Accounts (all approval-gated) | Intuit developer account with company address and payment method on file; MoR (#59). | as above |

**Feature-request thread (left unread in round 2).** Intuit's UK Idea Exchange was archived on 2023-11-06; a user reported in May 2025 that only one idea was marked delivered in about 18 months [report: [QuickBooks Community](https://quickbooks.intuit.com/community/do-more-with-quickbooks-33/idea-exchange-board-archived-102929)]. The successor forum (feedback.qbo.intuit.com) is full of spam posts in search results [fact: search results 2026-10-11]. So Intuit's request boards are a weak demand source; individual Community threads were used instead.

### HubSpot App Marketplace

| Item | Finding | Label and source |
|---|---|---|
| How apps are listed | At least 3 active installs in unaffiliated production accounts in the last 30 days **before** submitting; unlisted apps capped at 25 installs; one app in review at a time; first review about 10 business days, the whole process up to about 60 days. Demo videos replaced test logins on 2026-03-31. Unneeded scopes are a rejection reason. | [report: [SpotDev, 2026-06-14](https://www.spotdev.co.uk/blog/how-to-list-a-saas-product-on-hubspot-app-marketplace)] |
| Certification | Listed 6+ months and 60+ active installs over a trailing 6 months; 2-year recertification. | same |
| Who bills | We do. Listing prices are "for display only"; buyers contact the partner. | [fact: e.g. [Calculations listing](https://ecosystem.hubspot.com/marketplace/apps/calculations-3449553)]; revenue share [assume] none |
| Platform changes | Projects 2025.1 support ended 2026-08-01. **Classic CRM cards stop rendering on 2026-10-31.** | [fact: [HubSpot developer blog, 2026-02-23](https://developers.hubspot.com/blog/developer-platform-migration-timeline)] |
| Accounts (all approval-gated) | HubSpot developer account [assume free]; 3 unaffiliated customers before listing; MoR (#59). | as above |

**Implication:** HubSpot's install threshold means the marketplace can't be our first demand test. Distribution there starts only after we find three users elsewhere.

## Denominator

13 candidates (5 Workspace, 4 QuickBooks, 4 HubSpot). 0 hit a hard disqualifier. 1 held at Signal as a near-miss; 10 parked (one near-miss, one folded into the Sunset-replacement watch); 1 killed; 1 not pursued (its lens came up empty).

Lenses per ecosystem: Workspace — retired apps (1, 2, 5), workarounds (4), AI (3), paid-app complaints (4). QuickBooks — long-open requests (6, 7, 9), workarounds (6), AI (8), paid-app complaints (9). HubSpot — long-open requests (11), workarounds (10), retired or breaking apps (13), paid-app complaints (12). Not used for HubSpot: AI.

| # | Ecosystem | Candidate | Outcome | Main reason |
|---|---|---|---|---|
| 1 | Workspace | Replace Gmail's POP fetch / Gmailify | Parked | PopRelay and Pop3Fetch already launched (Pop3Fetch free for one mailbox, CASA Tier 2, $0/month revenue shown); Google postponed the cut-off with no final date; Gmail write scope means CASA every year |
| 2 | Workspace | Google Tables replacement | Parked | Search titles only ([TechCrunch, 2025-09-11](https://techcrunch.com/2025/09/11/google-is-shutting-down-tables-its-airtable-rival/)); Airtable-class tools and AppSheet already absorb it [assume] |
| 3 | Workspace | AI/fuzzy record matching in Sheets | Parked | Flookup sells it at $10 per 30-day pass with 11 reviews ([GetApp](https://www.getapp.co.uk/software/2051824/flookup-for-google-sheets)); generic AI add-ons and Sheets' own AI functions overlap [assume] |
| 4 | Workspace | Calendar time reports for client billing | **Signal, near-miss 1** | See file; three scores need sources before Screen |
| 5 | Workspace | Doc generation after Autocrat | Not pursued | No evidence Autocrat is retiring (one search, nothing found) |
| 6 | QuickBooks | Audit-log export | Parked | One 2022 thread with one reply; workaround is print to PDF; nobody asked to pay ([Community](https://quickbooks.intuit.com/community/reports-accounting-69/can-i-export-the-audit-log-to-excel-160488)) |
| 7 | QuickBooks | Sales orders for ex-Desktop users | Parked | Served by inventory/order suites (ERPlain named by users); drifts toward inventory and production systems ([Community](https://ooxbu36397.lithium.com/learn-support/en-us/reports-and-accounting/re-how-do-i-create-a-sales-order-in-quikbooks-online/01/1486538)) |
| 8 | QuickBooks | AI PDF bank statement → QuickBooks import | Killed | Six paid converters with published prices (DocuClipper from $39/month, MoneyThumb from $24.95, ProperSoft $19.99, AutoEntry, Transaction Pro, Nanonets) [vendor: [DocuClipper](https://www.docuclipper.com/blog/best-pdf-to-qbo-converters/)]; bank statements raise data-handling load |
| 9 | QuickBooks | Scheduled customer statements below QBO Advanced | Parked (near-miss 2) | See file; listing likely needs the $300/month Silver tier |
| 10 | HubSpot | Notes/activities export | Parked | HubSpot added partial notes export (reported Feb 2024); Ultimate Data Export app exists ([Community](https://community.hubspot.com/t/exporting-notes/8235)) |
| 11 | HubSpot | Calculated properties for Free/Starter | Parked | Calculation apps are workflow actions, and workflows need Pro; no paid price found (Calculations by T&H Digital lists $0, 90+ installs) |
| 12 | HubSpot | HubSpot ↔ QuickBooks invoice sync gaps | Parked | HubSpot's free native app syncs contacts, products, invoices, credit memos and payments both ways ([HubSpot KB, 2026-07-21](https://knowledge.hubspot.com/integrations/connect-hubspot-and-quickbooks-online?data=data)); paid rival Commercient starts at $900/month with fewer than 10 installs ([listing](https://ecosystem.hubspot.com/marketplace/apps/quickbooks-online-sync-commercient)) |
| 13 | HubSpot | Apps orphaned when classic CRM cards stop rendering | Parked into the Sunset-replacement watch | Date is fixed (2026-10-31), but no specific abandoned app with paying users was identified this round |

## Overlap with earlier rounds

- Candidate 3 differs from the parked Sheets–SQL connector: it matches records inside one sheet, with no database connection.
- Candidate 9 differs from the M365 and Xero work: it is a QuickBooks tier gap, and QuickBooks' Builder API tier is $0 where Xero's isn't.
- Candidate 13 is a new source for the existing Sunset-replacement watch, not a new opportunity.
