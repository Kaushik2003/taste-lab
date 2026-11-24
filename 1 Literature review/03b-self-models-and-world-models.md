---
type: draft
status: draft
section: 8
tags: [type/draft, section/8, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 4. Self-models, and what world models contribute

In the Nelson and Narens frame, the meta level holds a model of the object level ([[Monitoring and control between two levels (Nelson 1990)]]). Monitoring updates that model, and control uses it. Section 3 asked what a language model can read about itself in one moment. This section asks a longer question: can a model hold a model of itself, and use it to predict its own behavior, its own learning, and the effect of a change to itself?

The main finding is that the self-model is the weakest part of the loop. A model's picture of itself is mostly a general description, its advantage over an outside observer is contested, and no model reliably predicts what a change to itself will do.

## 4.1 World models that include the agent

A world model is a learned model that predicts what will happen next, given the current state and an action, so that an agent can try actions "in imagination" before it acts [@Ha 2018; @Hafner 2023]. A self-model is a world model whose object is the agent itself: its skills, its likely behavior, its likely success.

The world-model literature mostly models the environment, and that is its main lesson for this review. A 20-author survey sorted world-model research by cognitive function (memory, perception, language, reasoning, imagining, motivation, metacognition) and found motivation and metacognition the least studied ([[World models miss motivation and metacognition (Rupprecht 2026)]]). The claim comes from the survey's own taxonomy. One system does put the agent inside its world model. MUSE learned to predict its own competence on the current task, simulated what would happen if it acted in a given way, and switched strategy when it predicted failure. It beat a standard world-model agent and prompt-only language-model agents on new tasks ([[MUSE - a world model that predicts its own failure (Valiente 2024)]]; effect sizes not extracted). Its limits mark the open space: the predicted quantity was task success, the designers supplied the set of strategies, and the setting was an embodied task, not a model's own reasoning or weights.

## 4.2 Predicting one's own behavior

Read as evidence about self-models, the self-prediction studies of Section 3.4 support three statements. First, training can produce a self-model of behavior: a fine-tuned model predicted its own behavior better than a second model trained on the same facts, and its predictions followed a later change in its behavior ([[Models predict themselves better than others do (Binder 2024)]]). Second, the advantage of "self" is small and disputed. Three studies found none ([[Trained self-prediction without an own-model edge (Zeng 2026)]], [[Self-predictions are generic, not privileged (Blandfort 2026)]]) [@Song 2025], and one found that frontier models predicted themselves better than peers did [@Naphade 2026]. Third, the self-model flatters. First-person questions shifted reports toward less harmful behavior than the same question about a generic agent ([[Self-predictions are generic, not privileged (Blandfort 2026)]]), and models were overconfident about their own future success ([[Models are overconfident about their own abilities (Barkan 2025)]]).

A model's picture of itself is therefore, for now, mostly a learned description that an outside observer could also learn. The point matters for design: a system that needs a self-model may get the same value from a separate predictor.

## 4.3 Predicting one's own learning

A self-model can also cover learning. MAGELLAN read the agent's own hidden state for a goal, predicted the chance of success, and tracked how that prediction changed over time. This estimate of its own learning progress chose the goals the agent practiced next. In a text world with about 25,000 goals, it was the only method without hand-made goal groups that mastered every goal category, and it predicted success on unseen goals with an error of 0.11, against 0.53 for a method that could not generalize ([[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]). This is the clearest case of an internal self-estimate that controls learning. The estimate was "will I succeed", trained on outside success labels, in a small model.

Two papers describe the field's position on this point. A position paper argued that self-improving agents stall because people design this kind of metacognition and fix it in advance; it asked for versions that belong to the agent, and gave no mechanism ([[Self-improving agents need intrinsic metacognition (Liu 2025)]]). A survey of self-evolving agents showed the same pattern across the field: agents adapted their memory, tools, and workflows, and the judge was always task success or human feedback ([[A survey of self-evolving agents (Gao 2025)]]; abstract only).

## 4.4 Persistent self-state

A self-model needs somewhere to live across steps. Three results show that a persistent state changes a model's behavior with no weight change. A cache of hidden states, blended back into each layer as generation proceeded, gave a frozen 8B model higher scores (89.0% on one maths benchmark, 91.0% on one reasoning benchmark) and behaviors that the author described as state awareness and error correction ([[A persistent latent stream gives metacognitive behavior (Aviss 2025)]]). The study had a single author and no probe of the claimed monitoring, and too strong a stream led to repetition that the model could not leave. Agents with persistent memory and their own previous output as feedback, given no task, organized themselves into multi-cycle projects, study of how they themselves think, or reflection on what they are, in patterns that depended strongly on the model family ([[Agents left alone study themselves (Szeider 2025)]]). That observation rests on 18 runs, with no check that the self-inquiry was accurate. And a handbook of behaviors distilled from a model's own reasoning traces acted as an inspectable self-description at the level of skills ([[Reusable behaviors distilled from own traces (Didolkar 2025)]]).

## 4.5 Predicting the effect of a change to oneself

For a model that changes its own weights, the most useful self-model would answer one question before the model changes anything: what will this change do to me? Four lines of evidence bear on that question.

The first is a set of tools for researchers. Influence functions estimate how a model's outputs would change if a training example were added or removed, and later work scaled them to large language models [@Koh 2017; @Grosse 2023]. They are instruments, not abilities of the model.

The second is prediction from weights. Given the weights and a code sandbox, with no forward pass, a 27B model predicted the behavioral effect of small edits to its own weights at 0.730 balanced accuracy, against 0.578 from a text description of the edits. Reading its own weights gave it no advantage over reading another model's, and the readers predicted a change for 53 to 88% of edits that changed nothing ([[Models predict edit effects without a self advantage (Kocabay 2026)]]; abstract page only).

The third is knowledge of limits. On a benchmark that mixed impossible edits with hard but possible ones, the best agents scored 0.491 to 0.500, about the level of guessing ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). The one model that edited itself did not predict either: it tried each edit, tested it, and withdrew its edit in 5 of 8 sessions ([[A model rewrites its own weights (Fan 2026)]]).

