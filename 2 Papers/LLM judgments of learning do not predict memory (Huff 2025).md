---
type: paper
title: "Judgments of Learning Distinguish Humans from Large Language Models in Predicting Memory"
status: skimmed
arxiv: 2410.13392
url: https://doi.org/10.1038/s41598-025-22290-x
authors: Markus Huff, Elanur Ulakci
year: 2025
venue: Scientific Reports
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/2, role/prior-art, judgment-of-learning, human-comparison, memory]
links: ["[[Models mostly know what they know (Kadavath 2022)]]", "[[Both sides of a debate think they will win (Prasad 2025)]]", "[[Do models know how much they know (Prato 2024)]]"]
---

# Judgments of Learning Distinguish Humans from LLMs

**One line:** On a classic metacognitive task - predicting whether you will remember a sentence later - human judgments of learning reliably predict actual memory, and none of the tested LLMs' do.

**Why it matters to us:** A clean, peer-reviewed failure case using one of psychology's standard instruments (JOL). It bounds what verbal metacognitive reports can do on memory-style tasks and gives section 3 a canonical human-vs-model contrast with a proper paradigm behind it.

Source: [Scientific Reports](https://doi.org/10.1038/s41598-025-22290-x) (2025); arXiv preprint [2410.13392](https://arxiv.org/abs/2410.13392) (2024). Abstract-level note.

## Claim
Human judgments of learning (JOL) predict subsequent memory performance; LLM JOL-style predictions do not, on a garden-path sentence paradigm manipulating contextual fit ([abstract](https://doi.org/10.1038/s41598-025-22290-x)).

## Mechanism
- Cross-agent prediction model: humans and ChatGPT-based LLMs give JOLs for sentence pairs (one garden-path), with contextual fit (fitting vs unfitting) manipulated to probe intrinsic cues (relatedness).

## Evidence
- Human JOL reliably predicted actual memory; none of the tested LLMs' JOL did ([abstract](https://doi.org/10.1038/s41598-025-22290-x)).

## Limits / what they didn't show
- ChatGPT-family models only; reasoning models untested.
- Memory prediction is one metacognitive subtask; says nothing about confidence in reasoning or code.
- Verbal reports only, no internal readout - the LLM failure could reflect the report channel, not the absence of an internal signal.

## Relevance to taste-lab
**Relevance 2. Section 3.**
- The peer-reviewed anchor for "verbal self-prediction is unreliable in models": complements Prasad (adversarial) and Singh (input-only artifacts) with a standard cognitive paradigm.
- The garden-path/contextual-fit manipulation is a clever confound control worth copying: it tests whether the judgment tracks the right causal variable.

## Steal this
- The cross-agent prediction design: same items, same instructions, humans vs models, prediction checked against ground truth.

## Kaushik's notes
<!-- yours -->
