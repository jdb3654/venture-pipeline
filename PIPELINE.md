# Pipeline

One row per opportunity. Details live in `opportunities/<slug>.md`. Keep edits to this file small.

| Opportunity | Stage | Owner agent | Next step | Updated |
|---|---|---|---|---|
| [Forge replacements for orphaned Atlassian Connect apps](opportunities/atlassian-connect-replacements.md) | Screen → Validate recommended | claude | List retired or at-risk Connect apps with install counts; pick 1–2 targets | 2026-10-10 |
| [Manufacturing spreadsheet templates](opportunities/manufacturing-templates.md) | Validate | claude | TaktTools shop open; 4 listings saved as drafts (not published), waiting on owner review and publish; then 30-day test | 2026-10-10 |
| [Paid data tools on Apify (Actors/MCP)](opportunities/apify-niche-actors.md) | Screen | claude | Optional parallel test: 3 tools, 30 days | 2026-10-10 |
| [Niche Ignition SCADA module](opportunities/ignition-module.md) | Screen | claude | Mine Ignition forum for repeated unmet requests | 2026-10-10 |
| [Software-only downtime/OEE tracker](opportunities/small-shop-downtime-tracker.md) | Screen | claude | Wait on template results; then waitlist test | 2026-10-10 |
| Sunset-replacement watch (Shopify, Chrome, WordPress) | Signal | — | Agents watch marketplaces for apps being retired with large installed bases. Shopify's Stocky sunset drew replacement competitors quickly ([Prediko](https://www.prediko.io/stocky-sunsetting)), so speed matters | 2026-10-10 |
| [Opportunity Radar (cross-market discovery)](opportunities/opportunity-radar.md) | Signal | claude | Round 1 done, no market passes; owner to decide round 2 on platform sunsets | 2026-10-11 |
| Artist opportunity feed (ART-01, inherited) | Signal | — | Re-screen with the new template; see old repo `PORTFOLIO.md` | 2026-10-10 |

## Parked and killed

| Opportunity | Status | Reason | Reconsider if |
|---|---|---|---|
| Full machine-monitoring/OEE SaaS with sensors | Killed | Hardware installs and on-site support; crowded vendors priced per machine ([GlobalReader](https://www.globalreader.eu/blog/10-best-oee-software-for-sme-european-manufacturers)) | Never under the current brief |
| OPC UA / Modbus data logger app | Parked | Plant-floor connectivity support is environment-specific and urgent | Ignition research shows a software-only gap |
| ICS security advisory alerts matched to equipment | Parked | Similar Apify tool had 2 users ([Apify](https://apify.com/zentrafoundry/cisa-ics-advisory-asset-exposure-watcher)); free government alerts exist | Fold into the Apify test as one of its three tools |
| Google Sheets ↔ SQL database connector | Parked | Crowded (Coefficient and smaller rivals such as QueryStreams) | A specific database or workflow is clearly unserved |
| Generic Shopify app | Parked | Crowded; no specific gap found. 0% revenue share on the first $1M lifetime is attractive ([Shopify](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)) | Sunset watch finds a retired app with a large base |
| Generic WordPress plugin | Parked | Crowded and support-heavy (assumption) | Sunset watch finds a gap |
| Generic Chrome extension | Parked | Works for some indies (self-reported, mostly 2019–2021 figures, [ExtensionPay](https://extensionpay.com/articles/browser-extensions-make-money)), but needs a specific workflow | A specific professional workflow gap is found |
| Programmatic SEO calculator sites with ads | Parked | Needs large traffic; AI search answers reduce clicks (assumption) | Paired with a paid product as a lead source |
| LLM cost/usage monitoring for small teams | Killed | Crowded with funded and open-source tools (assumption, not sourced this round) | — |
| Selling agent skill packs or prompt templates | Killed | Easily copied, low willingness to pay (assumption) | — |
| Buying an existing micro-SaaS | Parked | Budget; average Acquire.com SaaS listing asks ~$484K ([Beancount.io](https://beancount.io/blog/2026/07/11/bootstrapped-saas-valuation-multiples-2026-acquire-com-indie-founders-guide)) | Portfolio profit can fund a small acquisition |
| Paid project / service work | Parked | Owner hasn't decided whether it's an acceptable stepping stone | Owner says yes |
| Niche public bid alerts (BID-01, inherited) | Parked | Free official alerts and cheap aggregators; wrong deadlines create urgent exceptions (old repo `2026-10-10/bid-alert-research.md`) | A segment with no free alerting is found |
| Agency DNS change monitoring (DNS-01, inherited) | Parked | No differentiation found in prior research | Old repo reconsideration trigger is met |
| Nine earlier parked ideas (print-file, visual regression, localization, subtitle, SCORM, Shopify catalog, SQL diagnostics, RFP, MSP handover) | Parked | See old repo `PORTFOLIO.md` | Their recorded triggers |