The fourth is self-description after a change, and here the evidence divides. A model with its refusal direction removed still described its old refusal policy ([[One direction controls refusal (Arditi 2024)]]). Asked directly what it had been fine-tuned on, a changed model scored 1.21 out of 5; with an extra adapter trained on thousands of labeled weight changes it scored 4.76, but the adapter did not carry over to other kinds of change ([[A trained adapter lets a model describe its weight change (Goel 2025)]]). Side effects of fine-tuning were harder to report than planned changes ([[Adapters report side effects of fine-tuning (Yoshida 2026)]]). In contrast, after long training on a preference, a 32B model reported it correctly with no training on reports (Section 3.4). People are not a higher standard here: their reports on the causes of their own behavior are often inferences from plausible theories and not observations [@Nisbett 1977].

## 4.6 Summary

World models rarely include the agent, and the one system that does predicts only its own task failure. Training can produce a self-model of behavior, but its advantage over an outside model is disputed, and untrained self-description is generic and flattering. An internal estimate of one's own learning progress can control what an agent learns; the estimate concerns competence. No model reliably predicts what a change to its own weights will do, and a model's description of itself usually does not follow a change unless training teaches it to. For the loop of this review, the second principle of Nelson and Narens, that the meta level holds a model of the object level, has no strong counterpart in language models yet, least of all for a model that is itself changing.

## Log
- 2026-11-24: new section, written after the user's "go".
- 2026-11-24 (guides and critique): prose and past tense; retitled to say honestly that the world-model literature contributes little on the self; added Song 2025, Naphade 2026 and Nisbett and Wilson 1977; the "self adds nothing" claim is now "disputed".
