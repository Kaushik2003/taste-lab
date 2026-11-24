---
type: paper
title: "Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation"
status: skimmed
arxiv: 2608.20569
url: https://arxiv.org/abs/2608.20569
authors: Emilio Ferrara
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, role/threat, introspection, self-report]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Refusal hides a real injection-detection ability (Macar 2026)]]", "[[2026-11-23 gap check]]"]
---
# Open-Weight Masked Introspection (Ferrara 2026)

**One line:** Eight open models (0.5B to 15B) cannot say whether their own hidden states were changed: their yes/no reports are at chance. But the information is in their activations, and a fine-tuned model reports it almost perfectly.

Read 2026-11-24: abstract, introduction, framework (Sec. 3), discussion, limitations, conclusion. Results tables not read.

## Mechanism
Take a normal benchmark item, change one internal object (a residual-stream site, an attention head or a sparse-autoencoder feature), then ask the model what changed. Three controls: sham runs with no change; random changes matched for how much they disturb the output; a text-only observer that sees only the visible output (Sec. 3.4).

## Evidence
- Over 78,000 measurements; pooled over 11,216 paired trials, report discrimination is AUROC of about 0.5007, and an equivalence test bounds the advantage below 0.15 percentage points (Abstract, Sec. 1).
- A linear probe on the same activations recovers the change at 95.8% and 75.0% held-out accuracy in the two dose-calibrated models (chance 50%), with no held-out error at later layers (Sec. 1, Sec. 8).
- A model fine-tuned to report this kind of change reaches AUROC of about 1.0 on held-out directions (Sec. 1).
- In Qwen2.5-7B-Instruct the yes/no answer never varies, but the confidence attached to it separates change from sham at AUROC 0.647 (Sec. 1, Sec. 10).

## Limits (authors, Sec. 9)
- Changes are to **activations during one run, not to weights**.
- Models of 0.5B to 15B only. Larger and closed models are open.
- Mostly one residual site and immediate questions; delayed and spontaneous tracks are thin.

## Relevance to taste-lab
The cleanest statement of "the signal is there, the report is not". For the question "does a model notice its own weight edit": this is the nearest negative evidence, but it does not test weight edits or models above 15B. The opposite result at 27B is in [[Refusal hides a real injection-detection ability (Macar 2026)]]. The confidence result suggests measuring a graded confidence, not only a yes/no report.
