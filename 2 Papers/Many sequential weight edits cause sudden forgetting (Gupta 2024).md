---
type: paper
title: "Model Editing at Scale leads to Gradual and Catastrophic Forgetting"
status: skimmed
arxiv: 2401.07453
url: https://arxiv.org/abs/2401.07453
authors: Akshat Gupta, Anurag Rao, Gopala Anumanchipalli
year: 2024
venue: arXiv preprint [unverified: later venue]
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [consolidation, anchor]
tags: [type/paper, section/6, test/self-reinforcing, component/consolidation, status/skimmed, relevance/3, role/threat, model-editing, forgetting]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Models that change their own weights]]", "[[A few edits can collapse a model (Yang 2024)]]", "[[2026-11-23 gap check]]"]
---
# Model editing at scale leads to gradual and catastrophic forgetting (Gupta 2024)

**One line:** When the direct weight editors ROME and MEMIT make many edits one after another to the same model, the model forgets: first slowly, then suddenly.

## Claim
Model editing must be judged by many edits to one model, not one edit at a time.

## Mechanism
Sequential fact edits with ROME and MEMIT (closed-form, localized weight edits; no gradient training loop). Track earlier edits and downstream tasks as edits pile up.

## Evidence (abstract)
- The model keeps forgetting earlier edits and loses downstream task ability as edits accumulate.
- Two phases: gradual, progressive forgetting, then abrupt catastrophic forgetting. The second phase caps how many edits are possible.

## Limits
- Fact edits, not behavior or style edits. Older editors; later methods claim to fix this (for example r-ROME, arXiv 2403.07175, and a 2026 spectral method tested up to 20,000 edits, arXiv 2601.11042) [abstract only].

## Relevance to taste-lab
The main prior art and threat for gap point 1 (repeated self-edits). Repeated direct edits are known to break models. A self-editing loop needs a stop or rollback rule and a cheap health signal after each edit (see [[A few edits can collapse a model (Yang 2024)]]: perplexity).
