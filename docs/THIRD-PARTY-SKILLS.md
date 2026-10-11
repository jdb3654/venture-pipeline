# Third-party skills

The skills in `.agents/skills/` (copied to `.claude/skills/`) are adapted from [mattpocock/skills](https://github.com/mattpocock/skills) at commit [`49dd158`](https://github.com/mattpocock/skills/tree/49dd158) (October 9, 2026). They were reviewed before adoption: plain Markdown instructions, plus one bash template (`wizard/template.sh`) with no downloads, telemetry or network calls other than optional `gh secret`/`gh variable` writes.

| Skill here | Source | What changed |
|---|---|---|
| `grilling` | `skills/productivity/grilling` | Reads `BRIEF.md` and the opportunity first; sub-agent lookup is optional so Codex and Claude both work; records outcomes in this repo's files. |
| `to-questionnaire` | `skills/productivity/to-questionnaire` | Never sent by an agent (needs owner approval); public-repo privacy rules; saved beside the opportunity; customer-discovery question guidance. |
| `domain-modeling` | `skills/engineering/domain-modeling` | Business glossary and portfolio-wide decision records instead of code architecture; single context; opportunity decisions stay in opportunity files. |
| `handoff` | `skills/productivity/handoff` | Posted as a comment on the GitHub issue (the work queue) instead of a temp file; never committed; Claude/Codex invocation names. |
| `retro` | `skills/engineering/retro` | Categories for this repo: coordination between agents, owner time, `AGENTS.md` size; no coding-standards file. |
| `wizard` | `skills/engineering/wizard` | Only after an approved `needs:owner` issue; secrets only in product repositories, never this public one; Windows via Git Bash or WSL. The template library is unchanged. |

Updates are not automatic. To pick up upstream changes, diff the source at a newer commit, re-apply the adaptations, update the commit above, and run `python scripts/sync_skills.py`.

## License

```
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
