---
type: paper
title: "Nested Learning: The Illusion of Deep Learning Architectures"
status: skimmed
arxiv: 2512.24695
url: https://arxiv.org/abs/2512.24695
authors: Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni
year: 2025
venue: NeurIPS 2025
relevance: 2
section: 5
tier: skim
tests: [self-reinforcing]
components: [consolidation, controller]
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, component/controller, status/skimmed, relevance/2, question/Q4, role/prior-art, self-referential, continual-learning, multi-timescale, test-time-memory, foundations]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[SRWM - a weight matrix that rewrites itself (Irie 2022)]]", "[[Neuromodulators as learning settings]]", "[[Q4 Can the model edit its own weights]]"]
---

# Nested Learning: a model as nested learners at different speeds

**One line:** The paper treats a model as a stack of learning problems that update at different rates. Its demo model, Hope, makes its own keys, values and learning rates and uses them to update its own memory while it reads. At 760M and 1.3B parameters it beats a Transformer and Titans on language modeling.

Source: [arXiv 2512.24695](https://arxiv.org/abs/2512.24695) (v1 31 Dec 2025; the arXiv comment says a version is published at NeurIPS 2025), [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/116123), [Google Research blog, 7 Nov 2025](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/). HTML read for Sections 7 to 10. This verifies the [unverified] entry in [[Reading list]].

**Words used here:**
- **Nested Learning:** a view in which architecture and optimizer are the same kind of thing: learning problems at different levels, each with its own update rate.
- **Continuum memory system (CMS):** a chain of MLP blocks, each updated at its own frequency. Fast blocks hold short-term memory; slow blocks hold longer-term knowledge (Sec. 7).
- **Titans:** an earlier Google model with a memory that learns at test time. Hope is a variant of Titans.

## Claim
Common optimizers (such as Adam and momentum) can be read as memories that compress gradients. A model whose parts learn at many speeds, and which generates its own update targets, learns continually better than standard models ([arXiv](https://arxiv.org/abs/2512.24695), Abstract).

## Mechanism
1. **Self-referential memory (Sec. 8.1):** keys, values, learning rates and retention gates are produced by memory modules that themselves adapt in context. Each memory makes its own target value from the input and updates toward it with a delta-style rule plus weight decay. Only the query projection is fixed.
2. The starting state of every memory is learned in pre-training and fixed within one context (Sec. 8.1).
3. **Update rates (Sec. 7, 8.2):** each CMS block updates every C steps. Lower-frequency blocks change less often and keep information longer.

## Evidence
- Trained from scratch at 760M parameters (30B tokens) and 1.3B parameters (100B tokens) (Sec. 9.3).
- At 1.3B, Wikipedia perplexity is 14.39 for Hope, 15.60 for Titans and 17.92 for Transformer++. Average common-sense accuracy is 58.04, 56.82 and 53.38 (Table 2).
- In continual text classification and continual translation of two new languages, Hope beats in-context learning and older continual-learning methods. Exact numbers are only in figures (Sec. 9.1).
- Removing any part (including CMS) hurts perplexity or accuracy (Table 6).

## Limits / what they didn't show
- The authors say catastrophic forgetting is "not solved in general" and call the framework a roadmap (Sec. 10).
- Hope still trails Transformers on short in-context recall (Table 3) and uses more memory (Sec. 9).
- All self-changes happen in fast memory within one context. Pre-trained weights are not rewritten by the model.
- The self-made target is a learned function of the input, not an evaluation of good or bad.
- Results are from the authors only; no independent replication found [unverified].

## Relevance to taste-lab
**Relevance 2. Section 5, persistent control. Foundation for the gap "no language model edits its own weights by its own judgment of good and bad"** in `1 Literature review/gaps.md`.
- Like [[SRWM - a weight matrix that rewrites itself (Irie 2022)]], it is self-modification by a learned rule, not by judgment. It is the strongest current language-model example of that kind.
- **Controller link:** the model makes its own learning rate and retention gate per step. That is close to the Doya-style learning-rate knob in [[Neuromodulators as learning settings]], but the signal is not an evaluation.
- **Persist link:** multi-speed memory is a possible answer to "how does a change become permanent": slow blocks consolidate what fast blocks hold. Our loop has no such time-scale design yet.
- Note: a decision on writing this note was open in `TASKS.md` ("in or out"). This note was written at the request of a scout run; Harshit can still mark it out.

## Steal this
- Separate fast and slow memories by update frequency as a frame for the persist step.
- The ablation table as a template for "which part of a self-modifying system carries the gain".

## Harshit's notes
<!-- yours -->
