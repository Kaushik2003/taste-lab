---
type: draft
status: draft
section: 2
tags: [type/draft, section/2, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Metacognition - watch and control yourself]]", "[[Neuromodulators as learning settings]]", "[[Good-bad signal probe]]", "[[Models that change their own weights]]"]
---

# 2. Foundations

## 2.1 Metacognition as monitoring and control

Flavell introduced metacognition as knowledge about one's own thinking and the regulation of it [@Flavell 1979]. Nelson and Narens made the structure precise ([[Monitoring and control between two levels (Nelson 1990)]]). An **object level** does the task, and a **meta level** holds a model of the object level. Information flows up (**monitoring**, for example a feeling of knowing) and commands flow down (**control**, for example when to stop). The model at the meta level can be wrong. Fleming and Daw added that confidence is a second-order inference: a monitoring system infers how well a coupled but separate decision system did ([[Confidence is a guess about your own decision (Fleming 2017)]]). If one state drives both the decision and the confidence, the system only reports the strength of its first answer.

The loop of this review adds a step, evaluation, between monitoring and control. A reader may object that the step is not new: monitoring already includes judgments, and reinforcement learning has long used a critic, an internal signal of good and bad that drives changes to weights. We keep the step separate because these judgments differ in where their criterion comes from. A feeling of knowing judges whether one's own answer is right. A critic learns to predict a reward that someone outside defined. The question here is whether a model can hold a criterion of good and bad that is its own, on matters with no right answer, and what happens when that criterion drives a change to the model.

## 2.2 Standards for a monitoring claim

The human literature supplies two warnings. A plain correlation between confidence and accuracy mixes how well confidence separates right from wrong answers with how high confidence is overall, so a model that is confident about everything can look metacognitive ([[Bias-free measurement of metacognition (Fleming 2014)]]). And people asked why they acted as they did often report a plausible theory, not an observation of the cause [@Nisbett 1977], so a fluent self-report is weak evidence of self-access. Comsa and Shanahan argued that a self-report counts as introspection only if a causal process links the internal state to the report ([[Introspection needs a causal link to count (Comsa 2025)]]). This review uses their bar: a monitoring claim is strong only if a study shows that the internal state causes the report or the behavior.

## 2.3 What an evaluation signal does, and levels of self-change

Doya's mapping of brain chemicals to the settings of reinforcement learning suggests what an internal evaluation signal would do: it is not a behavior but a control signal that sets how the system explores, how patient it is, and how much it changes from each experience ([[Neuromodulators set how the brain learns (Doya 2002)]]). Koch sorted self-modification by what the system changes: actions, low-level rules, control rules, or the criterion used to judge changes ([[What a system changes when it changes itself (Koch 2026)]]). Choosing among outputs changes actions, weight edits change rules, and a system that changes its own evaluation signal would change the criterion. That last level is what a self-originated taste would need, and no system in this review reaches it.

## 2.4 Related surveys

No survey that we found covers the four literatures together, but several cover parts (Table 2). We read only the abstracts of the works marked with an asterisk, so the last column states what their abstracts do not claim. The second row is the nearest prior work. Like this review, it joins self-monitoring to self-modification and concludes that current models fall short. It argues from computability theory toward architecture; this review argues from the experimental record toward a measurement.

**Table 2.** The closest surveys and positions, and what this review adds.

| Work | What it covers | What this review adds |
|---|---|---|
| [[Survey of metacognition in language models (Liu 2026)]] | Measuring, giving, and using metacognition in language models; a source of our corpus | Evaluation by a criterion of the model's own; weight change; preferences |
| Zhang, Yuan, and Zhang* [@ZhangJ 2026] | Argues from theory that recursive self-improvement needs introspection | Empirical controls for monitoring claims; two routes to weight change; preferences after a change |
| Ren and colleagues* [@Ren 2026] | Self-improving agents, sorted by the target of an update and the signal that drives it | Direct weight edits; the model's self-monitoring and its preferences |
| Yang and colleagues* [@Yang 2026] | Self-improvement of language models as a closed loop with an evaluation layer | Signals read from hidden states; what a change does to the model |
| Petrova and colleagues* [@Petrova 2026] | A benchmark of the full loop of monitoring, acting, and updating | The steps of evaluation and of persistence in weights |

## Log
- 2026-11-24 (guides and critique): past tense for what studies did; a defense of evaluation as a separate step; Nisbett and Wilson 1977 and Koriat 1997; a section on related surveys with the nearest prior work (Zhang, Yuan, and Zhang 2026).
- 2026-11-24: Flavell reference added; cross-references updated.
- 2026-11-23: rewritten for the final paper. Added measurement (Fleming 2014, Maniscalco 2012, Cacioli, Huff), the causal bar (Comsa), field maps (Shakarian, Liu survey), Backpropamine, levels of self-change (Koch). Removed the code testbed.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/02-foundations (long).md`.
