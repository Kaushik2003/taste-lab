---
type: paper
title: "MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces"
status: skimmed
arxiv: 2502.07709
url: https://arxiv.org/abs/2502.07709
authors: Loris Gaven, Thomas Carta, Clément Romac, Cédric Colas, Sylvain Lamprier, Olivier Sigaud, Pierre-Yves Oudeyer
year: 2025
venue: ICML 2025 (PMLR 267)
relevance: 3
section: 5
tier: deep
tests: [self-reinforcing, grounded]
components: [controller, monitoring]
tags: [type/paper, section/5, test/self-reinforcing, test/grounded, component/controller, component/monitoring, status/skimmed, relevance/3, question/Q3, question/Q6, role/prior-art, learning-progress, curriculum, intrinsic-motivation, metacognitive-control, autotelic]
links: ["[[Neuromodulators as learning settings]]", "[[Metacognition - watch and control yourself]]", "[[Field map - Changes that stay in the weights]]", "[[OMNI - models judge which tasks are interesting (Zhang 2023)]]", "[[Open-ended means novel and learnable to an observer (Hughes 2024)]]", "[[Backpropamine - a network sets its own plasticity (Miconi 2019)]]", "[[Q3 Can self-learning avoid collapse]]", "[[Q6 Can the model read and use its own signal]]"]
---

# MAGELLAN: an LLM agent predicts its own learning progress to choose what to practice

**One line:** A small language model agent reads its own last-layer representation of a goal to predict its chance of success, tracks how that prediction changes, and practices the goals where it is learning fastest. It is the only method without hand-made goal groups that masters a goal space of about 25,000 goals.

Source: [arXiv 2502.07709](https://arxiv.org/abs/2502.07709) (v3 Jun 2025), [ICML 2025 / PMLR 267](https://proceedings.mlr.press/v267/gaven25a.html). Full HTML read for Sections 3 to 5.

**Words used here:**
- **Autotelic agent:** an agent that sets and pursues its own goals.
- **Competence:** the predicted chance of success on a goal.
- **Absolute learning progress (ALP):** the size of the change in competence over the last N updates. It rises when the agent improves and also when it forgets (Eq. 1).
- **LoRA adapter:** a small set of extra weights trained on top of a frozen model.

## Claim
An LLM agent can learn to predict its own competence and learning progress online, including on goals it has never tried, and use this to build its own curriculum without expert goal groups ([arXiv](https://arxiv.org/abs/2502.07709), Abstract).

## Mechanism
1. **Self-monitor:** put the goal in the prompt; an MLP reads the last token's final-layer state of the agent's own model and outputs a success chance. It is trained on recent episode outcomes. It runs on a separate LoRA adapter of the same base model (Sec. 3.2).
2. Because similar goals have similar representations, one update also moves estimates for related goals. This lets it estimate untried goals.
3. **Learning progress:** compare today's estimate with the estimate from N updates ago (Eq. 1).
4. **Control:** a bandit samples goals in proportion to estimated progress, with some random exploration (ε from 1 down to 0.2) (Sec. 3.2).
5. The policy (Flan-T5, 248M parameters) is trained by reinforcement learning on the chosen goals (Sec. 3.3).

## Evidence
- Environment: Little-Zoo, a text world with about 19.5 million goals; about 80% are impossible. Experiments use about 25,000 goals, 8 seeds per method (Sec. 3.4, 4.2).
- Over 500,000 episodes, MAGELLAN is the only method without expert groups to reach at least 90% success in every goal category (Sec. 4.2, Fig. 5).
- Error on unseen goals: 0.11 for MAGELLAN versus 0.53 for online progress tracking without generalization, and 0.09 for the method with expert groups (Sec. 4.3, Table 2).
- When goals are swapped during training, it adapts and roughly matches the expert-group method (Sec. 4.4).
- A frozen model as the competence reader performed poorly; the reader must learn (Sec. 3.2, Appendix D.1).

## Limits / what they didn't show
- Small models and a controlled text world (authors, Impact Statement).
- The competence reader is trained on outside success labels. The signal is "will I succeed", not "is this good".
- Slower than the expert-group method because of uniform exploration (Sec. 4.2).
- No check that the agent's own self-report agrees with the probe.

## Relevance to taste-lab
**Relevance 3. Section 5 (control of what goes into the weights), with links to section 2.**
- **Gap it speaks to:** "no hidden-state monitoring signal controls learning". This is the closest case found: a readout of the model's own hidden state decides what the model trains on next. It narrows that gap. What stays open: the signal is competence, trained on outside labels, not an evaluation of quality.
- **Loop mapping:** monitor (hidden-state readout), evaluate (learning progress), control (goal choice), persist (reinforcement learning on chosen goals). Only the evaluate step differs from ours.
- **Anchor link:** learning progress favors goals that are neither too easy nor impossible. That is a built-in guard against settling on one's prior, and it fits the "learnable to an observer" definition of open-endedness ([[Open-ended means novel and learnable to an observer (Hughes 2024)]]).
- The human basis: people choose tasks by learning progress, not only by competence ([Ten et al. 2021, Nature Communications](https://doi.org/10.1038/s41467-021-26196-w)).

## Steal this
- Learning progress as the control signal (change in a self-estimate over time), instead of the raw estimate.
- A hidden-state reader on a separate adapter of the same model.
- Code is available according to the listing [unverified link].

## Harshit's notes
<!-- yours -->
