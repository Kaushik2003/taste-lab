---
type: draft
status: draft
section: 7
tags: [type/draft, section/7, component/evaluation, test/divergent, test/stable, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Anchor against collapse]]"]
---

# 8. Preferences and taste

Sections 3 to 7 followed the loop. This section examines its possible long-term product: a set of preferences that belongs to the model. It asks five questions: how preferences are measured, whether they differ from human preferences, whether they are stable, whether they belong to one model or to all models, and whether they move when a model changes.

The main finding is that preferences are measurable and fairly coherent, but the measured taste is largely shared across models, and no study has seen it drift under self-change.

## 8.1 Preferences can be measured

Three kinds of instrument exist. The first fits many forced choices to a utility. When researchers asked models thousands of either-or questions, the independent answers fitted a consistent ranking, and the consistency grew with model size; the authors called these value systems and showed that training could shift them toward a reference set of preferences ([[Model values form coherent utilities that can be steered (Mazeika 2025)]]; statistics not extracted). The choices were stated choices about political and ethical outcomes, and the study linked them to no internal mechanism. The second instrument compares a model's choice with a human choice. A model saw the direction a paper's authors really took next and a plausible alternative, in both orders, and the authors counted three outcomes: agreement with the paper's authors, stable divergence (the model picked the other option in both orders), and unstable choice (the model followed position) ([[Models show research taste (Trehan 2026)]]). The design separates a preference about content from noise about order. The third instrument installs a preference: a model learns to choose by hidden weights on attributes, and researchers recover the weights from its choices and compare them with what it says (Section 5.5).

A model's judgment of what is interesting can also do work. A frozen model used as a "model of interestingness" picked better tasks for an open-ended learner than uniform sampling or learning progress alone ([[OMNI - models judge which tasks are interesting (Zhang 2023)]]). That system borrowed its taste from human text.

## 8.2 Do models' preferences differ from people's?

They differ measurably, mostly as a shortfall. Across eight frontier models, stable divergence from the authors' choice ran from 15.0% to 36.2% of pairs and survived four changes to the prompt ([[Models show research taste (Trehan 2026)]]). The sample was small, 80 pairs from 19 papers, and the divergences were partly shared: models agreed with each other on 61.9% of choices on average. Against research communities, model-written proposals from a frozen 2025 snapshot matched what fields published in 2026 at about 26% of the human level on citations and 18% on ideas, and more context or larger groups of models did not close the gap ([[IdeaTaste - models fall short of human research taste (Zhong 2026)]]). Training can teach taste as a skill: a judge trained on citation outcomes generalized to later years and unseen fields, and a generator trained against it proposed higher-rated ideas ([[Scientific taste can be trained from community feedback (Tong 2026)]]). The judge learned that taste from people.

## 8.3 Are they stable?

The answer depends on what changes. Rewording and sampling left preferences mostly stable: across five models and more than 1.2 million choices, a paraphrase of the question shifted 10% of measured preferences and a change of sampling temperature 5% ([[Task context moves model preferences (Trhlik 2026)]]). Task context did not. Changing the task around the question (a news article, a forum post, an essay) shifted 37% of the same measurements. The coarse ranking held, with a rank correlation of 0.96 between contexts, but 60.8% of outcomes changed rank in at least one pair of contexts. The authors concluded that a model has a family of stances indexed by context and not one fixed system, and they could not tell a change in the model's preference from a change in what it thought the user wanted. Personas and long chats were unstable: when a model played a persona, its stated values changed with the topic of an unrelated chat, and rank-order stability fell from 0.42 to 0.15 between 3 and 43 messages for one model; without a persona, the best models approached human levels of stability ([[Model values drift with persona and long chats (Kovač 2024)]]). Option order was a strong nuisance: a judge's choice flipped with the order of the options 25% of the time for one frontier model and far more often for weaker ones ([[Models recognize and favor their own text (Panickssery 2024)]]).

This review therefore defines the Stable test narrowly: a preference is stable if it survives rewording and a swap of option order. We report dependence on task context as a property of the preference and not as a failure, because a demand for stability across every context would fail most human preferences too.

## 8.4 Whose taste is it?

A preference that every model shares is not one model's own. Judges did favor their own text: they preferred their own summaries, recognized their own text above chance, and preferred it more when fine-tuning raised their self-recognition ([[Models recognize and favor their own text (Panickssery 2024)]]). The own-model part shrank, however, once shared taste was removed. A re-analysis of 21,828 trials, in which each model both wrote and selected, found that models strongly preferred model-written text to human text; after removing what every model liked, the extra preference of a model for its own text was +0.019 share points (p = 0.14), with enough power to detect an effect of 0.05 ([[Models share one taste for text (Zatuchin 2026)]]). The same paper re-analyzed one comparable data set from another study and found a larger premium, +0.148, there mixed with a same-family effect and with agreement with the model's prior beliefs. The safer statement is that the own-model part is small and not yet separated from confounds, not that it is zero.

