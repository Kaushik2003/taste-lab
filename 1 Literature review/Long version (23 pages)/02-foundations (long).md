---
type: draft
status: draft
section: 2
tags: [type/draft, section/2, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Metacognition - watch and control yourself]]", "[[Neuromodulators as learning settings]]", "[[Good-bad signal probe]]", "[[Models that change their own weights]]"]
---

# 2. Foundations

This section supplies the ideas that the rest of the review depends on: the two-level model of metacognition, the standards for measuring it, a view of an evaluation signal as a controller of learning, and a way to sort kinds of self-change.

## 2.1 Metacognition as monitoring and control

Flavell introduced metacognition as knowledge about one's own thinking and the regulation of it [@Flavell 1979]. He included "metacognitive experiences", felt senses that one is or is not getting somewhere. These are the classic ancestor of an internal evaluation signal. Nelson and Narens made the structure precise ([[Monitoring and control between two levels (Nelson 1990)]]). Cognition splits into an **object level**, which does the task, and a **meta level**, which holds a model of the object level. Information flows up from the object level to the meta level. This is **monitoring**: feelings of knowing, judgments of learning, confidence. Commands flow down from the meta level. This is **control**: how long to study, when to stop, which strategy to use. Two of their principles matter most for this review. The meta level contains a model of the object level, and that model can be wrong. And the flow is two-way: the meta level both reads and changes the object level.

Fleming and Daw gave the computational account ([[Confidence is a guess about your own decision (Fleming 2017)]]). Confidence is a **second-order inference**: a monitoring system infers how well a coupled but separate decision system did. This is the same computation as judging another agent's decision. It needs the states behind the decision and the states behind the confidence to be partly separate. If one state drives both, the system is not evaluating itself. It is only reporting the strength of its first answer. This distinction returns in Section 3, where some self-reports of language models turn out to be readable from the input text alone.

The loop of this review adds a step, evaluation, between monitoring and control, and a reader may object that the step is not new. Monitoring in Nelson and Narens already includes judgments, such as the feeling of knowing. And reinforcement learning has long used a critic, an internal signal of good and bad that drives changes to weights. We keep the step separate for one reason: these judgments differ in where their criterion comes from. A feeling of knowing is a judgment about whether one's own answer is right. A critic learns to predict a reward that someone outside defined. The question of this review is whether a model can hold a criterion of good and bad that is its own, on matters with no right answer, and what happens when that criterion drives a change to the model. Section 5 sorts the candidate signals by the origin of their criterion.

## 2.2 How metacognition is measured

The human literature warns that the obvious measure is wrong. A plain correlation between confidence and accuracy mixes two things: how well confidence separates right from wrong answers (**sensitivity**), and how high confidence is overall (**bias**) ([[Bias-free measurement of metacognition (Fleming 2014)]]). A third quantity, efficiency, asks how good the sensitivity is given how well the task itself was done. The measure meta-d' expresses this. It is the task accuracy that an ideal observer would need to reach the observed confidence sensitivity ([[Meta-d-prime - sensitivity relative to task performance (Maniscalco 2012)]]). Psychologists built these measures for human yes/no tasks. Applying them to language models needs care about what counts as a trial and a criterion. But the warning holds: a model that is simply confident about everything can look metacognitive under a crude measure.

Recent work applies the human test batteries to language models directly. A preregistered battery of 524 items from classic psychology tasks tested whether 20 frontier models withdrew wrong answers more often than right ones. Accuracy and metacognitive sensitivity ranked the models almost in reverse order ([[A test battery for self-monitoring (Cacioli 2026)]]). On a classic memory task, human judgments of learning predicted later recall, and no tested model's judgments did ([[LLM judgments of learning do not predict memory (Huff 2025)]]). So metacognitive skill in models is not a side effect of general skill.

A second standard concerns causation, and psychology supplies the warning here too. People asked why they acted as they did often report a plausible theory and not an observation of the cause [@Nisbett 1977], and their judgments of their own learning rest on cues such as how easily an item comes to mind, not on direct access to memory [@Koriat 1997]. A fluent self-report is therefore weak evidence of self-access, in people and in models. Comsa and Shanahan argued that a self-report counts as introspection only if a causal process links the internal state to the report ([[Introspection needs a causal link to count (Comsa 2025)]]). By this bar, a model's account of its own "creative process" is role play. But its correct inference of its own sampling temperature, read from its own recent outputs, is a minimal real case. This review uses their bar throughout: a monitoring claim is strong only if a study shows that the internal state causes the report or the behavior.

## 2.3 Where the field stands, in its own words

Two positions frame the field. Johnson and colleagues imported the psychology of wisdom into AI as a specification: object-level strategies manage problems, metacognitive strategies manage the object-level strategies, and current AI is strong at the first and weak at the second ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). Li and colleagues treated awareness as a measurable function, and warned that better self-models may also fake alignment better ([[AI awareness as a measurable capacity (Li 2025)]]). A survey of artificial metacognition sorted the field into monitoring, control, and communication of one's own cognition, and listed human metacognitive abilities that AI has not yet tried to build ([[A map of artificial metacognition (Shakarian 2026)]]). The 2026 survey of metacognition in language models covers monitoring and control, but has no section on evaluation by the model's own preferences and none on self-edits to weights ([[Survey of metacognition in language models (Liu 2026)]]).

