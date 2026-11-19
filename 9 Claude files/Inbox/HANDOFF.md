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
- learned: `1 Literature review/outline.md` doesn't exist yet, so sections were assigned from the section names alone; `gaps.md`, `outline.md` and `matrix.md` must stay frontmatter-free (the dashboard shows them as-is)
- open-next: Harshit to check the section/tier picks and write `outline.md`; `/next` starts with Ferrara (section 3)

## 2026-11-20 · personal-laptop · claude-code
- did: organised the vault for Obsidian graph view and InfraNodus. Frontmatter `links` were invalid YAML (`[[a]], [[b]]`), so Obsidian dropped them; now quoted (`["[[a]]"]`) in 42 notes. Added nested tags (`type/ section/ test/ component/ status/ relevance/ thread/ role/`), linked every paper to its section's landscape hub and component concept notes, gave threads/experiment/digest tags, set graph color groups + forces, excluded `9 Claude files/Templates/`, `CLAUDE.md`, `scripts/` from the graph, updated templates and the CLAUDE.md conventions.
- learned: `scripts/dashboard.py` parses frontmatter line by line, so every list must stay on one line. Security review flagged XSS escaping and a missing Host check in `dashboard.py` (left for later, on the to-do list).
- open-next: `[[Steer2Edit - steering into small weight edits (Sun 2026)]]` and `[[ThinkEdit - edit weights to think longer (Sun 2025)]]` (Q5) are still unresolved, so ingest them or leave them as visible gaps; run InfraNodus gap detection on the `2 Papers` + `3 Ideas` folders.
- 2026-11-20 later: renamed Q1–Q5 and one concept to ASD-STE100-style names (e.g. `Q1 Does the model sense code quality`, `Q4 Can the model edit its own weights`, `Models that change their own weights`), with STE titles; old names are in each thread's Log. Naming rule added to CLAUDE.md conventions.
- 2026-11-20 later: rebuilt HOME.md as a plain-English, click-only front page. Dataview was never installed, so its tables showed as code; tables now come from built-in Obsidian Bases in `9 Claude files/Tables/`. Bookmarked HOME.

## 2026-11-20 · personal-laptop · claude-code
- did: committed the uncommitted landscape work (job 2), then delegated the prior-art update to 3 sub-agents: ingested ThinkEdit + Steer2Edit (Q5 links now resolve), built `1 Literature review/outline.md` (section 8 written out) + `matrix.md` (new "prior art or threat to" column), red-teamed Q1 against the new papers.
- learned: Q1 is not scooped (Gao steers readability, never checks human ratings), but valence must beat a layer-0 probe and a supervised readability direction. Stable is the least covered test; Q3 faces the most threats.
- open-next: Harshit to accept/reject the proposed Q1 kill line and the cheap Buse-Weimer pre-check; update exp01 spec controls; verify Steer2Edit Table 10 numbers against the PDF.

## 2026-11-20 · personal-laptop · claude-code (2)
- did: `TASKS.md` is now the one task list ("For you" / "For Claude"). Plain-English file names for all notes; `03-threads` is now `5 Research ideas (later)`; T1-T5 are now Q1-Q5. Writing rule (80% ASD-STE100) and naming rule are in CLAUDE.md.
- learned: the user found tasks spread over many files, codes like "T1" and kebab-case names hard to read. Answer "what is pending" from `TASKS.md` only.
- open-next: see `TASKS.md`.
- 2026-11-20 later: new folders (5 Research ideas (later), 2 Papers, 3 Ideas, 4 My notes, 9 Claude files). Rewrote HOME, TASKS, Q1-Q5 and the 3 papers of this week in plain English. Other notes still use the old style.
- 2026-11-20 later: back to metacognition. Q1 is now a go/no-go check; new Q6 (proposed): can the model read and use its own signal? Notes for Ji-An 2025 and Lindsey 2025; Ji-An replaces Gao in Read this week. Decision on Q6 is in TASKS.
- 2026-11-20 later: refocused on the literature review (due 2026-11-24). Review is now folder "1 Literature review"; questions parked in "5 Research ideas (later)". CLAUDE.md has a "Current goal" section: no experiment work unless asked. Next for Claude: notes for missing core papers, then gaps.md, then the first section draft.

## 2026-11-20 · personal-laptop · claude-code (review loop)
- did: ran the user's 7-step review plan in 8 rounds, no sub-agents. 13 new paper notes (7 core + 6 from a new search; sections 2, 3, 5, 6, 7), 30 arXiv finds scored in Reading list, outline + matrix (38 rows), `gaps.md` (13 gaps), first drafts `03-monitoring.md` and `05-persistent-control.md` with critic fixes and open doubts, HOME "Read this week" swapped (user had ticked Jiang; note set to read).
- learned: arXiv HTML often drops numbers in math markup, so many results numbers are flagged [unverified]; Doya 2002 has no open full text (note is abstract-only). Critic pass caught two overclaims: self-reward *does* use own signals for learning (gap is hidden-state signals only), and older self-modifying networks (Irie 2022, Nested Learning) must be cited before claiming self-modification is new.
- open-next: see `TASKS.md` (user: read drafts, decide Irie/Nested Learning in or out, pick next sections; Claude: notes for Rubin 2611.15267, Fleming and Daw 2017, Zeng 2026, number checks). `9 Claude files/Tables/papers.base` has an uncommitted user change, left alone.

## 2026-11-20 · personal-laptop · claude-code (review loop 2)
- did: 5 rounds, no sub-agents. Notes for Rubin 2611.15267, Fleming and Daw 2017, Zeng 2608.30980; all numbers in sections 3 and 5 checked against 26 full texts (report in `9 Claude files/Reports/2026-11-20 number check.md`), Steer2Edit Table 10 checked in PDF; XSS + DNS-rebinding fix in `scripts/dashboard.py`; removed worktree `prior-art-landscape` (branch name left, fully merged).
- learned: we had misquoted Rubin: chance-level reports only at an early OLMo checkpoint, 89.6% at the released base (layer 0 injection). Zeng finds no consistent own-model edge in trained self-prediction. arXiv HTML + `pdftotext` via curl work without sub-agents.
- open-next: every "For Claude" item now waits for the user (Irie/Nested Learning in or out, section order, scout guard). `papers.base` user change still uncommitted, left alone.
