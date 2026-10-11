# Refrigerant leak-rate log for small HVAC/R contractors (EPA Part 84)

- **Slug:** refrigerant-leak-log
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #56)

Labels: **[fact]** verified on the cited page, **[report]** first-hand report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11.

## The idea in two sentences

A phone-friendly log where a refrigeration technician records each refrigerant addition; it calculates the leak rate by EPA's methods, flags repair deadlines, and keeps the three-year record the equipment owner must hold. Small HVAC/R contractors pay per technician, and give owners the record as part of their service.

## Signal

Lenses: forced deadline, non-tech trade.

- From **2026-01-01**, EPA leak-repair rules cover appliances with **15 lb or more** of HFC (or substitute, GWP above 53); leak-rate thresholds are 30% industrial process, 20% commercial refrigeration, 10% comfort cooling and others; records kept **3 years**; leaks of 125%+ of charge reported by March 1. Residential and light-commercial AC and heat pumps are exempt. Owners/operators and technicians both must comply [fact: [EPA fact sheet](https://www.epa.gov/system/files/documents/2026-01/er-r-fact-sheet-leak-repair-2026-01-13_1.pdf), January 2026].
- A practitioner site says technicians must calculate and record a leak rate each time refrigerant is added, calls the paperwork an annoyance, and says previously exempt small and medium businesses are now covered [report, vendor-linked to FMHero: [HVACR School](https://www.hvacrschool.com/the-epas-15-pound-refrigerant-threshold-in-2026/), 2026-02-21].

## Customers and distribution

- **Buyer:** independent refrigeration contractors serving restaurants, convenience stores and walk-in coolers [assume, from covered categories above].
- **Today they use:** paper, field-service software with refrigerant modules, CMMS (Oxmaint, Plyrium) and free leak-rate sheets (MangoApps template) [fact: search results 2026-10-11; pages not read].
- **Route without ads:** search for "leak rate calculator" and trade forums [assume]; field-service marketplaces (e.g. ServiceTitan) not checked and approval-gated.
- **Competitors:** **Ref LeakLog**, $29/$59/$89 per month by user count, free trial, implements 40 CFR 84 leak-rate methods, **0 reviews** [fact on listing: [GetApp](https://www.getapp.com/compliance-software/a/ref-leaklog/)]. The same idea is listed on a startup-ideas site ([liveinthefuture.org](https://liveinthefuture.org/startups/refrigerant-compliance-saas.html), title only).

## Strongest reason it fails

The rule may be rolled back. Search headlines report EPA moving to loosen HFC emissions rules, a "freeze" on refrigerant rules, and an NRDC lawsuit over an HFC rollback ([NRDC](https://www.nrdc.org/trump-watch/epa-moves-loosen-emissions-rules-planet-warming-hfcs), [JD Supra](https://www.jdsupra.com/legalnews/epa-puts-freeze-on-refrigerant-rules-3082457/), [Refindustry](https://refindustry.com/news/nrdc-sues-epa-over-senseless-wasteful-hfc-rollback/); headlines only, not read; the JD Supra page blocked fetching). If the 15 lb leak-repair provisions are stayed or relaxed, demand disappears. Separately, contractors already running field-service software will get this as a free module, and there is no evidence anyone has paid for a standalone version.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 2 | Search and trade forums only [assume]; field-service marketplaces unchecked and approval-gated. |
| Willingness to pay | 2 | Only asking prices ($29–89/month) with 0 reviews [fact on listing: [GetApp](https://www.getapp.com/compliance-software/a/ref-leaklog/)]; no sales evidence. |
| Build effort | 4 | Leak-rate methods are specified in 40 CFR 84 subpart C [fact: [EPA fact sheet](https://www.epa.gov/system/files/documents/2026-01/er-r-fact-sheet-leak-repair-2026-01-13_1.pdf)]; a log plus calculator is small [est]. |
| Operating load | 4 | Self-serve logging; questions about rule interpretation [assume]. |
| Owner time | 5 | No calls or site work [assume]. |
| Legal and compliance load | 3 | Wrong calculations could expose customers; rule in flux [headlines above]. No regulated personal data. |
| Sellability | 3 | Niche, but could be sold to a field-service vendor [assume]. |
| Window | 2 | Open since 2026-01-01 [fact], threatened by rollback [headlines] and by bundling into existing tools [assume]. |
| Cost | 5 | Small web app, a few dollars a month [est]. |

Disqualifiers checked: illegal or platform-risky: no / needs owner on calls: no / regulated data: no / employer-related: no (HVAC/R, not plant-floor MES; the owner should still confirm no conflict with an automaker employer).

## Economics (estimates, not forecasts)

- Price: $15/month per technician [est], under Ref LeakLog.
- Running cost: about $5/month [est].
- Payments: merchant of record, roughly 5% + $0.50 [assume].
- Customers needed: 1 covers costs; about 75 technicians for $1k/month owner cash [est].

## Owner tasks that remain

- Approve a public calculator page — once.

## Validation plan

First, $0 and one session: read the current EPA docket to see whether the 15 lb leak-repair provisions are stayed or being reconsidered. If they stand, a free leak-rate calculator page with an opt-in for the log at $15/month, 45 days. Pass: 300 calculator uses and 10 opt-ins. Fail: fewer than 3 opt-ins.

## Kill criteria

EPA stays or withdraws the 15–50 lb leak-repair provisions; or validation fails.

## Exit

Sell to a field-service or CMMS vendor, or a refrigerant distributor.

## Decision log

- 2026-10-11: entered at Screen from discovery round 2 (#56), by Claude. Ranked fourth of five; check rule status before any other work.
