---
type: draft
status: draft
section: 8
tags: [type/draft, section/8, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Metacognition - watch and control yourself]]", "[[Models that change their own weights]]"]
---

# 4. Self-models and world models

In the Nelson and Narens frame, the meta level holds a *model* of the object level ([[Monitoring and control between two levels (Nelson 1990)]]). Monitoring updates that model, and control uses it. Section 3 asked what a language model can read about itself in one moment. This section asks a longer question: can a model hold a model of itself, and use it to predict its own behavior, its own learning, and the effect of a change to itself?

**Terms used here.**
- **World model:** a learned model that predicts what will happen next, given the current state and an action. An agent can use it to try actions "in imagination" before it acts [@Ha 2018; @Hafner 2023].
- **Self-model:** a world model whose object is the agent itself: its skills, its likely behavior, its likely success.

## 4.1 World models that include the agent

The world-model literature mostly models the environment. A 20-author survey sorts world-model research by cognitive function (memory, perception, language, reasoning, imagining, motivation, metacognition) and finds that motivation and metacognition are the least studied ([[World models miss motivation and metacognition (Rupprecht 2026)]]). The gap claim comes from their taxonomy and should be cited as such.

One system puts the agent inside its own world model. MUSE learns to predict its own competence on the current task, simulates "what happens if I act this way", and switches strategy when it predicts failure. It beats a standard world-model agent and prompt-only language-model agents on new tasks ([[MUSE - a world model that predicts its own failure (Valiente 2024)]]; effect sizes not extracted). Its limits define the open space: the predicted quantity is task success, the set of strategies is given, and the setting is an embodied task, not a model's own reasoning or weights.

## 4.2 Predicting one's own behavior

Section 3.4 covered trained self-prediction. Read as evidence about self-models, it says three things.

- **A self-model of behavior can be trained.** A model fine-tuned to predict its own behavior beats a second model trained on the same facts about it, and its predictions follow a later change in its behavior ([[Models predict themselves better than others do (Binder 2024)]]). A trained observer role catches the assistant role's lies better than outside monitors ([[Training LMs to watch themselves (Wang 2026)]]).
- **The advantage of "self" is small and not stable.** A 2026 study finds no consistent own-model advantage in trained self-prediction ([[Trained self-prediction without an own-model edge (Zeng 2026)]]). Without training, self-prediction is no better than a general theory of AI assistants, and other models predict a model as well as it predicts itself ([[Self-predictions are generic, not privileged (Blandfort 2026)]]).
- **The self-model flatters.** First-person questions shift reports toward less harmful behavior than the same question about a generic agent ([[Self-predictions are generic, not privileged (Blandfort 2026)]]). Models are also overconfident about their own future success, more so as a task goes on ([[Models are overconfident about their own abilities (Barkan 2025)]]).

So a model's picture of itself is, for now, mostly a learned description that an outside observer could also learn. This matters for design: a system that needs a self-model may get the same value from a separate predictor.

## 4.3 Predicting one's own learning

A self-model can also cover learning. MAGELLAN reads the agent's own hidden state for a goal, predicts the chance of success, and tracks how that prediction changes over time. This estimate of its own learning progress chooses which goals the agent practices next. In a text world with about 25,000 goals it is the only method without hand-made goal groups that masters every goal category, and it predicts success on unseen goals with an error of 0.11 against 0.53 for a method that cannot generalize ([[MAGELLAN - an agent predicts its own learning progress (Gaven 2025)]]). This is the clearest case of an internal self-estimate that controls learning. The estimate is "will I succeed", trained on outside success labels, in a small model.

A position paper argues that self-improving agents stall because this kind of metacognition is designed by people and fixed. It asks for intrinsic versions: the agent's own knowledge of its abilities, its own planning of what to learn, and its own evaluation of how learning went ([[Self-improving agents need intrinsic metacognition (Liu 2025)]]). It gives no mechanism. A survey of self-evolving agents shows the same pattern across the field: agents adapt their memory, tools and workflows, and the judge is always task success or human feedback ([[A survey of self-evolving agents (Gao 2025)]]; abstract only).

