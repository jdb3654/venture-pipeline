# Software-only downtime and OEE tracker for small shops

- **Slug:** small-shop-downtime-tracker
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-10 / 2026-10-10

## The idea in two sentences

A simple web app that small manufacturers use on a shop-floor tablet to log downtime and output, with automatic OEE reports and an optional CSV or database import. No sensors or hardware, priced per site rather than per machine.

## Signal

- Mid-market OEE tools are priced per machine and usually bundle hardware. One vendor's July 2026 comparison lists, for example, FourJaw at about €105 per machine per month plus a sensor with a 5-machine minimum, Evocon at €189–319 per machine per month with a 1-year minimum, and Guidewheel from about $15,000 a year. Prices are as reported by a competing vendor. [GlobalReader](https://www.globalreader.eu/blog/10-best-oee-software-for-sme-european-manufacturers)
- The free end is spreadsheets and limited free tiers (for example, Evocon's free plan covers one machine), per a vendor article from April 2026. [TeepTrak](https://teeptrak.com/en/free-downtime-tracking-software/)
- The gap hypothesis: a shop with 5–20 machines that won't spend €1,000+ a month or install sensors, but has outgrown a spreadsheet.

## Customers and distribution

- **Buyer:** owners and plant managers of small manufacturers.
- **Distribution:** search for "OEE calculator" or "downtime tracking template," a free calculator or template as the entry point, and manufacturing communities. No marketplace. Search is contested by vendors publishing heavily on these terms (both sources above are vendor content marketing).
- **Competition:** well-funded vendors moving down-market with free tiers.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | No marketplace; search is crowded with vendor content. |
| Willingness to pay | 2 | Small shops have spreadsheets and free tiers as substitutes; low-end WTP unproven. |
| Build effort | 4 | A tablet-friendly CRUD app with reports (estimate). |
| Operating load | 3 | Manual entry keeps support simple; imports add variety (assumption). |
| Owner time | 3 | Manufacturing buyers often expect a call before buying (assumption). |
| Legal and compliance load | 4 | Production data only; standard SaaS terms. |
| Sellability | 3 | Small vertical SaaS sells at modest multiples; average Acquire.com bootstrapped SaaS listing reported at ~2.6x revenue (secondary source, 2026). [Beancount.io](https://beancount.io/blog/2026/07/11/bootstrapped-saas-valuation-multiples-2026-acquire-com-indie-founders-guide) |
| Window | 4 | Not time-limited. |
| Cost | 4 | Small hosting cost. |

Disqualifiers checked: possible overlap with the owner's employer's industry, which the owner is handling.

## Economics (estimates, not forecasts)

- Price idea: $29–79 per site per month.
- At $49, about 20 sites gives ~$1,000 a month before fees and costs (arithmetic on an assumed price).

## Owner tasks that remain

- Possible pre-sale questions from buyers who want a person.
- Domain judgment on feature requests.

## Validation plan

Start with the template (see `manufacturing-templates`) and a free web OEE calculator that captures emails, then offer a waitlist for the tracker. Pass: 30+ waitlist signups from manufacturers in 60 days. Cost: domain plus small hosting.

## Kill criteria

Under 10 manufacturer signups in 60 days.

## Exit

Sell to an OEE vendor wanting a low-end funnel, or on Acquire.com.

## Decision log

- 2026-10-10: screened by Claude. Keep behind the template test rather than building first.
