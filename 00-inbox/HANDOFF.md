---
type: handoff
status: active
tags: [type/handoff, protocol, multi-account]
links: []
---

# HANDOFF

Shared memory across Claude accounts. Nothing carries over between accounts unless it's written here or elsewhere in the repo.

- **Session start:** read the last 3 entries.
- **Session end:** append one entry. Newest goes at the bottom.
- Keep each entry under 6 lines, in this format:

```
## YYYY-MM-DD · <account label> · <surface>
- did: ...
- learned: ...
- open-next: ...
```

---

## 2026-11-19 · personal · claude.ai
- did: scaffolded repo, 6 papers, 6 concepts, T1–T5, exp01 spec, first digest
- learned: open models can't self-report emotion states but probes decode them (2611.10123, [[2026-ferrara-all-quiet-pain]]), so T1 uses a probe readout; WSP rank-one edits ≈ baked-in steering, which led to proposed [[permanent-steering-change-T5|T5]]
- open-next: promote/kill T5, line up 2 raters for exp01, start reading-queue Priority

## 2026-11-19 · personal-laptop · claude-code
- did: wired up the dashboard: `section` + `tier` on all 6 papers, `dashboard.json`, new `/next` and `/gaps` commands, lit review file names in CLAUDE.md
- learned: `07-drafts/litreview/outline.md` doesn't exist yet, so sections were assigned from the section names alone; `gaps.md`, `outline.md` and `matrix.md` must stay frontmatter-free (the dashboard shows them as-is)
- open-next: Harshit to check the section/tier picks and write `outline.md`; `/next` starts with Ferrara (section 3)

## 2026-11-20 · personal-laptop · claude-code
- did: organised the vault for Obsidian graph view and InfraNodus. Frontmatter `links` were invalid YAML (`[[a]], [[b]]`), so Obsidian dropped them; now quoted (`["[[a]]"]`) in 42 notes. Added nested tags (`type/ section/ test/ component/ status/ relevance/ thread/ role/`), linked every paper to its section's landscape hub and component concept notes, gave threads/experiment/digest tags, set graph color groups + forces, excluded `_templates/`, `CLAUDE.md`, `scripts/` from the graph, updated templates and the CLAUDE.md conventions.
- learned: `scripts/dashboard.py` parses frontmatter line by line, so every list must stay on one line. Security review flagged XSS escaping and a missing Host check in `dashboard.py` (left for later, on the to-do list).
- open-next: `[[2026-sun-steer2edit]]` and `[[2025-sun-thinkedit]]` (T5) are still unresolved, so ingest them or leave them as visible gaps; run InfraNodus gap detection on the `01-papers` + `02-concepts` folders.
- 2026-11-20 later: renamed T1–T5 and one concept to ASD-STE100-style names (e.g. `code-quality-signal-T1`, `self-weight-change-T4`, `self-weight-updates`), with STE titles; old names are in each thread's Log. Naming rule added to CLAUDE.md conventions.
- 2026-11-20 later: rebuilt HOME.md as a plain-English, click-only front page. Dataview was never installed, so its tables showed as code; tables now come from built-in Obsidian Bases in `_views/`. Bookmarked HOME.

## 2026-11-20 · personal-laptop · claude-code
- did: committed the uncommitted landscape work (job 2), then delegated the prior-art update to 3 sub-agents: ingested ThinkEdit + Steer2Edit (T5 links now resolve), built `07-drafts/litreview/outline.md` (section 8 written out) + `matrix.md` (new "prior art or threat to" column), red-teamed T1 against the new papers.
- learned: T1 is not scooped (Gao steers readability, never checks human ratings), but valence must beat a layer-0 probe and a supervised readability direction. Stable is the least covered test; T3 faces the most threats.
- open-next: Harshit to accept/reject the proposed T1 kill line and the cheap Buse-Weimer pre-check; update exp01 spec controls; verify Steer2Edit Table 10 numbers against the PDF.

## 2026-11-21 · instinct · whatsapp-agent
- did: ran fetch_arxiv.py for the last 3d (2 candidates), triaged, wrote digest + note for WeightCode (2611.25476, score 2); drafted all 9 lit-review sections (08 moved from outline), references.md auto-compiled from frontmatter, first gaps.md; added .github/workflows/scout.yml (daily cloud fetch, 09:15 IST); foundation notes for Nelson&Narens, Doya, Fleming&Daw with [unverified] flags from the concept notes.
- learned: only 2 new arXiv candidates in 3 days - the watchlist is quiet, so gap-filling from the reading queue back-catalog is worth more than more fetching; CLAUDE.md says "Harshit" is PI but the repo owner is Kaushik (template leftover?); the github integration used here is read+PR only, so this session's commits were pushed over HTTPS with a fine-grained PAT (repo-scoped, Contents+PR rw).
- open-next: verify the [unverified] foundation details against PDFs; ingest the ~10 "Next" papers in the reading queue; Kaushik to review the 9 section drafts (all status: draft); wire triage into the cloud workflow once an agent API key is available.

## 2026-11-21 (cont.) · instinct · whatsapp-agent
- did: ingested the architecture-metacognition set (SST, MUSE, Liu & van der Schaar) and both surveys (2607.11881, 2604.16592); cleared the reading queue "Next" list (introspective oversight, GUARD, WeightBench, WSP-scope, Lindsey, Ji-An, persona vectors + audit); added INTUITOR, AI Can Learn Scientific Taste, IdeaTaste, self-evolving agents survey from Background. 36 notes total (was 22). gaps.md gained G5 (architecture gap) and a "New since 2026-11-21" section; trends.md links the new cluster. fetch_semantic_scholar.py now merges with earlier same-day results so a 429 run never clobbers candidates.
- learned: S2 shared-pool 429s persist for hours - an API key (.env S2_API_KEY) would unblock the backfill; "metacognitive space" (Ji-An) is the ceiling constraint on any valence readout; preventative persona steering is real T4 prior-art pressure.
- open-next: verify [unverified] foundation details against PDFs; re-pass matrix threat counts against the 14 new notes; Background list remainder (Utility Engineering, OMNI, model collapse, alignment faking, Rényi crossings, Irie, Nested Learning); .github/workflows/scout.yml still local - needs a token with Workflows scope or a manual add.
