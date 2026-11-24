---
type: draft
status: draft
section: 8
tags: [type/draft, section/8, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 4. Self-models, and what world models contribute

In the Nelson and Narens frame, the meta level holds a model of the object level. This section asks whether a language model can hold a model of itself and use it to predict its own behavior, its own learning, and the effect of a change to itself. The main finding is that the self-model is the weakest part of the loop.

## 4.1 Self-models of behavior and of learning

A world model is a learned model that predicts what will happen next, given a state and an action, so that an agent can try actions "in imagination" before it acts [@Ha 2018]. A self-model is a world model whose object is the agent itself. The world-model literature mostly models the environment: a 20-author survey sorted it by cognitive function and found motivation and metacognition the least studied ([[World models miss motivation and metacognition (Rupprecht 2026)]]).

For language models, the studies of Section 3.3 support three statements. Training can produce a self-model of behavior. The advantage of "self" over an outside model is small and disputed. And the self-model flatters ([[Self-predictions are generic, not privileged (Blandfort 2026)]], [[Models are overconfident about their own abilities (Barkan 2025)]]). A model's picture of itself is therefore, for now, mostly a learned description that an outside observer could also learn.

A self-model can also cover learning. MAGELLAN read the agent's own hidden state for a goal, predicted the chance of success, and used the change in that prediction, its learning progress, to choose the goals the agent practiced next. In a text world with about 25,000 goals, it predicted success on unseen goals with an error of 0.11, against 0.53 for a method that could not generalize ([[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]). This is the clearest case of an internal self-estimate that controls learning. The estimate was "will I succeed", trained on outside success labels, in a small model.

## 4.2 Predicting the effect of a change to oneself

For a model that changes its own weights, the most useful self-model would answer one question before the model changes anything: what will this change do to me? Three lines of evidence bear on it.

The first is prediction from weights. Given the weights and a code sandbox, with no forward pass, a 27B model predicted the behavioral effect of small edits to its own weights at 0.730 balanced accuracy, against 0.578 from a text description of the edits. Reading its own weights gave it no advantage over reading another model's, and the readers predicted a change for 53 to 88% of edits that changed nothing ([[Models predict edit effects without a self advantage (Kocabay 2026)]]; abstract page only).

The second is knowledge of limits. On a benchmark that mixed impossible edits with hard but possible ones, the best agents scored 0.491 to 0.500, about the level of guessing ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). The one model that edited itself did not predict either: it tried each edit, tested it, and withdrew its edit in 5 of 8 sessions ([[A model rewrites its own weights (Fan 2026)]]).

The third is self-description after a change, and here the evidence divides. A model with its refusal direction removed still described its old refusal policy ([[One direction controls refusal (Arditi 2024)]]). Asked directly what it had been fine-tuned on, a changed model scored 1.21 out of 5; with an extra adapter trained on thousands of labeled weight changes it scored 4.76, but the adapter did not carry over to other kinds of change ([[A trained adapter lets a model describe its weight change (Goel 2025)]]). In contrast, after long training on a preference, a 32B model reported it correctly with no training on reports (Section 3.3). The principle that the meta level holds a model of the object level has no strong counterpart in language models yet, least of all for a model that is itself changing.

## Log
- 2026-11-24: new section, written after the user's "go".
- 2026-11-24 (guides and critique): prose and past tense; retitled to say honestly that the world-model literature contributes little on the self; added Song 2025, Naphade 2026 and Nisbett and Wilson 1977; the "self adds nothing" claim is now "disputed".
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/03b-self-models-and-world-models (long).md`.
