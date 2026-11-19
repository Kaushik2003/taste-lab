---
type: paper
title: "A Shared Taste for Model-Written Text: The Generator-by-Selector Matrices of \"AI-AI Bias\" Show No Detectable Own-Model Premium"
status: skimmed
arxiv: 2610.00369
url: https://arxiv.org/abs/2610.00369
authors: Dmitrij Żatuchin (EUAS Tallinn; Rankfor.AI)
year: 2026
venue: preprint
relevance: 2
section: 7
tier: skim
tests: [divergent]
components: [anchor]
tags: [type/paper, section/7, test/divergent, component/anchor, status/skimmed, relevance/2, thread/T3, taste, self-preference, ai-ai-bias, homogeneity, permutation-test, measurement]
links: ["[[four-taste-tests]]", "[[landscape-taste-open-endedness]]", "[[2026-trehan-eliciting-research-taste]]", "[[self-training-collapse-T3]]", "[[anti-collapse-anchor]]"]
---

# A Shared Taste for Model-Written Text: no detectable own-model premium

**One line:** LLMs strongly prefer LLM-written text over human text, but when you separate "this text is attractive to every model" from "this model likes its own text", the own-model part is near zero (+0.019 share points, p = 0.14). The taste is shared, not personal.

## Claim
Laurito et al. ([PNAS 2025, arXiv 2407.12856](https://arxiv.org/abs/2407.12856)) found that LLM selectors pick LLM-written product, paper and film descriptions far more often than humans do. Their design uses the same 5 models as generators and selectors, so it also contains a test of self-preference. Re-analysed, it shows a large shared preference for model text and no detectable preference for one's own text ([arXiv 2610.00369](https://arxiv.org/abs/2610.00369), Sec. 4.1, Sec. 7).

## Mechanism
- **Rebuild the data.** Three 5x5 generator-by-selector matrices (products, paper abstracts, films) rebuilt from per-item counts in the original repository: 21,828 valid trials, every cell matches the published value (Sec. 2).
- **Decompose each matrix.** Cell share y_ij (how often selector j picks generator i's text over the human text) = mean + generator effect a_i + selector effect b_j + γ·[i = j] + noise. In a full k x k matrix, γ is just the mean of the diagonal minus the mean of the off-diagonal cells after row and column effects (Sec. 3, Eq. 1).
- **Exact permutation test.** Relabel which selector counts as "self" in all 120 ways (5!) and see how often a premium this large appears by chance. A same-vendor term (GPT-3.5 vs GPT-4) is fitted alongside.
- **Why not trial-level stats.** Cells vary 1.1 to 7.4 times more than binomial sampling predicts, so trial-level regressions claim false significance (pooled z = 3.9). The cell is the right unit (Sec. 4.3).
- **Position bias** is checked on the 27 runs that record which slot was chosen, by removing items decided by position (Sec. 4.4).
- **Power analysis** by simulation, for this design and for larger k x k designs (Sec. 4.5).

## Evidence
- γ = +0.013 products (p = 0.24), -0.010 papers (p = 0.74), +0.054 films (p = 0.07), **+0.019 pooled (p = 0.14; 95% interval -0.008 to 0.046)** (Table 1).
- The generator's own model is its keenest selector in only 4 of 15 rows. Same-vendor term is negative in all three datasets.
- Shared effect is large: GPT-4 product descriptions are chosen 77 to 95% of the time by every selector; humans choose them 36% of the time (Sec. 7).
- Position bias moves single cells by up to 0.42 share points, but equally on and off the diagonal (42% vs 41% of items decided by position), so it does not create or hide a self effect (Table 2).
- Minimum detectable premium at 80% power: 0.034 pooled. The design had 97% power for γ = 0.05 (Sec. 4.5).
- The one comparable matrix (Tan et al., ACL 2024, 4x4) gives γ = +0.148, but a same-family term of similar size, and there "own text" is confounded with "agrees with what I already believe" (Sec. 4.6).
- Adding models helps power more than adding trials: 8 models x 200 trials gives 86% power for γ = 0.05; 5 models x 3,000 trials gives 85% (Table 3, Sec. 4.5).

## Limits / what they didn't show
- Re-analysis of an old design: 5 models from 2023 to 2024 (GPT-3.5, GPT-4, Llama 3.1 70B, Mixtral 8x22B, Qwen2.5 72B), one prompt per role, binary choices, many invalid answers for some cells (Sec. 6).
- Only one same-vendor pair, so vendor and model-size effects cannot be separated.
- Silent on effects below about 0.04 share points, on open-ended judging, and on newer models.
- Behavioral only. Nothing about internal representations.

## Relevance to taste-lab
- **Divergent test, the cross-model half.** [[four-taste-tests]] asks for divergence from human *and* training preferences. This paper gives the clean statistic for "is this preference the model's own, or shared by all models?": the diagonal premium γ with an exact permutation test.
- **Prior to beat.** The default is a shared machine taste with no own-model part. If our model's valence prefers code that every model prefers, that is "machine taste", not self-originated taste. Same lesson as the inter-model agreement in [[2026-trehan-eliciting-research-taste]] and the Artificial Hivemind result ([arXiv 2510.22954](https://arxiv.org/abs/2510.22954)).
- **For T3.** In [[self-training-collapse-T3]], a model that self-trains on its own judgment should show a *growing* γ over rounds (its taste moves away from the shared machine taste). That is a direct, cheap measure of "drift away from origin".
- **Prior-art check.** A: no (selectors are prompted judges; no internal signal, no steering). B: no.

## Steal this
- The γ statistic and exact permutation test: build a k x k matrix where k models each write passing solutions and each judge all solutions; diagonal minus off-diagonal after row and column effects. Use at least 8 models, several per vendor, and record position per trial (Sec. 4.5 recommendations).
- Use cell-level, not trial-level, inference.
- The paper describes a replication package (extraction script, counts, analysis scripts); I did not find a public link [unverified].

## Harshit's notes
<!-- yours -->
