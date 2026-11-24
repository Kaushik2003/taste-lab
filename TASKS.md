---
type: tasks
status: active
tags: [type/hub, tasks]
links: ["[[HOME]]", "[[outline]]", "[[matrix]]"]
---

# Tasks

This is the only list of open work. Claude updates it at the end of each session.
Our goal now: **finish the literature review (first full draft written on 24 November 2026).** No experiments for now.

- **For you:** only you can do these. Each task says what to do and when it is done.
- **For Claude:** Claude does these. Some need your "yes" first.
- When you finish a task, tick the box. Claude moves it to "Done" at the next session.

## For you

- [ ] **Read the full review once, from start to end.**
  It is written: 10 sections, about 17,000 words, 147 references. You must be able to explain each section in two sentences, because your name goes on it.
  Open [[Literature review - full paper]], or the Word and PDF files in the folder `1 Literature review/export`. Start with the abstract, Section 9 and Section 10 (20 minutes); they hold the argument.
  *Done when:* you tell Claude what to change, or "review OK".

- [ ] **Add the author names and check where the review goes.**
  The title page says "[add names]". Claude does not know the author list, the reader (a course, a supervisor, a journal) or a length limit. If there is a length limit, tell Claude and it will cut.
  *Done when:* you give Claude the names and the destination.

- [ ] **Read the starred papers in the reading guide.**
  The review cites 147 sources and you have read few of them. The guide lists the ones you need to defend the review: 11 starred papers, about 3 hours.
  Open [[Reading guide for 24 November]].
  *Done when:* you can say one sentence per starred paper.

- [ ] **Say "commit" so Claude can save the work in git.**
  Nothing from 23 and 24 November is committed: the review, 17 new paper notes, the reports and the build script exist only as files on this laptop. Claude tried to commit and the tool's safety check stopped it, because you had not asked for a commit.
  *Done when:* you say "commit" (and "push" if you also want it on GitHub).

## For Claude

- [ ] Check every claim marked "abstract only" in the review against the full paper (13 places), and the author lists that still say "et al." in the references. *Waits for:* nothing; next session.
- [ ] Apply your changes to the review after you read it. *Waits for:* your reading.
- [ ] Write notes for the gap-check finds still without notes (end of [[Reading list]]).
- [ ] Bring [[gaps]], [[matrix]], [[outline]] and [[HOME]] in line with the new review (they still describe the old code-readability plan in places).
- [ ] Add a safety check to the daily scout script before it runs every hour. *Waits for:* your "yes".

## Later (after the review)

These were research tasks. They wait until the review is done.
- Decide on the new question Q6, "Can the model read and use its own signal?" ([[Q6 Can the model read and use its own signal]]).
- Decide the stop rule for Q1 and the quick test on public data ([[Q1 Does the model sense code quality]]).
- Find 5 people to rate code, and add the new controls to the Q1 experiment.

## Done

- [x] 2026-11-24: You said "go". Claude wrote the whole review and exported it to Word and PDF. Decisions used: the full idea is an open agenda with its eight problems stated; a taste of a model's own is a possibility, not a prediction; the closing question is "when a model's weights change after deployment, do its preferences move, and does its self-monitoring change?". Claude kept its rewrite of sections 1 to 3 and built on it. The old code-readability synthesis is kept in [[Parked - old synthesis and study protocol]].
- [x] 2026-11-24: Claude read in full, at your request: the Sleep paper, the paper on self-distillation and lost doubt (Kim 2026), and six papers on whether a model notices its own change. Notes are in `2 Papers`.
- [x] 2026-11-24: You chose the direction: the full idea (a model that edits itself by its own judgment and may develop taste) is the frame of the review; the first research question is "do direct weight edits move a model's preferences?". Claude checked that question: one close paper (Fafuła 2026, one edit shifts disposition), none on a sequence of edits. See [[2026-11-23 gap check]].
- [x] 2026-11-24: These older tasks are closed by the new direction: the "Read this week" list (replaced by today's guide), the open doubts of sections 3 and 5, older self-modifying networks (in, one paragraph), the new main gap (replaced by the gap check), the Stable test (the review reports the evidence: wording moves 10% of preferences, task context 37%), the section order (all sections are written together), world models (a section of their own in the review).
- [x] 2026-11-23: Claude checked whether your idea is a real gap: 2 search rounds, 8 new notes, verdict in [[2026-11-23 gap check]].
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
