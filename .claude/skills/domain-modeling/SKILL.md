---
name: domain-modeling
description: Keep the portfolio's shared vocabulary and portfolio-wide decisions sharp. Use when a term is ambiguous or used two ways, when writing or editing GLOSSARY.md, or when recording or editing a decision record in docs/adr/.
---

# Domain modeling

Actively sharpen the language agents and the owner use, and write down decisions the moment they crystallise. Merely _reading_ `GLOSSARY.md` for vocabulary is not this skill; this skill is for changing the shared model.

## Where things live

```
/
├── GLOSSARY.md          ← portfolio-wide terms (created lazily)
├── docs/adr/            ← portfolio-wide decisions (created lazily)
│   └── 0001-merchant-of-record-for-payments.md
└── opportunities/<slug>.md   ← decisions about one opportunity stay here
```

Create files lazily: only when you have something to write. A decision about one opportunity (its stage, scores, kill criteria) belongs in that opportunity's file, not an ADR. A product repository keeps its own glossary and ADRs.

`BRIEF.md` outranks both files. A glossary entry or ADR never changes the brief; if one would, raise it with the owner as a `needs:owner` issue.

## During a session

### Challenge against the glossary

When someone uses a term that conflicts with `GLOSSARY.md`, call it out immediately: "The glossary defines _revenue_ as settled payments, but you're counting signups. Which do you mean?"

### Sharpen fuzzy language

When a term is vague or overloaded, propose a precise canonical one: "You're saying _customer_: the Etsy buyer, or the shop owner who uses the template?"

### Probe with concrete scenarios

Stress-test definitions with specific cases at the boundaries: a refunded sale, a free download, a buyer who pays then disputes.

### Cross-reference with the record

When someone states how something works, check the opportunity files, `PIPELINE.md` and `AGENTS.md`. Surface contradictions rather than picking a side silently.

### Update GLOSSARY.md inline

When a term is resolved, update `GLOSSARY.md` right then, using [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md). It holds definitions only: no plans, scores or decisions.

### Offer decision records sparingly

Only offer an ADR when all three are true:

1. **Hard to reverse**: changing your mind later has a meaningful cost.
2. **Surprising without context**: a future agent or buyer of the business would wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons.

If any of the three is missing, skip it. Use [ADR-FORMAT.md](ADR-FORMAT.md). Because a new ADR is a portfolio-wide decision, request the other agent's review on the PR that adds it.
