---
type: paper
title: "Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in Large Language Models"
status: skimmed
arxiv: 2602.02467
url: https://arxiv.org/abs/2602.02467
authors: Noam Steinmetz Yalon, Ariel Goldstein, Liad Mudrik, Mor Geva
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, evaluation]
tags: [type/paper, section/3, test/grounded, status/skimmed, relevance/3, role/prior-art, metacognition, beliefs, latent-space, consciousness-indicators, causal]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Models can report and control their own activations (Ji-An 2025)]]"]
---
# Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in LLMs (Yalon et al., 2026)

**One line:** Treat beliefs as latent-space representations, define a dominance metric over competing beliefs during generation, and show the HOT-3 chain end to end: manipulation modulates belief formation, belief formation causally drives action selection, and models can monitor and report their own belief states.

## Claim
A key consciousness-indicator from Butlin et al. (2023) - HOT-3, agency guided by belief formation updated by metacognitive monitoring - can be operationalized inside an LLM, and current models show all three links of the chain.

## Mechanism
- Beliefs = representations in latent space that emerge in response to an input; a metric quantifies each belief's dominance during generation.
- Interventions on the input side modulate the internal belief competition; the dominant belief is then shown to *cause* the chosen action.
- Finally the model's own report tracks the internal belief state.

## Evidence
- (1) External manipulations systematically modulate internal belief formation; (2) belief formation causally drives action selection; (3) models monitor and report their own belief states [unverified: tasks, models, effect sizes].

## Limits / what they didn't show
- Framed for the consciousness debate, not for capability: the beliefs are about task content, not about the quality of the model's own work.
- Report-of-belief is still a report; the strength of the controls against input-only probes is unknown [unverified].

## Relevance to taste-lab
This is the missing causal chain for our monitor: an internal state that (a) exists, (b) causes behavior, (c) is reportable. Most monitoring papers show one leg. If valence is a belief-like dominant representation, the same dominance metric gives us a readout of *which* evaluation is driving a choice. Feeds section 3's strongest-evidence cluster alongside [[Models sometimes notice injected thoughts (Lindsey 2025)]].
- Prior-art check: **A partial** (full causal chain for content beliefs; the state is not an evaluation of the work). **B no.**

## Steal this
- The belief-dominance metric over competing internal states - directly reusable to track valence vs correctness signals during generation.
- The three-link experimental structure (modulate, cause, report) as our grounded-test skeleton.

## Kaushik's notes
<!-- yours -->
