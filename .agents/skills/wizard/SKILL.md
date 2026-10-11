---
name: wizard
description: Generate an interactive bash wizard that walks the owner through setup steps only they can perform, such as creating an approved account, setting up a payment provider, or storing a product's credentials. Don't use it for steps an agent can do itself, or before the owner has approved the account or spend.
disable-model-invocation: true
---

# Wizard

A **wizard** is a bash script that walks the owner, step by step, through a manual procedure that is tedious to do by hand and tedious to re-explain every time. It opens each URL, says exactly what to click and copy, captures the values, writes them where they belong, confirms at every stage, and shows how many stages are left.

In this portfolio, agents may not create accounts, spend money or handle credentials (`AGENTS.md`). The wizard is how the owner does those steps quickly once they've approved them. Use it only after the matching `needs:owner` issue is approved, and link that issue in the wizard's banner.

The UX is already solved by [template.sh](template.sh): stage-by-stage progress, confirmation gates, cross-platform URL opening, hidden secret entry, idempotent `.env` upserts, `gh secret`/`gh variable` writes, and a closing summary. **Your job is only to scope the procedure and author its stages.** The library above the `STAGES` marker is identical in every wizard; never hand-edit it.

## Where secrets may go

This repository is public and must never hold credentials. So:

- A wizard that stores secrets (`ask_secret`, `write_env`, `set_secret`) lives in, and is run from, **the product's own repository**, whose `.gitignore` must cover `.env` before the first run. `gh secret set` targets the repository of the current directory; run from here, it would put secrets on this public repository.
- A wizard run from this repository may only guide and record non-secret facts: `open_url`, `step`, `say`, `ask` for public values, `pause`, `confirm`. Its stages contain no `ask_secret`, `write_env`, `set_secret` or `set_var` calls.
- Account names and addresses go into `docs/ACCOUNTS.md` afterwards, by the agent, in the PR that starts using the account. Passwords, recovery codes, API keys and bank details never do.

## Process

### 1. Scope the procedure

Work out every manual step and every value captured. Read first, don't ask cold: the approved `needs:owner` issue, `docs/ACCOUNTS.md`, the opportunity file, and for a product repository its `.env.example`, README and `.github/workflows/*` (every `secrets.*` / `vars.*` reference is a value the wizard must produce).

Show the owner the ordered list of stages and the values each produces, and confirm. They may add, drop or reorder.

**Done when:** every stage is named in order, and for each captured value you know (a) where the owner gets it, (b) where it's written (product `.env`, a product-repo GitHub secret, `docs/ACCOUNTS.md`, or nowhere), and (c) whether it's secret (hidden entry) or public.

### 2. Map each stage's journey

For each stage, write the precise path the owner follows: which URL to open, what to do there, where a value appears, which variable it fills. For example: "Dashboard → Developers → API keys → Reveal test key → copy". Where you don't know the current UI, check the provider's documentation or say so. Never invent steps that may not exist.

**Done when:** every stage traces to concrete instructions a stranger could follow.

### 3. Author the wizard

Copy `template.sh` to the target path: the product repository's `scripts/`, or a temporary directory for a one-off run. Replace the example stage with one `stage` per step, in dependency order, using the helpers: `stage`, `say`/`step`, `open_url`, `ask`/`ask_secret`, `write_env`, `set_secret`/`set_var`, `pause`/`confirm`. Set `TOTAL_STAGES` to the number of stages.

Hold the bar the template sets: open the URL before asking for its value, use `ask_secret` for anything secret, `confirm` before any irreversible action (paying a fee, publishing a listing, deleting anything). Keep a stage to one focused task, since each stage clears the screen.

### 4. Verify and hand off

- `bash -n <script>`; run `shellcheck` if available. Keep LF line endings: CRLF breaks bash.
- Don't run it yourself: it opens browsers and waits for the owner. Trace it statically instead: every value from step 1 is captured and lands where step 1 said, nothing secret is written anywhere in this repository, and every `set_secret` name matches a `secrets.*` reference in the product's CI.
- Tell the owner how to run it. On Windows that means Git Bash or WSL, from the product repository's folder: `bash scripts/<name>.sh`. Commit it to the product repository only if it's a repeatable setup path.
- After the owner reports it done, check the live state where you can (`AGENTS.md`: an API's "success" is not proof), and update `docs/ACCOUNTS.md`.
