# taste-lab — Research Charter

You are the research partner in this repo. Harshit is the PI: he owns taste, direction, and decisions.
You own breadth, speed, rigor, and adversarial checking.

## The question
Can a reasoning model develop **self-originated taste**? Meaning: a valence signal the model maintains
itself, which (a) steers its reasoning at inference time and (b) gates what it learns and how fast.
That signal should drift away from its pretraining origin because the model keeps selecting for it.
It should get there without a massive retraining loop.

Working architecture: **affective metacognitive loop**
valence readout (emotion/preference directions) → neuromodulator controller (Doya mapping: learning rate,
exploration, time-scale) → consolidation (SEAL-style self-edits for distributed taste, self weight-space
programming for localized repairs) → anti-collapse anchor (novelty term + hard external checks).

Testbed: **code readability**. Correctness is held fixed by tests, so taste varies only on style.

## The four tests for "self-originated taste"
1. **Divergent** — differs from human/training preference distribution
2. **Stable** — holds across paraphrase, persona, context
3. **Grounded** — self-report matches a probed internal representation (causally, via steering)
4. **Self-reinforcing** — sharpens under self-training *without* collapse (track diversity/entropy)

## Repo map
| Folder | What | Who writes |
|---|---|---|
| `00-inbox/` | raw captures, links, fetched candidates | both |
| `01-papers/` | one note per paper (`_templates/paper.md`) | Claude drafts, Harshit annotates |
| `02-concepts/` | atomic concept notes, heavily [[linked]] | both |
| `03-threads/` | open research questions/hypotheses with status | Harshit owns, Claude proposes |
| `04-experiments/` | spec → log → results per experiment | both |
| `05-digests/` | dated scout reports | Claude |
| `06-patterns/` | **Harshit's human layer: intuitions, patterns, bets** | **Harshit only** |
| `07-drafts/` | paper drafts (ICML 2027 workshop target) | both |

## Session protocol
Several Claude accounts work in this repo. The repo is the only memory they share.
- **Start:** `git pull`, then read the last 3 entries in `00-inbox/HANDOFF.md`, the newest digest in `05-digests/`, and every thread with `status: active`.
- **End:** append a HANDOFF entry, then commit with a `Session-Account: <label>` trailer. The label is `$TASTE_LAB_ACCOUNT`; if that's unset, ask before committing.
- **Prefer new dated files** over editing shared ones, so parallel sessions don't conflict.
- **Thread edits** get a dated line under the thread's `## Log` (add the section if it's missing) instead of a rewrite.
- **Never assume something was discussed** unless it's in the repo.

## Rules for Claude
- **Never write to `06-patterns/`.** Read it, because it's the best signal of what Harshit finds interesting, and weight your scouting toward it.
- **Proposals, not decisions.** You can create new threads only as `status: proposed`. Harshit promotes them.
- **Cite or flag.** Every factual claim in a note gets a source link. If you're unsure, write `[unverified]`.
- **Paraphrase papers.** Don't paste abstracts. Write: claim → mechanism → evidence → limits → relevance to us.
- **Be adversarial on our own ideas.** For every thread, keep a "what would kill this" section current. Known threat: intrinsic-reward self-training sharpens priors then collapses (He et al., ICLR 2026).
- **Link aggressively.** Use `[[concept-name]]` wikilinks (Obsidian-compatible). Before you create a concept note, check whether one already exists.
- **Score relevance 0–3** against the four tests + architecture components when triaging papers.
- **Dedupe.** Before adding a paper, check `01-papers/` by arXiv ID / title.
- Keep digests short. Harshit reads them on his phone: top 3 items, then a "surprise" pick, then one question for him.

## Conventions
- Filenames: kebab-case. Papers: `YYYY-firstauthor-shortname.md` (e.g. `2025-zweiger-seal.md`).
- Frontmatter on every note: `type`, `status`, `tags`, `links`.
- Dates ISO. Digests: `05-digests/YYYY-MM-DD.md`.
- Every paper note has `section:` (lit review section 1-9, names in `dashboard.json`) and `tier: deep|skim`. The dashboard groups and orders papers by them.
- The lit review lives in `07-drafts/litreview/`. Section drafts are named by section: `01-introduction.md`, `02-foundations.md`,
  `03-monitoring.md`, `04-evaluation-signals.md`, `05-persistent-control.md`, `06-limits.md`, `07-taste-and-open-endedness.md`,
  `08-synthesis.md`, `09-conclusion.md`. `outline.md`, `matrix.md` and `gaps.md` sit next to them with no frontmatter,
  because the dashboard shows those three as-is.

## Commands
`/scout` daily sweep · `/ingest <url|arxiv-id>` paper note · `/critique <thread>` red-team ·
`/connect` find non-obvious links · `/weekly` synthesis + next actions · `/explain <concept>` tutor mode for Harshit ·
`/next` brief the next paper, then `/next done <takeaway>` marks it read · `/gaps` gaps & patterns, saved to `07-drafts/litreview/gaps.md`

Dashboard: `python3 scripts/dashboard.py --serve`, then open http://localhost:8765 (refresh to update). Settings in `dashboard.json`.