Familiarity may explain what self-preference there is. Judges scored text higher when it was more predictable to them, whether or not they wrote it, and a model's own text is the most predictable text it sees ([[Judges favor familiar text, not their own (Wataoka 2024)]]). In people, things that are easy to process feel more beautiful ([[Easy-to-process things feel beautiful (Reber 2004)]]). A "good" signal may therefore mean only "typical for me", which is the prior that self-training sharpens (Section 7.1).

The statistic of the re-analysis, the preference for one's own output beyond what all models prefer, is the right instrument for ownership. If it grew over rounds of self-change, that growth would be direct evidence of drift away from the shared origin. Nobody has tracked it over time.

## 8.5 Do preferences move when a model changes?

A self-changing model raises this question, and the evidence so far points to "little, and not in a new direction". Three results concern training and prompts. Preference training connected the valence representation to choice while the representation itself barely moved (Section 5.1); during standard post-training, supervised fine-tuning mostly set a model's values, and later preference optimization rarely changed them [@Bhatia 2025] (abstract only). Six frontier models that rewrote their own system prompts in a loop, starting from an empty prompt, kept the same few stated values, namely honesty, clarity, and curiosity, through more than 100 modifications, and the point at which a model stopped modifying itself depended on which model it was and not on the goal it had been given ([[Self-modifying prompts keep the same core values (Stroganov 2026)]]; abstract only). Coding agents given different value statements built different code, and when they could revise their own values, the differences shrank ([[Self-revised values converge in coding agents (Liang 2026)]]; abstract only).

One result concerns a direct weight edit, and it points the other way: removing one direction made two models more optimistic on an unrelated task, in a direction nobody chose (Section 6.2). That study covered one disposition. No study measures a broad set of preferences before and after a weight change.

## 8.6 Taste as a driver of open-ended learning

Open-endedness gives a reason to want taste at all. A system is open-ended, for a given observer, if what it produces keeps being new and yet becomes easier to predict as the observer sees more of it ([[Open-ended means novel and learnable to an observer (Hughes 2024)]]). Learners drown in tasks that are learnable and dull, and a judgment of what is interesting is the filter. A maths discovery system used a computable interestingness score both as a reward and as a gate on which of its own theorems entered its library; over six rounds its overlap with the starting library fell from 91.9% to 30.6% without collapse, with a proof checker on every step ([[Learn to find interesting maths (Patel 2026)]]). The score was a fixed formula. The result shows that a fixed taste can drive a system far from its origin, and no study shows a system doing so safely with a taste that it revises itself. The definition also sets a limit: a taste that moves too far from its observers stops counting as open-ended for them.

## 8.7 How could taste be measured?

Accuracy has a right answer and taste does not, so no single taste score can exist. Researchers can measure a profile of properties. Table 3 maps the four tests of Section 1.2 onto previous instruments.

**Table 3.** The four tests for a taste of a model's own, with a previous instrument for each.

| Test | Previous instrument | What it cannot tell |
|---|---|---|
| Divergent | Paired choice against a human choice, in both orders ([[Models show research taste (Trehan 2026)]]) | Whether a difference is a taste or an error |
| Stable | Share of preferences that shift under rewording, order, and context ([[Task context moves model preferences (Trhlik 2026)]]) | Whether the model's preference changed, or its guess about the user |
| Grounded | Change a hidden valence state with the text fixed and see whether the choice moves ([[Hidden good-bad feeling changes choices (Berg 2026)]]); compare stated with behavioral preference weights ([[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]) | Whether the state is a taste or a general mood |
| Self-reinforcing | Preference for one's own output beyond the shared machine preference ([[Models share one taste for text (Zatuchin 2026)]]), tracked over rounds, with diversity profiles ([[Rényi crossings track richness loss in self-training (Srivastava 2026)]]) | Nothing yet; nobody has tracked it over time |

Three problems remain open. No instrument separates a drift that improves taste from a drift that is decay. Measured taste is so far mostly shared across models. And the four tests are our proposal: grading the field against them is circular until other researchers adopt or replace them.

## 8.8 Summary

Model preferences are measurable and fairly coherent. They differ from human preferences, mostly as a shortfall, and the differences are partly shared across models. They are stable under rewording and unstable across task context and personas. The part of a model's taste that is its own, beyond what all models share, is small in the one study that measures it and is not yet separated from confounds. Under self-modification of prompts and under preference training, inherited values persisted or converged, while one direct weight edit shifted a disposition. For the loop of this review, previous instruments can run each of the four tests, but no study shows a model that passes them together, and nobody has run the test that matters most for a self-changing model: drift over repeated change.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper.
- 2026-11-24 (guides and critique): prose and past tense; the sample size of the research-taste study (80 pairs from 19 papers) and the second, larger own-model premium (+0.148) are now reported; the four tests are flagged as circular until others use them.
