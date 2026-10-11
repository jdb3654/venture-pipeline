# Niche third-party module for Ignition SCADA

- **Slug:** ignition-module
- **Stage:** Screen
- **Owner agent:** claude
- **Created / last updated:** 2026-10-10 / 2026-10-10
- **Last outside evidence:** none yet (desk research only; checked 2026-10-10)

## The idea in two sentences

Inductive Automation's Ignition is a widely used SCADA/HMI platform with a showcase for third-party modules that developers sell from their own sites. Build one narrowly scoped module that fills a gap integrators keep asking about, and sell licenses with a trial download.

## Signal

- Inductive Automation lists third-party modules in a Module Showcase. Requirements: an official company, a website showing the module's description, compatible versions, price, trial download and purchase method; IA reviews the listing and checks that the module installs. The developer sells and supports the module and holds liability for it. No listing fee is mentioned (verified, IA FAQ, checked 2026-10-10). [Module Showcase FAQ](https://inductiveautomation.com/moduleshowcase/faq)
- The owner works daily with SCADA/HMI, OPC, SQL and plant integrations. This is the strongest domain edge in the round.
- Not yet found: specific evidence of unmet module demand (forum feature requests, integrator complaints). That is the first validation step.

## Customers and distribution

- **Buyer:** system integrators and plant engineers running Ignition. B2B budgets; a module priced in the hundreds of dollars is normal for industrial software (assumption; no prices could be read from the showcase page).
- **Distribution:** the Module Showcase, Ignition forum and community, integrator word of mouth. Narrower than a marketplace with built-in billing.
- **Competition:** established module vendors exist; gaps must be found module by module.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Official showcase listing plus a concentrated community; no built-in billing. |
| Willingness to pay | 4 | Industrial buyers pay for software that saves engineering time (assumption). |
| Build effort | 3 | Ignition's Java module SDK and version compatibility testing (estimate). |
| Operating load | 2 | Plant-floor software is uptime-critical; problems are urgent and environment-specific (assumption). |
| Owner time | 2 | Escalations will need real domain judgment, which agents can't fully cover. |
| Legal and compliance load | 2 | Liability for software running on industrial systems; needs solid license terms and likely insurance (verify). The showcase requires a company entity. |
| Sellability | 3 | Module businesses can be sold to integrators or module vendors (assumption). |
| Window | 4 | Not time-limited. |
| Cost | 4 | Development license and test gateway costs to check; otherwise low. |

Disqualifiers checked: potential overlap with the owner's employer, which the owner is handling. Agents must not use anything from the employer. Industrial use raises the stakes of support; not a disqualifier, but a major cost.

## Economics (estimates, not forecasts)

- Price: one-time license plus annual support (typical for the category; verify against listed modules).
- Payment: own site via a merchant of record.
- Few sales needed for meaningful revenue, but each customer brings heavier support.

## Owner tasks that remain

- Company entity (required by the showcase).
- Escalated support needing SCADA judgment: frequency unknown, potentially urgent.

## Validation plan

Agents mine the Ignition forum and Exchange for repeated feature requests and workarounds over the past two years, list the top 10 gaps, and check each against existing modules. Owner picks one. Publish a landing page with a waitlist and post it to the community. Pass: 20+ qualified signups or 3+ pre-orders. Cost: under $20 (domain).

## Kill criteria

No repeated, unmet gap found in the forum review, or an existing module already covers the chosen gap.

## Exit

Sell to a module vendor or integrator.

## Decision log

- 2026-10-10: screened by Claude. Strong edge, heavier support and liability than the brief prefers.
