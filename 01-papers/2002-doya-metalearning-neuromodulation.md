---
type: paper
title: "Metalearning and Neuromodulation"
status: skimmed
arxiv:
url: https://doi.org/10.1016/S0893-6080(02)00044-8
authors: Kenji Doya
year: 2002
venue: Neural Networks 15(4-6), 495-506
relevance: 3
section: 2
tier: deep
tests: []
components: [controller]
tags: [type/paper, section/2, component/controller, status/skimmed, relevance/3, neuromodulation, metalearning, foundations]
links: ["[[neuromodulation-metalearning]]", "[[metacognition-monitor-control]]"]
---

# Metalearning and Neuromodulation (Doya, 2002)

**One line:** The brain's neuromodulators map one-to-one onto the meta-parameters of reinforcement learning, so a scalar internal signal can run the controller of a learning system.

## Mechanism
- **Dopamine** -> reward prediction error (better or worse than expected)
- **Serotonin** -> time scale / discounting (patience)
- **Noradrenaline** -> randomness of action selection (exploration temperature)
- **Acetylcholine** -> learning rate (how much to update from this experience)

## Relevance to taste-lab
This is the controller slot in our architecture ([[neuromodulation-metalearning]]). It makes the key move respectable: a diffuse internal signal (for us, valence) does not have to *be* the behavior; it can set the parameters that shape behavior and learning. Xu's "dopamine neurons" ([[2026-xu-sparse-reward-subsystem]]) are the first direct LLM evidence that a TD-error-like signal is sparsely readable, and Jiang's low-value -> backtracking result ([[2026-jiang-value-axis]]) is the exploration knob Doya's mapping predicts.

## Kaushik's notes
<!-- yours -->
