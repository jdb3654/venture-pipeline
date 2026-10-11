# Knitwear pattern grading tool for indie designers

- **Slug:** knitwear-grading-tool
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #56)

Labels: **[fact]** verified on the cited page, **[report]** first-hand report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A web tool that takes a designer's gauge, base-size pattern and size chart and produces graded stitch and row counts, shaping and a schematic across sizes, with an AI pass that drafts the written instructions for review. Indie knitting and crochet pattern designers, who sell patterns on Ravelry, Etsy and their own sites, pay for it instead of hiring a human grader.

## Signal

Lenses: picks and shovels for small sellers, non-tech hobby, newly possible with AI (drafting graded written instructions).

- A tech editor's public rate card: grading at **£30/hour**, about **6–10 hours for a simple garment and 10–16 hours for a complex one**; tech editing also £30/hour [vendor price list: [Sam Loves Yarn](https://www.samlovesyarn.co.uk/services-7), no date shown]. That's roughly £180–£480 of paid human work per graded garment.

## Customers and distribution

- **Buyer:** independent pattern designers who sell multi-size garment patterns. Count unknown [assume: thousands, unquantified].
- **Today they use:** a human grader or tech editor (above), their own spreadsheets [assume], or the new Skein app.
- **Route without ads:** a free single-construction calculator (e.g. hats or socks) shared in designer communities and found by search; designers talk to each other on Ravelry and Instagram [assume, not checked this round].
- **Competitors:** **Skein: Knit and Grade** (iPhone/iPad/Mac), grading across 9 sizes for six constructions with schematics; Designer Pro **$7.99/month or $59.99/year**; released 2026-06-18, **0 ratings** [fact on listing: [AppsHunter](https://appshunter.io/ios/app/skein-knit-and-grade/id6780070426)]. Human graders (above).

## Strongest reason it fails

The grading maths is deterministic and already packaged: Skein shipped it in June 2026 at $59.99/year. Designers who release a few garments a year can hire a grader once rather than subscribe, and because one wrong count damages a designer's reputation with buyers [assume], they will probably still pay a tech editor to check the output. If the tool doesn't remove that paid human step, it saves less than the £180–£480 headline.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Free calculators can spread in designer communities and search [assume]; no marketplace. Skein uses the App Store ([AppsHunter](https://appshunter.io/ios/app/skein-knit-and-grade/id6780070426)). |
| Willingness to pay | 3 | Designers pay humans £30/hour for 6–16 hours of grading per garment [vendor price list: [Sam Loves Yarn](https://www.samlovesyarn.co.uk/services-7)]. Software WTP unproven: Skein's $59.99/yr is an asking price with 0 ratings. |
| Build effort | 3 | Two or three garment constructions with correct shaping maths, schematics, and tests against hand-graded examples [est]. |
| Operating load | 4 | Self-serve; support is mostly "these numbers look wrong" questions [assume]. |
| Owner time | 5 | No calls, no deadlines, no on-site work [assume]. |
| Legal and compliance load | 5 | No regulated data, no licensing; designers keep their own copyright [assume]. |
| Sellability | 3 | Small niche tool; plausible buyer is a knitting software or yarn company [assume]. |
| Window | 3 | Skein entered in June 2026 [fact]; window narrows if it gains traction. |
| Cost | 5 | Static web app plus occasional LLM calls; a few dollars a month [est]. |

Disqualifiers checked: illegal or platform-risky: no / needs owner on calls: no / regulated data: no / employer-related: no.

## Economics (estimates, not forecasts)

- Price: $5/month or $40/year, or $15 per graded pattern [est].
- Running cost: about $5/month [est].
- Payments: merchant of record, roughly 5% + $0.50 [assume, not rechecked].
- Customers needed: 2 annual subscribers cover costs; about 300 annual subscribers for $1k/month owner cash [est].

## Owner tasks that remain

- Approve publishing a free calculator page — once.
- Approve any community post (must not look like spam) — once per community.

## Validation plan

Only after a blind `case-against` is answered (AGENTS.md). Then: $0, 30 days, owner approval to publish: a free hat/sock grading calculator with an email opt-in for "garment grading (sweaters), $40/year — join the list." Pass: 40 or more opt-ins and 5 or more replies naming a garment they'd grade. Fail: fewer than 15 opt-ins.

## Kill criteria

Validation fails; or Skein reaches 50+ ratings with strong reviews before we launch.

## Exit

Sell to a knitting software, pattern platform or yarn company. Needs a clean customer list and documented grading rules.

## Decision log

- 2026-10-11: entered at Screen from discovery round 2 (#56), by Claude. Ranked second of five.
