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
- did: scaffolded repo, 6 papers, 6 concepts, Q1–Q5, exp01 spec, first digest
- learned: open models can't self-report emotion states but probes decode them (2611.10123, [[Models do not report injected pain (Ferrara 2026)]]), so Q1 uses a probe readout; WSP rank-one edits ≈ baked-in steering, which led to proposed [[Q5 (stopped) Make steering permanent|Q5]]
- open-next: promote/kill Q5, line up 2 raters for exp01, start Reading list Priority

## 2026-11-19 · personal-laptop · claude-code
- did: wired up the dashboard: `section` + `tier` on all 6 papers, `dashboard.json`, new `/next` and `/gaps` commands, lit review file names in CLAUDE.md
- learned: `9 Claude files/Writing/litreview/outline.md` doesn't exist yet, so sections were assigned from the section names alone; `gaps.md`, `outline.md` and `matrix.md` must stay frontmatter-free (the dashboard shows them as-is)
- open-next: Harshit to check the section/tier picks and write `outline.md`; `/next` starts with Ferrara (section 3)

## 2026-11-20 · personal-laptop · claude-code
- did: organised the vault for Obsidian graph view and InfraNodus. Frontmatter `links` were invalid YAML (`[[a]], [[b]]`), so Obsidian dropped them; now quoted (`["[[a]]"]`) in 42 notes. Added nested tags (`type/ section/ test/ component/ status/ relevance/ thread/ role/`), linked every paper to its section's landscape hub and component concept notes, gave threads/experiment/digest tags, set graph color groups + forces, excluded `9 Claude files/Templates/`, `CLAUDE.md`, `scripts/` from the graph, updated templates and the CLAUDE.md conventions.
- learned: `scripts/dashboard.py` parses frontmatter line by line, so every list must stay on one line. Security review flagged XSS escaping and a missing Host check in `dashboard.py` (left for later, on the to-do list).
- open-next: `[[Steer2Edit - steering into small weight edits (Sun 2026)]]` and `[[ThinkEdit - edit weights to think longer (Sun 2025)]]` (Q5) are still unresolved, so ingest them or leave them as visible gaps; run InfraNodus gap detection on the `2 Papers` + `3 Ideas` folders.
- 2026-11-20 later: renamed Q1–Q5 and one concept to ASD-STE100-style names (e.g. `Q1 Does the model sense code quality`, `Q4 Can the model edit its own weights`, `Models that change their own weights`), with STE titles; old names are in each thread's Log. Naming rule added to CLAUDE.md conventions.
- 2026-11-20 later: rebuilt HOME.md as a plain-English, click-only front page. Dataview was never installed, so its tables showed as code; tables now come from built-in Obsidian Bases in `9 Claude files/Tables/`. Bookmarked HOME.

## 2026-11-20 · personal-laptop · claude-code
- did: committed the uncommitted landscape work (job 2), then delegated the prior-art update to 3 sub-agents: ingested ThinkEdit + Steer2Edit (Q5 links now resolve), built `9 Claude files/Writing/litreview/outline.md` (section 8 written out) + `matrix.md` (new "prior art or threat to" column), red-teamed Q1 against the new papers.
- learned: Q1 is not scooped (Gao steers readability, never checks human ratings), but valence must beat a layer-0 probe and a supervised readability direction. Stable is the least covered test; Q3 faces the most threats.
- open-next: Harshit to accept/reject the proposed Q1 kill line and the cheap Buse-Weimer pre-check; update exp01 spec controls; verify Steer2Edit Table 10 numbers against the PDF.

## 2026-11-20 · personal-laptop · claude-code (2)
- did: `TASKS.md` is now the one task list ("For you" / "For Claude"). Plain-English file names for all notes; `03-threads` is now `1 Questions`; T1-T5 are now Q1-Q5. Writing rule (80% ASD-STE100) and naming rule are in CLAUDE.md.
- learned: the user found tasks spread over many files, codes like "T1" and kebab-case names hard to read. Answer "what is pending" from `TASKS.md` only.
- open-next: see `TASKS.md`.
