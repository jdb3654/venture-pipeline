# Opportunity Radar: source-discovery round 1

Issue #52. Researched 2026-10-11 by Claude. Budget: one session, about 40 lookups (used about 39), $0 spend, no collection runs. Source registry: [`radar-sources.csv`](radar-sources.csv).

Labels: **[fact]** verified on the cited page, **[txn]** completed transaction, **[report]** first-hand report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption.

## Decision memo

**No market passes the gates yet, and the direct-resale half of the prompt mostly fails `BRIEF.md`.** One signal type is worth a second, bounded round: platform sunsets (closed WordPress plugins first), which the pipeline already tracks as "Sunset-replacement watch" and which we can act on with software rather than capital.

1. **No sign that raw public-signal feeds sell.** Others already resell WARN layoffs, bankruptcy filings and ICS advisories as per-result feeds, each with 1–2 total users. Apify's `total_users` includes the actor's owner and doesn't show payments ([Apify docs](https://docs.apify.com/api/client/python/reference/class/ActorStats)), so this is weak engagement evidence: willingness to pay is unknown, not disproven. What it does show is that building the feed is easy and already done. [fact on counts; inference on demand]
2. **Physical resale hits a disqualifier.** Government surplus needs pickup within 5–10 business days, sells as-is with no returns, and lands 15–25% above the hammer price before shrink. [vendor] That puts the owner on-site, which `AGENTS.md` disqualifies.
3. **Completed-sale comps exist but are approval-gated.** eBay's sold-items API is limited release, and small developers report being refused [report]. eBay's Seller Hub Product Research shows 3 years of sold prices to sellers ([eBay help](https://www.ebay.com/help/selling/selling-tools/product-research?id=4853)) [fact], but it is a manual tool behind a seller account (owner approval) with no stated API or export. So comps can verify a handful of finds by hand, not feed an automated valuation. This doesn't rescue surplus resale, which already fails on the on-site rule.
4. **Brokering is licensed.** In Idaho, referral fees to unlicensed people are prohibited fee splitting. [fact, Idaho guidance] Assume the same for real-estate "facilitation" elsewhere until checked.
5. **Procurement intelligence does sell, but it's crowded.** HigherGov charges $500–$2,500 a year. [vendor, via a competitor's page] Free official alerts exist, so BID-01 stays parked.

**Next bounded action (owner decision, issue to follow):** one session to count closed WordPress plugins with large installed bases over the last 90 days, and check whether replacements already appear. Pass: at least 2 closures with 10,000+ installs and no maintained fork or clear replacement. Fail: stop and fold the watch into the existing Signal row.

## Signal ledger (denominator)

13 records reviewed; 0 pass all four gates. Rejections keep their reasons.

| # | Category | Signal | Evidence | Label | Outcome |
|---|---|---|---|---|---|
| 1 | Closures | WARN layoff/closure feed (CA, TX) on Apify, $0.005 per notice; targets liquidators, CRE brokers, recruiters | [Apify](https://apify.com/deadwood_data_solutions/warn-layoff-signal-feed) | fact: 1 total user (may be only the publisher) | No demand evidence; willingness to pay unknown |
| 2 | Closures | At least 5 other WARN monitors on Apify | [search, 2026-10-11](https://apify.com/tagadanar/us-warn-layoffs) | fact | Crowded free-data resale |
| 3 | Closures | Bankruptcy monitor built on CourtListener's free API, $5 per 1,000 rows | [Apify](https://apify.com/lavender_whistle/bankruptcy-filings-monitor) | fact: 2 total users incl. owner, 1 monthly | No demand evidence; willingness to pay unknown |
| 4 | Surplus | GSA Auctions: public API for federal surplus listings | [data.gov](https://catalog.data.gov/dataset/gsa-auctions-api) | fact (fields unconfirmed) | Keep as a source; no buyer route |
| 5 | Surplus | GovDeals buyer costs: 5–10% premium, 5–10 day pickup, as-is, $150–$400 pallet freight, 25–30% shrink on untested electronics | [Closo, Sep 2026](https://closo.co/blogs/inventory-liquidation/govdeals-liquidation) | vendor (sells wholesale lots) | Reject direct action: on-site disqualifier |
| 6 | Surplus | GovDeals scrapers sold by third parties | [Apify](https://apify.com/parseforge/govdeals-scraper) | fact | Not permission; terms unread, so paused |
| 7 | Resale comps | eBay Marketplace Insights limited; small devs denied | [eBay community](https://community.ebay.com/t5/eBay-APIs-Talk-to-your-fellow/Marketplace-Insights-API-access/m-p/34838736) | report | API closed to us; see row 13 |
| 8 | Consumer resale | Keepa API sells Amazon price history by tokens | [Keepa](https://keepa.com/api-docs/plans-tokens.html) | fact | Incumbent data; needs spend and inventory capital |
| 9 | Discontinued parts | Octopart/Nexar API: closed beta, lifecycle status an add-on, prices after sign-up | [Altium](https://developer.altium.com/octopart-api-plans) | fact | Reject now; counterfeit risk for brokers [assume] |
| 10 | Procurement | HigherGov $500/yr (1 user) to $2,500/yr (10 users) | [Gov Contract Finder, checked Jul 2026](https://govcontractfinder.com/compare/highergov/pricing) | vendor (competitor's page) | WTP exists; crowded; BID-01 parked |
| 11 | Real estate | Unlicensed referral fees prohibited (Idaho) | [Idaho REC guideline](https://dopl.idaho.gov/wp-content/uploads/2023/11/REC-Guideline-10-rev-03.19.pdf) | fact | Reject facilitation without a license |
| 12 | Digital assets | WordPress plugin with 4,000+ installs closed permanently for a security issue on 2026-04-07 | [WordPress.org](https://wordpress.org/plugins/post-grid-and-filter-ultimate/advanced/) | fact | **Keep:** orphaned users, act with software |
| 13 | Resale comps | eBay Seller Hub Product Research: 3 years of sold prices, manual, seller account needed | [eBay help](https://www.ebay.com/help/selling/selling-tools/product-research?id=4853) | fact | Approval-gated; usable for manual spot checks only |

Not covered this round: domain aftermarket (NameBio failed to load), regional price gaps, collectibles, permits. Regulatory triggers: the Federal Register API needs no key [fact], but nothing here shows anyone pays for the alerts.

## Markets compared

Scores 1–5 (5 best), subjective, from this round's evidence only. Weights favour what `BRIEF.md` constrains most.

| Market | Lawful repeatable source (×3) | Buyer or act route (×3) | Owner time fits (×3) | Capital (×2) | Competition (×1) | Weighted /60 | Confidence |
|---|---|---|---|---|---|---|---|
| Platform sunsets (WP, Shopify, Chrome, Atlassian) | 4 | 3 | 4 | 5 | 3 | 46 | low (1 instance) |
| Regulatory triggers | 5 | 1 | 4 | 5 | 3 | 43 | low |
| Closures → intelligence feed | 4 | 2 | 4 | 5 | 2 | 42 | low |
| Gov procurement intelligence | 4 | 2 | 4 | 5 | 1 | 41 | medium |
| Consumer resale arbitrage | 3 | 3 | 2 | 1 | 1 | 27 | low |
| Gov surplus → resale | 3 | 2 | 1 | 2 | 2 | 24 | medium |
| Discontinued parts | 1 | 2 | 3 | 2 | 2 | 24 | low |
| Real estate signals | 2 | 1 | 2 | 1 | 2 | 19 | low |

Read the top row as "worth one more session", not "attractive market". Regulatory triggers rank second only because access is easy; with no buyer they belong as inputs to other markets, not as a market.

## Gates (predeclared for round 2)

A market reaches Validate only with all four: (1) a lawful, repeatable source with confirmed collection method; (2) a named buyer or direct-action route within `BRIEF.md`; (3) at least two independently checked instances with positive conservative economics; (4) owner time under about 2 hours a week and no on-site work. Report the denominator (scanned, filtered, reviewed, rejected, verified) and compare against a manual search of the same sources with a fixed time box.

## Opportunity score (individual finds)

Net upside after all costs ×3, valuation evidence ×3 (completed sales only score above 2), identification confidence ×2, ability to act under `BRIEF.md` ×3, downside/capital at risk ×2, time sensitivity ×1. Any disqualifier in `AGENTS.md` sets the score to 0.

## Smallest design, when evidence justifies it (not built)

- **Registry:** the CSV above. Add `last_attempt`, `last_success`, `last_change` and `last_error` columns only when a collector exists.
- **Store:** one SQLite file with three tables: `observation` (source_id, external_id, content_hash, event/published/detected timestamps, raw JSON), `signal` (normalized fields, dedupe key, status, rejection reason) and `review` (valuation, skeptic notes, verified_at, outcome). Six timestamps from the prompt map to: event, published, detected (observation); verified, actionable, expired (review).
- **Run:** one scheduled GitHub Actions job per cadence group, each calling a small deterministic collector that does conditional requests and hash-based change detection, then appends a Markdown digest to an issue. LLM calls only on signals that pass deterministic filters, with a per-run cost cap that suspends the job. Home server untouched.
- **Agents:** discovery and extraction are code; matching, valuation and the decision are one LLM pass; the skeptic is the other agent via the existing `case-against` skill, which already gives independence.
- **Alerts:** critical goes to a `needs:owner` issue; high to a daily digest issue; medium stays in the database; low is archived with its reason.

## 21-day plan, re-scoped

The prompt's 150-signal target assumes collection at scale. This round found that most categories fail on owner time, capital or licensing before collection matters, so the plan narrows to one category with a no-go exit.

| Days | Work | Stop rule |
|---|---|---|
| 1–3 | Round 2: count recent high-install WordPress closures; check Shopify/Chrome/Atlassian sunset sources for a sanctioned feed | Fewer than 2 qualifying closures in 90 days: stop |
| 4–10 | Manual watch, logged in the ledger: time to replacement appearing, migration complaints on support forums | No orphaned-user complaints found: park |
| 11–15 | `case-against` by Codex on the best target | Any disqualifier: kill |
| 16–21 | If one target survives, it enters the normal pipeline as its own opportunity | — |

$0 throughout. A collector is built only if the manual watch finds signals faster than the manual baseline can handle.
