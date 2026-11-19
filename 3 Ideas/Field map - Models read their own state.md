---
type: landscape
status: draft
cluster: 1
section: 3
tags: [type/landscape, section/3, landscape, metacognition, introspection, monitoring, control, confidence]
links: ["[[Metacognition - watch and control yourself]]", "[[Four tests for own taste]]", "[[Models do not report injected pain (Ferrara 2026)]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Models know when they are right (Zhang 2025)]]", "[[Outside controller steers thinking modes (Karpf 2026)]]", "[[Q1 Does the model sense code quality]]", "[[Q2 Can the model steer its own code]]", "[[Good-bad signal probe]]", "[[Gaps in the field]]"]
---

# Landscape 1: Metacognitive monitoring and introspection

**Guiding question:** Can a model read its own internal state, and can it use that reading to change how it reasons while it is reasoning?

## Timeline
- 1979 · [[Metacognition - watch and control yourself]] · Flavell: people know things about their own thinking and use that knowledge to regulate it.
- 1990 · [[Metacognition - watch and control yourself]] · Nelson & Narens: a meta level reads the object level (monitoring) and sends changes back down (control).
- 2017 · [[Metacognition - watch and control yourself]] · Fleming & Daw: confidence is a second-order inference about one's own decision, so it can come apart from task performance.
- 2022 · [Kadavath et al.](https://arxiv.org/abs/2207.05221) · Large models are fairly calibrated when asked if their own answer is true, and can be trained to predict "I know this" before answering; transfer to new tasks is weaker.
- 2024 · [Binder et al.](https://arxiv.org/abs/2410.13787) (ICLR 2025) · A model trained to predict its own behavior beats a second model trained on the same behavior data, but only on simple tasks.
- 2025 · [[Models know when they are right (Zhang 2025)]] · A probe on reasoning-model hidden states reads whether each intermediate answer is right; stopping on it saves about 24% of tokens at equal accuracy.
- 2025 · [Ji-An et al.](https://arxiv.org/abs/2505.13763) (NeurIPS 2025) · Neurofeedback: from in-context examples, models report and shift chosen activation directions, but only inside a small "metacognitive space".
- 2026-01 · [Lindsey](https://arxiv.org/abs/2601.01828) · Concept injection: Claude Opus 4.1 notices and names an injected concept in about 20% of trials at the best layer, with 0 false positives on controls.
- 2026-05 · [[Introspection claims fail basic checks (Singh 2026)]] (COLM 2026) · Input-only probes match the neurofeedback self-reports, and injection "detection" also fires when only the prompt was manipulated.
- 2026-09 · [Aoki et al.](https://arxiv.org/abs/2609.00904) · Neurofeedback redone so the target can't be guessed from the text: control effects are small (all d < 0.5) and inconsistent across models.
- 2026-09 · [[Outside controller steers thinking modes (Karpf 2026)]] · An outside controller reads a frozen 1T model's residual stream, picks a thinking regime, and adds steering vectors learned from scientists' corrections. Qualitative results only.
- 2026-09 · [MetaCtrl](https://arxiv.org/abs/2609.37304) · A separate 4B controller, trained with RL, reads the reasoning text and tells a frozen reasoner to continue, shorten, skip or stop: +5.7 points with 47% fewer tokens on R1-Distill-Qwen-7B (Table 1).
- 2026-11 · [[Probes find injections long before models report them (Rubin 2026)]] + [[Models do not report injected pain (Ferrara 2026)]] · A linear probe reads injected states at 98 to 100%. In Rubin, the model's own answer is at chance early in training but reaches 89.6% at the released base model (injection at layer 0); in Ferrara, open models never name the pain state.
- 2026-11 · [Wang et al.](https://arxiv.org/abs/2611.23365) · A trained "observer" role inside the same model answers questions about the assistant's behavior with mean AUROC 0.907, above activation oracles at 0.796 (abstract).

## Current best result
Reading plus acting: an external probe on R1-Distill-Llama-8B hidden states stops reasoning on MATH at 88.2% accuracy (same as no exit) with about 24% fewer tokens ([[Models know when they are right (Zhang 2025)]], Section 5). Best self-report: a trained observer role in Qwen3.6-27B reaches 0.907 mean AUROC on five held-out oversight tests ([2611.23365](https://arxiv.org/abs/2611.23365)). Best control gain, MetaCtrl's +5.7 points at 47% fewer tokens, comes from a controller that reads text, not internal state ([2609.37304](https://arxiv.org/abs/2609.37304)).

## Biggest open problem
Every loop that works today puts the "reader" outside the model: a probe, a second network, or a trained adapter. When tests rule out input cues, in-context self-report matches input-only probes ([2605.26242](https://arxiv.org/abs/2605.26242)) and in-context self-control mostly disappears ([2609.00904](https://arxiv.org/abs/2609.00904)). No one has yet shown a model using a privileged reading of its own state to improve its reasoning.

## Leading groups
- Anthropic interpretability [unverified for Gurnee et al.]: Jack Lindsey, Wes Gurnee. [Lindsey 2601.01828](https://arxiv.org/abs/2601.01828); the "J-space" workspace paper [2607.15495](https://arxiv.org/abs/2607.15495).
- NYU, Linzen and Ravfogel [affiliations unverified]: the skeptical side. [[Introspection claims fail basic checks (Singh 2026)]].
- NYU and NYU Shanghai, He He's group: probing reasoning models for self-verification. [[Models know when they are right (Zhang 2025)]].
- Ji-An Li, Marcelo Mattar, Marcus Benna [UCSD/NYU unverified]: neurofeedback paradigm, now also confidence in thinking models. [2505.13763](https://arxiv.org/abs/2505.13763), [2607.26845](https://arxiv.org/abs/2607.26845).
- David Bau's group [Northeastern unverified], with David Atkinson: when self-reports of learned preferences become faithful, and how to train them without causal bypass. [2610.07186](https://arxiv.org/abs/2610.07186), [2610.38911](https://arxiv.org/abs/2610.38911).

## Closest to taste-lab
- **Q2 prior art, and a name clash:** [[Outside controller steers thinking modes (Karpf 2026)]] has the same loop shape as [[Q2 Can the model steer its own code]] (read internal state, pick a control, add layer-specific vectors). It differs: its directions come from human scientists, the reader is an external controller, there is no valence, and there are no numbers. Cite it and state the difference.
- **Q2 baseline and warning:** [[Models know when they are right (Zhang 2025)]] is the working template (internal signal, external probe, early exit). [Kirin 2607.18553](https://arxiv.org/abs/2607.18553) found a correctness probe helped rank finished answers, but steering, branching and LoRA driven by it gave no gain. So Q2's best-of-n arm has more support than its steering arm.
- **Grounded test (Q1):** [[Introspection claims fail basic checks (Singh 2026)]] means every "report matches probe" claim needs an input-only (layer-0) probe baseline. Code readability is visible in the text, so this control matters more for us than for injected states.
- **Grounded test path:** [Atkinson et al. 2610.07186](https://arxiv.org/abs/2610.07186) got faithful self-reports of LoRA-learned preferences without training the report, in Qwen3-32B only, as the preference moved to earlier layers. This is the nearest template for "the model can say what it prefers".
- **Code-specific monitoring:** hidden states predict code correctness at 0.90 AUROC on LiveCodeBench ([2609.13975](https://arxiv.org/abs/2609.13975), abstract). In Q1, correctness is fixed by tests, so a valence readout must add something beyond this. See also cluster 2's [[Value axis - model knows it is on track (Jiang 2026)]].

## Reading order for Harshit
1. **must-read** · [[Introspection claims fail basic checks (Singh 2026)]] · Section 3 (the two conditions) and the injection results with the "gaslight" control. It sets the bar our grounded test has to meet.
2. **must-read** · [[Models know when they are right (Zhang 2025)]] · Probe setup and Section 5 (early exit). This is the simplest monitor-to-control loop, and Q2 has to beat it.
3. **must-read** · [[Outside controller steers thinking modes (Karpf 2026)]] · Section 3.3 only (the closed loop). This is the closest prior art to Q2; know exactly where we differ.
4. **skim** · [Ji-An et al. 2505.13763](https://arxiv.org/abs/2505.13763) then [Aoki et al. 2609.00904](https://arxiv.org/abs/2609.00904) Section 5 · Read the neurofeedback claim, then see why it weakens when the target is privileged.
5. **skim** · [Atkinson et al. 2610.07186](https://arxiv.org/abs/2610.07186) · Sections 4 and 5: when a model's report of its own learned preference becomes faithful.
6. **skim** · [Kirin 2607.18553](https://arxiv.org/abs/2607.18553) · The list of failed uses of the probe (steering, branching, LoRA). These are failure modes to plan for in Q2.
