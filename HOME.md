---
type: dashboard
status: active
tags: [type/hub, dashboard]
links: ["[[TASKS]]", "[[Reading list]]", "[[HANDOFF]]", "[[Gaps in the field]]", "[[outline]]", "[[matrix]]"]
---

# Home

> [!tip] Start here
> This is the front page. Click any colored link to open a note.
> To come back, click **Home** in the bookmarks panel on the left (the bookmark icon).
> You do not need the terminal. To ask Claude for help, write a normal sentence (see the last section).

> [!important] Your tasks
> Open [[TASKS]] to see what you need to do. It is the only task list.

> [!note] The folders
> - **1 Literature review:** the main work. The plan, the paper table and the section drafts.
> - **2 Papers:** one short note per paper.
> - **3 Ideas:** short notes that explain one idea each.
> - **4 My notes:** your own thoughts. Only you write here.
> - **5 Research ideas (later):** possible research questions. They wait until the review is done.
> - **9 Claude files:** Claude's working files. You can ignore this folder.

## 1. What we are doing now

We are **writing a literature review**. It is due on **24 November 2026**.
We are still choosing our research idea. The review shows what other people did and what is still missing.

The angle:
- **Metacognition:** can a model watch its own state and control it?
- **Models that change their own weights:** weight-space programming (WSP) and self-edits (SEAL).
- **Taste:** can a model have likes and dislikes of its own?
- **World models:** a model's inner picture of the world and of itself. Added 20 November; where it fits is still open.

Open these:
- [[outline|The plan of the review]]: 9 sections and the papers in each one.
- [[matrix|The paper table]]: which paper covers which part.
- [[gaps|What nobody has done yet]] (14 gaps, updated 21 November)
- [[08-synthesis|Section 8, Synthesis]]: where the whole argument comes together. Read this first if you read one section.
- First drafts that wait for your review: [[03-monitoring|Section 3, Monitoring]] and [[05-persistent-control|Section 5, Persistent control]]. Each ends with a list of open doubts.

**Where things stand (21 November):** all 9 sections have a draft in **1 Literature review**. There are 119 paper notes in **2 Papers**. Sections 1, 2, 4, 6, 7, 8 and 9 were deepened on 21 November. Sections 3 and 5 are untouched and wait for your "draft OK".

## 2. Read this week

Start with these 4 papers. Open the note first (it is short). Open the full paper only if you want more.
Tick the box when you finish.

- [ ] [[Survey of metacognition in language models (Liu 2026)|The 2026 survey of metacognition in language models]]: the review we must position against. It covers "watch" and "control", but never taste and never models that change their own weights. Those two parts are our space.
- [ ] [[Training LMs to watch themselves (Wang 2026)|A model trained to watch itself]]: the strongest new evidence that a model reads its own behavior better than other models do. It is about behavior, not inner states.
- [ ] [[WeightBench - models cannot yet patch models (Marasini 2026)|WeightBench]]: strong models cannot yet fix language models by editing weights, and cannot tell an impossible edit from a hard one. This joins our two topics.
- [ ] [[A model rewrites its own weights (Fan 2026)|A model rewrites its own weights]] (new today): a 27B model edits its own weights after it reads its own hidden states. Graded answers still decide which edits to keep. This changed section 5 and the first gap.

Still open from last week (read if you have time):
- [ ] [[Models can report and control their own activations (Ji-An 2025)|Models report and control their own activations]]
- [ ] [[Introspection claims fail basic checks (Singh 2026)|Can models look inside themselves?]]
- [x] [[Value axis - model knows it is on track (Jiang 2026)|The Value Axis]] (done)

Finished these? The list below shows what to read next.

![[9 Claude files/Tables/papers.base#Read next]]

## 3. Possible research ideas (later)

These are ideas the review may lead to. They wait until the review is done.

![[9 Claude files/Tables/questions.base]]

## 4. Warnings

These papers show limits and failures. The review must discuss them.

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
- "Draft section 3 of the review."
- "What gaps do the papers show?"
- "Update the home page."

## More

- [[Reading list|Full reading list]] (long, use only when the list above is empty)
- [[HANDOFF|Work log]] (what each Claude session did)

All papers:

![[9 Claude files/Tables/papers.base#All papers]]
