---
type: paper
title: "ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models"
status: skimmed
arxiv: 2503.22048
url: https://arxiv.org/abs/2503.22048
authors: Chung-En Sun, Ge Yan, Tsui-Wei Weng
year: 2025
venue: EMNLP 2025
relevance: 2
section: 5
tier: skim
tests: [grounded]
components: [consolidation, monitoring]
tags: [type/paper, role/prior-art, question/Q5, section/5, test/grounded, component/consolidation, component/monitoring, status/skimmed, relevance/2, steering-to-weights, directional-ablation, reasoning-length, attention-heads, reasoning-models]
links: ["[[Q5 (stopped) Make steering permanent]]", "[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[Steer2Edit - steering into small weight edits (Sun 2026)]]", "[[One direction controls refusal (Arditi 2024)]]", "[[TFTV - turn a steering vector into a weight edit (Perin 2026)]]", "[[Metacognition - watch and control yourself]]"]
---

# ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models

**One line:** In R1-distilled reasoning models, "how long to think" is a linear direction. Steering along it changes CoT length, and projecting that direction out of the output weights of about 4% of attention heads (about 0.2% of parameters) makes the change permanent and lifts math accuracy, mostly on the problems the model used to under-think.

## Claim
Reasoning length is linearly represented in the residual stream, a small set of attention heads drives the "too short" end of it, and a closed-form weight edit on just those heads fixes overly short reasoning with no training ([abs](https://arxiv.org/abs/2503.22048)).

## Mechanism
From the [full text](https://arxiv.org/html/2503.22048).
1. **Direction.** Generate CoT on 2,000 GSM8K training problems. Split into long (CoT > 1000 tokens) and short (< 100 tokens). For each layer, average the post-attention and post-MLP residual activations over CoT tokens, then over problems. Direction v = mean(long) minus mean(short), per layer and per sublayer.
2. **Steering check.** Add α·v at every layer, α in [-0.08, 0.08]. Positive α lengthens CoT, negative shortens it. Middle layers matter most in a one-layer-at-a-time scan.
3. **Head selection.** For each head, take its output contribution (attention output times its slice of W_o), average it over CoT tokens of short-reasoning examples, and project onto the short-reasoning direction (-v̂). Keep the top 4% of heads by that score.
4. **Edit.** For each selected head, W_o ← W_o (I − v̂ v̂ᵀ). The head can no longer write anything along the length direction. This is directional ablation (as in [[One direction controls refusal (Arditi 2024)]]) restricted to a few heads, not an additive push.

## Evidence
Models: DeepSeek-R1-distill Qwen-1.5B, Llama3-8B, Qwen-14B (main), Qwen-32B (App. A.5). Five math sets: GSM8K, MMLU elementary math, MATH-L1, MATH-L5, MATH-500 (Table 1).
- **Overall accuracy.** Llama3-8B GSM8K 82.26 → 89.44. Qwen-1.5B MMLU elementary math 68.52 → 90.66. Qwen-14B GSM8K 90.80 → 93.78. Hard sets barely move (Qwen-14B MATH-500 91.48 → 91.92; Qwen-1.5B MATH-L5 75.48 → 75.05, a small loss).
- **Shortest-CoT subsets (Table 2).** The gains land here. Llama3-8B MATH-L5, shortest 5%: 78.64 → 95.76. Llama3-8B MATH-500, shortest 5%: 82.00 → 95.60.
- **Length (Table 4, App. A.3).** Average CoT length changes little: +2.94% (Qwen-14B), +3.53% (Llama3-8B), −5.73% (Qwen-1.5B). So the edit does not just make the model think longer everywhere; it removes the "cut short" failure.
- Headline (abstract): +6.39% on short-reasoning cases, +3.34% overall.
- **Steering is not simply "longer is better".** On MATH-L5, negative α hurts, but large positive α does not reliably help, and the 1.5B model loses about 10% on GSM8K when steered longer (§3).

## Limits / what they didn't show
- **The direction is chosen by an external label** (token count), not by the model. Nothing self-originated.
- **Removal, not addition.** The edit only deletes a direction from some heads. It cannot install a new preference, which is what Q5 wanted for taste.
- One behavior (length), one domain (math), one model family (R1 distills). Length is a scalar and easy to measure. Style is not.
- The authors say the benefit is mostly for models that under-think; models that are already verbose may gain little.
- No matched comparison of "edit vs steering at the same strength", so no "fraction of steering gain kept" number.
- Head count is given only as a percentage (4%); the exact number of heads per model is not stated.

## Relevance to taste-lab
- **Why this killed [[Q5 (stopped) Make steering permanent]]:** it shows, on reasoning models, that a behavior found by a linear direction and checked by steering can be fixed into the weights with a tiny closed-form edit and no training. That is the shape of Q5's claim. The follow-up [[Steer2Edit - steering into small weight edits (Sun 2026)]] generalizes it to additive rank-one edits on heads and neurons.
- **What Q5 had that this does not cover:** (a) the direction comes from the model's own [[Good-bad signal probe]] instead of an external label; (b) an additive edit that installs a preference, not ablation that removes one; (c) code readability with correctness fixed by tests; (d) a recovery ratio vs inference steering.
- **[[Metacognition - watch and control yourself]] angle:** this is a crude monitor-and-control loop on "how much to think", but the controller is the experimenter. A version where the model's own confidence or valence sets which heads to edit would be new.
- **Grounded test:** the steer-then-edit check (direction moves behavior causally, then the edit reproduces it) is a template for the causal half of the grounded test.

## Steal this
- Code: [github.com/Trustworthy-ML-Lab/ThinkEdit](https://github.com/Trustworthy-ML-Lab/ThinkEdit).
- Head scoring (project each head's mean output onto the direction, take the top k%) as a cheap way to localize a readability direction before editing.
- Evaluate on the "worst k%" subset (their shortest 5/10/20%), not just the mean. For us: the least readable k% of solutions.

## Harshit's notes
<!-- yours -->
