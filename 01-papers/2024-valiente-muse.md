---
type: paper
title: "Competence-Aware AI Agents with Metacognition for Unknown Situations and Environments (MUSE)"
status: skimmed
arxiv: 2411.13537
url: https://arxiv.org/abs/2411.13537
authors: Rodolfo Valiente, Praveen K. Pilly (HRL Laboratories)
year: 2024
venue: preprint (v2, Nov 2025)
relevance: 3
section: 3
tier: deep
tests: []
components: [monitoring, controller]
tags: [type/paper, section/3, component/monitoring, component/controller, status/skimmed, relevance/3, world-model, competence-awareness, strategy-selection, agents]
links: ["[[landscape-metacognitive-monitoring]]", "[[metacognition-monitor-control]]", "[[neuromodulation-metalearning]]"]
---

# MUSE: Metacognition for Unknown Situations and Environments

**One line:** Put a self-awareness head on a world model: the agent simulates its own future success on a novel task, and when failure is predicted it switches strategy instead of following its policy. Two instantiations (world-model based and LLM based), both beating Dreamer-v3 RL and prompt-only LLM agents on out-of-distribution tasks.

## Claim
Metacognition - competence awareness plus strategy selection - is the missing ingredient for agents in novel environments, and it can be built as an explicit cycle on top of a learned world model ([abs](https://arxiv.org/abs/2411.13537)).

## Mechanism
- The world-model version learns to predict its own competence on the current task (self-awareness), then uses that estimate to pick among strategies (self-regulation), iterating the cycle as the task unfolds.
- The agent itself is part of the modeled world: the world model simulates "what happens if *I* act this way", which is what makes the competence estimate possible before acting.

## Evidence
- Significant improvements in self-awareness and self-regulation vs Dreamer-v3-based RL and purely prompt-based LLM agents on novel OOD tasks [unverified: effect sizes not extracted, read the paper's tables before citing numbers].

## Limits / what they didn't show
- Competence is task success/failure - a correctness-adjacent signal again, not preference or style.
- Strategy set is given; the agent does not invent strategies.
- Embodied/task environment, not reasoning or code; transfer of the cycle to an LLM's internal states is untested.

## Relevance to taste-lab
**The world-model leg of the architecture gap.** SST ([[2025-aviss-state-stream-transformer]]) supplies persistent self-state; MUSE supplies the self included in a world model. The missing middle is our evaluator: a valence readout ([[valence-readout]]) playing the role of MUSE's competence estimate, but on a quality beyond task success. A "MUSE for reasoning style" - simulate candidate continuations, read valence on the simulated outcomes, regulate - is a concrete architecture the review can propose.
- Prior-art check: **A partial** (the agent's own model of itself gates its own strategy, but the signal is external task success). **B no.**

## Steal this
- The metacognitive cycle as an explicit loop diagram (assess competence -> select strategy -> act -> reassess) for the review's synthesis figure.
- "Agent as part of its own world model" as the clean one-line definition of what a self-model is.

## Kaushik's notes
<!-- yours -->
