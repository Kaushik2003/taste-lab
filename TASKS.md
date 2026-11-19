---
type: tasks
status: active
tags: [type/hub, tasks]
links: ["[[HOME]]", "[[outline]]", "[[matrix]]"]
---

# Tasks

This is the only list of open work. Claude updates it at the end of each session.
Our goal now: **write the literature review by 24 November 2026.** No experiments for now.

- **For you:** only you can do these. Each task says what to do and when it is done.
- **For Claude:** Claude does these. Some need your "yes" first.
- When you finish a task, tick the box. Claude moves it to "Done" at the next session.

## For you

- [ ] **Check the plan of the review.**
  Open [[outline]]. It has 9 sections and the papers in each one.
  Check the sections, their order, and where each paper sits.
  *Done when:* you tell Claude "outline is OK" or what to change.

- [ ] **Say what is in and out of the review.**
  The angle now: metacognition, models that change their own weights (WSP, SEAL), and model taste.
  Tell Claude if a topic must be added or removed. Examples: "add uncertainty and calibration", "drop the maths papers".
  *Done when:* you tell Claude the scope, or "scope is OK".

- [ ] **Read the 3 papers under "Read this week" on [[HOME]].**
  Ji-An (models report their own activations), Jiang (value axis) and Singh (introspection checks).
  After each one, tell Claude your opinion in one or two sentences. Claude saves it in the paper note.
  *Done when:* you tick them on HOME.

- [ ] **Pick the section Claude drafts first.**
  Claude suggests section 3, "Monitoring", because it is the center of the metacognition angle.
  *Done when:* you tell Claude the section.

## For Claude

- [ ] Find the core papers the review still misses, and write notes for them. Metacognition: Nelson and Narens (1990), "Language models (mostly) know what they know" and other self-knowledge work, "Training LMs for introspective oversight". Weight editing: "Exploring WSP", WeightBench, GUARD, Doya (2002).
- [ ] Write `1 Literature review/gaps.md`: the gaps and patterns across all papers (the /gaps command). Start from [[Gaps in the field]].
- [ ] Draft the first section. *Waits for:* your choice of section and your OK on the outline.
- [ ] Check one number in the Steer2Edit paper against the PDF (Table 10, the drop from 87.8 to 77.3).
- [ ] Fix a security problem in the dashboard script (a bad link in a note can run code in the page).
- [ ] Add a safety check to the daily scout script before it runs every hour. *Waits for:* your "yes".
- [ ] Delete the old extra copy of the repo (the work copy named `worktree-prior-art-landscape`).

## Later (after the review)

These were research tasks. They wait until the review is done.
- Decide on the new question Q6, "Can the model read and use its own signal?" ([[Q6 Can the model read and use its own signal]]).
- Decide the stop rule for Q1 and the quick test on public data ([[Q1 Does the model sense code quality]]).
- Find 5 people to rate code, and add the new controls to the Q1 experiment.

## Done

- [x] 2026-11-20: Claude moved the review to the top (folder "1 Literature review") and parked the research questions in "5 Research ideas (later)".
- [x] 2026-11-20: Claude wrote notes for Ji-An 2025 and Lindsey 2025, two core metacognition papers.
- [x] 2026-11-20: Claude gave every note a plain name. Claude made this file the one task list.
- [x] 2026-11-20: Claude saved and sent the paper search (17 papers) and the literature review plan to GitHub.
