---
type: paper
title: "OMNI: Open-endedness via Models of human Notions of Interestingness"
status: skimmed
arxiv: 2306.01711
url: https://arxiv.org/abs/2306.01711
authors: Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune
year: 2023
venue: ICLR 2024
relevance: 3
section: 7
tier: deep
tests: [divergent, self-reinforcing]
components: [anchor, controller]
tags: [type/paper, section/7, test/divergent, test/self-reinforcing, component/anchor, component/controller, status/skimmed, relevance/3, role/prior-art, open-endedness, interestingness, auto-curriculum]
links: ["[[Field map - Taste and new ideas]]", "[[Anchor against collapse]]", "[[Learn to find interesting maths (Patel 2026)]]", "[[Open-ended means novel and learnable to an observer (Hughes 2024)]]", "[[Models share one taste for text (Zatuchin 2026)]]"]
---

# OMNI: Open-endedness via Models of human Notions of Interestingness

**One line:** Ask a language model which task is interesting to learn next, and combine that with "can the agent learn it now". The agent then learns more useful skills than when it picks tasks at random or by learning progress alone.

**Why it matters to us:** It is the founding paper for using a model's judgment of "interesting" to steer what gets learned. That is taste used as control over learning, but the taste is borrowed from human text, not the model's own.

Source: [arXiv 2306.01711](https://arxiv.org/abs/2306.01711) (v1 2 Jun 2023, v3 15 Feb 2024), [ICLR 2024](https://iclr.cc/virtual/2024/poster/19242). Introduction and method of the PDF read (first 12 pages).

**Words used here:**
- **Open-ended algorithm:** a system meant to keep learning new, interesting behaviors without end.
- **Learning progress:** how fast the agent's success on a task is changing. High progress means the task is at the right difficulty.
- **Model of interestingness (MoI):** a model that judges which tasks are worth doing, here a foundation model.
- **Auto-curriculum:** the system picks its own next training tasks.

## Claim
Learnable is not enough: many learnable tasks are boring (small variants of known tasks). Foundation models already hold human ideas of what is interesting, because humans write about what they find interesting or boring. So a foundation model can act as the interestingness filter ([arXiv abstract](https://arxiv.org/abs/2306.01711)).

## Mechanism
1. Track learning progress for each task, to find tasks at the right difficulty.
2. Give a language model the list of tasks the agent has learned, and ask which candidate tasks are interesting next.
3. Sample training tasks that are both learnable and judged interesting.
- Domains: Crafter (a 2D Minecraft-like game), BabyAI (a 2D grid world with language goals) and AI2-THOR (a 3D home robotics simulator) (PDF p. 3).

## Evidence
- OMNI beats uniform task sampling and learning-progress-only sampling in these domains (abstract, PDF p. 3). We did not copy the per-domain numbers [unverified].
- The tasks are built by the authors; there is no human check that the chosen tasks are truly more interesting (noted by a third-party summary, [deepai](https://deepai.org/publication/omni-open-endedness-via-models-of-human-notions-of-interestingness)) [unverified].

## Limits / what they didn't show
- The interestingness judge is a frozen outside model (GPT-3 or GPT-4 class) [unverified which version per domain]. It never changes, and it is not the learner.
- The taste is human taste, as written in the training data. The paper does not ask whether the model's notion of interesting differs from humans.
- Bounded task lists in game worlds, not an open space.

## Relevance to taste-lab
**Relevance 3.** Section 7, taste and open-endedness.
- **Control stage:** shows a judgment of "interesting" can usefully decide what to learn next. That is the control-over-learning step of our loop ([[Neuromodulators as learning settings]] gives the same idea in brain terms).
- **Divergent test:** OMNI is the opposite of divergent. Its value comes from copying human taste. A self-originated taste must move away from this starting point, as [[Learn to find interesting maths (Patel 2026)]] and [[Models share one taste for text (Zatuchin 2026)]] test in different ways.
- **Anchor:** pairing interestingness with learning progress is a working anchor: the agent cannot chase interesting but impossible tasks.

## Steal this
- The two-filter rule: learnable (learning progress) AND interesting (model judgment).
- "Ask the model what it finds interesting, given what it has already learned" as a prompt pattern for measuring a model's taste.

## Harshit's notes
<!-- yours -->
