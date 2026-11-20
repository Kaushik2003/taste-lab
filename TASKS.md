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

- [ ] **Read the papers under "Read this week" on [[HOME]].**
  First the 3 new ones: the 2026 metacognition survey (Liu), the model trained to watch itself (Wang) and WeightBench (Marasini).
  Also the new one from today's scout: a model that rewrites its own weights (Fan 2026). It changed section 5 and gap 1.
  Then, if you have time, the 2 left from last week: models that report their own activations (Ji-An) and the introspection checks (Singh).
  After each one, tell Claude your opinion in one or two sentences. Claude saves it in the paper note.
  You ticked the Value Axis paper: tell Claude your opinion of it too.
  *Done when:* you tick the 4 new ones on HOME.

- [ ] **Read the two section drafts and their open doubts.**
  Section 3 [[03-monitoring]] and section 5 [[05-persistent-control]] are first drafts, built from paper notes only.
  Each ends with a list of open doubts. Say which doubts matter and whether the main line of each section is right.
  *Done when:* you tell Claude "draft OK" or what to change, for each section.

- [ ] **Decide if older self-modifying networks are in the review.**
  Section 5 now cites one language model that edits its own weights (Fan 2026). Older networks also learn to rewrite their own weights (Irie 2022, Nested Learning 2025).
  The notes now exist: Claude's search wrote them on 2026-11-20 before you decided ([[SRWM - a weight matrix that rewrites itself (Irie 2022)]], [[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]). Both change themselves by a learned rule, with no judgment of good and bad.
  If "in", section 5 gets one more paragraph. If "out", Claude removes the two notes and the review says why in one sentence.
  *Done when:* you say "in" or "out".

- [ ] **Check the new main gap.**
  Today's scout found a model that edits its own weights after it reads its own hidden states (Fan 2026).
  So Claude changed gap 1: the gap is now "no model edits itself by its own judgment of good and bad". Section 5, the outline and the paper table now say this too.
  Open [[gaps]] (first row) and section 5.2 in [[05-persistent-control]].
  *Done when:* you tell Claude "new gap OK" or how to change it.

- [ ] **Decide what the Stable test means.**
  Two new papers show that a model's preferences move when the task context changes (37% of cases) or when it plays a persona. Rewording moves them much less (10%).
  So "stable across context" may be too strict. The other choice: stable across wording only, and accept that fine-grained taste depends on context.
  See the Stable row in [[gaps]] and [[Task context moves model preferences (Trhlik 2026)]].
  *Done when:* you tell Claude "across context" or "across wording only".

- [ ] **Pick the next sections to draft.**
  Due date is 24 November. Claude suggests section 2 "Foundations" (6 notes now) and section 6 "Limits" next, then 4 and 7.
  *Done when:* you tell Claude the order.

## For Claude

- [ ] Search for papers on world models and propose where they fit in the [[outline]]. World models were added to the scope on 2026-11-20. Two likely links: a self-model (the meta level's model of the object level), and a model that predicts the effect of a self-edit before it writes the edit. Then ask you to confirm the placement.
- [ ] Add one paragraph on older self-modifying networks to section 5, or remove the Irie and Nested Learning notes. *Waits for:* your "in or out" decision above.
- [ ] Draft the next sections. *Waits for:* your choice of order.
- [ ] Add a safety check to the daily scout script before it runs every hour. *Waits for:* your "yes".

## Later (after the review)

These were research tasks. They wait until the review is done.
- Decide on the new question Q6, "Can the model read and use its own signal?" ([[Q6 Can the model read and use its own signal]]).
- Decide the stop rule for Q1 and the quick test on public data ([[Q1 Does the model sense code quality]]).
- Find 5 people to rate code, and add the new controls to the Q1 experiment.

## Done

- [x] 2026-11-20: Claude searched 6 new angles and wrote 12 notes (8 at the top score). [[outline]], [[gaps]] and [[matrix]] are updated. Report: [[2026-11-20 angles]].
- [x] 2026-11-20: You checked the [[outline]]: it is OK for now.
- [x] 2026-11-20: You set the scope: metacognition, models that change their own weights, model taste, and now **world models** too.
- [x] 2026-11-20: Claude ran a 5-round review loop:
  - notes for Rubin 2026, Fleming and Daw 2017 and Zeng 2026. Rubin changed a claim in section 3: the model answers at chance only early in training (89.6% at the released model);
  - every number in sections 3 and 5 checked against 26 sources, all correct ([[2026-11-20 number check]]); Steer2Edit Table 10 checked in the PDF;
  - dashboard security fix (a bad link in a note could run code in the page);
  - old extra copy of the repo removed.
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
