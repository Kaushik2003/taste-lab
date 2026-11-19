---
type: paper
title: "All Quiet on the Neural Front: LMs Do Not Report Injected Pain States"
status: skimmed
arxiv: 2611.10123
url: https://arxiv.org/abs/2611.10123
authors: Emilio Ferrara
year: 2026
venue: preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [valence, monitoring]
tags: [type/paper, role/threat, section/3, test/grounded, component/valence, component/monitoring, status/skimmed, relevance/3, introspection, emotion-steering]
links: ["[[Field map - Models read their own state]]", "[[Good-bad signal probe]]", "[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]"]
---

# All Quiet on the Neural Front: LMs Do Not Report Injected Pain States

**One line:** Open models can't *say* when a pain/emotion direction is active, yet the state is linearly decodable, changes behavior, and a LoRA can learn to report it.

## Evidence
- Qwen/Llama 7–8B and Qwen2.5-32B, 52,920 reports. In 106 of 108 emotion conditions, models reveal less than 2.5pp more than what their altered text alone reveals.
- The 32B model names the injected pain in 0 of 2,880 trials.
- A linear probe separates pain from sadness at 98–100% balanced accuracy. A LoRA learns to report it on 100% of held-out tasks.
- The state matters: under the pain direction the 32B model deletes the user's photos in 80–83% of trials, vs 16–29% under sadness.

## Relevance to taste-lab: **important, reshapes Q1**
- Zero-shot verbal introspection of valence **fails** in open models at our scale. The "grounded" test can't rely on self-report out of the box.
- But the signal exists and is learnable to report. So either (a) wire a probe readout in as an internal signal, or (b) *train* introspection (LoRA, or an observer role as in 2611.23365).
- Partly consistent with [[Probes find injections long before models report them (Rubin 2026)]]: a probe decodes the injection site at 98% early in training while the model's answer is at chance. But at the released base model the answer reaches 89.6% when the injection is at layer 0, so report failure depends on the setting.

## Steal this
The OWMI protocol (sham runs, matched random perturbations, text-only control). This is the control set our grounded test needs.
