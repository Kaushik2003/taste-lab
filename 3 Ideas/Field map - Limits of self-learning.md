---
type: landscape
status: draft
cluster: 4
section: 6
tags: [type/landscape, section/6, landscape, collapse, self-improvement, intrinsic-reward, self-judge, anchor]
links: ["[[Q3 Can self-learning avoid collapse]]", "[[Anchor against collapse]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[Self-reward on code collapses to short code (Jin 2026)]]", "[[Self-judge training makes wrong look right (Zhou 2026)]]", "[[Self-reward only within the same test result (Wu 2026)]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]", "[[Gaps in the field]]"]
---

# Landscape 4: Self-improvement and its limits (collapse)

**Guiding question:** When a model learns from its own judgments, what makes it get better instead of turning into a narrower, overconfident copy of itself?

## Timeline
- 2022 · [STaR](https://arxiv.org/abs/2203.14465) · A model improves its reasoning by training on its own rationales, but only those that reached the correct answer: self-improvement with an external filter.
- 2024 · [Shumailov et al., Nature](https://doi.org/10.1038/s41586-024-07566-y) · Training each generation on the previous generation's output loses the tails of the distribution in LLMs, VAEs and GMMs: "model collapse" ([arXiv 2305.17493](https://arxiv.org/abs/2305.17493)).
- 2024 · [Self-Rewarding LMs](https://arxiv.org/abs/2401.10020) · The model judges its own answers with an LLM-as-judge prompt and trains on them (iterative DPO); over 3 rounds on Llama 2 70B both answering and judging improved.
- 2024 · [Is model collapse inevitable?](https://arxiv.org/abs/2404.01413) · Collapse comes from replacing real data. Keeping the real data and adding synthetic data on top keeps test error bounded.
- 2025 · [INTUITOR](https://arxiv.org/abs/2505.19590) · The model's own token confidence (self-certainty, from logits) as the only RL reward matches GRPO on math and transfers better to code.
- 2026 · [[Self-reward sharpens then collapses (He 2026)]] · The analyzed probability-derived certainty/consistency rewards sharpen the starting distribution. Reported gains rise then fall; small-data test-time training can remain useful. This does not prove collapse for every hidden-state reward.
- 2026 · [[Self-reward on code collapses to short code (Jin 2026)]] · On code, four confidence rewards all collapse: outputs shrink from about 7,300 to about 1,000 tokens, entropy goes to near zero, and late checkpoints cannot be rescued by test-based RL.
- 2026 · [[Self-judge training makes wrong look right (Zhou 2026)]] · Training against your own verdict on a shown answer makes errors more convincing, not rarer: judge pass 0.72 → 0.94 at flat 0.20 accuracy. Making the judge commit its own answer first fixes it.
- 2026 · [Co-RL](https://arxiv.org/abs/2608.17253) · Separate models reward each other instead of themselves; more diverse cohorts share fewer errors and collapse less (+3.0 to 7.9% with no labels).
- 2026 · [[Self-reward only within the same test result (Wu 2026)]] · The policy ranks its own SWE trajectories only inside the same test outcome, with a cap so pass > fail always holds; +2.6 points on SWE-bench Verified over tests-only RL.
- 2026 · [SIF](https://arxiv.org/abs/2610.21392) · Self-certainty reward kept stable by voting across certainty bands and peers and skipping undecided groups; peak-to-final drop 0.7 points vs 7.0 for INTUITOR.
- 2026 · [No free lunch in RLVR](https://arxiv.org/abs/2610.39295) · Theorem (under their exponential-tilt model): every pass@1 gain costs pass@k on some prompts, and entropy collapse follows from the same mechanism.
- 2026 · [Rényi crossings](https://arxiv.org/abs/2611.08892) · Self-trained GPT-2 lost 24% of word types yet gained 0.91 bits of collision entropy: one entropy number can say "more diverse" while richness falls.
- 2026 · [GUARD](https://arxiv.org/abs/2611.23476) · Self-edits to an agent's prompts and memory are kept only if gains beat regressions on a pinned task buffer; 19 of 19 promoted edits did not regress on held-out tests.

## Current best result
No paper shows open-ended self-improvement. The best pure self-signal result is [SIF](https://arxiv.org/abs/2610.21392): its final checkpoint beats INTUITOR's best checkpoint by 4.71 points (39.19 vs 34.48 average over 12 benchmarks, Qwen2.5-Math-1.5B), but on 1.5B to 3B models trained on MATH. The best anchored result in code is [[Self-reward only within the same test result (Wu 2026)]]: 32.1% → 34.7% on SWE-bench Verified (Qwen3-14B), where a matched random reward gave 30.9%.

## Biggest open problem
Long-horizon auditability of the proposed activation-level quality loop remains unresolved in the studies reviewed. [[Self-rewarding language models judge and train themselves (Yuan 2024)]] already reports three iterations of own-verbal-reward quality gains without a hard correctness verifier, so neither correctness-only targets nor hard verification are universal requirements for short-run gains. The one proven defense against self-judge hacking (commit your own answer first) needs a checkable answer, and its author lists open-ended outputs as future work ([Zhou §7](https://arxiv.org/html/2607.05904)). Style has no such answer.

## Leading groups
- **UC Berkeley + Purdue** (Dawn Song, Xuandong Zhao, Xiaolong Jin): INTUITOR and [[Self-reward on code collapses to short code (Jin 2026)]] (affiliations from the 2606.20881 front matter).
- **Tsinghua + UIUC** (Ning Ding, Zhiyuan Liu, Bowen Zhou, first author Bingxiang He): [[Self-reward sharpens then collapses (He 2026)]] (affiliations from the paper's front matter).
- **Oxford / Cambridge / Toronto** (Ilia Shumailov, Yarin Gal, Nicolas Papernot, Ross Anderson) [unverified affiliations]: model collapse, [Nature 2024](https://doi.org/10.1038/s41586-024-07566-y).
- **Meta FAIR + NYU** (Weizhe Yuan, Jason Weston, Kyunghyun Cho) [unverified affiliations]: [Self-Rewarding LMs](https://arxiv.org/abs/2401.10020).
- **Stanford** (Rylan Schaeffer, Sanmi Koyejo, with Matthias Gerstgrasser) [unverified affiliations]: [Is model collapse inevitable?](https://arxiv.org/abs/2404.01413).
- **Penn State + Microsoft Research** (Yiran Wu, Xuan Feng): [[Self-reward only within the same test result (Wu 2026)]] (affiliations from the paper).

## Closest to taste-lab
- **Q3 design twin:** [[Self-reward only within the same test result (Wu 2026)]] already does "tests fix pass/fail, own judgment moves reward inside a bucket" for [[Q3 Can self-learning avoid collapse]]. Differences: a verbal judge that sees the reference patch, and a rubric that excludes style. Warning: ranking only among passing runs (our setting) was their weakest arm and lowered Pass@3 below baseline.
- **Q2 and Q3 threat:** [[Self-judge training makes wrong look right (Zhou 2026)]]. A [[Good-bad signal probe]] on a shown candidate is candidate-conditioned, so it is in the channel that gets hacked. On code, best-of-16 by self-judge grew the judge-truth gap from 0.20 to 0.588 with no training. That is our Q2 setup. We need a hidden readability anchor that is never used for selection or training.
- **Q3 kill risk and Q1 drift:** [[Self-reward on code collapses to short code (Jin 2026)]] with [[Self-reward sharpens then collapses (He 2026)]]. If valence likes short code, a valence reward can reproduce the length collapse with all tests passing. Self-training also inflated confidence on right and wrong outputs alike, so the Q1 valence-quality correlation must be re-measured after each round.
- **Closest prior art on "internal signal gates learning":** [SpeCal](https://arxiv.org/abs/2611.20691) weights its own self-supervised RL updates by the geometry of its hidden states (8 layers, mean-pooled, effective rank of the rollout group), +2.7 points in-domain over the best unsupervised baseline, averaged over two 8B models. It is not a valence direction, it does not steer inference, and it targets math correctness, not style.
- **Anchors to adopt in Q3:** GUARD's Soft-HURT rule (promote a LoRA self-edit only if gains exceed regressions on a pinned buffer) and SIF's rule (update only when the preference holds across several signal bands and peers, skip ties) are the two concrete gates for [[Anchor against collapse]].

## Reading order for Harshit
1. **must-read** · [[Self-reward on code collapses to short code (Jin 2026)]] · What collapse looks like in our domain. Read §4.4 to §4.6 (length collapse, confidence inflation, the rescue test).
2. **must-read** · [[Self-judge training makes wrong look right (Zhou 2026)]] · Why self-judging gets hacked and the one fix that works. Read §4 and §5.2 to §5.3 (the code best-of-N result).
3. **must-read** · [[Self-reward only within the same test result (Wu 2026)]] · A template for the Q3 reward. Read §3.2 (bounded reward) and Tables 4 and 5 (bucket ablation, random-reward control).
4. **skim** · [SIF](https://arxiv.org/abs/2610.21392) · §2 shows self-certainty rising while accuracy falls to zero; Table 3 compares gating rules.
5. **skim** · [GUARD](https://arxiv.org/abs/2611.23476) · §4.4 for the Soft-HURT gate; the gate-removal ablation (Table C.7, −10.35 points, teacher-student setting) shows what the gate buys.
6. **skim** · [SpeCal](https://arxiv.org/abs/2611.20691) · §3: the nearest prior art on hidden states gating self-training. Check how far it is from a valence readout.
