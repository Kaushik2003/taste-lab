---
type: paper
title: "Metalearning and neuromodulation"
status: read
arxiv:
url: https://doi.org/10.1016/S0893-6080(02)00044-8
doi: 10.1016/S0893-6080(02)00044-8
authors: Kenji Doya
year: 2002
venue: Neural Networks 15(4-6), 495-506 (special issue "Computational Models of Neuromodulation")
relevance: 2
section: 2
tier: skim
tests: []
components: [controller]
tags: [type/paper, section/2, component/controller, status/skimmed, relevance/2, role/prior-art, neuroscience, metalearning, reinforcement-learning, foundations]
links: ["[[Neuromodulators as learning settings]]", "[[Metacognition - watch and control yourself]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Outside controller steers thinking modes (Karpf 2026)]]"]
---

# Metalearning and neuromodulation

**One line:** Four brain chemicals may each set one setting of learning: dopamine the reward error, serotonin how far ahead to look, noradrenaline how random to act, acetylcholine how fast to update memory.

**Why it matters to us:** It gives the "control" arrow of [[Monitoring and control between two levels (Nelson 1990)]] a concrete set of knobs. Our architecture uses this mapping for the controller ([[Neuromodulators as learning settings]]).

Source: full text read from an open copy of Neural Networks 15(4-6), 495-506 ([mirror PDF](https://fleetwood.dev/papers/doya2002.pdf)), via `pdftotext`. DOI [10.1016/S0893-6080(02)00044-8](https://doi.org/10.1016/S0893-6080(02)00044-8). Earlier abstract-only flags resolved 2026-11-21.

**Words used here:**
- **Reinforcement learning (RL):** learning from rewards. The learner tries actions and makes rewarded ones more likely.
- **Metalearning:** learning how to learn. Here it means tuning the settings of the learner, not the knowledge itself.
- **Meta-parameter:** a setting of the learning process, such as the learning rate.
- **Reward prediction error:** the gap between the reward you expected and the reward you got.
- **Discount factor:** how much a future reward counts compared to a reward now. A high value means "patient".
- **Neuromodulator:** a brain chemical that is sent widely and changes how many neurons respond and learn, not one specific message.

## Claim
The ascending neuromodulator systems carry global signals that regulate learning across the brain. Each maps to one RL meta-parameter (abstract, via [researchr](https://researchr.org/publication/Doya02/bibtex)):
- **Dopamine** signals the error in reward prediction.
- **Serotonin** controls the time scale of reward prediction (the discount factor).
- **Noradrenaline** controls the randomness of action selection (exploration).
- **Acetylcholine** controls the speed of memory update (the learning rate).

## Mechanism
- The theory starts from standard RL. An agent learns value predictions from reward prediction errors.
- Such learners need meta-parameters set well: learning rate, exploration randomness and discount factor. Doya proposes that the brain sets them dynamically with neuromodulators, and that this is a form of metalearning.
- The paper builds the mapping from a review of experimental data and theoretical models (Sec. 1). It then walks each neuromodulator against the RL formalism: dopamine against the reward prediction error (Sec. 3.1), serotonin against the discount factor, with a simulated maze task showing how gamma shifts decisions (Sec. 3.2, Fig. 7), noradrenaline against the inverse temperature of action selection (Sec. 3.3), acetylcholine against the learning rate of memory update (Sec. 3.4).

## Evidence
- A theory paper. Its support is a review of earlier animal and modelling studies plus small simulations of its own (e.g. the discount-factor maze, Fig. 7), not a new experiment. The four mappings are stated explicitly in Sec. 3, items 1-4.
- It is widely cited in computational neuroscience; we did not check a citation count.

## Limits / what they didn't show
- One chemical, one knob is a simplification, and the paper itself says so: serotonin shows "complex, context-dependent functions" beyond the discount factor, and a whole passage covers serotonin-dopamine interactions (both mutually facilitatory and opponent cases, Sec. 3.2). Later work has pushed the mixed-roles view further.
- It describes how a brain could set its learning settings. It says nothing about who decides what is good (the reward is given), so it has no "taste".
- No link to language models. Any mapping to a model's learning rate, sampling temperature or planning horizon is our analogy, not the paper's claim.

## Relevance to taste-lab
**Relevance 2.** Foundations section. It supports the controller part of the architecture ([[Neuromodulators as learning settings]]).
- It is the cleanest older statement of "a meta level sets how the object level learns". That is the persist side of our loop: control that reaches learning, not only behavior.
- The closest model-side work is a trained controller that steers reasoning modes ([[Outside controller steers thinking modes (Karpf 2026)]]), but there the controller is outside and fixed.
- **What would weaken our use of it:** if no language-model paper shows an internal signal that sets learning rate or exploration, the Doya mapping stays a metaphor in the review, and we should present it as one.

## Steal this
- The four-knob table (reward error, discount, exploration, learning rate) as a way to sort control papers in section 5: which knob does each paper's controller turn?

## Harshit's notes
<!-- yours -->
