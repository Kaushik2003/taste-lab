---
type: paper
title: "Open-Endedness is Essential for Artificial Superhuman Intelligence"
status: skimmed
arxiv: 2406.04268
url: https://arxiv.org/abs/2406.04268
authors: Edward Hughes, Michael Dennis, Jack Parker-Holder, Feryal Behbahani, Aditi Mavalankar, Yuge Shi, Tom Schaul, Tim Rocktäschel
year: 2024
venue: ICML 2024 (position paper) [unverified venue]
relevance: 3
section: 7
tier: deep
tests: [divergent, self-reinforcing]
components: [anchor]
tags: [type/paper, section/7, test/divergent, test/self-reinforcing, component/anchor, status/skimmed, relevance/3, role/prior-art, open-endedness, novelty, learnability, position-paper]
links: ["[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[OMNI - models judge which tasks are interesting (Zhang 2023)]]", "[[Anchor against collapse]]", "[[Training on own outputs erases rare data (Shumailov 2024)]]"]
---

# Open-Endedness is Essential for Artificial Superhuman Intelligence

**One line:** A system is open-ended, for a given observer, if what it makes keeps getting harder to predict (novel) but becomes easier to predict as the observer sees more of it (learnable).

**Why it matters to us:** It gives a formal, testable definition that fits our self-reinforcing test: a taste that sharpens without collapse should keep producing work that is novel and learnable, not repetitive (collapse) and not random (noise).

Source: [arXiv 2406.04268](https://arxiv.org/abs/2406.04268) (v1 6 Jun 2024). HTML read for Sections 1 and 2. Position paper.

**Words used here:**
- **Artifact:** anything the system produces, such as a design, a program or a proof.
- **Observer:** whoever judges the artifacts, with their own predictive model and their own measure of error.
- **Novel:** artifacts become less predictable for the observer's model over time.
- **Learnable:** seeing a longer history of artifacts makes new ones more predictable.
- **Noisy TV:** a source of pure random noise. It is learnable at first but stops being novel once the observer models the noise.

## Claim
1. Open-endedness can be defined formally as novelty plus learnability to an observer (Sec. 2.1).
2. Open-endedness is essential for any artificial superhuman intelligence.
3. Foundation models now make open-ended systems possible, but such systems raise safety issues (abstract).

## Mechanism
- An observer has a statistical model that predicts the next artifact from past ones, and a loss that scores the prediction.
- **Novelty:** expected loss on future artifacts rises over time, for a fixed observer model.
- **Learnability:** expected loss falls when the observer conditions on a longer history.
- Open-ended means both hold (Sec. 2.1).
- **"Interesting" is not a separate term:** it lives in the observer's choice of loss, that is, which features the observer cares to predict. Different observers find different things interesting (Sec. 2.1).

## Evidence
- A position paper: arguments and examples (AlphaGo, adaptive agents, self-improving language models), no new experiments.

## Limits / what they didn't show
- Open-endedness is always relative to an observer. For "self-originated taste", the observer would be the model itself, which the paper does not discuss.
- Hard to measure in practice: one needs a trained observer model over time.
- Says nothing about how to keep a system open-ended in the long run.

## Relevance to taste-lab
**Relevance 3.** Section 7, and a definition the review can use for the self-reinforcing test ([[Four tests for own taste]]).
- **Self-reinforcing without collapse = novel and learnable.** Collapse ([[Training on own outputs erases rare data (Shumailov 2024)]]) fails novelty: outputs become predictable. Pure noise fails learnability. This gives the review a crisp test.
- **Observer-relative taste:** "interesting = what the observer chooses to predict". A model's taste could be defined as its own choice of loss. That is a useful framing for section 7 [our interpretation, not the paper's].
- **Divergent test:** if the observer is a human, the system must stay human-relevant. A taste that diverges too far may stop being learnable to humans. This is a real tension for the divergent test.

## Steal this
- The novelty + learnability definition as the review's working definition of open-endedness.
- The noisy-TV example to explain why diversity alone is not a sign of healthy self-training.

## Harshit's notes
<!-- yours -->
