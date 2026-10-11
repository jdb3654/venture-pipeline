---
name: grilling
description: Grill the owner relentlessly about a plan, decision, or opportunity until there is a shared understanding. Use when the owner wants to stress-test an idea, a stage gate, a validation plan or a kill decision, or says "grill me". Not for questions you can answer yourself by research.
---

Interview the owner relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Read `BRIEF.md` and the relevant opportunity file first. The brief already settles goals, budget, contact limits and disqualifiers: treat those as settled branches, not questions.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the owner's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer. The owner has about two hours a day, so keep each round answerable in a few minutes.

Each round the owner answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the owner's. When a frontier question needs a fact (repo files, marketplace data, competitor pricing, platform rules), look it up. If your harness can run a sub-agent, dispatch one so you don't block: only the questions downstream of it wait; ask the rest of the frontier now. Otherwise look it up yourself before asking that question. The _decisions_ are the owner's: put each to them and wait.

The session is done when the frontier is empty: every branch visited, nothing left silently assumed. Do not act on it until the owner confirms you have reached a shared understanding. Then record the outcome where it belongs: the opportunity file for stage and scoring decisions, the `domain-modeling` skill's formats for terms and portfolio-wide decisions.
