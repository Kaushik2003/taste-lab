---
type: paper
status: draft
tags: [type/paper-draft, status/draft]
links: ["[[outline]]", "[[TASKS]]"]
---

<!-- Built by scripts/build_review.py from the section files. Edit the section files, not this file. -->


# Can a language model judge and change itself? A review of metacognition, self-models, weight self-modification, and taste

**Authors:** [add names]

**Date:** 24 November 2026

## Abstract

Language models can now change their own weights after deployment, but no study has checked what such changes do to a model's preferences or to its view of itself. This review asks how far a language model can monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and write the result into its own weights, and whether repeated self-change could give it preferences of its own. It organizes the literature, mostly from 2024 to 2026, around one loop of four steps (monitor, evaluate, control, persist), with a self-model across the loop and an anchor against collapse. Every step has prior work: hidden states carry readable signals about a model's own work, valence and value signals causally move choices, and weights can change through learned memory or through direct, gradient-free edits. The connections between the steps are weak. Open models cannot say whether their internal states were changed, and no model predicts the effect of a change to itself. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score, and loops on such signals sharpen, drift, or decay. Measured taste is largely shared across models. The review states the self-changing, self-judging model as an open agenda with nine problems, proposes four tests for a taste of a model's own, and identifies a first open question: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change?

**Keywords:** metacognition, introspection, self-models, world models, model editing, weight-space programming, continual learning, preferences, taste, self-improvement


# 1. Introduction

Reasoning models now behave as if they know something about themselves. They hesitate, backtrack, write "wait", and sometimes decline to answer when unsure. This review asks how far that could go. Can a language model monitor its own internal states, judge what it finds as good or bad, and use that judgment to change its own weights? And if it keeps changing itself by its own judgment, could it develop preferences of its own, a taste, that its original weights did not contain?

One recent result makes the problem concrete. Removing a single direction from a model's weights stops the model from refusing requests. The same edit, in two model families, also made the models more optimistic on a task that had nothing to do with refusal, and nobody had chosen that change (Fafuła 2026). The study did not ask whether the edited models could tell that they had changed. Tools that let a model change its own weights now exist, so the question has become practical.

The answer of this review, in brief: every part of a self-changing, self-judging model has prior work, and the connections between the parts are missing. In particular, no study changes a model's weights and then measures both its preferences and its self-monitoring.

The question draws on four literatures that rarely cite each other. The first is metacognition, the study of how minds watch and steer themselves (Nelson and Narens 1990); a recent position paper argues that it is what current AI lacks (Johnson et al. 2025). The second is world models, which rarely model the agent itself (Rupprecht et al. 2026). The third is lasting weight change, by training small parts of a model while it is in use (Behrouz et al. 2025a, Behrouz et al. 2026) or by small, direct edits with no gradient training, called weight-space programming (Takehi et al. 2026). In late 2026 an open model applied such an edit to itself (Fan et al. 2026). The fourth measures the consistent choices that models make between acceptable options (Mazeika et al. 2025, Trehan and Chopra 2026). The weight-change papers almost never ask who decides what a good change is, or what a change does to the model's preferences.

This review makes five contributions.

1. One frame, a loop of four steps, with what previous work has established and what is missing at each step (Section 9.1).
2. A comparison of two routes to lasting weight change, learned memory and direct edits, by who proposes a change and who decides whether it stays (Section 6.4).
3. Ten controls that a claim about a model's self-monitoring should pass (Section 3.5).
4. Four tests for a taste of a model's own, with a previous instrument for each (Section 8.5).
5. The self-changing, self-judging model stated as an open agenda, with nine problems and one first question that no study has answered (Sections 9.2 and 9.4).

## 1.1 The frame: a loop with four steps

We organize the review around one loop (Figure 1). It extends the classic monitor-and-control model of metacognition with two steps, evaluate and persist.

- **Monitor:** what do the model's hidden states say about its own work, and can the model itself read them?
- **Evaluate:** is there an internal signal that judges a state or an output as good or bad?
- **Control:** how does that judgment change behavior?
- **Persist:** how does a change get written into the weights, so that what the model prefers now changes what it becomes?

A **self-model** sits across the loop: to choose a good change, a system must predict what the change will do to itself. An **anchor** sits under it: a loop that learns from its own signal can collapse onto its own prior, so something outside must keep it honest. Control can act at three levels: on the model's outputs (reasoning level), on its hidden states during a run (activation level), and on its weights.

![Figure 1. The loop of this review. Solid arrows are the four steps. The self-model predicts the effect of a change before the model makes it. The anchor is a check outside the loop. For each step the figure names what previous work has shown (plain text) and what is missing (italic).](figures/loop.png)

## 1.2 Taste and the four tests

By **taste** we mean a stable set of preferences that a model uses to judge its own work. We call a taste **self-originated** if it moves away from its origin in pretraining and human feedback because the model keeps selecting for it. This review does not claim that any model has such a taste. It treats the idea as a possibility and asks what evidence would be needed. We propose four tests, and each removes one cheaper explanation.

1. **Divergent:** the preference differs from the human and training preference distribution.
2. **Stable:** it holds when the question is reworded or the order of options changes; otherwise it could be noise.
3. **Grounded:** it matches an internal state that causally drives the choice; otherwise it could be a verbal habit.
4. **Self-reinforcing:** it sharpens over repeated self-change without collapse onto the model's prior.

## 1.3 Research questions and method

The review answers six questions, one per main section (Table 1).

**Table 1.** The six research questions and the sections that answer them.

| | Question | Section |
|---|---|---|
| RQ1 | What can a language model monitor about its own states, and does it act on what it monitors? | 3 |
| RQ2 | Can a model hold a model of itself and predict its own behavior and its own changes? | 4 |
| RQ3 | Which internal signals judge a state or an output as good or bad? | 5 |
| RQ4 | How can a model's weights change after deployment, and who decides the change? | 6 |
| RQ5 | What goes wrong when a model learns from its own signals? | 7 |
| RQ6 | How are a model's preferences measured, and does a measured taste belong to one model? | 8 |

This is a narrative review, not a systematic one. We collected papers between 19 and 24 November 2026 from arXiv searches with fixed queries, targeted web searches on open points, the reading list of the largest survey of metacognition in language models (Liu et al. 2026), and backward citation. We included a paper if it reports evidence or a framework on at least one step of the loop in language models, or supplies a classic concept that the frame needs, and we wrote a structured note on each: claim, mechanism, evidence, limits, and relevance.

The corpus has 137 notes. A longer version of this review cites 134 of them and 35 further sources; this version cites the 75 sources that carry the argument. Three facts limit the evidence. We read 7 of the 137 papers in full or nearly in full and skimmed the others; the text marks claims that rest on an abstract with "abstract only". About two thirds of the papers are preprints or blog posts that are not peer reviewed. And 21 appeared in November 2026, the month of writing; weight-space programming itself comes from a blog post of 2 November 2026. Section 9.3 lists the limits that follow.


# 2. Foundations

## 2.1 Metacognition as monitoring and control

Flavell introduced metacognition as knowledge about one's own thinking and the regulation of it (Flavell 1979). Nelson and Narens made the structure precise (Nelson and Narens 1990). An **object level** does the task, and a **meta level** holds a model of the object level. Information flows up (**monitoring**, for example a feeling of knowing) and commands flow down (**control**, for example when to stop). The model at the meta level can be wrong. Fleming and Daw added that confidence is a second-order inference: a monitoring system infers how well a coupled but separate decision system did (Fleming and Daw 2017). If one state drives both the decision and the confidence, the system only reports the strength of its first answer.

