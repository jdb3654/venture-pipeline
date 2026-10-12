# SMB marketplaces, round 2: monday.com, Figma Community, GitHub Marketplace

Issue #67 (round 2 of up to 3; round 1 was #65 / #66). Researched 2026-10-12 by Claude in one scheduled session. Budget about 60 lookups; used 56 (28 searches, 28 fetches; one fetch was refused by the fetch tool and one hit a redirect, both counted). $0 spend. No accounts, outreach or publishing.

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report (forum posts, third-party write-ups), **[vendor]** vendor claim (including the platform's own marketing), **[est]** estimate, **[assume]** assumption, **[title]** search-result title only, page not opened. Pages checked 2026-10-12 unless a date is given. Installs, ratings, reviews, likes and views are engagement, not sales.

## Bottom line

**No candidate meets the "found" bar.** 17 candidates; none scores 4+ on both Distribution and Willingness to pay with no factor below 2. Wherever a published price showed that people pay (backups, time-in-status, email reports, merge queues, token sync, changelogs), a named vendor already sells it. Where a gap had no seller (library analytics on Figma Pro, deployment approvals on GitHub Team), a free tool or nothing at all showed that people won't pay.

One near-miss is filed:

| Rank | Candidate | Dist | WTP | Lowest other | Falls short on |
|---|---|---|---|---|---|
| 1 | [Scheduled board email reports for monday.com](../opportunities/monday-board-email-reports.md) (Signal, near-miss) | 3 | 4 | 3 (several, mostly assumptions) | Distribution: Stiltsoft already sells exactly this on the monday marketplace; native monday features may overlap [assume, not checked]. Its demand test also needs a monday developer account and Payoneer, so it fails the "no new account" part of the bar. |

A second near-miss was considered and not filed: Figma variables sync for non-Enterprise plans (WTP 3, Distribution 3). Free sync already exists, so it is parked rather than given a file.

**Pattern worth recording:** Atlassian Marketplace vendors (SaaSJet, Stiltsoft, Appfire's BigPicture, resolution) are porting their Jira apps to monday.com with seat-tier prices [fact: their help pages, below]. The proven Jira categories are already being carried across by vendors who own the Jira listings. That makes "port a proven Jira app to monday" a crowded play, not an open one.

## Route map

### monday.com apps marketplace

| Item | Finding | Label and source |
|---|---|---|
| How apps are listed | New apps need marketplace approval before publishing. Prerequisites: app submitted, pricing and plan tiers defined, Payoneer eligibility verified, webhook endpoints ready, subscription test plan. The page names an app review checklist but this round didn't open it. | [fact: [monday dev docs, Implement monetization](https://developer.monday.com/apps/docs/implementing-monetization)] |
| Who bills | **monday.com.** "All new marketplace apps must use monday's built-in monetization." monday collects payments and handles renewals, taxes and compliance, so it acts as merchant and our MoR (#59) isn't needed for monday-only sales. The app must enforce plan limits itself. | [fact: same docs page]; [vendor: taxes, [monday.com/appsdeveloper](https://monday.com/appsdeveloper)] |
| Platform cut | **0% until $200,000 lifetime app revenue**, then 15% ("85% of revenue goes to you and 15% goes to monday.com"). Revenue-share program announced 2024-06-17. | [vendor: [monday.com/appsdeveloper](https://monday.com/appsdeveloper)]; [fact: date, [changelog](https://developer.monday.com/apps/changelog/announcing-the-revshare-program)] |
| Payout | Monthly, via Payoneer, after you register as a vendor ("You can't receive payments from monday until this process is completed"). No minimum is stated. | [fact: docs page above] |
| Pricing models | Feature tiers and seat-bucket tiers (up to 20 seat tiers). Seat-based pricing is available to all monetized apps. All accounts support monetization (staff, 2023-08-16). | [report: [Untapped pricing report for monday, Feb 2024](https://dapulse-res.cloudinary.com/image/upload/v1711643936/remote_mondaycom_static/uploads/DiproBhowmik/App%20Pricing%20Document%20-%20Untapped/monday.com_-_Developer_Pricing_Report.pdf)]; [title: [seat-based pricing changelog](https://developer.monday.com/apps/changelog/seat-based-pricing-available-for-all-monetized-apps)]; [report: [developer community](https://developer-community.monday.com/api-apps-framework-4/what-percentage-of-users-customers-are-supported-by-the-monday-monetization-framework-2082)] |
| Size | About 250k customers, 850+ live apps, 1.6M installs; 49% of accounts have installed at least one app. Partner tiers start at Bronze for $5K ARR; ProBackup announced Bronze status, which implies at least $5K ARR from one small vendor's monday app. | [vendor: [monday.com/appsdeveloper](https://monday.com/appsdeveloper)]; [title: [ProBackup blog](https://www.probackup.io/blog/probackup-earns-bronze-partner-status-on-the-monday-com-marketplace)] |
| Accounts (all approval-gated) | monday account to build and test in [assume: free developer account, not verified]; marketplace submission and approval [fact]; Payoneer account and monday vendor registration [fact]. | as above |

**Cost and lead time:** $0 in fees found [vendor]. Lead time: approval review of unstated length plus Payoneer onboarding [fact that both exist; length unknown]. **monday is the cheapest route found in either round for getting paid inside a marketplace**: no cut until $200K, and monday is the merchant. It is still approval-gated end to end.

### Figma Community (paid plugins)

| Item | Finding | Label and source |
|---|---|---|
| How plugins are listed | Published to Figma Community from a Figma account. Paid resources can be published only from individual accounts "approved to sell on Community." | [fact: [Figma Help, About selling Community resources](https://help.figma.com/hc/en-us/articles/12067637274519-About-selling-Community-resources), undated] |
| Seller approval (the gate) | The help page says Figma is "not approving new creators to sell paid files." Staff said on 2025-09-10 that new **plugin and widget** sellers are being approved. Developers reported on 2026-03-26 and 2026-03-30 that the Price field was still disabled, with no staff reply. Treat native selling as uncertain for a new seller. | [fact: help page]; [report: [Figma forum](https://forum.figma.com/ask-the-community-7/is-it-currently-impossible-to-sell-a-figma-plugin-yes-or-no-42302)] |
| Who bills (native) | Figma. 15% flat fee per sale, covering card processing, purchase support, **sales-tax collection**, delivery and fraud monitoring. Plugins can be one-time or subscription, minimum $2 in whole USD; subscription price rises are capped at 50% once every 30 days; 7-day trial by default. | [fact: help page] |
| Payout (native) | Cash-out 30 US business days after a sale, at most once a week; 76 payout countries; non-US creators file W-8 forms. No minimum stated. | [fact: help page] |
| Who bills (external) | Allowed: staff confirmed on 2025-07-14 that plugins can be monetized with third-party payment pages, linked from the plugin UI and the Community description (no in-plugin payment form, per 2022 staff). So the MoR route (#59) works without Figma's seller approval. | [report: staff replies, same forum thread] |
| Platform API limits that shape demand | The Variables REST API is Enterprise-only (thread opened 2023-08-23, 33 replies, still complained about on 2026-05-03); plugins can read variables on any plan. | [report: [Figma forum](https://forum.figma.com/suggest-a-feature-11/why-s-the-variables-api-only-available-on-enterprise-plans-36426/index4.html)] |
| Accounts (all approval-gated) | Figma account (free plan exists [assume]); either Figma seller approval + Stripe via Figma, or the MoR from #59. Plugin review time not checked this round. | as above |

**Cost and lead time:** native: 15% of sales, 30-business-day payout lag, and seller approval that may not be granted [fact/report]. External: MoR fees only, but the buyer leaves Figma to pay, so the "built-in billing" advantage is lost [assume].

### GitHub Marketplace

| Item | Finding | Label and source |
|---|---|---|
| How paid apps are listed | App must be owned by an organization that is a **verified publisher** (DNS TXT domain verification, verified email, 2FA on the org). GitHub Apps "should" have **100+ installations** (OAuth apps 200+ users) before a paid listing. Publicly available, privacy policy, support contact, Marketplace Developer Agreement; then request verification of the listing. Adding a paid plan needs verification and financial onboarding. | [fact: [GitHub Docs, requirements for listing an app](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app)]; [fact: verification steps, [GitHub blog, 2021-02-04](https://github.blog/news-insights/company-news/github-reduces-marketplace-transaction-fees-revamps-technology-partner-program/)] |
| Who bills | **GitHub**, on the customer's GitHub payment method. Flat-rate or per-user plans, up to 10 plans, monthly **and** annual price required for each, fixed 14-day trials (one per customer per product). If a paid version is sold outside Marketplace, a free Marketplace listing must also offer a paid plan in Marketplace. | [fact: [GitHub Docs, pricing plans](https://docs.github.com/en/apps/github-marketplace/selling-your-app-on-github-marketplace/pricing-plans-for-github-marketplace-apps)]; [fact: listing requirements page] |
| Platform cut | 5% (since 2021-01-01; 25% before). | [fact: [GitHub Docs, receiving payment](https://docs.github.com/en/apps/github-marketplace/selling-your-app-on-github-marketplace/receiving-payment-for-app-purchases)] |
| Payout | Monthly, **only once the month's revenue reaches $500**; paid at the end of the following month, by electronic payment. | [fact: same page] |
| Native features moving in | GitHub Code Quality priced at $10 per active committer/month, GA 2026-07-20. GitHub Classroom deprecated 2026-08-28 in favour of unnamed partners. | [title: [GitHub changelog](https://github.blog/changelog/2026-06-16-github-code-quality-generally-available-july-20-2026)]; [fact: [GitHub changelog](https://github.blog/changelog/2026-08-27-github-classroom-deprecated)] |
| Accounts (all approval-gated) | GitHub organization for the product (separate from the owner's personal account, for sellability); a domain we control for DNS verification (**costs money: a domain**, about $10–15/year [est]); publisher verification; financial onboarding. | as above |

**Cost and lead time:** 5% fee, plus a domain [est $10–15/year]; months of lead time, since a paid listing needs ~100 installs first. **Like HubSpot in round 1, GitHub Marketplace can't be the first demand test.** Sales before that would go through the MoR (#59), and the $500/month payout floor makes small early revenue lumpy.

## Denominator

17 candidates (8 monday.com, 4 Figma, 5 GitHub). 0 hit a hard disqualifier. 1 near-miss held at Signal; 12 parked; 3 killed; 1 not pursued (its lens came up empty).

Lenses per ecosystem: monday — long-open requests (2, 3, 8), retired apps (searched; nothing found), workarounds (3, 8), paid apps and their pricing (1, 4, 5, 6, 7). AI not used. Figma — long-open requests (9), workarounds for plan limits (9, 10), retired plugins (12), paid apps (11). AI covered only by assumption (Figma's own AI). GitHub — retired features (13), workarounds for plan limits (14, 15), AI (16, 17), paid apps and their pricing (15, 16). Long-open requests: one search returned nothing usable; 14 was a July 2026 request.

| # | Ecosystem | Candidate | Outcome | Main reason |
|---|---|---|---|---|
| 1 | monday | Board backup and restore | Parked | Rewind is documented in monday's own support centre; ProBackup (Bronze partner) and Board & Doc Backups also sell it [title: [monday support](https://support.monday.com/hc/en-us/articles/27928614737042-Back-up-and-restore-your-data-with-Rewind-backups), [ProBackup](https://www.probackup.io/compare/probackup-vs-rewind-for-monday-com)]; needs account-wide read access, the highest security load |
| 2 | monday | Print or PDF of the Updates tab | Parked | DocCreate and The PDF Maker are recommended in the request thread; requesters there say third-party apps aren't allowed for them, which cuts the paying pool [report: [community](https://community.monday.com/t/export-pdf-or-print-updates-tab-view-to-pdf/43609?page=2)] |
| 3 | monday | Items and updates combined in one Excel export | Parked | One thread, no replies visible, no price anyone pays [report: [community](https://community.monday.com/t/export-main-table-updates-together-in-one-excel-sheet/115044)]; sibling threads exist [title: [subitem updates](https://community.monday.com/t/export-subitem-updates/70758)] |
| 4 | monday | Time tracking and billable hours | Killed | Everhour, Harvest and TimeBits already integrate [title: [Everhour](https://everhour.com/time-tracking/time-tracking-app-for-mondaycom), [Harvest](https://www.getharvest.com/time-tracking/time-tracking-app-for-mondaycom), [TimeBits](https://community.monday.com/t/introducing-timebits-the-ultimate-time-tracking-power-up-for-monday-com/113868)]; overlaps the existing calendar time-reports near-miss |
| 5 | monday | Time in status / cycle-time reports | Parked | SaaSJet sells it from $2/month (2 seats) to $84/month (unlimited) [vendor: [SaaSJet help, modified 2025-12-03](https://help.saasjet.com/monday/how-to-calculate-the-price-for-app-on-your-monday-account)] |
| 6 | monday | Email to items | Parked | SaaSJet Email to Tasks & Capture, $10–300/month [vendor: same page]; monday's native email integration likely overlaps [assume] |
| 7 | monday | Scheduled board email reports | **Signal, near-miss** | See file. Stiltsoft Board Email Reports, $10–500/month [vendor] |
| 8 | monday | Required fields / item validation | Parked | resolution.de sells a "required fields automation" app [title: [resolution wiki](https://wiki.resolution.de/doc/monday-required-fields-automation/installation)]; page redirected, price not seen |
| 9 | Figma | Variables → code/Git sync for non-Enterprise plans | Parked | Real long-open complaint (2023-08-23 to 2026-05-03) [report: forum], but Tokens Studio's free plan includes Git sync, with Plus at €39–49/user/month [vendor: [Tokens Studio](https://tokens.studio/pro-pricing)]; Design System Sync launched 2026-04-25 at $10/month (0 replies, 179 views) [report: [forum](https://forum.figma.com/share-your-feedback-26/export-figma-variables-directly-to-github-as-pull-requests-53332)]; TokensBrücke is free [title: [README](https://cdn.jsdelivr.net/npm/tokens-bruecke@3.15.1/README.md)] |
| 10 | Figma | Library/component-usage analytics for Pro plans | Parked | No paid competitor and no request thread found in one search; Figma keeps it for higher plans [title: [Figma Help](https://help.figma.com/hc/en-us/articles/360039238353-Track-library-and-component-usage)] |
| 11 | Figma | Logic-driven prototyping | Parked | Prototyper by Mighty (paid) and ProtoPie Connect ($17/month) [report: [Line25, 2026-04-13](https://line25.com/articles/best-figma-plugins-for-web-designers/)]; Figma's own AI prototyping likely overlaps [assume] |
| 12 | Figma | Replacement for a retired paid plugin | Not pursued | One search found no retired plugin with paying users |
| 13 | GitHub | GitHub Classroom replacement | Parked | Classroom 50 (free, open source, from CS50's nonprofit, announced 2026-07-01) [report: [Elgort, 2026-07-20](https://bruceelgort.com/2026/07/20/github-classroom-is-gone-heres-the-free-tool-that-replaces-it/)]; Codio markets itself as the paid successor [title: [Codio](https://www.codio.com/after-github-classroom)]; school procurement and student data add load |
| 14 | GitHub | Deployment approvals for private repos on Free/Pro/Team | Parked | Real gap: required reviewers on environments need Enterprise for private repos [report: [community, 2026-07-24](https://github.com/orgs/community/discussions/202852)]; but the free, widely forked `manual-approval` action covers it [title: [Marketplace](https://github.com:443/marketplace/actions/manual-workflow-approval?version=v1.7.0)]; no paid competitor found |
| 15 | GitHub | Merge queue for private repos below Enterprise | Killed | Mergify from $8/user/month (free for ≤5 private contributors) [report: [Stackpick, Jul 2026](https://www.stackpick.net/pricing/mergify/)], plus funded Trunk, Aviator and Graphite [title: [Trunk](https://www.trunk.io/trunk-vs-aviator)]; critical-path CI with repo write access is a high operating and security load; Build effort 1 |
| 16 | GitHub | AI release notes from PRs | Parked | ReleasePad $35/month drafts notes from GitHub PRs; git-cliff is free; eight more changelog tools from $25/month [report: [ReleasePad blog, 2026-08-07, author's own product ranked first](https://www.releasepad.io/blog/best-changelog-tools/)] |
| 17 | GitHub | AI code-quality / PR review app | Killed | GitHub Code Quality at $10/committer/month, GA 2026-07-20 [title: changelog above]; CodeRabbit and Copilot review crowd it [assume] |

## Overlap with earlier rounds

- 4 overlaps the calendar time-reports near-miss (round 1), so it is killed here rather than re-screened.
- 9 and 14 differ from the parked "Paid PowerShell module / VS Code extension" (round 1 Microsoft): they would be listed in Figma or GitHub, not in those marketplaces.
- 1 is not the parked "Sheets ↔ SQL connector"; it is a backup of one SaaS.
- The Atlassian-porting pattern bears on [Forge replacements for orphaned Atlassian Connect apps](../opportunities/atlassian-connect-replacements.md): the same vendors are moving across ecosystems, so a gap they leave on Atlassian is likely a gap they can't be bothered to fill [assume].

## Round 3 proposal

Owner-listed candidates were Zapier/Make, Notion and Salesforce AppExchange. Round 1 already argued against all three (no paid route for Zapier/Make integrations; Notion templates easily copied; AppExchange review and revenue share above budget), all as assumptions. This round's finding is that **platform-billed marketplaces with a low cut (monday) are the cheapest route**, so round 3 should look for more of those. Proposed instead (each is an assumption to verify in round 3):

1. **Wix App Market**: Wix bills site owners for apps, and its buyers are small businesses that don't write code [assume].
2. **Pipedrive Marketplace**: SMB sales CRM with a marketplace, smaller than HubSpot's, and no install threshold known [assume].
3. **Zendesk Marketplace**: paid apps for small support teams; a support-tool buyer is used to per-agent pricing [assume].

If the owner prefers the original list, Notion is the strongest of the three: its template marketplace bills buyers directly [assume].
