---
type: draft
status: draft
section: 7
tags: [type/draft, section/7, component/evaluation, test/divergent, test/stable, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Anchor against collapse]]"]
---

# 8. Preferences and taste

Sections 3 to 7 followed the loop. This section examines its possible long-term product: a set of preferences that belongs to the model. The main finding is that preferences are measurable and fairly coherent, but the measured taste is largely shared across models, and no study has seen it drift under self-change.

## 8.1 Measuring preferences

Two kinds of instrument matter here. The first fits many forced choices to a utility. When researchers asked models thousands of either-or questions, the independent answers fitted a consistent ranking, and the consistency grew with model size ([[Model values form coherent utilities that can be steered (Mazeika 2025)]]; statistics not extracted). The second compares a model's choice with a human choice. A model saw the direction a paper's authors really took next and a plausible alternative, in both orders, and the authors counted agreement, stable divergence (the model picked the other option in both orders), and unstable choice (the model followed position) ([[Models show research taste (Trehan 2026)]]). The design separates a preference about content from noise about order.

## 8.2 Divergence and stability

Models' preferences differ measurably from people's. Across eight frontier models, stable divergence from the authors' choice ran from 15.0% to 36.2% of pairs. The sample was small, 80 pairs from 19 papers, and the divergences were partly shared: models agreed with each other on 61.9% of choices on average ([[Models show research taste (Trehan 2026)]]).

Stability depends on what changes. Across five models and more than 1.2 million choices, a paraphrase of the question shifted 10% of measured preferences, and a change of the task around the question (a news article, a forum post, an essay) shifted 37% ([[Task context moves model preferences (Trhlik 2026)]]). The authors could not tell a change in the model's preference from a change in what it thought the user wanted. A judge's choice also flipped with the order of the options 25% of the time for one frontier model ([[Models recognize and favor their own text (Panickssery 2024)]]). This review therefore defines the Stable test narrowly: a preference is stable if it survives rewording and a swap of option order. We report dependence on task context as a property of the preference and not as a failure, because a demand for stability across every context would fail most human preferences too.

## 8.3 Whose taste is it?

A preference that every model shares is not one model's own. Judges favor their own text ([[Models recognize and favor their own text (Panickssery 2024)]]), but the own-model part shrank once shared taste was removed. A re-analysis of 21,828 trials, in which each model both wrote and selected, found that models strongly preferred model-written text to human text; after removing what every model liked, the extra preference of a model for its own text was +0.019 share points (p = 0.14) ([[Models share one taste for text (Zatuchin 2026)]]). The same paper re-analyzed one data set from another study and found a larger premium, +0.148, there mixed with a same-family effect. The safer statement is that the own-model part is small and not yet separated from confounds, not that it is zero.

Familiarity may explain what self-preference there is: judges scored text higher when it was more predictable to them, whether or not they wrote it ([[Judges favor familiar text, not their own (Wataoka 2024)]]). A "good" signal may therefore mean only "typical for me", which is the prior that self-training sharpens (Section 7.1). The statistic of the re-analysis, the preference for one's own output beyond what all models prefer, is the right instrument for ownership. If it grew over rounds of self-change, that growth would be direct evidence of drift away from the shared origin. Nobody has tracked it over time.

## 8.4 Do preferences move when a model changes?

The evidence so far points to "little, and not in a new direction". Six frontier models that rewrote their own system prompts in a loop, starting from an empty prompt, kept the same few stated values through more than 100 modifications ([[Self-modifying prompts keep the same core values (Stroganov 2026)]]; abstract only). A fixed taste can drive a system far from its origin: the maths discovery loop of Section 7.4 cut its overlap with its starting library from 91.9% to 30.6% under a fixed interestingness score. No study shows a system doing so with a taste that it revises itself.

One result concerns a direct weight edit, and it points the other way: removing one direction made two models more optimistic on an unrelated task, in a direction nobody chose (Section 6.2). That study covered one disposition. No study measures a broad set of preferences before and after a weight change.

## 8.5 How could taste be measured?

Accuracy has a right answer and taste does not, so no single taste score can exist. Researchers can measure a profile of properties. Table 5 maps the four tests of Section 1.2 onto previous instruments and gives the current evidence for each.

**Table 5.** The four tests for a taste of a model's own: a previous instrument, its blind spot, and the state of the evidence.

| Test | Previous instrument | What it cannot tell | State of the evidence |
|---|---|---|---|
| Divergent | Paired choice against a human choice, in both orders ([[Models show research taste (Trehan 2026)]]) | Whether a difference is a taste or an error | Measured: 15 to 36% stable divergence from human choices, partly shared across models |
| Stable | Share of preferences that shift under rewording, order, and context ([[Task context moves model preferences (Trhlik 2026)]]) | Whether the model's preference changed, or its guess about the user | Holds under rewording (10% of preferences shift); does not hold across task context (37%) |
| Grounded | Change a hidden valence state with the text fixed and see whether the choice moves ([[Hidden good-bad feeling changes choices (Berg 2026)]]); compare stated with behavioral preference weights ([[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]) | Whether the state is a taste or a general mood | Valence causally moved choices in five of seven models; faithful report of a trained preference appeared only in a 32B model |
| Self-reinforcing | Preference for one's own output beyond the shared machine preference ([[Models share one taste for text (Zatuchin 2026)]]), tracked over rounds | Nothing yet; nobody has tracked it over time | Not shown. Loops on a model's own signal sharpen and collapse; values persist under self-modification |

Two problems remain open. No instrument separates a drift that improves taste from a drift that is decay. And the four tests are our proposal: grading the field against them is circular until other researchers adopt or replace them. No study shows a model that passes the four tests together, and nobody has attempted the fourth with weight changes.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper.
- 2026-11-24 (guides and critique): prose and past tense; the sample size of the research-taste study (80 pairs from 19 papers) and the second, larger own-model premium (+0.148) are now reported; the four tests are flagged as circular until others use them.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/07-taste-and-open-endedness (long).md`.