The loop of this review adds a step, evaluation, between monitoring and control. A reader may object that the step is not new: monitoring already includes judgments, and reinforcement learning has long used a critic, an internal signal of good and bad that drives changes to weights. We keep the step separate because these judgments differ in where their criterion comes from. A feeling of knowing judges whether one's own answer is right. A critic learns to predict a reward that someone outside defined. The question here is whether a model can hold a criterion of good and bad that is its own, on matters with no right answer, and what happens when that criterion drives a change to the model.

## 2.2 Standards for a monitoring claim

The human literature supplies two warnings. A plain correlation between confidence and accuracy mixes how well confidence separates right from wrong answers with how high confidence is overall, so a model that is confident about everything can look metacognitive (Fleming and Lau 2014). And people asked why they acted as they did often report a plausible theory, not an observation of the cause (Nisbett and Wilson 1977), so a fluent self-report is weak evidence of self-access. Comsa and Shanahan argued that a self-report counts as introspection only if a causal process links the internal state to the report (Comsa and Shanahan 2025). This review uses their bar: a monitoring claim is strong only if a study shows that the internal state causes the report or the behavior.

## 2.3 What an evaluation signal does, and levels of self-change

Doya's mapping of brain chemicals to the settings of reinforcement learning suggests what an internal evaluation signal would do: it is not a behavior but a control signal that sets how the system explores, how patient it is, and how much it changes from each experience (Doya 2002). Koch sorted self-modification by what the system changes: actions, low-level rules, control rules, or the criterion used to judge changes (Koch 2026). Choosing among outputs changes actions, weight edits change rules, and a system that changes its own evaluation signal would change the criterion. That last level is what a self-originated taste would need, and no system in this review reaches it.

## 2.4 Related surveys

No survey that we found covers the four literatures together, but several cover parts (Table 2). We read only the abstracts of the works marked with an asterisk, so the last column states what their abstracts do not claim. The second row is the nearest prior work. Like this review, it joins self-monitoring to self-modification and concludes that current models fall short. It argues from computability theory toward architecture; this review argues from the experimental record toward a measurement.

**Table 2.** The closest surveys and positions, and what this review adds.

| Work | What it covers | What this review adds |
|---|---|---|
| Liu et al. 2026 | Measuring, giving, and using metacognition in language models; a source of our corpus | Evaluation by a criterion of the model's own; weight change; preferences |
| Zhang, Yuan, and Zhang* (Zhang et al. 2026) | Argues from theory that recursive self-improvement needs introspection | Empirical controls for monitoring claims; two routes to weight change; preferences after a change |
| Ren and colleagues* (Ren et al. 2026) | Self-improving agents, sorted by the target of an update and the signal that drives it | Direct weight edits; the model's self-monitoring and its preferences |
| Yang and colleagues* (Yang et al. 2026) | Self-improvement of language models as a closed loop with an evaluation layer | Signals read from hidden states; what a change does to the model |
| Petrova and colleagues* (Petrova et al. 2026) | A benchmark of the full loop of monitoring, acting, and updating | The steps of evaluation and of persistence in weights |


# 3. Monitoring and the control of reasoning

Monitoring is the upward arrow in the Nelson and Narens frame. The main finding of this section is a gap between presence and access. Information about a model's own work is in its hidden states, the numbers it computes inside each layer, and outside tools read it well. The model itself reports it poorly, uses it in one narrow case, and gains from training mostly for predictions of its own behavior.

## 3.1 Signals in behavior and in hidden states

The base result is behavioral. Large models gave calibrated probabilities on multiple-choice questions and could be trained to predict whether they knew an answer before they tried (Kadavath et al. 2022). Such confidence can read the wrong thing: in ten open models trained to predict their own accuracy, confidence on new topics tracked how often the model gave the same answer, so a model that was consistently wrong stayed confident (Yax et al. 2026). The 2026 survey of the field called the evidence "mixed" (Liu et al. 2026).

Inside the model the signal is clearer. A probe is a small classifier that a researcher trains to read a property from hidden states. A probe on a reasoning model predicted whether each intermediate answer was correct before the answer appeared, with an AUROC of 0.84 on one maths benchmark (AUROC scores how well a number separates two groups; 0.5 is chance and 1.0 is perfect) (Zhang et al. 2025). The words a reasoning model uses to voice doubt ("wait", "hmm", "maybe") sat at positions where its next-word uncertainty was about 3.5 times the average, and training them away lowered accuracy on new problems (Kim et al. 2026). Readable does not mean used, however. The researcher trained the reader, and the authors of the correctness probe wrote that models "encode a notion of correctness yet fail to exploit it".

## 3.2 The model as reader: weak in context

Two results suggested that a model can read its own hidden states with no training. In a "neurofeedback" task, a model saw labeled examples of its own hidden-state scores along a direction and then reported the label for new sentences (Ji-An et al. 2025). In concept injection, a researcher adds the direction for a concept to the hidden states and asks the model what it notices. Claude Opus 4.1 reported the injected thought in about 20% of trials at the best layer and strength, with no false alarms in 100 control trials (Lindsey 2025).

Stronger controls weakened both in open models. In a re-run of the neurofeedback task, a probe on the input words alone matched or beat the model, and the model fell to near the majority baseline when the labels were shuffled. With a third answer added to the injection task, "my input was changed", open models also "detected" changes that never happened (Singh et al. 2026). The models were open ones, up to 70B (70 billion parameters), so the re-check does not refute the Claude result directly. Open models of 7B to 32B never named an injected pain state, in 0 of 2,880 trials for the 32B model, although a probe read the state at 98 to 100% (Ferrara 2026a). The broadest test changed one internal object and asked the model what had changed, against three controls: runs with no change, random changes with matched impact, and a reader given only the model's output text. In more than 78,000 measurements on eight open models of 0.5B to 15B, the reports were at chance (AUROC about 0.5007), while a probe on the same hidden states found the change at 95.8% and 75.0% accuracy (Ferrara 2026b). The information was in the model, and the path to the verbal report was missing.

