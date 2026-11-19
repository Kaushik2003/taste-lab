---
type: paper
title: "When Do Intrinsic Rewards Work for Code Reasoning? A Comprehensive Study"
status: skimmed
arxiv: 2606.20881
url: https://arxiv.org/abs/2606.20881
authors: Xiaolong Jin, Xuandong Zhao, Wenbo Guo, Xiangyu Zhang, Dawn Song (Purdue, UC Berkeley, UC Santa Barbara)
year: 2026
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor, valence]
tags: [type/paper, role/threat, section/6, test/self-reinforcing, component/anchor, component/valence, status/skimmed, relevance/3, question/Q3, collapse, intrinsic-reward, code, rlif]
links: ["[[Field map - Limits of self-learning]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[Q3 Can self-learning avoid collapse]]", "[[Anchor against collapse]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# When Do Intrinsic Rewards Work for Code Reasoning? A Comprehensive Study

**One line:** On code, every confidence-based self-reward helps for a few dozen steps, then the model learns to write short, overconfident, repetitive answers and gets worse. Late checkpoints cannot be rescued by normal test-based RL ([abs](https://arxiv.org/abs/2606.20881)).

## Claim
Certainty-based RL from internal feedback (RLIF) does not transfer well from math to code. All four methods tested collapse; hyperparameters change the speed, not the outcome ([§1, §4](https://arxiv.org/html/2606.20881)).

## Mechanism
Four logit-level rewards, all of the form f(mean over tokens of g(p_t)) ([§3, Table 1](https://arxiv.org/html/2606.20881)):
- Self-certainty: KL(uniform ‖ p_t), as in INTUITOR.
- Token entropy: −H(p_t).
- Trajectory entropy: mean log-prob of the sampled tokens.
- Probability disparity: top-1 minus top-2 probability.

Setup: DeepSeek-R1-Distill-Qwen-1.5B (plus Qwen3-4B and Qwen2.5-Coder-7B-Instruct in the appendix), verl, 6,753 competitive-programming problems, 16 rollouts per prompt, temperature 1.0, lr 1e-6, no KL by default. GRPO with test-case rewards is the baseline ([§4.1, App. C](https://arxiv.org/html/2606.20881)).

## Evidence
- Peaks then falls: token entropy peaks at 16.6% avg@4 on LiveCodeBench v5 (step 30); self-certainty falls to 9.3% by step 200. GRPO reaches 15.4% at step 100 and keeps going ([§4.3](https://arxiv.org/html/2606.20881)).
- **Length collapse:** responses shrink from about 7,300 tokens to 731 to 1,049 tokens by step 100 (GRPO stays near 5,300). Trajectory entropy drops 1.05 → 0.10 to 0.21; repetition ratio rises from 0.001 to 0.017 to 0.030 ([§4.4](https://arxiv.org/html/2606.20881)).
- **Confidence inflates for right and wrong answers alike,** so certainty loses its power to separate correct from incorrect code (rank-biserial r is weaker after self-certainty training than after GRPO) ([§4.5, Fig. 3](https://arxiv.org/html/2606.20881)).
- Rescue test: GRPO started from the self-certainty step-50 checkpoint reaches 0.151 (scratch GRPO 0.154); from step 80, 0.125; from step 105, 0.120. Once entropy is gone, test-based RL cannot recover it in 40 steps ([§4.6](https://arxiv.org/html/2606.20881)).
- Test-time training on the 279 LCB v5 problems slows collapse (around step 70) but does not stop it; self-certainty pass@1 16% → 10% ([§4.7](https://arxiv.org/html/2606.20881)).
- Ablations: fewer rollouts (N=8, 12) collapse more slowly; higher temperature (1.2) gives a higher peak but a worse end; KL 0.005 slows but does not prevent collapse, including at 7B ([App. B.5, C.3](https://arxiv.org/html/2606.20881)).
- With N=16, entropy rewards can collapse the other way, to max-length degenerate outputs ([App. B.5](https://arxiv.org/html/2606.20881)).

## Limits / what they didn't show
- Function-level competitive programming only, small models (1.5B to 7B), about 100 to 200 steps ([Limitations](https://arxiv.org/html/2606.20881)).
- No ensemble or hybrid methods (intrinsic plus sparse tests), which is the regime we plan to use.
- Correctness is the target. Nothing on style or readability.

## Relevance to taste-lab
- **The baseline failure for Q3 in our own domain.** It confirms [[Self-reward sharpens then collapses (He 2026)]] on code: intrinsic signals sharpen, then collapse.
- **Length is the likely exploit.** If valence likes short code (readability ratings often do), a valence reward could reproduce this length collapse even with tests passing. Q3 needs length logged and controlled; Q2 already names length as a kill condition.
- **Re-check Q1 after training, not just at base.** Self-training inflated confidence for all outputs and destroyed its discriminative power. The same may happen to a valence-quality correlation.
- Their recommendation (use intrinsic reward early, then switch to verifiable reward before entropy collapses) fits a controller that lowers the learning rate when entropy drops, as in [[Neuromodulators as learning settings]].
- Prior-art check: **A partial** (studies the model's own logit-level confidence as its own training reward; logits, not activations; no inference-time steering). **B no.**

## Steal this
- The metric panel to log in every Q3 run: response length, trajectory entropy, repetition ratio, reasoning-token density, and certainty-correctness rank-biserial r per checkpoint.
- The "rescue test": continue with test-reward RL from checkpoints at several steps to find the point of no return.
- Benchmarks: LiveCodeBench v5/v6 and the 6,753-problem training set they adopt from Wang et al. 2025 ([§4.1](https://arxiv.org/html/2606.20881)).

## Harshit's notes
<!-- yours -->
