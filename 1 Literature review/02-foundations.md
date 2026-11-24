---
type: draft
status: draft
section: 2
tags: [type/draft, section/2, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Metacognition - watch and control yourself]]", "[[Neuromodulators as learning settings]]", "[[Good-bad signal probe]]", "[[Models that change their own weights]]"]
---

# 2. Foundations

## 2.1 Metacognition as monitoring and control

Flavell introduced metacognition as knowledge about one's own thinking and the regulation of it [@Flavell 1979]. He included "metacognitive experiences", felt senses that one is or is not getting somewhere. These are the classic ancestor of an internal evaluation signal. Nelson and Narens made the structure precise ([[Monitoring and control between two levels (Nelson 1990)]]). Cognition splits into an **object level**, which does the task, and a **meta level**, which holds a model of the object level. Information flows up from the object level to the meta level. This is **monitoring**: feelings of knowing, judgments of learning, confidence. Commands flow down from the meta level. This is **control**: how long to study, when to stop, which strategy to use. Two of their principles matter most for this review. The meta level contains a model of the object level, and that model can be wrong. And the flow is two-way: the meta level both reads and changes the object level.

Fleming and Daw give the computational account ([[Confidence is a guess about your own decision (Fleming 2017)]]). Confidence is a **second-order inference**: a monitoring system infers how well a coupled but separate decision system did. This is the same computation as judging another agent's decision. It needs the states behind the decision and the states behind the confidence to be partly separate. If one state drives both, the system is not evaluating itself. It is only reporting the strength of its first answer. This distinction returns in Section 3, where some self-reports of language models turn out to be readable from the input text alone.

## 2.2 How metacognition is measured

The human literature warns that the obvious measure is wrong. A plain correlation between confidence and accuracy mixes two things: how well confidence separates right from wrong answers (**sensitivity**), and how high confidence is overall (**bias**) ([[Bias-free measurement of metacognition (Fleming 2014)]]). A third quantity, **efficiency**, asks how good the sensitivity is given how well the task itself was done. The measure meta-d' expresses this. It is the task accuracy that an ideal observer would need to reach the observed confidence sensitivity ([[Meta-d-prime - sensitivity relative to task performance (Maniscalco 2012)]]). These measures were built for human yes/no tasks. Applying them to language models needs care about what counts as a trial and a criterion. But the warning holds: a model that is simply confident about everything can look metacognitive under a crude measure.

Recent work applies the human test batteries to language models directly. A preregistered battery of 524 items from classic psychology tasks tests whether 20 frontier models withdraw wrong answers more often than right ones. Accuracy and metacognitive sensitivity rank almost in reverse ([[A test battery for self-monitoring (Cacioli 2026)]]). On a classic memory task, human judgments of learning predict later recall, and no tested model's judgments do ([[LLM judgments of learning do not predict memory (Huff 2025)]]). So metacognitive skill in models is not a side effect of general skill.

A second standard concerns **causation**. Comsa and Shanahan argue that a self-report counts as introspection only if a causal process links the internal state to the report ([[Introspection needs a causal link to count (Comsa 2025)]]). By this bar, a model's account of its own "creative process" is role play. But its correct inference of its own sampling temperature, read from its own recent outputs, is a minimal real case. This review uses their bar throughout: a monitoring claim is strong only if the internal state is shown to cause the report or the behavior.

## 2.3 Where the field stands, in its own words

Two positions frame the field. Johnson and colleagues import the psychology of wisdom into AI as a specification: object-level strategies manage problems, metacognitive strategies manage the object-level strategies, and current AI is strong at the first and weak at the second ([[Wise machines need metacognition not just smarts (Johnson 2025)]]). Li and colleagues treat awareness as a measurable function, and warn that better self-models may also fake alignment better ([[AI awareness as a measurable capacity (Li 2025)]]). A survey of artificial metacognition sorts the field into monitoring, control and communication of one's own cognition, and lists human metacognitive abilities that AI has not yet tried to build ([[A map of artificial metacognition (Shakarian 2026)]]). The 2026 survey of metacognition in language models covers monitoring and control, but has no section on evaluation by the model's own preferences and none on self-edits to weights ([[Survey of metacognition in language models (Liu 2026)]]).

The bias literature gives the negative image. Five apparently separate biases of language models can be read as one syndrome of missing monitoring and control, "metacognitive myopia" ([[Metacognitive myopia as a frame for model bias (Scholten 2024)]]). Reasoning models already show measurable, family-specific habits such as "wait, did I miss anything?" ([[Reasoning models show habits of mind (Dong 2025)]]). These habits are the behavioral surface of a self-monitoring style, whatever lies under them.

## 2.4 Neuromodulation as the controller

What would an internal evaluation signal *do* once it exists? Doya's mapping of brain chemicals to the settings of reinforcement learning gives one answer ([[Neuromodulators set how the brain learns (Doya 2002)]]). Dopamine carries the reward prediction error. Serotonin sets the time scale, that is, how far ahead rewards count. Noradrenaline sets how random exploration is. Acetylcholine sets the learning rate. In this view, an internal good/bad signal is not a behavior itself. It is a control signal that sets how the system explores, how patient it is, and how much it changes from each experience ([[Neuromodulators as learning settings]]). Miconi and colleagues built a machine version of the learning-rate setting: a network that outputs its own "dopamine" signal, which sets how fast its own plastic weights change ([[Backpropamine - a network sets its own plasticity (Miconi 2019)]]). The mapping predicts two things that later sections test. An internal value signal should modulate persistence and backtracking (Section 5 finds this for a value axis). And a system that learns by its own signal needs guards against over-learning its own prior (Section 7).

## 2.5 Levels of self-change

Self-modification is not one thing. Koch sorts it by *what* is changed: actions only, low-level rules, control rules, or the criterion used to judge changes ([[What a system changes when it changes itself (Koch 2026)]]). He argues that current AI can be changed from outside at low levels, without a matching self-representation. This sorting fits the control ladder of Section 1.1. Choosing among outputs changes actions. Steering changes how rules are applied in one run. Weight edits change the rules. A system that changes its own evaluation signal would change the criterion. That last level is what a self-originated taste would need, and Section 9 shows that no system in this review reaches it.

## 2.6 The four tests

Because "taste" is easy to fake with cheaper mechanisms, the review applies the four tests from Section 1.2 throughout. Each test removes one cheap explanation. A divergent preference could just be noise, so it must also be stable. A stable preference could be a learned verbal habit, so it must be grounded in an internal state that causes the choice. A grounded preference could be fixed forever, so it must sharpen under self-change. And sharpening alone could be collapse onto the model's prior, so it must sharpen without collapse. Sections 3 to 8 report the evidence for each test, and Section 9 sums it up.

## Log
- 2026-11-24: Flavell reference added; cross-references updated.
- 2026-11-23: rewritten for the final paper. Added measurement (Fleming 2014, Maniscalco 2012, Cacioli, Huff), the causal bar (Comsa), field maps (Shakarian, Liu survey), Backpropamine, levels of self-change (Koch). Removed the code testbed.
