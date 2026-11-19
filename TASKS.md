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

- [ ] **Read the 3 new papers under "Read this week" on [[HOME]].**
  The 2026 metacognition survey (Liu), the model trained to watch itself (Wang) and WeightBench (Marasini).
  After each one, tell Claude your opinion in one or two sentences. Claude saves it in the paper note.
  You ticked the Value Axis paper: tell Claude your opinion of it too.
  *Done when:* you tick them on HOME.

- [ ] **Read the two section drafts and their open doubts.**
  Section 3 [[03-monitoring]] and section 5 [[05-persistent-control]] are first drafts, built from paper notes only.
  Each ends with a list of open doubts. Say which doubts matter and whether the main line of each section is right.
  *Done when:* you tell Claude "draft OK" or what to change, for each section.

- [ ] **Decide if older self-modifying networks are in the review.**
  Section 5 says no language model edits its own weights by reading them. But older networks learn to rewrite their own weights (Irie 2022, Nested Learning 2025).
  If they are in scope, Claude writes notes for them and section 5 gets one more paragraph. If not, the review must say why.
  *Done when:* you say "in" or "out".

- [ ] **Pick the next sections to draft.**
  Due date is 24 November. Claude suggests section 2 "Foundations" (6 notes now) and section 6 "Limits" next, then 4 and 7.
  *Done when:* you tell Claude the order.

## For Claude

- [x] Write notes for the papers the critic review found missing: Rubin 2026 (arXiv 2611.15267), Fleming and Daw (2017), Zeng 2026. Done 2026-11-20.
- [ ] Write notes for Irie 2022 and Nested Learning (older self-modifying networks). *Waits for:* your "in or out" decision above.
- [ ] Check the numbers in the two drafts against the papers (most come from skimmed notes). Start with the WSP math gain, the SEAL ARC gain and the observer scores.
- [ ] Draft the next sections. *Waits for:* your choice of order.
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

- [x] 2026-11-20: Claude finished the 7-step review plan in 8 rounds:
  - notes for the 7 core papers (Nelson and Narens, Kadavath, Doya, introspective oversight, Exploring WSP, WeightBench, GUARD);
  - a new search: 6 more notes (Liu survey, Binder, Yax, Shumailov, OMNI, Hughes), with 30 other finds scored in the [[Reading list]];
  - [[outline]] and [[matrix]] updated (38 papers);
  - [[gaps]] written (13 gaps);
  - first drafts of section 3 and section 5, reviewed by Claude as a critic, with open doubts listed;
  - "Read this week" on HOME updated.
- [x] 2026-11-20: You picked section 3 and then section 5 to draft first (in the review plan you gave Claude).

- [x] 2026-11-20: Claude moved the review to the top (folder "1 Literature review") and parked the research questions in "5 Research ideas (later)".
- [x] 2026-11-20: Claude wrote notes for Ji-An 2025 and Lindsey 2025, two core metacognition papers.
- [x] 2026-11-20: Claude gave every note a plain name. Claude made this file the one task list.
- [x] 2026-11-20: Claude saved and sent the paper search (17 papers) and the literature review plan to GitHub.
