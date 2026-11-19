---
type: tasks
status: active
tags: [type/hub, tasks]
links: ["[[HOME]]", "[[Q1 Does the model sense code quality]]"]
---

# Tasks

This is the only list of open work. Claude updates it at the end of each session.

- **For you:** only you can do these. Each task says what to do and when it is done.
- **For Claude:** Claude does these. Some need your "yes" first.
- When you finish a task, tick the box. Claude moves it to "Done" at the next session.

## For you

- [ ] **Decide the new stop rule for Question 1.**
  Question 1 asks: "Does the model have an internal signal for code quality?"
  A stop rule says which result makes us stop this question.
  Claude proposes a stricter rule, because a new paper (Gao) makes a weak result easy to explain away.
  Open [[Q1 Does the model sense code quality]], read the last line under "Log", and write "yes" or "no" under it.
  *Done when:* you write "yes" or "no".

- [ ] **Decide if we run a quick test first.**
  Before people rate code (2 to 3 days of work), we can test the idea on a public set of code that people already rated for readability.
  This takes about one afternoon on one GPU. If the result is bad, we save the 2 to 3 days.
  *Done when:* you tell Claude "yes" or "no".

- [ ] **Find 5 people to rate code.**
  Experiment 1 needs people who rate how easy code is to read.
  They must not know what we expect to find. So you cannot be one of them.
  *Done when:* you have 5 names.

- [ ] **Check the plan for the literature review before 24 Nov.**
  Open [[outline]]. Check that each paper is in the correct section.
  *Done when:* you tell Claude "outline is OK" or what to change.

- [ ] **Keep or drop the gap table.**
  [[Gaps in the field]] lists what other papers do not cover yet. It waits for your decision.
  *Done when:* you tell Claude "keep" or "drop".

- [ ] **Read 3 papers.** Start with the 3 papers under "Read this week" on [[HOME]].
  *Done when:* you tick them on HOME.

## For Claude

- [ ] Add the new controls to Experiment 1. *Waits for:* your stop-rule decision.
- [ ] Check one number in the Steer2Edit paper (Table 10, 87.8 to 77.3) against the PDF.
- [ ] Fix a security problem in the dashboard script (a bad link in a note can run code in the page).
- [ ] Add a safety check to the daily scout script before it runs every hour. *Waits for:* your "yes".
- [ ] Delete the old work copy of the repo (`worktree-prior-art-landscape`).

## Done

- [x] 2026-11-20: Claude gave every note a plain name (Q1 to Q5 for questions; papers show what they found). Claude made this file the one task list.

- [x] 2026-11-20: Claude saved and sent the paper search (17 papers) and the literature review plan to GitHub.
