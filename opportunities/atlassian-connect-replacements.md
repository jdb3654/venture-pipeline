# Forge replacements for orphaned Atlassian Connect apps

- **Slug:** atlassian-connect-replacements
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-10 / 2026-10-10

## The idea in two sentences

Atlassian ends support for its older Connect app framework around the end of 2026, and some Marketplace apps will be retired rather than rebuilt on Forge. Build small Forge-native replacements for retired apps that still have a real installed base, and sell them on the Atlassian Marketplace to the admins who are being told their app may stop working.

## Signal

- Connect timeline (verified, Atlassian blog, checked 2026-10-10): no more Connect app updates after March 31, 2026; Connect end of support at the end of 2026, after which Connect is use-at-your-own-risk with no security patches. [Atlassian](https://www.atlassian.com/blog/developer/connect-end-of-support-what-it-means-for-custom-apps-and-how-to-migrate-to-forge)
- Jira admins now see an in-product banner warning that apps not fully on Forge may stop working after January 2027 (first-hand vendor report, 2026-09-04). [Exalate community](https://community.exalate.com/t/jira-cloud-this-app-may-stop-working-after-december-january-2027-warning-atlassian-connect-deprecation/8353)
- Atlassian staff describe the banner as driven by each app's declared migration intent; no public count of apps that won't migrate exists (developer forum, 2026-09-11/13). [Atlassian developer community](https://community.developer.atlassian.com/t/connect-end-of-support-status-of-a-specific-app-and-the-admin-at-risk-banner/102640)
- At least one vendor retired four apps while consolidating around Forge (vendor post, Oct 2025, updated Jul 2026). [Amoeboids](https://amoeboids.com/blog/slimming-down-atlassian-marketplace-portfolio/)

## Customers and distribution

- **Buyer:** Jira/Confluence/JSM admins at companies whose existing app is retired or flagged at risk. They already pay for apps and already have Marketplace billing set up.
- **Distribution:** Marketplace search, plus being findable when admins search for an alternative to the specific retired app. This is the strongest built-in distribution of anything screened in this round.
- **Competition:** unknown per niche. Large vendors will migrate their popular apps; the opportunity is mid-sized apps whose vendors give up. Pattern evidence from Shopify: when Shopify sunset its Stocky inventory app (removed from the App Store Feb 2, 2026; APIs off Aug 31, 2026), several competitors published "Stocky replacement" pages quickly. [Prediko](https://www.prediko.io/stocky-sunsetting), [inFlow](https://www.inflowinventory.com/blog/stocky-shopify-app-sunsetting/). Expect the same speed here, so the replacement has to be picked early and narrowly.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 5 | Marketplace with paying buyers, and an in-product banner pushing admins to look for alternatives. |
| Willingness to pay | 4 | Buyers already pay for the retired app. Exact WTP depends on the app chosen (assumption until a target is picked). |
| Build effort | 3 | Forge is a new framework for the owner; a narrow app is weeks of agent work, not months (estimate). |
| Operating load | 3 | Jira admins expect responsive support and data migration help (assumption). |
| Owner time | 3 | Mostly escalations; Marketplace security and listing requirements add periodic work (assumption). |
| Legal and compliance load | 3 | Customer data stays on Atlassian's platform with Forge, which helps; Marketplace partner agreement and security requirements apply (verify). |
| Sellability | 4 | Marketplace apps are a recognized acquisition category (assumption; no source checked yet). |
| Window | 3 | Open now through roughly early 2027, then closes as admins switch. Must move within weeks. |
| Cost | 4 | Apps qualifying for Atlassian's "Runs on Atlassian" program keep 100% of earnings up to $1M lifetime Forge revenue (applies to all qualifying Forge apps from Jan 1, 2026); the standard Forge rate rose to 16% on Apr 1, 2026 and 17% on Oct 1, 2026. Building to qualify for that program is a design requirement. Hosting costs on Forge not yet checked. [Atlassian](https://www.atlassian.com/blog/developer/updates-to-marketplace-revenue-share-2026), [timeline extension](https://www.atlassian.com/blog/developer/extended-timelines-for-marketplace-revenue-share-changes) |

Disqualifiers checked: none apply.

## Economics (estimates, not forecasts)

- Pricing follows Marketplace per-user tiers; set by matching the retired app.
- Monthly running cost at launch: likely near $0 on Forge free allowances (unverified).
- Payment: Atlassian bills customers and pays the vendor. Confirm how sales tax is handled and what the partner agreement requires.
- Break-even is likely a handful of paying sites; real numbers depend on the chosen app.

## Owner tasks that remain

- One-time: Marketplace partner account and vendor agreement (owner approval needed).
- Weekly: answer escalated support tickets (estimate under 1 hour).
- Per release: approve listing changes.

## Validation plan

1. Agents compile a list of Connect apps that are retired or unlikely to migrate (vendor announcements, at-risk banner discussions, apps with no Forge version listed on forge-apps.com, a third-party site mentioned in the forum thread above), with install counts and review complaints.
2. Pick the 1–2 with the most installs and no Forge alternative.
3. Publish a free or low-priced Forge version of the core feature; measure installs and trial-to-paid in 30 days.
- Cost: $0 beyond agent time until listing. Pass: 50+ installs or 3+ paid conversions in 30 days (threshold is a hypothesis).

## Kill criteria

No viable orphaned app with 500+ installs found by end of October 2026, or a funded vendor ships a Forge replacement first.

## Exit

Sell to an Atlassian app vendor or on Acquire.com. Keep a dedicated partner account and support inbox so it can transfer.

## Decision log

- 2026-10-10: screened by Claude; recommended for Validate.
