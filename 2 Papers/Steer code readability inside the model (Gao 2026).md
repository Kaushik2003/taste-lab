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

**One line:** The authors add three separate steering directions (comments, names, branches) to 13B to 14B code models while they run. They claim more readable code at under 1% cost in correctness, but they measure both only through the model's own answer probabilities and never run or rate any code the model writes.

**Why it matters to us:** This is the closest earlier work to Q2 (can the model steer its own code?), on our exact topic of code readability. A reviewer will say "readability steering already exists", so we need a clear answer. Their weak test (no real code is run or rated) is also where our work can be stronger.

Source: [arXiv 2606.06214](https://arxiv.org/abs/2606.06214), full HTML read. Authors: Gao, He, Pan, Yu, Zeng, Qin, Sun (7 authors; the arXiv page lists Weidi Sun as the 7th). Affiliations: Xiamen, Shenzhen, Fujian Normal, Xidian, Northumbria (UK), Peking universities.

**Words used here:**
- **Hidden numbers (hidden states):** the numbers the model computes inside each layer for each token.
- **Steering:** adding a direction to the hidden numbers while the model runs, to change its behavior.
- **RepE (representation engineering):** find a direction in the hidden numbers for some property, then steer with it. MRepE is the version with several properties at once.
- **Orthogonal:** the directions are at right angles, so changing one does not move the others.
- **Cyclomatic complexity:** a count of the paths through the code (more if, else and loops gives a higher count).
- **NLL (negative log-likelihood):** how surprised the model is by a text. Lower means the model finds it more likely.
- **pass@1:** the share of problems where the first generated program passes the tests.

## Claim
Steering with several readability directions at once (MRepE) can make LLM code more readable with little loss of correctness. This works if the steering strengths (coefficients) are chosen well. Their math gives limits on the trade-off.

## Mechanism
- **Three readability measures:** comment density (CD), naming conventions (NC), cyclomatic complexity (CC).
- **Data:** They take 300 MBPP problems and build two sets. MBPP-CR has a readable and an unreadable version per measure (for example `reverse_words(s)` vs `r_w(s)`). MBPP-CC has 4-option multiple-choice questions for correctness. The paper does not say how they made the versions, or how many pairs each measure has.
- **Directions:** They take the difference in hidden numbers between paired prompts and subtract the mean. A PCA-like method (MOC-JPCA) then finds one direction of length 1 per measure. It finds all three together and forces them to be orthogonal. (Technically: a Riemannian gradient on the Stiefel manifold with a QR retraction, a standard way to keep directions at right angles during the search.)
- **Steering:** h ← h + c1·d1 + c2·d2 + c3·d3. Here h is the hidden numbers, d1 to d3 are the three directions, and c1 to c3 are their strengths. They apply this over chosen layer ranges for each model (Table III).
- **Theory:** Theorem 1 shows the search reaches a stable point. Theorem 2 gives a lower limit on the probability of a "readable" answer, based on the strengths. Theorem 3 gives an upper limit on how much the probability of the correct answer can change.

## Evidence
- Models: DeepSeek-R1-Distill 14B, Qwen2.5-Coder-14B-Instruct, CodeLlama-13B-Instruct. Python only.
- **How they measure readability:** They show the steered model a fixed piece of code and ask, for example, "Is the comment density of the following Python code high?". The score is the probability that it answers "yes". A second score is the ratio of the model's NLL on the readable vs the unreadable version. The gains are statistically significant (for example DeepSeek CD, t = -5.73, p = 2.85e-8, Table III). The size of the gains appears only in figures.
- **How they measure correctness:** the probability of picking the right option on MBPP-CC. Loss at the chosen strengths: 0.79% (DeepSeek), within 0.95% (Qwen-Coder), 0.28% (CodeLlama) (Sec. V-E).

## Limits / what they didn't show
- **No code the model writes is run or rated.** "Readability" is the steered model's yes/no judgment about fixed code, plus how likely it finds a fixed readable version. "Correctness" is a multiple-choice probability, not pass@1.
- So the result may be a change in the model's *judgments* (a self-report effect), not better code. The test partly measures itself.
- No human raters, no LLM judge, and no standard readability model (Buse-Weimer, Scalabrino).
- Only three surface measures, one benchmark and 300 items. No comparison runs (plain prompting, or RepE with one property only).
- Code "available upon request". No public repo.

## Prior-art check
Two questions decide if this paper already did our idea.
- **Does the model's own signal steer its own thinking or learning? No.** The directions come from the model's hidden numbers. But the authors chose the readable and unreadable labels, and they add the steering at fixed strengths. The model's own judgment plays no role.
- **Does it make a small, permanent edit to the weights? No.** It works only while the model runs. The paper says the weights do not change.

## Relevance to taste-lab
**Relevance 3: the closest earlier work to Q2 (can the model steer its own code?) on our exact testbed.**
- A reviewer will say "readability steering already exists". Our answer has three parts:
  1. Our signal is the model's *own* good/bad (valence or value) signal, not a contrast that people labeled for readability.
  2. We score real code the model writes. Tests keep correctness fixed, and raters who do not know the condition (blind raters) judge readability.
  3. We close the loop: the model's own signal chooses and controls.
- **Use it as a comparison arm in Q2** ([[Q2 Can the model steer its own code]]): a readability direction that the researchers define vs the model's own good/bad direction.
- **Conflict with [[Value axis - model knows it is on track (Jiang 2026)]]:** In that paper, steering toward high value removes comments. In this paper, the readability direction adds them. So the two directions may point opposite ways on comment density. We should measure the angle between them (cosine).

## Steal this
- CD, NC and CC as cheap automatic readability measures, to use as controls in Q1, does the model sense code quality? ([[Q1 Does the model sense code quality]]).
- Paired readable/unreadable versions, like MBPP-CR, as a quick contrast set.
- MOC-JPCA, if we need several separate (orthogonal) taste directions.

## Harshit's notes
<!-- yours -->
