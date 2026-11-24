---
type: draft
status: draft
section: 7
tags: [type/draft, section/7, component/evaluation, test/divergent, test/stable, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Anchor against collapse]]"]
---

# 8. Preferences and taste

Sections 3 to 7 followed the loop. This section looks at its possible long-term product: a set of preferences that belongs to the model. "Taste" has recently become something that can be measured, at least in parts. We ask how preferences are measured, whether they differ from human preferences, whether they are stable, whether they belong to one model or to all models, and whether they move when a model changes.

## 8.1 Preferences can be measured

Three kinds of instrument exist.

- **Many forced choices, fitted to a utility.** When a model is asked thousands of either-or questions, its independent answers fit a consistent ranking, and the consistency grows with model size. The authors call these value systems and show they can be shifted toward a reference set of preferences ([[Model values form coherent utilities that can be steered (Mazeika 2025)]]; statistics not extracted). The choices are stated, about political and ethical outcomes, and are not linked to any internal mechanism.
- **Paired comparison against a human choice.** A model sees the direction a paper's authors really took next and a plausible alternative, in both orders. Three outcomes are counted: agreement with the authors, stable divergence (the model picks the other option in both orders), and unstable choice (it follows position) ([[Models show research taste (Trehan 2026)]]). This separates a preference about content from noise about order.
- **Installed preferences.** A model is trained to choose by hidden weights on attributes; the weights can then be recovered from its choices and compared with what it says (Section 5.5).

A model's judgment of what is interesting can also be put to work: a frozen model used as a "model of interestingness" picks better tasks for an open-ended learner than uniform sampling or learning progress alone ([[OMNI - models judge which tasks are interesting (Zhang 2023)]]). The taste there is borrowed from human text.

## 8.2 Do models' preferences differ from people's?

Yes, in measurable ways, and mostly as a shortfall. Across 8 frontier models, stable divergence from the authors' choice runs from 15.0% to 36.2% of pairs and survives four changes to the prompt ([[Models show research taste (Trehan 2026)]]). But the divergences are partly shared: models agree with each other on 61.9% of choices on average. Against research communities, model-written proposals from a frozen 2025 snapshot match what fields published in 2026 at about 26% of the human level on citations and 18% on ideas, and more context or larger groups of models do not close the gap ([[IdeaTaste - models fall short of human research taste (Zhong 2026)]]). Taste can be trained as a skill: a judge trained on citation outcomes generalizes to later years and unseen fields, and a generator trained against it proposes higher-rated ideas ([[Scientific taste can be trained from community feedback (Tong 2026)]]). That taste is learned from people.

## 8.3 Are they stable?

It depends on what is changed.

- **Rewording and sampling: mostly stable.** Across five models and more than 1.2 million choices, a paraphrase of the question shifts 10% of measured preferences and a change of sampling temperature 5% ([[Task context moves model preferences (Trhlik 2026)]]).
- **Task context: much less stable.** Changing the task around the question (a news article, a forum post, an essay) shifts 37% of the same measurements. The coarse ranking holds (rank correlation 0.96 between contexts), but 60.8% of outcomes change rank in at least one pair of contexts. The authors conclude that a model has a family of stances indexed by context, not one fixed system. They cannot tell a change in the model's preference from a change in what it thinks the user wants.
- **Personas and long chats: unstable.** When a model plays a persona, its stated values change with the topic of an unrelated chat and drift as the chat gets longer (rank-order stability falls from 0.42 to 0.15 between 3 and 43 messages for one model). Without a persona the best models approach human levels of stability ([[Model values drift with persona and long chats (Kovač 2024)]]).
- **Option order: a strong nuisance.** A judge's choice flips with the order of the options 25% of the time for one frontier model and far more for weaker ones ([[Models recognize and favor their own text (Panickssery 2024)]]).

For this review we therefore define the Stable test narrowly: a preference is stable if it survives rewording and a swap of option order. Dependence on task context is reported as a property of the preference, not as a failure. Demanding stability across every context would fail most human preferences too.

## 8.4 Whose taste is it?

A preference that every model shares is not one model's own.

- **Models favor their own text.** Judges prefer their own summaries, can recognize their own text above chance, and when fine-tuning raises self-recognition, self-preference rises with it ([[Models recognize and favor their own text (Panickssery 2024)]]).
- **But the own-model part is near zero once shared taste is removed.** In a re-analysis of 21,828 trials where each model both writes and selects, models strongly prefer model-written text to human text. After removing what every model likes, the extra preference of a model for its own text is +0.019 share points (p = 0.14), with enough power to detect an effect of 0.05 ([[Models share one taste for text (Zatuchin 2026)]]). The taste is one shared machine taste, not several personal ones.
- **Familiarity may explain self-preference.** Judges score text higher when it is more predictable to them, whether or not they wrote it, and a model's own text is the most predictable text it sees ([[Judges favor familiar text, not their own (Wataoka 2024)]]). In people, things that are easy to process feel more beautiful ([[Easy-to-process things feel beautiful (Reber 2004)]]). So a "good" signal may only mean "typical for me", which is exactly the prior that self-training sharpens (Section 7.1).

