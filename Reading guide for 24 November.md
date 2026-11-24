---
type: guide
status: active
tags: [type/guide, reading]
links: ["[[TASKS]]", "[[2026-11-23 gap check]]", "[[2026-11-23 direction critique]]", "[[outline]]"]
---

# Reading guide for 24 November

**Goal for today:** understand the field well enough to choose how the literature review is framed. Total time: about 5 hours. If you have only 2 hours, read the papers marked ★.

**How to read each paper (10 to 25 minutes each):**
1. Read our note first (2 minutes). The link is in each row.
2. Open the paper. Read the abstract, look at the first figure, read the conclusion.
3. Write one sentence: "This paper shows ...". Tell it to Claude; Claude saves it in the note.
4. Do not read methods or appendices today.

## Start here (15 minutes)
- [[2026-11-23 direction critique]]: the eight problems with the full idea, and the three possible directions.
- [[2026-11-23 gap check]], only the "Final verdict" part.

## Block 1: can a model watch itself? (70 minutes)
*This block answers: is "metacognition in language models" solid enough to be the base of the review?*

| Paper | Min | Question to answer while you read |
|---|---|---|
| ★ [[Survey of metacognition in language models (Liu 2026)]] ([paper](https://arxiv.org/abs/2607.11881)) | 25 | Into which three parts does the survey split the field? What does it say is missing? |
| [[Models mostly know what they know (Kadavath 2022)]] ([paper](https://arxiv.org/abs/2207.05221)) | 10 | What can a model say about its own answers, and how was that tested? |
| ★ [[Models sometimes notice injected thoughts (Lindsey 2025)]] ([paper](https://transformer-circuits.pub/2025/introspection/index.html)) | 15 | How often does the model notice the injected thought? Why is "20% with no false alarms" still interesting? |
| ★ [[Introspection claims fail basic checks (Singh 2026)]] ([paper](https://arxiv.org/abs/2605.26242)) | 10 | Which two simple checks break the earlier claims? |
| [[Models act on their own confidence (Kumaran 2026)]] ([paper](https://arxiv.org/abs/2603.22161)) | 10 | What is the difference between "the signal exists" and "the model uses it"? |

**After block 1 you should be able to say:** models carry signals about their own work; outside tools read them well; the model itself reads them poorly, except for confidence.

## Block 2: can a model change its own weights? (85 minutes)
*This block answers: is weight editing real, and what are its limits?*

| Paper | Min | Question to answer while you read |
|---|---|---|
| ★ [[WSP - a model reads and edits weights (Takehi 2026)]] ([blog](https://rikiyat.github.io/blog/weight-space-programming/)) | 20 | What exactly did the editor change, and what fault did that fix? |
| ★ [[A model rewrites its own weights (Fan 2026)]] ([paper](https://arxiv.org/abs/2611.21885)) | 25 | Who decides which edit is kept? Does each session start from the original weights? Which model sizes fail? |
| [[One direction controls refusal (Arditi 2024)]] ([paper](https://arxiv.org/abs/2406.11717)) | 15 | How can one direction be removed from the weights with no training? (This is the simplest edit; the first project would use edits like it.) |
| [[A cheap optimizer beats the agent's weight repair (Salloum 2026)]] ([paper](https://arxiv.org/abs/2611.14210)) | 10 | If a $0.90 optimizer beats the agent, what is left for a self-editing model to add? |
| ★ [[Many sequential weight edits cause sudden forgetting (Gupta 2024)]] ([paper](https://arxiv.org/abs/2401.07453)) | 10 | What happens when edits pile up? What are the two phases? |
| ★ [[One weight edit shifts a model's disposition (Fafuła 2026)]] ([paper](https://arxiv.org/abs/2607.17427)) | 10 | What changed in the model besides refusals? Which follow-up does the author say is missing? (Closest work to the first project.) |
| ★ [[Self-report becomes faithful when preferences sit early (Atkinson 2026)]] ([paper](https://arxiv.org/abs/2610.07186)) | 15 | When does a model start to report its trained preferences correctly? Which model sizes can do it? |

**After block 2 you should be able to say:** small direct edits work for local faults; a model has edited itself once; repeated edits are known to break models; one edit can already shift a model's disposition.

## Block 3: does a model have preferences of its own? (65 minutes)
*This block answers: can "taste" be measured, and does it belong to one model?*

| Paper | Min | Question to answer while you read |
|---|---|---|
| ★ [[Hidden good-bad feeling changes choices (Berg 2026)]] ([paper](https://arxiv.org/abs/2609.35591)) | 20 | How do they show that a hidden good/bad state changes a choice while the text stays the same? |
| ★ [[Task context moves model preferences (Trhlik 2026)]] ([paper](https://arxiv.org/abs/2606.13944)) | 15 | How are preferences measured? What moves them most: wording, temperature or task? |
| [[Models share one taste for text (Zatuchin 2026)]] ([paper](https://arxiv.org/abs/2610.00369)) | 10 | What is the "own-model premium", and why is it near zero? |
| [[Model values form coherent utilities that can be steered (Mazeika 2025)]] ([paper](https://arxiv.org/abs/2502.08640)) | 10 | Abstract and first figure. In what sense do models have a value system? |
| [[Self-modifying prompts keep the same core values (Stroganov 2026)]] ([paper](https://arxiv.org/abs/2611.01304)) | 10 | What stays the same after 100 rounds of self-modification? |

**After block 3 you should be able to say:** models have measurable, fairly coherent preferences; those preferences depend on context; they look shared across models; and they have not been seen to change under self-modification.

## Block 4: what goes wrong when a model learns from itself? (35 minutes)
*This block answers: how honest must the review be about risk?*

| Paper | Min | Question to answer while you read |
|---|---|---|
| ★ [[Self-reward sharpens then collapses (He 2026)]] ([paper](https://arxiv.org/abs/2603.08660)) | 15 | Why can a self-reward only sharpen what the model already prefers? |
| [[Self-written tests miss real regressions (Guo 2026)]] ([paper](https://arxiv.org/abs/2607.24300)) | 10 | Why does a self-improving agent need one check that it cannot see or change? |
| [[Self-predictions are generic, not privileged (Blandfort 2026)]] ([paper](https://arxiv.org/abs/2609.09899)) | 10 | Does a model know itself better than another model knows it? |

**After block 4 you should be able to say:** self-judged loops rise and then decay; a model's view of itself is not special; an outside check is needed.

## Then decide (15 minutes)
Answer these three questions to Claude. Each answer changes the review.

1. **What is the review's main story?**
   - (a) A map of the field that ends with the full idea as an open agenda and names its problems. Claude recommends this.
   - (b) An argument that the full idea will work.
   - (c) A map of the field only, with no agenda of ours.
2. **How strong is the "taste" claim?** A possibility to test (recommended), or a prediction.
3. **Which first question closes the review?** "Do direct weight edits move a model's preferences?" (recommended), or "Does an internal good/bad signal predict which edits help?", or both.

## What you can skip today
The other 110 notes. Claude cites them in the review. You can read them when a reader asks about one.
