---
type: landscape
status: draft
cluster: 2
section: 4
tags: [type/landscape, section/4, landscape, valence, value, emotion, persona-vectors, steering, readability]
links: ["[[valence-readout]]", "[[four-taste-tests]]", "[[2026-anthropic-emotion-concepts]]", "[[2026-ferrara-all-quiet-pain]]", "[[2026-jiang-value-axis]]", "[[2026-gao-readability-repe]]", "[[2026-berg-hidden-valence]]", "[[code-quality-signal-T1]]", "[[inference-time-steering-T2]]", "[[landscape-gap-table]]"]
---

# Landscape 2: Evaluation signals: preference, emotion and value representations

**Guiding question:** Does a model carry its own internal "this is good / this is bad" signal that we can read, and does pushing on it change what the model does?

## Timeline
- 2023 · [Linear representations of sentiment](https://arxiv.org/abs/2310.15154) · one direction carries positive vs negative sentiment; ablating it removes 76% of above-chance accuracy on SST.
- 2023 · [Representation Engineering](https://arxiv.org/abs/2310.01405) · contrast pairs plus PCA find directions for honesty, harm and power-seeking, and adding them changes behavior: the "read, then steer" template.
- 2024 · [Scaling Monosemanticity](https://arxiv.org/abs/2605.29358) · SAE features in Claude 3 Sonnet include a general "code error" feature; clamping it makes the model invent or remove a bug (first released 2024, arXiv copy 2026).
- 2025 · [OPENIA](https://arxiv.org/abs/2501.12934) · a probe on code models' hidden states predicts whether their generated code is correct, beating black-box baselines.
- 2025 · [Utility Engineering](https://arxiv.org/abs/2502.08640) · pairwise preferences fit coherent utilities that sharpen with scale; probes recover them from activations in larger models.
- 2025 · [Persona Vectors](https://arxiv.org/abs/2507.21509) · trait directions from a text description; fine-tuning shifts along them track trait change (r = 0.76 to 0.97) and flag bad training data.
- 2026 · [[2026-anthropic-emotion-concepts]] · 171 emotion vectors in Claude Sonnet 4.5; valence predicts and causally shifts stated task preferences.
- 2026 · [Functional welfare axis](https://arxiv.org/abs/2605.30232) · RL on a neutral maze recruits an existing "how am I doing" axis; reward and punishment vectors go from cosine about -0.2 to -0.84/-0.95.
- 2026 · [[2026-gao-readability-repe]] · first readability steering for code (comments, naming, branching), but scored by the model's own judgments, not by running code.
- 2026 · [[2026-jiang-value-axis]] · a "value of my current trajectory" axis in Qwen3-8B separates correct from corrupted code; steering changes backtracking and code length.
- 2026 · [No usable capitulation direction](https://arxiv.org/abs/2609.17550) · a naive probe at AUROC 0.81 drops to 0.58 under proper cross-validation: a warning and a validation protocol.
- 2026 · [[2026-berg-hidden-valence]] · valence in the KV cache alone shifts later choices; the link forms during DPO; models switch off imposed negative states.
- 2026 · [[2026-ferrara-all-quiet-pain]] · open 7 to 32B models can't report an injected emotion state, though a probe decodes it at 98 to 100%.

## Current best result
[[2026-jiang-value-axis]]: one difference-in-means direction in Qwen3-8B, built from synthetic data, reaches AUROC above 0.95 on held-out tasks, separates correct from corrupted LeetCode code (Cohen's d up to 1.05), and causally changes backtracking when steered. DPO raises it for the rewarded behavior (top-rank rate 21% to 36.2%).

## Biggest open problem
Nobody closes the loop. In every paper a human reads the good/bad signal and then injects it at a fixed strength. No paper lets the model use its own readout to pick outputs, set its exploration, or gate what it learns (the nearest case, [[2026-karpf-metacognitive-steering]], uses an outside controller and has only qualitative evidence). It is also untested whether these signals track quality beyond correctness and familiarity, e.g. readability among solutions that all pass.

## Leading groups
- Anthropic and Anthropic Fellows (Jack Lindsey, Isaac Kauvar; fellows Nick Jiang, Runjin Chen): [[2026-jiang-value-axis]], [Persona Vectors](https://arxiv.org/abs/2507.21509), [[2026-anthropic-emotion-concepts]].
- NYU (Andy Q. Han, David Chalmers, Pavel Izmailov): [Functional welfare axis](https://arxiv.org/abs/2605.30232).
- Center for AI Safety (Dan Hendrycks, Mantas Mazeika; Andy Zou's affiliation [unverified]): [Utility Engineering](https://arxiv.org/abs/2502.08640), [RepE](https://arxiv.org/abs/2310.01405).
- Reciprocal Research and University of Warwick (Cameron Berg, Caspar Kaiser): [[2026-berg-hidden-valence]].
- Software-engineering groups in China and the UK (Xiamen, Shenzhen, Xidian, Northumbria; Yifeng Zeng, Shengchao Qin): [[2026-gao-readability-repe]].

## Closest to taste-lab
- **T1** ([[code-quality-signal-T1]]): the value axis already separates correct from broken code, so T1 only adds something if it works *among passing solutions*. High value also goes with shorter code and fewer comments, the same drift seen when confidence is used as a self-reward on code ([[2026-jin-intrinsic-rewards-code]]): the length and comment controls are essential.
- **T2** ([[inference-time-steering-T2]]): [[2026-gao-readability-repe]] already "steers for readability", but with a human-labeled direction and proxy scoring. Run it as a baseline arm; our claim must rest on the model's own signal and on real, tested generations.
- **Controller:** low value or negative welfare reliably causes backtracking and exploration ([[2026-jiang-value-axis]], [welfare axis](https://arxiv.org/abs/2605.30232)). A ready exploration knob for [[neuromodulation-metalearning]].
- **T3** ([[self-training-collapse-T3]]): DPO and RL wire an *existing* valence representation to choice while the vector barely moves (cosine near 1 across OLMo checkpoints). Training may change how valence is used more than what it values, which threatens the "drift from origin" claim.
- **Model choice:** valence steering failed in Qwen3-32B and Gemma-3-27B ([[2026-berg-hidden-valence]]) and in Qwen/Gemma in [Nine Emotion Centroids](https://arxiv.org/abs/2608.18090), yet worked in Qwen3-8B for value. Check steerability before committing.

## Reading order for Harshit
1. **must-read** · [[2026-jiang-value-axis]] · our closest evaluator. Read Sec. 2.1 (how the axis is built), 3.1 to 3.2 (code results and steering on LeetCode), 4 (DPO).
2. **must-read** · [[2026-gao-readability-repe]] · direct overlap with T2. Read Sec. III and V, and notice they never run the generated code.
3. **must-read** · [[2026-berg-hidden-valence]] · a test design for "grounded" and the nearest thing to a model controlling its own valence. Read the fixed-text design, the OLMo checkpoint figure, and the self-steering section.
4. **skim** · [Functional welfare axis](https://arxiv.org/abs/2605.30232) · the "recruited, not created" argument; matters for T3.
5. **skim** · [Persona Vectors](https://arxiv.org/abs/2507.21509) · the training-data screening section: the closest existing case of an internal signal gating what gets learned.
6. **skim** · [No usable capitulation direction](https://arxiv.org/abs/2609.17550) · the validation protocol (question-level CV, shuffled labels, positive control). Copy it for the T1 probe.