## 4.4 Persistent self-state

A self-model needs somewhere to live across steps. Three results show that giving a model a persistent state changes its behavior with no weight change.

- A cache of hidden states that is blended back into each layer as generation proceeds gives a frozen Llama 3.1 8B model higher scores (89.01% on GSM-8K, 91.04% on ARC-Challenge) and behaviors the author describes as state awareness and error correction ([[A persistent latent stream gives metacognitive behavior (Aviss 2025)]]). It is a single-author study with no probe of the claimed monitoring, and too strong a stream leads to repetition the model cannot leave.
- Agents with persistent memory and their own previous output as feedback, given no task, organize into multi-cycle projects, inquiry into their own cognitive processes, or reflection on their own nature. The pattern depends strongly on the model family ([[Agents left alone study themselves (Szeider 2025)]]). This is behavior in 18 runs, with no check that the self-inquiry is accurate.
- A handbook of behaviors distilled from the model's own reasoning traces acts as an inspectable, skill-level self-description that improves later reasoning ([[Reusable behaviors distilled from own traces (Didolkar 2025)]]).

## 4.5 Predicting the effect of a change to oneself

For a model that changes its own weights, the most useful self-model would answer one question before any change is made: *what will this change do to me?* Four lines of evidence bear on it.

- **Classic tools predict the effect of training data.** Influence functions estimate how a model's outputs would change if a training example were added or removed, and have been scaled to large language models [@Koh 2017; @Grosse 2023]. They are tools for the researcher, not abilities of the model.
- **Models can partly predict edits from weights.** Given the weights and a code sandbox, with no forward pass, a 27B model predicts the behavioral effect of small edits to its own weights at 0.730 balanced accuracy, against 0.578 from a text description of the edits. But there is no advantage for reading one's own weights over another model's, and the readers predicted a change for 53 to 88% of edits that changed nothing ([[Models predict edit effects without a self advantage (Kocabay 2026)]]; abstract page only).
- **Editors do not know the limits of edits.** On a benchmark that mixes impossible edits with hard but possible ones, the best agents score 0.491 to 0.500, about the level of guessing ([[WeightBench - models cannot yet patch models (Marasini 2026)]]). The one model that edits itself does not predict either: it tries each edit and tests it, and withdraws its edit in 5 of 8 sessions ([[A model rewrites its own weights (Fan 2026)]]).
- **After a change, the self-description often lags.** A model with its refusal direction removed still describes its old refusal policy ([[One direction controls refusal (Arditi 2024)]]). Asked directly what it was fine-tuned on, a changed model scores 1.21 out of 5; with an extra adapter trained on thousands of labeled weight changes it scores 4.76, but the adapter does not carry over to other kinds of change ([[A trained adapter lets a model describe its weight change (Goel 2025)]]). Side effects of fine-tuning are harder to report than planned changes ([[Adapters report side effects of fine-tuning (Yoshida 2026)]]). In contrast, after long training on a preference, a 32B model does report it correctly with no training on reports (Section 3.4).

## 4.6 Summary

- World models rarely include the agent. One system predicts its own task failure and acts on the prediction.
- A self-model of behavior can be trained, but it gives little or no advantage over an outside model of the same system, and untrained self-description is generic and flattering.
- An internal estimate of one's own learning progress can control what is learned. The estimate is about competence.
- No model reliably predicts what a change to its own weights will do, and a model's description of itself usually does not follow a change unless it is trained to.
- For the loop of this review: the self-model is the weakest part. Principle 2 of Nelson and Narens, that the meta level holds a model of the object level, has no strong counterpart in language models yet, least of all for a model that is itself changing.

## Log
- 2026-11-24: new section, written after the user's "go". World models were added to the scope on 2026-11-20; the user chose a short treatment, and the full read of the self-prediction and edit-prediction papers on 2026-11-23 and 24 made a section of its own necessary.