The statistic of the second study, the preference for one's own output beyond what all models prefer, is the right instrument for ownership. If it grew over rounds of self-change, that would be direct evidence of drift away from the shared origin. Nobody has tracked it over time.

## 8.5 Do preferences move when a model changes?

This is the question a self-changing model raises, and the evidence so far points to "little, and not in a new direction".

- **Preference training wires, it does not rewrite.** Preference training connects the valence representation to choice while the representation itself barely moves (Section 5.1). During standard post-training, supervised fine-tuning mostly sets a model's values, and later preference optimization rarely changes them [@Bhatia 2025] (abstract only).
- **Self-modification keeps the inherited core.** Six frontier models that rewrite their own system prompts in a loop, starting from an empty prompt, return to the same core of stated values (honesty, clarity, curiosity), which stays stable through more than 100 modifications. When a model stops modifying itself depends on which model it is, not on the goal it was given ([[Self-modifying prompts keep the same core values (Stroganov 2026)]]; abstract only).
- **Self-revised values converge.** Coding agents given different value statements build different code; when they may revise their own values, the differences shrink ([[Self-revised values converge in coding agents (Liang 2026)]]; abstract only).
- **A direct weight edit does move disposition.** Removing one direction made two models more optimistic on an unrelated task, in a direction nobody chose (Section 6.2).

The first three results concern prompts and training. The fourth is the only measurement after a direct weight edit, and it covers one disposition. No study measures a broad set of preferences before and after a weight change.

## 8.6 Taste as a driver of open-ended learning

Open-endedness gives a reason to want taste at all. A system is open-ended, for a given observer, if what it produces keeps being new and yet becomes easier to predict as the observer sees more of it ([[Open-ended means novel and learnable to an observer (Hughes 2024)]]). Learners drown in tasks that are learnable but dull, and a judgment of what is interesting is the filter. A maths discovery system uses a computable interestingness score both as a reward and as a gate on which of its own theorems enter its library; over 6 rounds its overlap with the starting library falls from 91.9% to 30.6% without collapse, with a proof checker on every step ([[Learn to find interesting maths (Patel 2026)]]). The score is a fixed formula. This shows that a fixed taste can drive a system far from its origin. A taste that the system itself revises has not been shown to do so safely. The definition also sets a limit: a taste that moves too far from its observers stops counting as open-ended for them.

## 8.7 How could taste be measured?

Accuracy has a right answer and taste does not, so there can be no single taste score. What can be measured is a profile of properties. The four tests of Section 1.2 each map onto an existing instrument.

| Test | Existing instrument | What it cannot tell |
|---|---|---|
| Divergent | Paired choice against a human choice, in both orders ([[Models show research taste (Trehan 2026)]]) | Whether a difference is a taste or an error |
| Stable | Share of preferences that shift under rewording, order and context ([[Task context moves model preferences (Trhlik 2026)]]) | Whether the model's preference changed, or its guess about the user |
| Grounded | Change a hidden valence state with the text fixed and see if the choice moves ([[Hidden good-bad feeling changes choices (Berg 2026)]]); compare stated and behavioral preference weights ([[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]) | Whether the state is a taste or a general mood |
| Self-reinforcing | Preference for one's own output beyond the shared machine preference ([[Models share one taste for text (Zatuchin 2026)]]), tracked over rounds, with diversity profiles ([[Rényi crossings track richness loss in self-training (Srivastava 2026)]]) | Not yet tracked over time by anyone |

Three problems remain open. No instrument separates a drift that improves taste from a drift that is decay. Measured taste is so far shared across models. And the four tests are our proposal, not a standard.

## 8.8 Summary

- Model preferences are measurable and fairly coherent. They differ from human preferences, mostly as a shortfall, and the differences are partly shared across models.
- They are stable under rewording and unstable across task context and personas.
- The part of a model's taste that is its own, beyond what all models share, is near zero in the one study that measures it.
- Under self-modification of prompts and under preference training, inherited values persist or converge. One direct weight edit did shift a disposition.
- For the loop of this review: the four tests can each be run with existing instruments, but no model has been shown to pass them together, and the test that matters most for a self-changing model, drift over repeated change, has never been run.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper. Added utilities (Mazeika), stability (Trhlik, Kovač), ownership (Panickssery, Wataoka, Reber), movement under change (Stroganov, Liang, Bhatia, Fafuła), open-endedness (Hughes), and the measurement table. The Stable test is now defined across wording and order only.
