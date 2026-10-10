# Paid data tools for AI agents on Apify (Actors and MCP)

- **Slug:** apify-niche-actors
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-10 / 2026-10-10

## The idea in two sentences

Publish small, reliable data tools (scrapers, monitors, clean feeds) on the Apify Store, where they can be called by people and by AI agents through MCP, and charged per result. Each tool is cheap to build, so we can launch several and keep the ones that get used.

## Signal

- Apify pays developers 80% of charged events and has a large existing store audience; MCP-specific marketplaces such as MCPize offer 85% but have a smaller audience (blog post, 2026; mixed vendor and author claims). [Godberry Studios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)
- The same article reports Apify's claim of over $4M paid out to Actor developers since the Store launched (platform claim, platform-wide, not MCP-specific). Apify's own developer page: [Apify](https://apify.com/mcp/developers)
- Counter-evidence: the same author launched a per-call MCP tool on 2026-04-12 and had zero paying users after two weeks. Revenue claims for top MCP servers are unverified or vendor-reported.
- Counter-evidence specific to the owner's edge: an existing Apify Actor that filters CISA's exploited-vulnerability feed to industrial vendors had 2 total users and 1 monthly active user when checked (2026-10-10). [Apify listing](https://apify.com/zentrafoundry/cisa-ics-advisory-asset-exposure-watcher)

## Customers and distribution

- **Buyer:** developers and teams building agents or data pipelines who need a specific, reliable source.
- **Distribution:** Apify Store search and MCP directories. Real, but each listing competes with many near-duplicates.
- **Competition:** heavy for popular sources; thin for obscure but useful ones. Demand is the open question, not supply.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Built-in store and agent access, but crowded listings (see above). |
| Willingness to pay | 2 | Pay-per-result works on Apify, but evidence for any specific niche is weak; the industrial example has ~no users. |
| Build effort | 5 | Days per tool with agents (estimate). |
| Operating load | 3 | Scrapers break when sources change; agents can fix most breaks (assumption). |
| Owner time | 4 | Near-zero customer contact; occasional approvals. |
| Legal and compliance load | 3 | Must respect site terms, robots rules and copyright; prefer official APIs and public-domain government data. |
| Sellability | 2 | Individual Actors are hard to sell; a portfolio might be (assumption). |
| Window | 3 | Agent tooling is growing now; platforms and data owners may ship official connectors (assumption). |
| Cost | 5 | Apify bills users and pays out; our cost is near zero (verify payout terms and tax forms). |

Disqualifiers checked: none apply if we avoid sources whose terms forbid scraping.

## Economics (estimates, not forecasts)

- Price: per result or per call, typically fractions of a cent to a few cents (source above).
- Running cost: compute is charged to the user on Apify (verify for our pricing model).
- Needs high volume: at $0.01 per result, $1,000 a month requires ~125,000 paid results (arithmetic on an assumed price, before Apify's 20%).

## Owner tasks that remain

- One-time: Apify developer account and payout setup (owner approval).
- Monthly: review which tools earn; approve kills.

## Validation plan

Publish 3 tools in different niches (one industrial or government data feed, one developer-oriented, one business-data source with an official API), each priced per result. Run 30 days with no promotion beyond the listing. Pass: any tool with 10+ paying users or $50+ earned. Cost: $0 beyond agent time.

## Kill criteria

All three tools under 5 paying users after 30 days.

## Exit

Shut down unused tools; bundle any earners and offer them to other Apify developers.

## Decision log

- 2026-10-10: screened by Claude. Cheap enough to test in parallel with the stronger candidates.
