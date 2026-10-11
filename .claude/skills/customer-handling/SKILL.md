---
name: customer-handling
description: Triage and answer customer messages for a product in Launch or Operate. Use when reading a product's support inbox, drafting a reply to a customer, or deciding whether to escalate to the owner.
---

Each product has its own support email address, owned by the product, not the owner personally. Agents triage incoming messages:

- **Routine** (how-to, account questions, bug reports, feature requests): answer from the product's docs, and log feedback to that product's repo.
- **Escalate to the owner:** refunds outside policy, angry or threatening messages, legal or security issues, anything involving payment disputes, and anything the agent is unsure about.

Start every product in **draft-and-approve** mode: agents draft replies, and the owner approves them. Move a category to auto-send only after the owner signs off on it. Tell customers they are talking with an AI assistant and how to reach a human.

Customer data and private messages never go into git (`AGENTS.md`). Log feedback to the product's own repository as anonymized summaries.
