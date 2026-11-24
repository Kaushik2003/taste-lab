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

- [ ] **Settle the rules on AI use with your supervisor or course, before you hand anything in.**
  An AI wrote the review, and you have read few of the sources. An independent check says this is the first problem: many universities treat undisclosed AI-written work as misconduct. The review now ends with a draft "Statement on the use of AI". Adapt it to the rule you are given.
  See [[2026-11-24 independent critique of the review]], point 1.
  *Done when:* you know the rule, and the statement in the review matches it.

- [ ] **Tell Claude which papers you read in full.**
  On 24 November you told Claude that you have read the papers and can defend the review. The review still says that 7 of 137 papers were read in full, because that is what the notes record. Give Claude your list, so that the method section and the statement on AI use say what is true.
  *Done when:* you give Claude the list (titles or first authors are enough).

- [ ] **Answer Claude's questions for Sections 1, 9 and 10, in your own words.**
  You asked for help with the writing. The plan: Claude asks short questions, you answer in rough words (chat is fine), Claude turns your answers into text, and you correct it. Then these three sections carry your argument in your voice. The statement on AI use will say that Claude helped.
  *Done when:* you answer the questions in the chat of 24 November, or ask Claude to ask them again.

- [ ] **Decide whether Claude shortens the abstract for the IEEE version.**
  The abstract has about 320 words. IEEE journals ask for 150 to 250. Claude did not cut it, because that changes your text.
  File: [[00-title-and-abstract]]. PDF: `1 Literature review/export/Literature review - full paper (IEEE).pdf`.
  *Done when:* you say "shorten it" or "keep it".

- [ ] **Add the author names and say where the review goes.**
  The title page says "[add names]". Claude does not know the reader (a course, a supervisor, a journal).
  *Done when:* you give Claude the names and the destination.

- [ ] **Say "commit" so Claude can save today's changes in git.**
  You committed the first draft yourself. Everything since then (the style pass, the answer to the critique, the figure) is not committed.
  Also: your commit put the folder `writing-guide` in git. It holds copies of published papers. Tell Claude to take it out of git before you push to a public place.
  *Done when:* you say "commit".

## For Claude

- [ ] Apply the fixes from [[2026-11-24 independent critique of the review]]: cite Zhang, Yuan and Zhang 2026 and four other close works, add the missing classic papers, fix the abstract, quote or reword eight phrases, fix the references. *Waits for:* your choice of fixes.
- [ ] Finish the critique's open points: evidence-quality column in [[matrix]], author lists that still say "et al.", years of Johnson and Lindsey, a plagiarism-tool run. See [[2026-11-24 response to the critique]].
- [ ] Check every claim marked "abstract only", "summary only" or "not extracted" in the review against the full paper (18 places), and the author lists that still say "et al." in the references. *Waits for:* nothing; next session.
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

- [x] 2026-11-24: You told Claude you have read the papers and can defend the review. Claude declined to rewrite the text to lower an AI-detector score, and ran a wording check against the sources instead.
- [x] 2026-11-24: Claude revised the review with your writing guides and answered the independent critique: Sections 3 to 8 rewritten as prose in the past tense, three overclaims corrected, 22 classic and related sources added, a section on related surveys, Figure 1, and a statement on AI use. Details: [[2026-11-24 response to the critique]].
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
