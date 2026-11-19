---
type: landscape
status: draft
cluster: 5
section: 7
tags: [type/landscape, section/7, landscape, taste, open-endedness, interestingness, novelty, homogeneity, code-readability]
links: ["[[Four tests for own taste]]", "[[Anchor against collapse]]", "[[Good-bad signal probe]]", "[[Models show research taste (Trehan 2026)]]", "[[Models share one taste for text (Zatuchin 2026)]]", "[[Learn to find interesting maths (Patel 2026)]]", "[[Q1 Does the model sense code quality]]", "[[Q3 Can self-learning avoid collapse]]", "[[Gaps in the field]]"]
---

# Landscape 5: Taste & open-endedness

**Guiding question:** How do we tell a model's own taste apart from copied human taste, a taste all models share, or noise, and what stops that taste from shrinking into a narrower copy of itself?

## Timeline
- 2008 · [Driven by Compression Progress](https://arxiv.org/abs/0812.4360) · Schmidhuber: data is interesting to an observer while the observer is getting better at compressing it, so taste comes from the observer's own learning, not a fixed target (formal version in IEEE TAMD 2010).
- 2010 · [Learning a Metric for Code Readability](https://web.eecs.umich.edu/~weimerw/p/weimer-tse2010-readability-preprint.pdf) · Buse & Weimer: 120 people rated 100 snippets, and a metric learned from them correlates with code changes and defect reports. Scalabrino et al. ([JSEP 2018](https://doi.org/10.1002/smr.1958)) extend it to 600+ snippets rated by 5K+ people.
- 2011 · [Abandoning Objectives](https://www.cs.swarthmore.edu/~meeden/cs81/f17/papers/lehman_ecj11.pdf) · Lehman & Stanley: searching only for new behavior beats objective-driven search on deceptive maze and biped tasks.
- 2023 · [OMNI](https://arxiv.org/abs/2306.01711) · a foundation model serves as a "model of interestingness" that picks tasks that are both learnable and interesting, beating learning-progress-only curricula. The taste is borrowed from human text.
- 2024 · [Open-Endedness is Essential for ASI](https://arxiv.org/abs/2406.04268) · Hughes et al. define open-endedness as novelty plus learnability, judged by an observer. This gives us a usable definition of "drifts but still means something".
- 2024 · [AI-AI Bias](https://arxiv.org/abs/2407.12856) · Laurito et al. (PNAS 2025): LLM selectors pick LLM-written descriptions far more often than human judges do.
- 2025 · [Artificial Hivemind](https://arxiv.org/abs/2510.22954) · Jiang et al.: on 26K open-ended prompts, each model repeats itself and different models give similar answers. Judges and reward models are least calibrated where humans disagree.
- 2025 · [CoReEval](https://arxiv.org/abs/2510.16579) · 1.4M LLM readability ratings compared with human ratings across Java, Python and CUDA. Agreement depends on language and prompt, and persona prompts shift scores (reported as near zero for Python in the ICSE 2026 poster [unverified]).
- 2026 · [AI Can Learn Scientific Taste](https://arxiv.org/abs/2603.14473) · Tong et al. train a judge on community signals such as citations, then train an idea generator against it (RLCF). Here taste means learned human consensus.
- 2026 · [AI lacks the imagination to diverge or negate](https://arxiv.org/abs/2606.08251) · Bao, Evans et al.: 6,749 scientists rate LLM ideas. Non-reasoning models fall into a narrow hivemind, no model proposes null hypotheses, and a 14B reward model trained on human ratings beats frontier judges.
- 2026 · [Human Creativity Benchmark](https://arxiv.org/abs/2606.30561) · 15,000 expert judgments: experts agree on checkable criteria and diverge on taste criteria once outputs pass a competence bar.
- 2026 · [[Learn to find interesting maths (Patel 2026)]] · a fixed "short statement, long proof" score gates a self-expanding Lean library. Overlap with mathlib drops from 91.9% to 30.6%.
- 2026 · [[Models share one taste for text (Zatuchin 2026)]] · the preference for model-written text is shared across models. The own-model premium is +0.019 share points (p = 0.14).
- 2026 · [[Models show research taste (Trehan 2026)]] · pairwise test shown in both orders. Models stably diverge from the authors' choice in 15 to 36% of pairs, mostly keep that choice under prompt changes, and partly share it with other models.

## Current best result
No paper yet shows a self-originated taste. The nearest pieces are:
- **A taste that steers a loop:** [[Learn to find interesting maths (Patel 2026)]] uses a computable taste score for RL and a 6-round self-expanding loop. Verified interestingness rises from 1.76 to 7.58, and overlap with known math falls from 91.9% to 30.6%. The score is external and frozen.
- **Measurement:** [[Models show research taste (Trehan 2026)]] finds 15 to 36% stable divergence, and 66.9 to 80.5% of it survives prompt ablations.
- **Taste as capability:** [TasteVal](https://arxiv.org/abs/2610.06824) puts Opus 5.5 at 2.3x expert compute efficiency (95% CI 1.15 to 4.37).

## Biggest open problem
Divergence is not ownership. Everything measured so far as "model taste" is either learned human consensus or a taste that all models share ([[Models share one taste for text (Zatuchin 2026)]], [Artificial Hivemind](https://arxiv.org/abs/2510.22954), the inter-model agreement in [[Models show research taste (Trehan 2026)]]). No paper shows a preference that passes all of these checks:
- it differs from humans *and* from other models;
- it holds across contexts;
- it matches an internal state;
- it gets sharper under the model's own selection without collapsing.

## Leading groups
- **Lossfunk** (Paras Chopra, Dhruv Trehan): behavioral research-taste elicitation, [[Models show research taste (Trehan 2026)]]. They also study perceptual geometry across LLM layers ([2605.27970](https://arxiv.org/abs/2605.27970)).
- **FAIR at Meta, ENPC and NYU** (Julia Kempe, Remi Munos, Amaury Hayat, Niket Patel): computable interestingness for self-expanding math, [[Learn to find interesting maths (Patel 2026)]].
- **Novelty-search / OMNI line** (Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune; UBC and collaborators [unverified]): [OMNI](https://arxiv.org/abs/2306.01711).
- **Google DeepMind open-endedness** (Edward Hughes, Tim Rocktäschel [unverified affiliation]): [2406.04268](https://arxiv.org/abs/2406.04268).
- **UW NLP** (Liwei Jiang, Yulia Tsvetkov, Maarten Sap [unverified current affiliations]): homogeneity across models, [Artificial Hivemind](https://arxiv.org/abs/2510.22954).
- **James Evans' group** (Honglin Bao, James Evans; UChicago Knowledge Lab [unverified]): large-scale scientist ratings of AI ideas, [2606.08251](https://arxiv.org/abs/2606.08251).

## Closest to taste-lab
- [[Models show research taste (Trehan 2026)]] already uses the term "stable divergence" for something very close to tests 1 and 2 of [[Four tests for own taste]]. We should reuse its both-order protocol on code pairs for [[Q1 Does the model sense code quality]], and set ourselves apart on tests 3 and 4 (probe grounding, self-training).
- [[Models share one taste for text (Zatuchin 2026)]] is the main threat to "self-originated". By default, we should expect a shared machine taste. Q1 needs a k-model matrix where every model writes solutions and judges all of them, scored with the diagonal premium γ. [[Q3 Can self-learning avoid collapse]] should track γ rising over rounds.
- [[Learn to find interesting maths (Patel 2026)]] is the closest analog to Q3: a hard verifier, promotion gated by taste, and RL. But its taste score is frozen and external, so it does not answer [[Self-reward sharpens then collapses (He 2026)]]. It supports the hard-check and novelty parts of [[Anchor against collapse]], and its "overlap with the reference library" rubric works as a drift metric.
- [Human Creativity Benchmark](https://arxiv.org/abs/2606.30561) and developer-consensus work ([Sergeyuk et al. 2024](https://arxiv.org/abs/2407.03790)) suggest readability is mostly a *convergent* axis where experts agree. On that axis, diverging from humans may just mean being wrong. This threatens the testbed choice in Q1. Fix: treat basic readability as the axis that should converge, and look for taste in the style choices above that bar.
- [Brand taste via DPO](https://arxiv.org/abs/2610.28272): preference training moves a model's picks by 11 to 24 points even in domains missing from the preference data. Self-edits in Q3 and [[Q4 Can the model edit its own weights]] could shift taste well outside code, so we should measure off-domain drift.

## Reading order for Harshit
1. **must-read** [[Models show research taste (Trehan 2026)]] · the metric we will reuse for Divergent and Stable. Read Sec. 2 (setup), Sec. 3.3 (robustness), and Tables 2, 5 and 9.
2. **must-read** [[Models share one taste for text (Zatuchin 2026)]] · how to test whether a taste is the model's own or shared. Read Sec. 3 (Eq. 1 and the permutation test) and Sec. 4.5 (power and design advice).
3. **must-read** [[Learn to find interesting maths (Patel 2026)]] · a self-expanding loop gated by taste, with a hard checker. Read Sec. 3.1, 3.3, 3.4 and App. D (ablation of the promotion rule).
4. **skim** [Human Creativity Benchmark](https://arxiv.org/abs/2606.30561) · convergence vs. divergence. Sec. 5.1 shows where taste starts: above the competence bar.
5. **skim** [Artificial Hivemind](https://arxiv.org/abs/2510.22954) · the baseline for how similar different models are. Read the intro and the inter-model figures.
6. **skim** [OMNI](https://arxiv.org/abs/2306.01711) · the reference design for a novelty or interestingness term. Method section only.
