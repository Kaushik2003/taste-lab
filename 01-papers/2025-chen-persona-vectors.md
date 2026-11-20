---
type: paper
title: "Persona Vectors: Monitoring and Controlling Character Traits in Language Models"
status: skimmed
arxiv: 2507.21509
url: https://arxiv.org/abs/2507.21509
authors: Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, Jack Lindsey (Anthropic Fellows / UT Austin / Constellation / Truthful AI / UC Berkeley / Anthropic)
year: 2025
venue: preprint
relevance: 3
section: 5
tier: deep
tests: []
components: [monitoring, controller]
tags: [type/paper, section/5, component/monitoring, component/controller, status/skimmed, relevance/3, persona-vectors, steering, finetuning, trait-drift]
links: ["[[2024-arditi-refusal-direction]]", "[[2026-berg-hidden-valence]]", "[[landscape-persistent-control]]"]
---

# Persona Vectors (Chen, Arditi, et al.)

**One line:** Automated extraction of activation-space directions for character traits (evil, sycophancy, hallucination propensity) from a natural-language description alone; the vectors monitor personality fluctuation at deployment, predict and control trait shifts during finetuning, and flag training data that will produce undesirable changes.

## Claim
High-level traits correspond to steerable directions; finetuning shifts (intended and unintended) are strongly correlated with movement along the relevant persona vector, and can be mitigated post-hoc or prevented during training ([abs](https://arxiv.org/abs/2507.21509), [code](https://github.com/safety-research/persona_vectors)).

## Mechanism
- Automated pipeline: trait description -> contrastive prompts -> persona vector.
- Deployment monitoring of trait expression; post-hoc steering; "preventative steering": add the vector during finetuning so the optimizer never encodes the trait in weights, remove it at evaluation.
- Data flagging at dataset and sample level by projecting candidate data onto the vector.

## Evidence
Strong correlation between finetuning trait shifts and vector movement; mitigation and prevention demonstrated [unverified: numbers not extracted]. See the independent audit: [[2026-tang-persona-steering-audit]].

## Limits / what they didn't show
- Traits are safety-relevant dispositions, not quality judgments: "evil" is a trait, "good code" is an evaluation. Whether the same pipeline extracts a taste vector is open.
- Preventative steering is the T4-adjacent move (control what's written into weights during training) but done by an external engineer, not the model.

## Relevance to taste-lab
**The closest existing method to a taste readout + the training-time control story.** If their pipeline works for "evil given a description", it may work for "readable code" or "elegant" - that is a concrete exp01 variant. Preventative steering is also the strongest existing "control what persists into weights" mechanism, the T4 thread done externally.
- Prior-art check: **A partial** (monitors and controls trait directions, external operator). **B partial** (preventative steering shapes what training writes into weights - the strongest prior-art hit on T4 so far; difference: external, trait-level, single direction).

## Steal this
- The automated trait-description -> vector pipeline as the extraction method for a taste vector.
- Data flagging by projection: score candidate self-training data against the valence direction before training on it.

## Kaushik's notes
<!-- yours -->