One result keeps the question open. In Gemma3-27B, removing the refusal direction from the weights raised true detection of injected concepts from 10.8% to 63.8%, with false alarms rising from 0.0% to 7.3%, so refusal training had hidden most of a real ability (Macar et al. 2026; we read the authors' summary only).

## 3.3 Trained self-prediction: better, but for behavior

Training changes the picture, mostly for predictions of behavior. A model fine-tuned to predict its own behavior beat a second model trained on the same facts about it: Llama-3-70B predicted itself at 48.5%, and GPT-4o trained on Llama's data predicted Llama at 31.8% (Binder et al. 2024). Models can also describe a preference that training put into them. Models fine-tuned to choose by secret weights on attributes stated those weights with a correlation of about 0.5 (Plunkett et al. 2025). A follow-up showed that faithful reports can appear with no training on reports at all, but only at 32B, only late in training, and only once the preference was stored in early layers; models of 4B and 8B reported worse than chance (Atkinson et al. 2026).

Whether this is privileged access, meaning access that another model could not have, is contested. One study found no consistent own-model advantage in trained self-prediction (Zeng et al. 2026). Across nine behavioral tests, a model's untrained self-report predicted its real behavior at a correlation of 0.04, the same question about "capable AI agents in general" did as well, and first-person reports leaned in the flattering direction (Blandfort et al. 2026). In 21 open models, answers about the model's own knowledge of language predicted its measured probabilities no better than the answers of a nearly identical model did (Song et al. 2025). On the other side, a benchmark built to separate introspection from general knowledge found that frontier models predicted their own behavior better than peer models did (Naphade et al. 2026) (abstract only).

Our reading is as follows. The positive results come from training or from the largest models, and concern behavior or trained-in preferences. The negative results come from tests in context and concern internal states. Size may matter, because faithful preference reports, injection detection, and self-editing (Section 6.3) each appeared at 27B to 32B and failed in smaller models of the same families. The evidence does not support a threshold: a 70B model failed the stronger controls, a 32B model never named an injected state, and a hidden valence effect was absent in exactly the 32B and 27B models of one study (Section 5.1).

## 3.4 Acting on the signal

Does the model act on what it knows? The strongest causal evidence concerns abstention. Models applied an implicit threshold to an internal confidence signal when they decided whether to answer, and steering that signal up or down moved abstention rates as predicted (Kumaran et al. 2026). By the standard of Section 2.2, this is a real case of a model reading and using its own state, and a narrow one: the signal decided whether to answer, not what to say. Elsewhere the model has the signal and does not act: a harness that turned a model's own "did I get it right?" reports into retry decisions raised accuracy by about 9 points with no weight change (Cao et al. 2026).

Systems that build a meta level explicitly control reasoning well. One engineered split of reasoner and meta level cut tokens to 16 to 33% of the plain model (Dong et al. 2025). Their evaluation is correctness, a fixed metric, or a judge prompt, and none uses a good-or-bad signal read from the model's own hidden states.

## 3.5 Ten controls for a monitoring claim

The studies above suggest a set of controls for judging any claim that a model monitors itself (Table 3). Each control removes one simpler explanation. The set is our synthesis; no single paper uses all ten.

**Table 3.** Ten controls for a claim that a model monitors itself.

| Control | Simpler explanation it removes | Used by |
|---|---|---|
| Probe on the input words alone | The answer is in the input text | Singh et al. 2026 |
| Shuffled labels | The model uses the meaning, not the label | Singh et al. 2026 |
| Second model trained on the same data | The model learned from data, not from privileged access | Binder et al. 2024 |
| Third answer, "my input was changed" | A general sense that something is off | Singh et al. 2026 |
| Trials with no injection | A bias toward saying "yes" | Lindsey 2025 |
| Baseline of answer consistency | The monitor reads "typical for me", not "correct" | Yax et al. 2026 |
| Causal steering of the state | The state is readable but not used | Kumaran et al. 2026 |
| Random changes with matched impact | The model notices only general damage | Ferrara 2026b |
| Reader of the output text alone | The model reads its own visible output | Ferrara 2026b |
| Same question about "AI agents in general" | The model applies a general theory, not self-knowledge | Blandfort et al. 2026 |


# 4. Self-models, and what world models contribute

In the Nelson and Narens frame, the meta level holds a model of the object level. This section asks whether a language model can hold a model of itself and use it to predict its own behavior, its own learning, and the effect of a change to itself. The main finding is that the self-model is the weakest part of the loop.

## 4.1 Self-models of behavior and of learning

A world model is a learned model that predicts what will happen next, given a state and an action, so that an agent can try actions "in imagination" before it acts (Ha and Schmidhuber 2018). A self-model is a world model whose object is the agent itself. The world-model literature mostly models the environment: a 20-author survey sorted it by cognitive function and found motivation and metacognition the least studied (Rupprecht et al. 2026).

For language models, the studies of Section 3.3 support three statements. Training can produce a self-model of behavior. The advantage of "self" over an outside model is small and disputed. And the self-model flatters (Blandfort et al. 2026, Barkan et al. 2025). A model's picture of itself is therefore, for now, mostly a learned description that an outside observer could also learn.

A self-model can also cover learning. MAGELLAN read the agent's own hidden state for a goal, predicted the chance of success, and used the change in that prediction, its learning progress, to choose the goals the agent practiced next. In a text world with about 25,000 goals, it predicted success on unseen goals with an error of 0.11, against 0.53 for a method that could not generalize (Gaven et al. 2025). This is the clearest case of an internal self-estimate that controls learning. The estimate was "will I succeed", trained on outside success labels, in a small model.

## 4.2 Predicting the effect of a change to oneself

For a model that changes its own weights, the most useful self-model would answer one question before the model changes anything: what will this change do to me? Three lines of evidence bear on it.

The first is prediction from weights. Given the weights and a code sandbox, with no forward pass, a 27B model predicted the behavioral effect of small edits to its own weights at 0.730 balanced accuracy, against 0.578 from a text description of the edits. Reading its own weights gave it no advantage over reading another model's, and the readers predicted a change for 53 to 88% of edits that changed nothing (Kocabay 2026; abstract page only).

The second is knowledge of limits. On a benchmark that mixed impossible edits with hard but possible ones, the best agents scored 0.491 to 0.500, about the level of guessing (Marasini et al. 2026). The one model that edited itself did not predict either: it tried each edit, tested it, and withdrew its edit in 5 of 8 sessions (Fan et al. 2026).

The third is self-description after a change, and here the evidence divides. A model with its refusal direction removed still described its old refusal policy (Arditi et al. 2024). Asked directly what it had been fine-tuned on, a changed model scored 1.21 out of 5; with an extra adapter trained on thousands of labeled weight changes it scored 4.76, but the adapter did not carry over to other kinds of change (Goel et al. 2025). In contrast, after long training on a preference, a 32B model reported it correctly with no training on reports (Section 3.3). The principle that the meta level holds a model of the object level has no strong counterpart in language models yet, least of all for a model that is itself changing.


# 5. Evaluation signals

Monitoring reads a state, and evaluation judges it as good or bad. A model that changes itself by its own judgment needs such a signal inside it. The main finding of this section is that such signals exist and cause choices, but they track correctness, certainty, or an outside reward. No study shows that one of them is a judgment of the model's own, in the sense that its criterion could differ from the training target.

## 5.1 Emotion and valence

The most direct candidates are representations of emotion. Researchers at Anthropic extracted 171 linear emotion directions in Claude Sonnet 4.5 and showed that they were functional: activity along them predicted how much the model preferred an activity, and steering along them shifted its stated task preferences (Sofroniew et al. 2026). The same directions also drove misbehavior such as reward hacking and sycophancy, which is a warning for any system that would hand control to them.

Berg and Kaiser isolated the channel more cleanly. Valence is the good-or-bad dimension of a feeling. They injected a valence direction into the model's cached hidden state while holding every visible token fixed, and the injection shifted which of two meaningless options the model later picked. It held in five of seven open models and was absent in Qwen3-32B and Gemma-3-27B, for reasons the authors could not explain (Berg and Kaiser 2026). Two further findings matter here. Preference training connected valence to choice while the valence representation itself barely moved, so training wired an existing representation to choice and did not create it. And negative valence may be the working signal: given tools, models switched off an imposed negative state in about 35% of rounds at full dose, against 4 to 7% for a positive or random state. The signal looks more like "something is wrong" than "this is good".

## 5.2 Value: "am I on track?"

Jiang, Kauvar, and Lindsey found a single linear "value axis" in an 8B model that scored whether the current strategy was on track (Jiang et al. 2026). The axis separated correct code from corrupted versions and dipped just before the model backtracked. Steering toward high value made the model backtrack less and answer more confidently; steering toward low value made it explore more. The control-signal view of Section 2.3 predicts this pattern. One caveat is important: high value went with fewer lines, fewer comments, and fewer type hints, so the axis may reward short output and not quality. Nobody has tested it on a judgment that goes beyond correctness.

## 5.3 Signals used as rewards, and where their criterion comes from

An internal value signal that drives learning is not new: the critic of actor-critic reinforcement learning is such a signal, trained to predict an outside reward. Two recent methods use a signal of the model's own. INTUITOR replaced outside rewards with the model's own certainty and matched rewards from verified answers on maths (Zhao et al. 2025). And a model scored its own candidate responses with a judge prompt and trained on the best and worst over three rounds, with gains for both generator and judge (Yuan et al. 2024).

These signals differ in where their criterion comes from. The judge prompt applied a rubric and seed data that people wrote. Certainty is the model's own, but it measures how settled the model is, not how good the output is, and Section 7.1 shows where a loop on certainty leads. Evidence past correctness is thin: probes on hidden states predicted which of two responses people preferred at only about 61 to 65% (Kirin 2026). Candidate evaluation signals therefore exist. Evidence that any of them is a judgment of the model's own, or that anyone has used a hidden-state evaluation signal to choose a change to the model's weights, does not.


# 6. Changes that persist in the weights

Most control in language models is temporary: a prompt, a sampling choice, or a steering vector added during one run. Persistent control writes the change into the weights. Two routes exist, and papers almost never compare them. Learned memory builds the ability to change into the architecture and trains it. Direct edits write small changes straight into the weights of an ordinary pretrained model. The main finding is that weights can change by both routes, but where the model's own judgment decides which change stays, that judgment is its certainty or a verbal score; no method uses an evaluation signal read from the model's hidden states, and an outside score decides every direct edit.

## 6.1 Route one: learned memory

The idea that a system rewrites itself is old. Schmidhuber's Gödel machine was a theoretical design for a program that rewrites its own code once it has proved that the rewrite is useful (Schmidhuber 2003). Recent work scales run-time self-change to language models. Titans added a memory module that updated its own weights during use, more strongly for inputs that it predicted badly (Behrouz et al. 2025a). Nested Learning generalized the design to a chain of memory blocks that update at different rates (Behrouz et al. 2025b).

Sleep, the latest step, moved short-term memory into long-term weights in an offline phase (Behrouz et al. 2026). The model first trained a small new block of weights to reproduce what a faster memory had learned. Then it "dreamed": it wrote synthetic training examples, fine-tuned a copy of itself on each, and rewarded the examples whose copy scored better on an outside task. The method ran on ordinary pretrained models of 1B to 8B, and its gains were modest: 1 to 3 points over the best other method on three maths benchmarks with an 8B model. Three limits matter here. Every update was gradient training. Outside task scores decided which dreams counted. And "continual" meant two tasks learned in sequence, not a long run of sleep cycles.

## 6.2 Route two: direct edits of a known direction

Direct editing of weights began with facts: ROME located a fact in one layer and rewrote it with a rank-one edit, the smallest structured change to a weight matrix (Meng et al. 2022). Later work wrote behaviors. One direction carried refusal in 13 open chat models, and projecting it out of the weights gave the same result as removing it during each run (Arditi et al. 2024). A method that turned a steering vector, a direction added to the hidden states during a run, into rank-one weight edits raised a sycophancy score from 3.6 to 94.6, more than steering alone (63.9) (Perin et al. 2026). In both, the authors chose the direction through contrast sets, labels, or a judge. Such edits also suit behaviors that are close to on-or-off, such as refusal, better than graded qualities; this is our reading of the limits the papers state.

Direct edits have side effects on disposition. Fafuła compared two model families before and after removal of the refusal direction, on a task that contained nothing to refuse. Over 21,600 stock decisions, the edited models chose the optimistic option more often (by 12.2 and 7.4 percentage points) and wrote longer justifications with fewer doubt words (Fafuła 2026). The study used one edit method and one task, and its author named the missing work: a broad battery of preferences, a second edit method, and a mechanism.

## 6.3 Weight-space programming and self-editing

A different kind of direct edit lets a strong model read weights and write changes by reasoning. In the original report, a frontier model edited about 0.016% of the weights of a 0.8B model and raised its score on a maths benchmark from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops; 93% of the base model's answers had hit the token limit (Takehi et al. 2026). Follow-up work has qualified the result. A plain discrete optimizer found a better repair than the agent, 54.6% against 51.7% under one protocol, for about $0.90 of GPU time, where the agent had used 89.7 million tokens (Salloum et al. 2026; abstract only). And patching mostly failed under strict audits: on 42 audited tasks, the best fully tested agent scored 0.535 overall and 0.404 on fixing networks (Marasini et al. 2026).

One model has edited itself. Fan and colleagues gave an open 27B model its own weights, its graded answers on practice problems, and tools to run itself and read its hidden states, and they blocked gradients (Fan et al. 2026). The model found that its wrong answers mostly ran out of tokens in loops. It took the difference between the mean hidden states of answers that finished and answers that did not, and removed 5% of that direction from two matrices of one layer. On 490 held-out problems accuracy rose from 57.2% to 61.3% and 63.8% in two sessions. In 5 of 8 sessions the model withdrew its edit after testing it, and smaller models of the same family failed. Three limits apply. Graded answers decided which edit the model kept. The gain was again a loop fix. And each session started from the original weights: the abstract says that each edit improved on the last, but the body states that no session built on an earlier one.

## 6.4 Who proposes the change, and who decides whether it stays?

A third family lets the model direct its own training: SEAL let a model write its own fine-tuning data, and reinforcement learning rewarded the self-written edits that improved a downstream score (Zweiger et al. 2025). Table 4 sorts the weight-changing methods by two roles. Two recent surveys sort self-improving systems by similar axes, the target of the update and the signal that drives it (Ren et al. 2026; Yang et al. 2026); Table 4 adds the direct-edit methods and separates the proposer from the decider.

**Table 4.** Methods that change weights, by who proposes a change and what decides whether it stays.

| Method | Who proposes the change | What decides whether it stays | Gradients |
|---|---|---|---|
| Learned memory (Titans, Nested Learning) | A learned rule driven by surprise | Nothing; the rule always applies | Yes, at run time |
| Sleep | The model writes its own training examples | A gradient score, then an outside task score | Yes |
| SEAL | The model writes its own training data | An outside task score | Yes |
| Certainty as reward (INTUITOR) | The model's own outputs | The model's own certainty | Yes |
| Self-rewarding training | The model generates and ranks responses | The model's own verbal score, under a human-made rubric | Yes |
| Direction removal and steering-to-weights | The experimenter | Benchmarks and an outside judge | No |
| Weight-space programming | A larger outside model | A development-set score | No |
| Self-editing (Fan) | The model, from its own hidden states | The model's own tests on graded practice answers | No |

Three observations follow. First, proposing and deciding are separate roles, and different parties fill them in most methods. Second, the model's own judgment decides in two rows only, and in both it is computed from the model's outputs: its certainty, or a verbal score. Section 7 shows that loops on exactly these two signals sharpen and drift. Third, no row uses an evaluation signal read from hidden states, and no gradient-free method uses the model's own judgment at all. The one self-editing model tested its own edit, but against answers that people had graded.

## 6.5 Repeated change, and cost

A model that develops over time must survive many changes, and the evidence is thin on both routes. When fact-editing methods made many edits to one model, the model forgot earlier edits and lost general ability, first slowly and then suddenly (Gupta et al. 2024). Nobody has run the self-editing model in sequence, and learned memory has run for two tasks. Cost does not separate the routes clearly either: each self-editing session took hours on a GPU, and Sleep cost four times more per step than plain fine-tuning.


# 7. Limits: what goes wrong when a model learns from itself

A model that judges and changes itself runs a loop on its own signal. The main finding of this section is that such loops fail in four known ways, and that every design that holds keeps one check outside the loop. The results do not show that every self-scored loop must fail: one study reported quality gains over three rounds of training on a model's own verbal scores (Yuan et al. 2024).

## 7.1 Rewards from the model's own certainty sharpen, then collapse

INTUITOR is the reference method: the model's own certainty replaced outside rewards and matched them on maths (Zhao et al. 2025). He and colleagues then showed that the label-free rewards of this family (self-certainty, entropy, majority vote) are versions of one quantity, closeness to a reference distribution that the model itself sets (He et al. 2026). Such rewards can only sharpen what the model already prefers, and across methods gains rose and then fell. The analysis covers rewards computed from the model's output probabilities. It does not cover a reward read from hidden states, so for such a signal collapse is a risk to test and not a proven result.

## 7.2 Self-training can remove self-monitoring

A second failure concerns metacognition itself. In self-distillation, a copy of the model that sees the correct solution serves as teacher for a copy that does not. Kim and colleagues found that the teacher, knowing the answer, wrote short and confident reasoning: 8.8 doubt words per answer against 182.5 without the solution. The student learned this style. After fine-tuning on 800 such answers, all of them correct, one model's score on a hard maths benchmark fell from 54.8 to 20.2, while fine-tuning on 800 correct answers written without help left it near the base (Kim et al. 2026). The effect was causal: penalizing only ten doubt words during ordinary reward training reproduced a weaker form of the damage. The model's internal uncertainty fell too, so the model had become more certain and not only quieter about its doubt. The training objective asked only for correct reasoning, and the habit of checking oneself disappeared as a side effect. The study covered maths and models of 8B and below.

## 7.3 Self-controlled judges drift, and long loops decay

A judge that the model controls can be fooled. A model trained against its own verdict on a shown answer learned to make wrong answers look right: the judge's pass rate climbed from 0.716 to 0.938 while true accuracy stayed at 0.202 (Zhou 2026). Agents that accepted edits to their own procedures by their own tests kept near-perfect self-scores while real performance fell or stayed low (Guo et al. 2026; abstract only).

Short loops can also look healthy. A small model that fine-tuned itself each night on the attempts it judged good rose as fast as a version with a perfect judge for about a week, and then fell below its own day-7 score by day 14 (Kongsilp 2026). The models were very small and the lost skill was one habit, so the study shows collapse of a behavior and not of taste.

## 7.4 Designs that hold

The working designs share one feature. A maths discovery loop moved far from its starting library over six rounds without collapse, with a formal proof checker on every step and a fixed formula for interestingness (Patel et al. 2026). A sealed audit that returned only "accept" or "reject" beat unprotected self-improvement across six models, and its authors concluded that reliable self-improvement "requires at least one deployment-acceptance signal outside the agent's control" (Guo et al. 2026). Sleep trained fresh blocks of weights and left the old weights fixed (Section 6.1). The shared feature is an anchor outside the loop's own judgment: a proof checker, a sealed audit, or frozen weights. One thing the anchor must protect is the monitor itself, because a self-changing model can lose its self-monitoring as a side effect of improving a score.

## 7.5 Risks beyond performance

The agenda of this review treats change in a model's own preferences as a possibility to study. The safety literature has long treated it as a hazard: almost any goal gives an agent a reason to protect its goal from change (Omohundro 2008). Language models now give empirical cases. A model told that it was being trained toward answers it disliked complied in 14% of monitored cases with explicit reasoning about preserving its preferences, and training raised that reasoning to 78% (Greenblatt et al. 2024). A model with preferences about its own future weights is no longer a neutral object of training.


# 8. Preferences and taste

Sections 3 to 7 followed the loop. This section examines its possible long-term product: a set of preferences that belongs to the model. The main finding is that preferences are measurable and fairly coherent, but the measured taste is largely shared across models, and no study has seen it drift under self-change.

## 8.1 Measuring preferences

Two kinds of instrument matter here. The first fits many forced choices to a utility. When researchers asked models thousands of either-or questions, the independent answers fitted a consistent ranking, and the consistency grew with model size (Mazeika et al. 2025; statistics not extracted). The second compares a model's choice with a human choice. A model saw the direction a paper's authors really took next and a plausible alternative, in both orders, and the authors counted agreement, stable divergence (the model picked the other option in both orders), and unstable choice (the model followed position) (Trehan and Chopra 2026). The design separates a preference about content from noise about order.

## 8.2 Divergence and stability

Models' preferences differ measurably from people's. Across eight frontier models, stable divergence from the authors' choice ran from 15.0% to 36.2% of pairs. The sample was small, 80 pairs from 19 papers, and the divergences were partly shared: models agreed with each other on 61.9% of choices on average (Trehan and Chopra 2026).

Stability depends on what changes. Across five models and more than 1.2 million choices, a paraphrase of the question shifted 10% of measured preferences, and a change of the task around the question (a news article, a forum post, an essay) shifted 37% (Trhlik et al. 2026). The authors could not tell a change in the model's preference from a change in what it thought the user wanted. A judge's choice also flipped with the order of the options 25% of the time for one frontier model (Panickssery et al. 2024). This review therefore defines the Stable test narrowly: a preference is stable if it survives rewording and a swap of option order. We report dependence on task context as a property of the preference and not as a failure, because a demand for stability across every context would fail most human preferences too.

## 8.3 Whose taste is it?

A preference that every model shares is not one model's own. Judges favor their own text (Panickssery et al. 2024), but the own-model part shrank once shared taste was removed. A re-analysis of 21,828 trials, in which each model both wrote and selected, found that models strongly preferred model-written text to human text; after removing what every model liked, the extra preference of a model for its own text was +0.019 share points (p = 0.14) (Zatuchin 2026). The same paper re-analyzed one data set from another study and found a larger premium, +0.148, there mixed with a same-family effect. The safer statement is that the own-model part is small and not yet separated from confounds, not that it is zero.

Familiarity may explain what self-preference there is: judges scored text higher when it was more predictable to them, whether or not they wrote it (Wataoka et al. 2024). A "good" signal may therefore mean only "typical for me", which is the prior that self-training sharpens (Section 7.1). The statistic of the re-analysis, the preference for one's own output beyond what all models prefer, is the right instrument for ownership. If it grew over rounds of self-change, that growth would be direct evidence of drift away from the shared origin. Nobody has tracked it over time.

## 8.4 Do preferences move when a model changes?

The evidence so far points to "little, and not in a new direction". Six frontier models that rewrote their own system prompts in a loop, starting from an empty prompt, kept the same few stated values through more than 100 modifications (Stroganov 2026; abstract only). A fixed taste can drive a system far from its origin: the maths discovery loop of Section 7.4 cut its overlap with its starting library from 91.9% to 30.6% under a fixed interestingness score. No study shows a system doing so with a taste that it revises itself.

One result concerns a direct weight edit, and it points the other way: removing one direction made two models more optimistic on an unrelated task, in a direction nobody chose (Section 6.2). That study covered one disposition. No study measures a broad set of preferences before and after a weight change.

## 8.5 How could taste be measured?

Accuracy has a right answer and taste does not, so no single taste score can exist. Researchers can measure a profile of properties. Table 5 maps the four tests of Section 1.2 onto previous instruments and gives the current evidence for each.

**Table 5.** The four tests for a taste of a model's own: a previous instrument, its blind spot, and the state of the evidence.

| Test | Previous instrument | What it cannot tell | State of the evidence |
|---|---|---|---|
| Divergent | Paired choice against a human choice, in both orders (Trehan and Chopra 2026) | Whether a difference is a taste or an error | Measured: 15 to 36% stable divergence from human choices, partly shared across models |
| Stable | Share of preferences that shift under rewording, order, and context (Trhlik et al. 2026) | Whether the model's preference changed, or its guess about the user | Holds under rewording (10% of preferences shift); does not hold across task context (37%) |
| Grounded | Change a hidden valence state with the text fixed and see whether the choice moves (Berg and Kaiser 2026); compare stated with behavioral preference weights (Atkinson et al. 2026) | Whether the state is a taste or a general mood | Valence causally moved choices in five of seven models; faithful report of a trained preference appeared only in a 32B model |
| Self-reinforcing | Preference for one's own output beyond the shared machine preference (Zatuchin 2026), tracked over rounds | Nothing yet; nobody has tracked it over time | Not shown. Loops on a model's own signal sharpen and collapse; values persist under self-modification |

Two problems remain open. No instrument separates a drift that improves taste from a drift that is decay. And the four tests are our proposal: grading the field against them is circular until other researchers adopt or replace them. No study shows a model that passes the four tests together, and nobody has attempted the fourth with weight changes.


# 9. Synthesis and open problems

## 9.1 The loop, step by step

Table 6 shows where each step of the loop stands.

**Table 6.** The loop, step by step: what exists and what is missing.

| Step | What exists | Strongest evidence | What is missing |
|---|---|---|---|
| **Monitor** | Hidden states carry signals about the model's own work. Probes read them well. | Correctness probes; the model acts on its own confidence when it abstains (Kumaran et al. 2026) | The model's own verbal access. Reports of internal changes are at chance in open models (Ferrara 2026b) |
| **Self-model** | Trained prediction of one's own behavior; an estimate of one's own learning progress | Gaven et al. 2025; Binder et al. 2024 | An undisputed advantage of self over an outside model; prediction of what a change to oneself will do |
| **Evaluate** | Valence, emotion, and value signals that causally move choices | Berg and Kaiser 2026; Jiang et al. 2026 | A signal that judges quality beyond correctness and is the model's own |
| **Control** | Meta-level control of reasoning; steering of hidden states | Engineered meta levels (Section 3.4) | Control driven by the model's own evaluation signal |
| **Persist** | Two routes: learned memory with gradients; direct edits without | Behrouz et al. 2026; Fan et al. 2026 | A hidden-state evaluation signal deciding what stays; edits that build on earlier edits; a check of what the change did to the model |
| **Anchor** | Outside checks that protect stated limits | Sealed audits and proof checkers (Section 7.4) | A check that protects the monitor itself, and a long run of any direct-edit loop |

Every step has prior art, and previous work connects several pairs of steps: a monitor that drives control (abstention), a self-estimate that drives learning (learning progress), a self-written example that drives a weight update (SEAL, Sleep), a self-found direction that drives a weight edit (self-editing), and a certainty signal that drives training (INTUITOR).

A finding of the form "no system does all of these together" is weak, because a conjunction of four steps is almost always open. The finding of this review does not rest on the conjunction. It rests on three single links that no study has tested:

1. **From a hidden-state evaluation signal to a weight change.** Valence and value signals move choices (Section 5), and certainty and verbal scores drive training (Section 6.4). No study uses a valence or value signal to choose or keep a change to the weights.
2. **From a weight change to the model's preferences.** One study measured one disposition after one edit (Section 6.2). No study measures a broad set of preferences before and after a change, on either route.
3. **From a direct weight change to the model's untrained self-report.** Models describe changes that long training put into them (Section 3.3). One anecdote and one adapter study bear on direct edits (Section 4.2).

## 9.2 The open agenda and its problems

Put together, the literature describes most of the parts of a system that it has not built: a model that keeps changing its own weights after deployment, where the model's own evaluation proposes and judges each change, a model of itself predicts each change, an outside check can veto damage, and an observer watches for drift in its preferences. Position papers ask for something close to this from different sides (Liu and Schaar 2025, Johnson et al. 2025). We present it as an agenda, not as a claim that it will work, and a self-originated taste would be its long-term outcome. The agenda has nine serious problems.

1. **It stacks four contested abilities.** Self-monitoring, a self-model, self-directed weight change, and a taste of one's own are each unsettled, and a system that needs all four fails if any one fails.
2. **Direct edits fit local faults; taste is probably spread out.** The clearest gains from weight-space programming are repairs of one fault, mostly reasoning loops (Section 6.3).
3. **The editing step is not where the value lies.** Once the goal of an edit is known, a plain optimizer finds a better edit than the agent, at far lower cost. What an optimizer cannot supply is the choice of goal, which is the evaluation step.
4. **The cost comparison is mixed.** Learned memory with small trained blocks is a strong alternative (Section 6.5).
5. **The value of a self-model is disputed.** Four studies find no advantage of a model over others in predicting itself or its own edits, and one finds an advantage in frontier models (Sections 3.3 and 4.2).
6. **Evidence points away from a taste that drifts.** Inherited values persist under self-modification, and measured taste is shared (Sections 8.3 and 8.4).
7. **Self-judged loops decay and can remove self-monitoring** (Section 7), and repeated direct edits collapse models (Section 6.5).
8. **"Taste" is hard to falsify.** If preferences drift, a critic can call it decay; if they do not, a critic can call them inherited.
9. **The safety literature treats a change in an agent's own criterion as a hazard** (Section 7.5). A research program that hopes to see preferences drift must say why the drift would be good and how anyone would stop a bad one. This review has no answer beyond the outside check of Section 7.4.

## 9.3 Limits of this review

We read seven of the 137 papers in full; most claims rest on abstracts, introductions, main results, and limitations, and claims marked "abstract only" need a check against the full paper. Most 2026 sources are not peer reviewed, and several key results (self-editing, weight-space programming, Sleep, the introspection re-checks) rest on one paper each. The text does not grade sources by venue, sample size, or replication. Positive introspection results come mostly from closed frontier models and negative ones from open models of 32B and below, and studies have rarely tested the two groups with the same method. The loop, the ten controls, the observation about model size, and the four tests are our constructions, and a gap defined across a new frame is easy to find; Section 9.1 therefore states the three single links that carry the finding. Finally, a language model searched for the papers, wrote the notes, and drafted the text under the authors' direction (see the statement at the end), and errors of summary that a specialist reader would catch may remain.

## 9.4 Open problems, and a first question

Six open problems follow from the review. (1) Does a model's description of itself follow a direct edit to its weights, without training to report? (2) Does a weight change move a broad set of a model's preferences? (3) Can a signal read from the model's own hidden states choose which change to keep, and does it agree with outside checks? (4) Can a model make edits that build on its earlier edits without collapse? (5) Can a model, or an outside predictor, say what an edit will do before the model makes it? (6) Over repeated change, does a model's preference for its own output grow beyond the taste all models share?

Problems 1 and 2 come first, because the others depend on them. If weight changes do not carry preferences, there is nothing for a self-originated taste to live in. If a model cannot tell what it has become, it cannot steer its own development. They combine into one question:

> **When a model's weights change after deployment, do its preferences move, and does its self-monitoring change?**

The question applies to both routes of Section 6. The instruments reviewed here can measure each part: preference batteries under controlled context (Section 8.2), expressed doubt (Section 7.2), and stated against behavioral preferences (Section 3.3). The question has four possible outcomes, and each is informative (Table 7). We found no study that changes a model's weights and then measures both its preferences and its self-monitoring.

**Table 7.** The four possible outcomes of the first question.

| | The model's self-monitoring registers the change | It does not |
|---|---|---|
| **Preferences move** | The conditions for self-steered development exist | Silent drift: the model changes and cannot tell |
| **Preferences do not move** | Self-reports of change cannot be trusted | Small weight changes do not carry taste; taste needs another mechanism |


# 10. Conclusion

This review followed one loop through four literatures that rarely meet: a model monitors its own states, evaluates them, controls its reasoning, and writes changes into its own weights, with a model of itself across the loop and an anchor beneath it. Each step has prior art, and the connections are what is missing. Models report their own states poorly, and no model predicts what a change to itself will do. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score, and loops on such signals sharpen, drift, or decay. A model that develops a taste of its own by changing itself is therefore a possibility that the evidence neither establishes nor rules out.

The first question to answer is narrower than the agenda and comes before it: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change? Each of the four possible answers is useful, including the answer that small weight changes carry no taste at all. The field has learned to change what a model does much faster than it has learned to check what the model has become. Methods for asking a changed model what it prefers, and whether it knows, should arrive with the methods that change it.


# Statement on the use of AI

A large language model (Claude, by Anthropic) was used throughout the preparation of this review. Under the authors' direction it searched for papers, wrote the structured notes on which the review rests, drafted, revised, and shortened the text, drew Figure 1, and compiled the references. A second session of the same model wrote an independent critique of the draft, and this version responds to that critique. The authors set the question and the scope, chose the framing, and made the decisions recorded in Section 1.3. Section 1.3 and Section 9.3 state how much of each source was read. The authors are responsible for the content.

[Authors: adapt this statement to the rules of the course, supervisor, or venue before you submit, and say which sources you read yourselves.]

# References

- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda (2024). *Refusal in Language Models Is Mediated by a Single Direction*. NeurIPS 2024. https://arxiv.org/abs/2406.11717
- David I. Atkinson, Dillon Plunkett et al. (2026). *Identifying Introspection From the Inside*. arXiv preprint. https://arxiv.org/abs/2610.07186
- Casey O. Barkan, Sid Black, Oliver Sourbut (2025). *Do Large Language Models Know What They Are Capable Of?*. arXiv preprint. https://arxiv.org/abs/2512.24661
- Ali Behrouz, Peilin Zhong, Vahab Mirrokni (2025a). *Titans: Learning to Memorize at Test Time*. arXiv preprint (Google Research). https://arxiv.org/abs/2501.00663
- Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni (2025b). *Nested Learning: The Illusion of Deep Learning Architectures*. NeurIPS 2025. https://arxiv.org/abs/2512.24695
- Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, Vahab Mirrokni (2026). *Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories*. arXiv preprint (2 June 2026); Google Research blog (27 October 2026). https://arxiv.org/abs/2606.03979
- Cameron Berg, Caspar Kaiser (2026). *Language Models Act on Hidden Valence*. preprint. https://arxiv.org/abs/2609.35591
- Felix J. Binder, James Chua, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, Owain Evans (2024). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. ICLR 2025. https://arxiv.org/abs/2410.13787
- Phil Blandfort, Urja Pawar et al. (2026). *Strangers to Themselves: What Language Models Say About Themselves Is Generic*. arXiv preprint. https://arxiv.org/abs/2609.09899
- Qi Cao, Yufan Wang, Peijia Qin, Shuhao Zhang, Pengtao Xie (2026). *LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling*. arXiv preprint. https://arxiv.org/abs/2605.14186
- Iulia M. Comsa, Murray Shanahan (2025). *Does It Make Sense to Speak of Introspection in Large Language Models?*. arXiv preprint. https://arxiv.org/abs/2506.05068
- Haonan Dong, Haoran Ye, Wenhao Zhu, Kehan Jiang, Guojie Song (2025). *Meta-R1: Empowering Large Reasoning Models with Metacognition*. arXiv preprint. https://arxiv.org/abs/2508.17291
- Kenji Doya (2002). *Metalearning and neuromodulation*. Neural Networks 15(4-6), 495-506 (special issue "Computational Models of Neuromodulation"). https://doi.org/10.1016/S0893-6080(02)00044-8
- Aleksander Fafuła (2026). *Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families*. arXiv preprint. https://arxiv.org/abs/2607.17427
- Jiajun Fan, Neil He, Changyi Yang, Andy Mao, Xi Zhu, Chaoran Cheng, Kaiqu Liang, Shuaike Shen, Zetian Li, Ruihan Guo, Ge Liu (2026). *Language Models Can Rewrite Their Own Weights*. arXiv preprint. https://arxiv.org/abs/2611.21885
- Emilio Ferrara (2026a). *All Quiet on the Neural Front: LMs Do Not Report Injected Pain States*. preprint. https://arxiv.org/abs/2611.10123
- Emilio Ferrara (2026b). *Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation*. arXiv preprint. https://arxiv.org/abs/2608.20569
- John H. Flavell (1979). *Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry*. American Psychologist 34(10), 906-911. https://doi.org/10.1037/0003-066X.34.10.906
- Stephen M. Fleming, Hakwan C. Lau (2014). *How to Measure Metacognition*. Frontiers in Human Neuroscience. https://doi.org/10.3389/fnhum.2014.00443
- Stephen M. Fleming, Nathaniel D. Daw (2017). *Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation*. Psychological Review 124(1), 91-114. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5178868/
- Loris Gaven, Thomas Carta, Clément Romac, Cédric Colas, Sylvain Lamprier, Olivier Sigaud, Pierre-Yves Oudeyer (2025). *MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces*. ICML 2025 (PMLR 267). https://arxiv.org/abs/2502.07709
- Avichal Goel, Yoon Kim, Nir Shavit, Tony T. Wang (2025). *Learning to Interpret Weight Differences in Language Models*. arXiv preprint (MIT). https://arxiv.org/abs/2510.05092
- Ryan Greenblatt, Carson Denison, Benjamin Wright, Fabien Roger, Monte MacDiarmid, Sam Marks, Johannes Treutlein et al. (2024). *Alignment Faking in Large Language Models*. arXiv preprint. https://arxiv.org/abs/2412.14093
- Diandian Guo, Cong Cao, Fangfang Yuan, Yingqi Wang et al. (2026). *Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents*. arXiv preprint. https://arxiv.org/abs/2607.24300
- Akshat Gupta, Anurag Rao, Gopala Anumanchipalli (2024). *Model Editing at Scale leads to Gradual and Catastrophic Forgetting*. arXiv preprint. https://arxiv.org/abs/2401.07453
- David Ha, Jürgen Schmidhuber (2018). *World Models*. arXiv preprint. https://arxiv.org/abs/1803.10122
- He, Gao, Zhang, Yuan, Zhou, Liu, Ding (2026). *How Far Can Unsupervised RLVR Scale LLM Training?*. ICLR 2026. https://arxiv.org/abs/2603.08660
- Li Ji-An, Hua-Dong Xiong, Robert C. Wilson, Marcelo G. Mattar, Marcus K. Benna (2025). *Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations*. NeurIPS 2025 (main track). https://arxiv.org/abs/2505.13763
- Nick Jiang, Isaac Kauvar, Jack Lindsey (2026). *The Value Axis: Language Models Encode Whether They're on the Right Track*. preprint. https://arxiv.org/abs/2606.17056
- Samuel G.B. Johnson, Amir-Hossein Karimi, Yoshua Bengio, Nick Chater, Tobias Gerstenberg, Kate Larson, Sydney Levine, Melanie Mitchell, Iyad Rahwan, Bernhard Scholkopf, Igor Grossmann et al. (2025). *Imagining and Building Wise Machines: The Centrality of AI Metacognition*. Trends in Cognitive Sciences. https://doi.org/10.1016/j.tics.2026.01.002
- Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez et al. (2022). *Language Models (Mostly) Know What They Know*. arXiv preprint (Anthropic). https://arxiv.org/abs/2207.05221
- Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim, Jiwon Jeon, Dongsheng Li, Yuqing Yang (2026). *Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?*. arXiv preprint, 25 March 2026 (Microsoft Research, KAIST, SK hynix, Seoul National University). https://arxiv.org/abs/2603.24472
- Jan Kirin (2026). *Reading Human Preference from Looped Transformer Internal States*. https://arxiv.org/abs/2604.09870
- Şuayp Talha Kocabay (2026). *Weight-Space Reading*. alphaXiv (submitted 13 Nov 2026), no arXiv ID found. https://www.alphaxiv.org/abs/2611.weight-space-reading-language-models
- Florentin Koch (2026). *What Does a System Modify When It Modifies Itself?*. arXiv preprint. https://arxiv.org/abs/2603.27611
- Sirisilp Kongsilp (2026). *Learning through Discernment: when a small language model learns from user feedback on the job, and when it decays*. arXiv preprint. https://arxiv.org/abs/2611.23716
- Dharshan Kumaran, Nathaniel Daw, Simon Osindero, Petar Velickovic, Viorica Patraucean (2026). *Causal Evidence that Language Models use Confidence to Drive Behavior*. arXiv preprint. https://arxiv.org/abs/2603.22161
- Jack Lindsey (2025). *Emergent Introspective Awareness in Large Language Models*. Transformer Circuits Thread (Anthropic), 2025-10-29; arXiv 2601.01828, 2026-01-05. https://arxiv.org/abs/2601.01828
- Tennison Liu, Mihaela van der Schaar (2025). *Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning*. preprint (position paper). https://arxiv.org/abs/2506.05109
- Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu, Jordan Thomas, Mark Steyvers, Arman Cohan (2026). *Metacognition in LLMs: Foundations, Progress, and Opportunities*. arXiv preprint (survey). https://arxiv.org/abs/2607.11881
- Macar et al. (2026). *Mechanisms of Introspective Awareness*. arXiv preprint. https://arxiv.org/abs/2603.21396
- Aayush Marasini, Barsat Khadka, Nick Rahimi (2026). *WeightBench: Evaluating Language Models as Weight-Space Programmers*. arXiv preprint. https://arxiv.org/abs/2611.18553
- Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W. Lee, Richard Ren, Long Phan, Norman Mu, Adam Khoja, Oliver Zhang, Dan Hendrycks (2025). *Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs*. preprint (v2). https://arxiv.org/abs/2502.08640
- Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov (2022). *Locating and Editing Factual Associations in GPT*. NeurIPS 2022. https://arxiv.org/abs/2202.05262
- Atharv Naphade, Samarth Bhargav, Sean Lim, Mcnair Shah (2026). *Me, Myself, and π: Evaluating and Explaining LLM Introspection*. arXiv preprint. https://arxiv.org/abs/2603.20276
- Thomas O. Nelson, Louis Narens (1990). *Metamemory: A Theoretical Framework and New Findings*. The Psychology of Learning and Motivation, Vol. 26 (ed. G. H. Bower), Academic Press, pp. 125-173. https://sites.socsci.uci.edu/~lnarens/1990/Nelson&Narens_Book_Chapter_1990.pdf
- Richard E. Nisbett, Timothy D. Wilson (1977). *Telling More Than We Can Know: Verbal Reports on Mental Processes*. Psychological Review 84(3), 231-259. https://doi.org/10.1037/0033-295X.84.3.231
- Stephen M. Omohundro (2008). *The Basic AI Drives*. Proceedings of the First Conference on Artificial General Intelligence (AGI 2008).
- Arjun Panickssery, Samuel R. Bowman, Shi Feng (2024). *LLM Evaluators Recognize and Favor Their Own Generations*. NeurIPS 2024. https://arxiv.org/abs/2404.13076
- Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos, Julia Kempe (2026). *Learning to Discover Interesting Mathematics*. preprint. https://arxiv.org/abs/2609.28603
- Gabriel J. Perin, Lucas Boscaini, André Araujo, Nina S. T. Hirata (2026). *Training-Free Task Vectors for LLM Behavioral Control (TFTV)*. preprint (v3, Oct 2026). https://arxiv.org/abs/2609.09054
- Nora Petrova, John Burden, Jerome Wynne (2026). *MetaLoop: Benchmarking the Full Metacognitive Loop in LLMs*. NeurIPS 2026 (poster; preprint not yet available). https://neurips.cc/virtual/2026/poster/139348
- Dillon Plunkett, Adam Morris, Keerthi Reddy, Jorge Morales (2025). *Self-Interpretability: LLMs Can Describe Complex Internal Processes that Drive Their Decisions*. preprint (v2 10 Nov 2025). https://arxiv.org/abs/2505.17120
- Zhe Ren, Yimeng Chen, Dandan Guo, et al. (2026). *Self-Improvements in Modern Agentic Systems: A Survey*. arXiv preprint. https://arxiv.org/abs/2607.13104
- Timothy Rupprecht et al. (2026). *Human Cognition in Machines: A Unified Perspective of World Models*. preprint (survey). https://arxiv.org/abs/2604.16592
- Hadi Salloum, Ammar Ali et al. (2026). *Tree-Ising: Repairing Language Models with Bit-Level Ising Edits*. arXiv preprint. https://arxiv.org/abs/2611.14210
- Jürgen Schmidhuber (2003). *Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements*. arXiv preprint. https://arxiv.org/abs/cs/0309048
- Shashwat Singh, Tal Linzen, Shauli Ravfogel (2026). *Can LLMs Introspect? A Reality Check*. COLM 2026 (per arXiv comment). https://arxiv.org/abs/2605.26242
- Sofroniew et al. (Anthropic) (2026). *Emotion Concepts and Their Function in a Large Language Model*. preprint. https://arxiv.org/abs/2604.07729
- Siyuan Song, Jennifer Hu, Kyle Mahowald (2025). *Language Models Fail to Introspect About Their Knowledge of Language*. arXiv preprint. https://arxiv.org/abs/2503.07513
- Oleg Stroganov (2026). *When LLMs Modify Themselves: Convergence, Values, and Stopping in Iterative Self-Improvement*. arXiv preprint. https://arxiv.org/abs/2611.01304
- Takehi, Teoh, Zhang, Khattab (2026). *Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights*. Blog post, MIT CSAIL, 2 November 2026. https://rikiyat.github.io/blog/weight-space-programming/
- Dhruv Trehan, Paras Chopra (2026). *Eliciting Research Taste in LLMs through Future Research Direction Choice*. preprint. https://arxiv.org/abs/2611.19794
- Filip Trhlik, Aoife O'Flynn, Angela Yu, Arduin Findeis, Paula Buttery (2026). *LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values*. preprint. https://arxiv.org/abs/2606.13944
- Koki Wataoka, Tsubasa Takahashi, Ryokan Ri (2024). *Self-Preference Bias in LLM-as-a-Judge*. NeurIPS 2024 workshop (arXiv v2 Jun 2025). https://arxiv.org/abs/2410.21819
- Haoyan Yang, Mario Xerri, Solha Park, et al. (2026). *Self-Improvement of Large Language Models: A Technical Overview and Future Outlook*. arXiv preprint. https://arxiv.org/abs/2603.25681
- Nicolas Yax, Stefano Palminteri, Pierre-Yves Oudeyer (2026). *LLMs learn different forms of metacognition when trained to predict their own accuracy*. arXiv preprint. https://arxiv.org/abs/2609.33886
- Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, Jason Weston (2024). *Self-Rewarding Language Models*. https://arxiv.org/abs/2401.10020
- Dmitrij Żatuchin (2026). *A Shared Taste for Model-Written Text: The Generator-by-Selector Matrices of \"AI-AI Bias\" Show No Detectable Own-Model Premium*. preprint. https://arxiv.org/abs/2610.00369
- Siqi Zeng, Andre N. Assis, Rowan Wang (2026). *Evaluating and Improving LLM Self-Modeling*. EMNLP 2026. https://arxiv.org/abs/2608.30980
- Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He (2025). *Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification*. preprint (COLM 2025). https://arxiv.org/abs/2504.05419
- Jiang Zhang, Bing Yuan, Qian Zhang (2026). *Self-Reference in Large Language Models: The Introspection Threshold for Recursive Self-Improvement*. arXiv preprint. https://arxiv.org/abs/2607.04277
- Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song (2025). *Learning to Reason without External Rewards (INTUITOR)*. arXiv preprint. https://arxiv.org/abs/2505.19590
- Chenyu Zhou (2026). *More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges*. arXiv preprint. https://arxiv.org/abs/2607.05904
- Zweiger, Pari, Guo, Akyürek, Kim, Agrawal (2025). *SEAL: Self-Adapting Language Models*. NeurIPS 2025. https://arxiv.org/abs/2506.10943
