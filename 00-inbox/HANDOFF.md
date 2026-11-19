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
