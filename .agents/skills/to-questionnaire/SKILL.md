---
name: to-questionnaire
description: Turn a decision the owner can't answer alone into a questionnaire for someone else to fill in, such as a prospective buyer, a niche practitioner or a CPA. User-invoked.
disable-model-invocation: true
---

Turn something the owner can't answer alone into a **questionnaire**: a Markdown document handed to one person to fill in async, or filled out together. The recipient holds knowledge the owner lacks; the questionnaire pulls it out of them.

Writing the questionnaire is allowed without asking. **Sending it is not**: contacting anyone outside this repo needs the owner's approval (`AGENTS.md`). Never send, post or message it yourself.

**Grill the send, not the subject.** Interview the owner only about the _send_, which they can always answer: who it goes to, and what they need back. The questions in the document then target the **gap** between what the recipient knows and what the owner needs.

1. **Who is it going to?** Ask, in one exchange, the recipient's role, expertise and relationship to the owner. This fixes tone and how much context the document must carry. Done when you know who the recipient is and what they know that the owner doesn't.

2. **What do you need back?** Ask, in one exchange, the specific decisions or facts the owner can't resolve alone. Done when you have a concrete list of what the owner must walk away able to decide.

3. **Write the questionnaire.** Draft questions aimed at the gap, following the structure below. This repo is public: include nothing about the owner's identity, employer, income or private accounts. For a prospective customer, never pitch inside the questions or ask leading ones; ask about what they do and pay for today. Save it next to the opportunity it serves, as `opportunities/<opportunity-slug>-questionnaire-<topic>.md`, or `docs/questionnaire-<topic>.md` when it serves no single opportunity. Done when the file exists and every item from step 2 is covered by a question.

4. **Hand it over.** Report the path. If it needs sending, open or update a `needs:owner` issue saying who it goes to and why, so the owner can approve and send it.

## Document structure

Frame it as a **discovery questionnaire**. Order questions most-important-first, since async means you may only get one pass, and group them under `##` headings by theme once there are more than a handful.

<questionnaire-template>

# <Questionnaire title>

**Purpose:** why this questionnaire exists and the decision riding on it.

**How your answers will be used:** <where they go>

## Context

One paragraph orienting a recipient who wasn't in the owner's head. Enough to answer well, not a page.

## How to answer

Deadline and rough effort. Partial answers and "I don't know" are useful: flag anything you're unsure of rather than skipping it.

## <Theme heading>

One `##` section per theme. Under each, its questions, most-important-first. Every question is one idea, never compound, with an answer stub directly beneath, and a one-line _why this matters_ only where the question could be misread.

<question-example>
### How do you track downtime on your machines today?

_Why this matters: it shows what a new tool would have to replace._

>
</question-example>

## Anything else?

A closing catch-all: anything we didn't ask that we should know?

</questionnaire-template>
