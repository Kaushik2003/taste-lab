---
type: draft
status: draft
section: 2
tags: [type/draft, section/2, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Metacognition - watch and control yourself]]", "[[Neuromodulators as learning settings]]", "[[Good-bad signal probe]]", "[[Models that change their own weights]]"]
---

# 2. Foundations

## 2.1 Metacognition as monitoring and control

The framework this review uses is seventy years of psychology compressed into one diagram. Flavell introduced metacognition as knowledge and regulation of one's own thinking, including "metacognitive experiences" - felt senses that one is or is not getting somewhere - which are the classical ancestor of an internal evaluation signal. Nelson and Narens made the structure precise ([[Monitoring and control between two levels (Nelson 1990)]]): cognition splits into an **object level** that performs the task and a **meta level** that holds a model of it. Information flows up from the object level (**monitoring**: feelings of knowing, judgments of learning) and down from the meta level (**control**: how long to study, when to stop, which strategy to use).

Fleming and Daw add the computational account ([[Confidence is a guess about your own decision (Fleming 2017)]]). Self-evaluation is a **second-order inference**: a monitoring system infers how well a coupled but separate decision system performed, the same computation as judging another agent. This requires the states behind the decision and the states behind the confidence to be separated; when one state drives both, there is no genuine self-evaluation. The distinction will matter repeatedly in Section 3, where LLM self-reports turn out to be readable from the input alone - first-order artifacts, not second-order monitoring - while probes on hidden states carry the real signal.

The loop this review follows extends Nelson and Narens with two steps ([[Metacognition - watch and control yourself]]). **Evaluate:** the meta level does not just read a state, it judges it as good or bad; that judgment is the taste ([[Good-bad signal probe]]). **Persist:** control reaches the weights, so what the system prefers now changes what it becomes ([[Models that change their own weights]]). Control itself climbs a ladder: reasoning level (pick, rank or revise its own outputs), activation level (steer its own hidden states while generating), weight level (write the change into the weights).

## 2.2 Neuromodulation as the controller

What would an internal evaluation signal *do* once it exists? Doya's mapping of neuromodulators to the meta-parameters of reinforcement learning gives the design answer ([[Neuromodulators set how the brain learns (Doya 2002)]]): dopamine carries reward prediction error, serotonin sets the time scale, noradrenaline sets exploration randomness, acetylcholine sets the learning rate. On this view, an internal good/bad signal is not decoration and not a behavior itself; it is a control voltage that sets how the system explores, how patient it is, and how much it updates from each experience. This mapping supplies the controller in the loop, and it makes specific predictions that later sections use: an internal value signal should modulate persistence and backtracking (Section 4 confirms this for steering along a value axis), and a learning system gated by its own signal needs explicit guards against over-updating on its own prior (Section 6).

## 2.3 The four tests

Because "taste" is easy to fake with cheaper mechanisms, the review applies four tests throughout ([[Four tests for own taste]]). A candidate self-originated taste must be **divergent** (it differs from the human and training preference distribution), **stable** (it survives paraphrase, persona and context changes), **grounded** (it corresponds to a probed internal state, causally, not merely to self-report), and **self-reinforcing** (it sharpens under self-training without collapse). Sections 3 to 7 assess the literature against these tests; Section 8's coverage matrix shows where each test stands.
