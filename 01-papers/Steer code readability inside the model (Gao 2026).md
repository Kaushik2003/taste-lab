---
type: paper
title: "Towards the Readability of LLM-Generated Codes through Multitask Representation Engineering"
status: skimmed
arxiv: 2606.06214
url: https://arxiv.org/abs/2606.06214
authors: Huifan Gao, Liuhua He, Yinghui Pan, Shenbao Yu, Yifeng Zeng, Shengchao Qin, Weidi Sun
year: 2026
venue: preprint (cs.SE)
relevance: 3
section: 4
tier: deep
tests: []
components: [controller]
tags: [type/paper, role/prior-art, section/4, component/controller, status/skimmed, relevance/3, question/Q2, question/Q1, readability, repe, steering, code]
links: ["[[Field map - Models judge good and bad]]", "[[Q2 Can the model steer its own code]]", "[[Q1 Does the model sense code quality]]", "[[Neuromodulators as learning settings]]"]
---

# Towards the Readability of LLM-Generated Codes through Multitask Representation Engineering

**One line:** Three orthogonal steering directions (comments, naming, branching) are added to 13 to 14B code models at inference. The paper claims better readability at under 1% correctness cost, but it measures both only through the model's own answer probabilities and never runs or rates generated code.

Source: [arXiv 2606.06214](https://arxiv.org/abs/2606.06214), full HTML read. Affiliations: Xiamen, Shenzhen, Fujian Normal, Xidian, Northumbria (UK), Peking universities.

## Claim
Multitask representation engineering (MRepE) can raise the readability of LLM code with little loss of correctness, if the steering coefficients are chosen well. Theory gives bounds on the trade-off.

## Mechanism
- **Three readability metrics:** comment density (CD), naming conventions (NC), cyclomatic complexity (CC).
- **Data:** 300 MBPP problems expanded into MBPP-CR (readable vs unreadable variant per metric, e.g. `reverse_words(s)` vs `r_w(s)`) and MBPP-CC (4-option multiple choice for correctness). The paper does not say how the variants were made or how many pairs per metric.
- **Directions:** hidden-state differences between paired prompts, mean-centered. A PCA-like method (MOC-JPCA) finds one unit direction per metric jointly, forced to be orthogonal (Riemannian gradient on the Stiefel manifold, QR retraction).
- **Steering:** h ← h + c1·d1 + c2·d2 + c3·d3 over chosen layer ranges per model (Table III).
- **Theory:** Thm 1, convergence to a stationary point. Thm 2, a lower bound on the readability-query probability as a function of coefficients. Thm 3, an upper bound on how much the correctness-query probability can change.

## Evidence
- Models: DeepSeek-R1-Distill 14B, Qwen2.5-Coder-14B-Instruct, CodeLlama-13B-Instruct. Python only.
- **Readability metric:** probability that the steered model answers "yes" to queries such as "Is the comment density of the following Python code high?" about a given snippet. Secondary: ratio of the model's NLL on readable vs unreadable variants. Gains are significant (e.g. DeepSeek CD, t = -5.73, p = 2.85e-8, Table III), but sizes appear only in figures.
- **Correctness metric:** probability of picking the right option on MBPP-CC. Loss at chosen coefficients: 0.79% (DeepSeek), within 0.95% (Qwen-Coder), 0.28% (CodeLlama) (Sec. V-E).

## Limits / what they didn't show
- **No generated code is executed or rated.** "Readability" is the steered model's yes/no judgment about fixed code, plus its likelihood of a fixed readable variant. "Correctness" is multiple-choice probability, not pass@1.
- So the result may be a shift in the model's *judgments* (a self-report effect), not better code. The evaluation is partly circular.
- No human raters, no LLM judge, no established readability model (Buse-Weimer, Scalabrino).
- Three surface metrics, one benchmark, 300 items, no experimental baselines (prompting or single-task RepE).
- Code "available upon request", no public repo.

## Prior-art check
- **A (own signal steers own reasoning/learning): no.** The direction comes from the model's activations, but the readable/unreadable labels are the authors' and the steering is injected at fixed coefficients. The model's own evaluation plays no role.
- **B (permanent small weight edit): no.** Inference-time only. The paper says weights are not changed.

## Relevance to taste-lab
**Relevance 3: the closest prior art to Q2 on our exact testbed.**
- A reviewer will say "readability steering already exists". Our answer: (1) our signal is the model's *own* valence/value, not a human-labeled readability contrast; (2) we score real generations, with tests holding correctness fixed and blind raters for readability; (3) we close the loop.
- **Use it as a baseline arm in Q2** ([[Q2 Can the model steer its own code]]): an experimenter-defined readability direction vs the model's own valence direction.
- **Tension with [[Value axis - model knows it is on track (Jiang 2026)]]:** high-value steering removes comments; this paper's readability direction adds them. The two directions may point opposite ways on comment density. Worth measuring the cosine.

## Steal this
- CD / NC / CC as cheap automatic readability covariates for the Q1 controls ([[Q1 Does the model sense code quality]]).
- MBPP-CR-style paired variants as a quick contrast set.
- MOC-JPCA if we need several orthogonal taste sub-directions.

## Harshit's notes
<!-- yours -->
