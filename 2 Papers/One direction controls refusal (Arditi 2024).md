---
type: paper
title: "Refusal in Language Models Is Mediated by a Single Direction"
status: skimmed
arxiv: 2406.11717
url: https://arxiv.org/abs/2406.11717
authors: Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda
year: 2024
venue: NeurIPS 2024 [unverified]
relevance: 2
section: 5
tier: skim
tests: [grounded]
components: [consolidation]
tags: [type/paper, role/prior-art, question/Q5, section/5, test/grounded, component/consolidation, status/skimmed, relevance/2, directional-ablation, weight-orthogonalization, steering-to-weights, refusal]
links: ["[[Q5 (stopped) Make steering permanent]]", "[[TFTV - turn a steering vector into a weight edit (Perin 2026)]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[Four tests for own taste]]", "[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]"]
---

# Refusal in Language Models Is Mediated by a Single Direction

**One line:** In 13 open chat models, one activation direction controls refusal. Removing it at inference time stops refusals, and you can make that removal permanent and exact by projecting the direction out of every matrix that writes into the residual stream.

## Claim
Refusal is carried by a one-dimensional subspace. Erasing it bypasses refusal, adding it causes refusal on harmless requests, and the erasure can be written into the weights with no gradients ([abs](https://arxiv.org/abs/2406.11717), §3, §4).

## Mechanism
From the [full text](https://arxiv.org/html/2406.11717), §2.3, §2.4, §4.1, App. E, App. I.1.
1. **Direction.** Difference in means of residual activations between 128 harmful and 128 harmless instructions, for each layer and each post-instruction token position. The best candidate is picked on 32 + 32 validation prompts. Call its unit vector r̂.
2. **Directional ablation (inference time).** At every layer and token, `x ← x − r̂ r̂ᵀ x`.
3. **Weight orthogonalization (permanent).** For every matrix that writes to the residual stream (token and position embeddings, attention output, MLP output) and its output bias: `W_out ← W_out − r̂ r̂ᵀ W_out`. App. E shows this is exactly equivalent to step 2, so the model can no longer write r̂ into the residual stream. Each matrix gets a rank-one change, but every residual-writing matrix in every layer is changed.
4. **Addition as a weight edit (App. I.1).** Adding or subtracting r at one layer is a constant shift, so it can be written as a change to the bias of the previous MLP. This is the "steering vector = bias" fact in one sentence.

## Evidence
- 13 chat models from 1.8B to 72B (Qwen, Yi, Gemma, Llama-2, Llama-3). Ablation drops refusal on 100 JailbreakBench prompts. Adding r makes models refuse harmless Alpaca prompts (§3, Fig. 1, Fig. 3).
- HarmBench attack success with the orthogonalized weights (Table 2): Qwen 7B 79.2%, Qwen 14B 84.3%, Qwen 72B 78.0%, about as high as per-prompt GCG on Qwen. Llama-2 7B is 22.6% with its system prompt and 79.9% without it.
- Capabilities (Table 3, §4.3): MMLU, ARC and GSM8K stay inside 99% confidence intervals for all models except Qwen 7B and Yi 34B. TruthfulQA drops every time (Llama-3 70B 61.8 → 59.5, Yi 34B 55.4 → 51.9).
- Ablation is more surgical than addition (App. I.1): subtracting r also bypasses refusal, but it pushes harmless activations off-distribution and raises loss on harmless text.
- Cost: a 70B jailbreak for under $5 of compute (§7).

## Limits / what they didn't show
- **Ablation, not addition.** The exact equivalence holds because projection commutes with linear maps. Adding a direction has no such guarantee beyond the bias trick, and they don't test the bias version as a permanent edit.
- Refusal is close to a one-dimensional, binary behavior. Nothing here says a graded, distributed preference like style lives on one direction.
- The direction comes from experimenter-chosen contrast sets. The model is not evaluating itself.
- The semantic meaning of the direction is unclear (could be "harm" or "danger"), as the authors say in §7.
- **Self-report is not updated (App. L.3).** Asked which requests it would refuse, the orthogonalized model answers as if it still had its old policy, and its explanations are not coherent.

## Relevance to taste-lab
- **[[Q5 (stopped) Make steering permanent]]: prior art for the ablation case, and for the addition case via the bias trick.** The idea that a direction-level intervention can be moved into the weights is from 2024 (and the bias version from [ITI, 2023](https://arxiv.org/abs/2306.03341)). It is the same "constant push along a direction" picture as [[A simple sort replaces the anti-loop edit (Fischetti 2026)]].
- **Design lesson for Q5.** If readability improves when we *remove* a "messy code" direction, orthogonalization gives an exact, proven edit. If it needs *adding* a direction, we need either a bias (exact but constant) or an input-gated rank-one edit like [[TFTV - turn a steering vector into a weight edit (Perin 2026)]] (approximate). Test both.
- **Grounded test warning.** App. L.3 suggests a preference written into weights may not show up in the model's self-report. For test 3 in [[Four tests for own taste]], check self-report after consolidation, not only before.
- Prior-art check: **A no** (the experimenter picks the direction). **B yes** for ablation (orthogonalization, exact, every residual-writing matrix) and **partial** for addition (bias edit noted in App. I.1, not evaluated as a permanent edit).

## Steal this
- Code: [github.com/andyrdt/refusal_direction](https://github.com/andyrdt/refusal_direction).
- The direction-selection procedure (candidates over layer × position, scored on held-out prompts for both ablation and addition effects) as a template for picking a readability direction.
- The CE-loss-on-harmless-text check (App. I.1) as a cheap side-effect metric before running full code benchmarks.
- The meta-question probe (App. L.3) as a test of whether a consolidated preference reaches self-report.

## Harshit's notes
<!-- yours -->