The bias literature gives the negative image. One analysis read five apparently separate biases of language models as one syndrome of missing monitoring and control, "metacognitive myopia" ([[Metacognitive myopia as a frame for model bias (Scholten 2024)]]). Reasoning models already showed measurable, family-specific habits such as "wait, did I miss anything?" ([[Reasoning models show habits of mind (Dong 2025)]]). These habits are the behavioral surface of a self-monitoring style, whatever lies under them.

## 2.4 Neuromodulation as the controller

What would an internal evaluation signal *do* once it exists? Doya's mapping of brain chemicals to the settings of reinforcement learning gives one answer ([[Neuromodulators set how the brain learns (Doya 2002)]]). Dopamine carries the reward prediction error. Serotonin sets the time scale, that is, how far ahead rewards count. Noradrenaline sets how random exploration is. Acetylcholine sets the learning rate. In this view, an internal good/bad signal is not a behavior itself. It is a control signal that sets how the system explores, how patient it is, and how much it changes from each experience ([[Neuromodulators as learning settings]]). Miconi and colleagues built a machine version of the learning-rate setting: a network that outputs its own "dopamine" signal, which sets how fast its own plastic weights change ([[Backpropamine - a network sets its own plasticity (Miconi 2019)]]). The mapping predicts two things that later sections test. An internal value signal should modulate persistence and backtracking (Section 5 finds this for a value axis). And a system that learns by its own signal needs guards against over-learning its own prior (Section 7).

## 2.5 Levels of self-change

Self-modification is not one thing. Koch sorted it by what the system changes: actions only, low-level rules, control rules, or the criterion used to judge changes ([[What a system changes when it changes itself (Koch 2026)]]). He argued that people can change current AI from outside at low levels, without a matching self-representation. This sorting fits the control ladder of Section 1.1. Choosing among outputs changes actions. Steering changes how the model applies its rules in one run. Weight edits change the rules. A system that changes its own evaluation signal would change the criterion. That last level is what a self-originated taste would need, and Section 9 shows that no system in this review reaches it.

## 2.6 Related surveys, and how this review differs

No survey that we found covers the four literatures together, but several cover parts, and two use axes close to ours. Table 4 lists them. We read the abstracts of the four works marked with an asterisk and not their full text, so the last column states what their abstracts do not claim.

**Table 4.** The closest surveys and positions, and what this review adds.

| Work | What it covers | What this review adds |
|---|---|---|
| [[Survey of metacognition in language models (Liu 2026)]] | Measuring, giving, and using metacognition in language models; the largest survey of that half, and a source of our corpus | Evaluation by a criterion of the model's own; weight change; preferences |
| Zhang, Yuan, and Zhang* [@ZhangJ 2026] | Argues from theory that sustainable recursive self-improvement needs introspection, reviews the partial metacognition of current models, and proposes architectural paths | The empirical controls for monitoring claims; the two routes to weight change; measurement of preferences after a change |
| Ren and colleagues* [@Ren 2026] | Self-improving agents, sorted by the target of an update and the signal that drives it | Direct weight edits; the model's self-monitoring and its preferences |
| Yang and colleagues* [@Yang 2026] | Self-improvement of language models as a closed loop of data, selection, optimization, and refinement, with an evaluation layer | Signals read from hidden states; self-report; what a change does to the model |
| [[A survey of self-evolving agents (Gao 2025)]] | What, when, how, and where agents evolve | The case where the judge is the model itself |
| [[World models miss motivation and metacognition (Rupprecht 2026)]] | World models by cognitive function; names metacognition as a gap | The evidence on self-models in language models |
| Petrova and colleagues* [@Petrova 2026] | A benchmark of the full loop of monitoring, acting, and updating, in models and people | The steps of evaluation and of persistence in weights |

The second row is the nearest prior work. Like this review, it joins self-monitoring to self-modification and concludes that current models fall short. It argues from computability theory toward architecture. This review argues from the experimental record toward a measurement: what a weight change does to a model's preferences and to its self-monitoring.

## 2.7 The four tests

Because "taste" is easy to fake with cheaper mechanisms, the review applies the four tests from Section 1.2 throughout. Each test removes one cheap explanation. A divergent preference could just be noise, so it must also be stable. A stable preference could be a learned verbal habit, so it must be grounded in an internal state that causes the choice. A grounded preference could be fixed forever, so it must sharpen under self-change. And sharpening alone could be collapse onto the model's prior, so it must sharpen without collapse. Sections 3 to 8 report the evidence for each test, and Section 9 sums it up.

## Log
- 2026-11-24 (guides and critique): past tense for what studies did; a defense of evaluation as a separate step; Nisbett and Wilson 1977 and Koriat 1997; a section on related surveys with the nearest prior work (Zhang, Yuan, and Zhang 2026).
- 2026-11-24: Flavell reference added; cross-references updated.
- 2026-11-23: rewritten for the final paper. Added measurement (Fleming 2014, Maniscalco 2012, Cacioli, Huff), the causal bar (Comsa), field maps (Shakarian, Liu survey), Backpropamine, levels of self-change (Koch). Removed the code testbed.
