---
type: paper
title: "Generalization of Fine-Tuned Uncertainty Communication and Metacognition in Large Language Models"
status: skimmed
arxiv: 2510.05126
url: https://arxiv.org/abs/2510.05126
authors: Mark Steyvers, Catarina Belem, Padhraic Smyth
year: 2025
venue: arXiv preprint
relevance: 2
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, status/skimmed, relevance/2, role/prior-art, metacognition, uncertainty, calibration, fine-tuning, generalization]
links: ["[[Models mostly know what they know (Kadavath 2022)]]", "[[Trained confidence tracks consistency, not accuracy (Yax 2026)]]", "[[Field map - Models read their own state]]"]
---
# Generalization of Fine-Tuned Uncertainty Communication and Metacognition in LLMs (Steyvers et al., 2025)

**One line:** Fine-tune models to report calibrated confidence (single-question estimates and pairwise "which am I more likely to get right"), and the gains transfer to held-out domains - medical, legal, truthfulness benchmarks - not just the training distribution.

## Claim
Uncertainty communication is trainable and the trained ability generalizes across domains and formats, so it is a real metacognitive skill rather than memorized calibration.

## Mechanism
- Supervised fine-tuning on general-knowledge, math and open-ended trivia with confidence targets.
- Two report formats tested: numeric confidence for one answer, and pairwise comparison of two questions.
- Evaluated on calibration, discrimination and accuracy, in and out of domain.

## Evidence
- Stated confidence is often poorly aligned with correctness before training; fine-tuning improves calibration and discrimination, with transfer to new domains [unverified: sizes].

## Limits / what they didn't show
- The signal is answer correctness; nothing about quality judgments beyond correctness.
- Trained report - by our lights this is a readout bolted on, not an architecture that develops monitoring.

## Relevance to taste-lab
Supports the trained-reportability wave section 3 predicts, with the generalization result [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] partially complicates: transfer across domains is evidence against a pure consistency readout. Also a design option: a trained pairwise-comparison head ("which of these two candidates is better") is exactly the evaluate step's cheapest form.
- Prior-art check: **A partial** (calibrated self-evaluation of correctness, trained). **B no.**

## Steal this
- Pairwise confidence comparison as the format for a taste readout - comparisons are easier to make calibrated than absolute scores.

## Kaushik's notes
<!-- yours -->
