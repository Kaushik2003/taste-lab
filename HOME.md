---
type: dashboard
status: active
tags: [type/hub, dashboard]
links: ["[[TASKS]]", "[[reading-queue]]", "[[HANDOFF]]", "[[Gaps in the field]]", "[[Q1 Does the model sense code quality]]"]
---

# Home

> [!tip] How to use this page
> Click any colored link to open a note. To come back here, click **Home** in the bookmarks panel on the left (the bookmark icon).
> You don't need the terminal. To ask Claude for help, write a normal sentence (see the last section).

> [!important] Your tasks
> Open [[TASKS]] to see what you need to do. It is the only task list.

## 1. What we are doing now

We want to know if an AI model can judge its own code: "this code is good" or "this code is bad".
The first step is one question and one experiment:

- **Question:** [[Q1 Does the model sense code quality|Does the model have an internal signal for code quality?]]
- **Experiment:** [[04-experiments/exp01-valence-probe/spec|Experiment 1: read that signal from the model]]

The other questions wait for this one.

## 2. Read this week

Start with these 3 papers. Open the note first (it is short). Open the full paper only if you want more.
Tick the box when you finish.

- [ ] [[Value axis - model knows it is on track (Jiang 2026)|The Value Axis]]: a model knows when it is "on the right track", tested on code. Closest to our work.
- [ ] [[Steer code readability inside the model (Gao 2026)|Readability of code with RepE]]: someone already steered code readability. How are we different?
- [ ] [[Introspection claims fail basic checks (Singh 2026)|Can LLMs introspect?]]: the strongest warning against our idea.

Finished these? The list below shows what to read next.

![[_views/papers.base#Read next]]

## 3. Our research questions

Status words: **active** = we work on it now, **parked** = later, **killed** = we stopped it.

![[_views/questions.base]]

## 4. Warnings

These papers show ways our idea can fail. Read them before you trust a result.

![[_views/papers.base#Warnings (papers against our idea)]]

## 5. The big picture

The field has 5 parts. Each note gives a short summary and its papers.

1. [[Field map - Models read their own state|Can a model watch its own thinking?]]
2. [[Field map - Models judge good and bad|Signals for "good" and "bad" inside the model]]
3. [[Field map - Changes that stay in the weights|Can a model change its own weights?]]
4. [[Field map - Limits of self-learning|Why self-training often fails]]
5. [[Field map - Taste and new ideas|Taste and new ideas]]

Where nobody has done the work yet: [[Gaps in the field|Gap table]]

## 6. Your own ideas

Write your thoughts, hunches and bets in the folder **06-patterns**. Claude reads this folder but never changes it.
Make a new note there: right-click the folder, then click **New note**.

## 7. Get help from Claude

Write a normal sentence to Claude. You do not need special commands. Some examples:

- "Explain the Value Axis paper in simple words."
- "What should I read next?"
- "I finished the Value Axis paper. My opinion: ..." (Claude saves it in the paper note.)
- "Find new papers about this topic."
- "What can go wrong with question Q1?"
- "Update the home page."

## More

- [[reading-queue|Full reading list]] (long, use only when the list above is empty)
- [[HANDOFF|Work log]] (what each Claude session did)

All papers:

![[_views/papers.base#All papers]]
