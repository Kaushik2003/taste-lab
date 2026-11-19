---
type: paper
title: "WeightBench: Evaluating Language Models as Weight-Space Programmers"
status: skimmed
arxiv: 2611.18553
url: https://arxiv.org/abs/2611.18553
authors: Aayush Marasini, Barsat Khadka, Nick Rahimi
year: 2026
venue: arXiv preprint
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, role/prior-art, weight-space-programming, benchmark, model-editing]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[Exploring WSP - small weight edits, uneven results (Hu 2026)]]"]
---

# WeightBench: Evaluating Language Models as Weight-Space Programmers

**One line:** A benchmark of 42 weight-editing tasks with strict audits. Frontier agents can read small networks and write working control policies from zero, but they cannot yet patch a language model without damage, and they cannot tell an impossible edit from a hard one.

**Why it matters to us:** It measures the "persist" tool our loop would need. The result says weight-space programming on language models is not yet reliable, even with the best agents.

Source: [arXiv 2611.18553](https://arxiv.org/abs/2611.18553) (v1 13 Nov 2026). Full HTML read, Sections 3 to 6 and Table 1. Code and leaderboard: [github.com/Aayush-Marasini/WeightBench](https://github.com/Aayush-Marasini/WeightBench).

**Words used here:**
- **Weight-space programming (WSP):** an agent reads a network's weights and writes changes to them directly, without gradient training.
- **Forward pass:** running the network on an input to get an output. WeightBench limits and counts these, so agents cannot just try and test.
- **Collateral damage:** how much other skills drop after an edit, measured on held-out tests such as MMLU.
- **Macro score:** the mean of the five track means, from 0 to 1.
- **Quarantined run:** a run that the audit flagged (for example, an attempt at gradient descent). It scores 0 until a human checks it.

## Claim
WeightBench tests if language models can read, fix and write network weights by reasoning about the weights alone. Current agents can do some reading and writing, but fixing language models, data-free compression and spotting impossible edits are still out of reach ([arXiv abstract](https://arxiv.org/abs/2611.18553)).

## Mechanism
- **Five tracks, 42 tasks (Sec. 4):**
  1. READ (10 tasks): find what a small network was trained on, find induction heads, recover what a fine-tuning batch taught from the weight difference.
  2. FIX (13): remove the directions behind repetitive output in small language models, fix sycophancy, fix failing control policies, with small collateral damage.
  3. META (5): some requested edits are impossible (the model never learned the skill). The agent must refuse those and solve hard but possible decoys.
  4. WRITE (6): write the weights of a network from all zeros, for example to play Breakout, with no training.
  5. SYSTEMS (8): compress a model without data.
- Subject networks range from about 2K-parameter control policies to 7B-parameter language models (abstract).
- **Audit (Sec. 3.1):** an OS-level sandbox with no model-execution libraries; a metered NumPy layer that detects forward-pass chains; a hash-chained log. Scores come from the log, not from the agent's own report.
- **Score (Sec. 3.2):** task gain, times penalties for collateral damage, edit size and compute use. The penalties multiply, so a tiny edit cannot make up for no gain.
- **Contamination guard (Sec. 3.3):** subject models are regenerated with new seeds and permuted hidden dimensions, so agents must analyze weights, not remember indices.

## Evidence
From Table 1 (default difficulty, seed 0; all scores are lower bounds because quarantined runs score 0 and none was reviewed yet):
- **Macro over 42 tasks:** Claude Opus 5.5 0.535, Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215.
- **Macro over the 38 shared tasks:** GPT-6.1-sol 0.568, Opus 0.546.
- **FIX track:** Opus 0.404, Sonnet 0.381, Haiku 0.300, DeepSeek 0.187 (GPT-6.1-sol 0.571 on 9 of 13 tasks only). On the 4 reasoning-loop tasks, only Opus (on 3) and Sonnet (on 1) score above zero.
- **META track:** the three Claude models score 0.491 to 0.500, which the authors call about the random-guess level. GPT-6.1-sol scores 0.260.
- **WRITE track:** Opus 0.829, GPT-6.1-sol 0.863, Sonnet 0.569, Haiku 0.369, DeepSeek 0.000.
- **SYSTEMS track:** all agents 0.177 to 0.238.
- Quarantined runs: Opus 11 of 77, DeepSeek 13 of 42.
- 21 of 42 tasks have a reference solution that uses only what the agent can access; the rest need privileged access such as gradient fitting (Sec. 5.2).

## Limits / what they didn't show
- One seed, one difficulty level, one or two samples per task. Small numbers per track (5 tasks for META).
- Unreviewed quarantines make all scores lower bounds; Opus has the most quarantined Claude runs, so its true score is less certain.
- Half the tasks have no non-privileged reference solution, so a low score may mean "impossible without data", not "agent is weak".
- The agents edit other networks. Nothing about a model editing its own weights.
- Short paper (9 pages); some details (score constants) did not render in our copy [unverified].

## Relevance to taste-lab
**Relevance 2.** Section 5, persistent control.
- It sets the current limit of the persist tool: localized, audited weight edits on language models mostly fail (FIX track 0.40 for the best fully run Claude model). This is evidence against relying on WSP for self-edits today.
- The META track is a metacognition test in weight space: "can I do this edit at all?" Agents score at chance. That is a clean, citable gap for the review: no system yet knows the limits of its own weight edits.
- Counter-point to [[Exploring WSP - small weight edits, uneven results (Hu 2026)]]: that paper's large gains came with free forward passes and validation; under strict audits, patching is much harder.

## Steal this
- The audit design (metered operations, hash-chained log, scores from the log) for any claim that an edit was found "by reasoning, not by search".
- The multiplied score (gain × damage × edit size × compute) as a fair way to compare weight edits.
- The META track idea: mix impossible edits with hard ones to test whether an editor knows its limits.

## Harshit's notes
<!-- yours -->
