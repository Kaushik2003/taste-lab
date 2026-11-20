---
type: paper
title: "LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling"
status: skimmed
arxiv: 2605.14186
url: https://arxiv.org/abs/2605.14186
authors: Qi Cao, Yufan Wang, Peijia Qin, Shuhao Zhang, Pengtao Xie
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/controller, status/skimmed, relevance/3, role/prior-art, question/Q6, metacognition, nelson-narens, feeling-of-knowing, test-time-scaling]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Models know when they are right (Zhang 2025)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Survey of metacognition in language models (Liu 2026)]]", "[[Q6 Can the model read and use its own signal]]"]
---

# LLMs Know When They Know, but Do Not Act on It

**One line:** A model's own "will I know this?" and "did I get it right?" reports carry real signal, but the model does not use them. A harness that turns the reports into retry decisions raises accuracy by about 9 points.

**Why it matters to us:** This is the reasoning-level rung of our control ladder, built directly on Nelson and Narens. It shows the gap between monitoring and control in behavior, not only in probes. It also shows that the control rule is still fitted from outside.

Source: [arXiv 2605.14186](https://arxiv.org/abs/2605.14186) (13 May 2026). Full PDF read for Sections 1 to 4 and the limits appendix through `pdftotext`.

**Words used here:**
- **Feeling of knowing (FOK):** a report, before solving, of how likely the model is to solve the problem.
- **Judgment of learning (JOL):** a report, after an attempt, of how likely that attempt is correct.
- **AUROC:** how well a score ranks right answers above wrong ones. 0.5 is chance, 1.0 is perfect.
- **Calibration error (ECE):** how far stated confidence is from actual accuracy. Lower is better.

## Claim
Models carry usable metacognitive signals but do not act on them by default. A harness that separates monitoring from reasoning and uses these signals to decide when to stop, retry or aggregate improves a fixed model ([abstract](https://arxiv.org/abs/2605.14186)).

## Mechanism
- **Meta level:** the model gives one FOK before solving and one JOL after each attempt. Both are text reports, not hidden states (Sec. 3).
- **Control rule:** for each model, a small classifier (a support vector machine) is trained on 100 labelled "anchor" problems to map (FOK, JOL) to "trust this answer" or "spend more compute" (Sec. 3).
- **Object level:** retry with short metacognitive feedback, or pass several attempts to a final aggregator.

## Evidence
- Fixed Claude Sonnet 4.6, text, code and multimodal benchmarks: pooled accuracy from 48.3 to 56.9, with no weight updates ([abstract](https://arxiv.org/abs/2605.14186)).
- Diagnosis on 100 anchor problems: for Sonnet 4.6, FOK AUROC 0.612, JOL AUROC 0.745, combined 0.757. Gemini 3 Flash ranks well (combined 0.834) but is badly calibrated. Gemma 4 fails on FOK (0.534) (Fig. 3 in the PDF).

## Limits / what they didn't show
- **The control rule is fitted on outside correctness labels.** The model reports, but a researcher-trained classifier decides. This is not self-originated control.
- Works only where the model's reports are good; the main test uses only Sonnet 4.6, the one model that passed every check (limits appendix).
- Text self-reports only. No link to internal states, so it says nothing about the grounded test's causal part.
- Correctness tasks only.

## Relevance to taste-lab
**Relevance 3. Section 3, and Question 6 (can the model read and use its own signal?).**
- It is the behavioral twin of the probe finding in [[Models know when they are right (Zhang 2025)]]: the signal is there, the model does not use it.
- For section 3: monitoring and control can be separated cleanly in Nelson and Narens terms, and the link between them still needs an outside rule.
- It is reasoning-level control only (rung 1 of our ladder). No activation or weight control.

## Steal this
- The FOK and JOL pair as a cheap behavioral baseline next to any probe readout.
- The "diagnosis card" (rank quality and calibration, each pass or fail) as a format for reporting whether a signal is usable for control.

## Harshit's notes
<!-- yours -->
