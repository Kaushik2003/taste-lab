---
type: dashboard
status: active
tags: [type/hub, dashboard]
links: ["[[TASKS]]", "[[Reading list]]", "[[HANDOFF]]", "[[Gaps in the field]]", "[[Q1 Does the model sense code quality]]"]
---

# Home

> [!tip] Start here
> This is the front page. Click any colored link to open a note.
> To come back, click **Home** in the bookmarks panel on the left (the bookmark icon).
> You do not need the terminal. To ask Claude for help, write a normal sentence (see the last section).

> [!important] Your tasks
> Open [[TASKS]] to see what you need to do. It is the only task list.

> [!note] The folders
> - **1 Questions:** our research questions and their experiments.
> - **2 Papers:** one short note per paper.
> - **3 Ideas:** short notes that explain one idea each.
> - **4 My notes:** your own thoughts. Only you write here.
> - **9 Claude files:** Claude's working files. You can ignore this folder.

## 1. What we are doing now

We want to know if an AI model can judge its own code: "this code is good" or "this code is bad".
The first step is one question and one experiment:

- **Question:** [[Q1 Does the model sense code quality|Does the model have an internal signal for code quality?]]
- **Experiment:** [[1 Questions/Q1 experiment - read the signal/Plan|Experiment 1: read that signal from the model]]

The other questions wait for this one.

## 2. Read this week

Start with these 3 papers. Open the note first (it is short). Open the full paper only if you want more.
Tick the box when you finish.

- [ ] [[Value axis - model knows it is on track (Jiang 2026)|The Value Axis]]: a model knows when it is "on the right track", tested on code. Closest to our work.
- [ ] [[Steer code readability inside the model (Gao 2026)|Steer code readability]]: other researchers already changed code readability from inside the model. How are we different?
- [ ] [[Introspection claims fail basic checks (Singh 2026)|Can models look inside themselves?]]: the strongest warning against our idea.

Finished these? The list below shows what to read next.

![[9 Claude files/Tables/papers.base#Read next]]

## 3. Our research questions

Status words: **active** = we work on it now, **parked** = later, **killed** = we stopped it.

![[9 Claude files/Tables/questions.base]]

## 4. Warnings

These papers show ways our idea can fail. Read them before you trust a result.

![[9 Claude files/Tables/papers.base#Warnings (papers against our idea)]]

## 5. The big picture

The field has 5 parts. Each note gives a short summary and its papers.

1. [[Field map - Models read their own state|Can a model watch its own thinking?]]
2. [[Field map - Models judge good and bad|Signals for "good" and "bad" inside the model]]
3. [[Field map - Changes that stay in the weights|Can a model change its own weights?]]
4. [[Field map - Limits of self-learning|Why self-training often fails]]
5. [[Field map - Taste and new ideas|Taste and new ideas]]

What nobody has done yet: [[Gaps in the field|Gap table]]

## 6. Your own ideas

Write your thoughts, hunches and bets in the folder **4 My notes**. Claude reads this folder but never changes it.
To make a new note there, right-click the folder, then click **New note**.

## 7. Get help from Claude

Write a normal sentence to Claude. You do not need special commands. Some examples:

- "Explain the Value Axis paper in simple words."
- "What should I read next?"
- "I finished the Value Axis paper. My opinion: ..." (Claude saves it in the paper note.)
- "Find new papers about this topic."
- "What can go wrong with the code quality question?"
- "Update the home page."

## More

- [[Reading list|Full reading list]] (long, use only when the list above is empty)
- [[HANDOFF|Work log]] (what each Claude session did)

All papers:

![[9 Claude files/Tables/papers.base#All papers]]
