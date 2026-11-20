---
type: paper
title: "WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming"
status: skimmed
arxiv: 2611.25476
url: https://arxiv.org/abs/2611.25476
authors: Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang
year: 2026
venue: preprint
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, role/prior-art, thread/T4, section/5, component/consolidation, status/skimmed, relevance/2, weight-space-programming, gradient-free, capability-install]
links: ["[[landscape-persistent-control]]", "[[self-weight-updates]]", "[[2026-takehi-weight-space-programming]]"]
---

# WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming

**One line:** A frozen LLM writes executable "weight programs" that install new capabilities into a trained network with no gradients. The kept program can be rerun on independently trained networks (83-110% of the gain survives) and later programs stack on earlier ones.

## Claim
WSP programs are reusable construction procedures, not one-off weight diffs. Capabilities can be installed, transferred across networks, and accumulated in succession ([abs](https://arxiv.org/abs/2611.25476)).

## Mechanism
- Program p takes weights W and task knowledge I (a rule, demonstrations, or labeled examples) and returns W' = p(W, I). The LLM proposes candidate computations (weight/activation statistics, SVD/PCA, closed-form fits, single-unit ablations); evaluation feedback on a check split selects.
- Retention rule: the kept program is the candidate with the best new+old score whose old-input loss stays inside a bound (e.g. at most 0.5% of 4,000 clean images). If none qualifies, the network is left unchanged.
- Rerun: the same program remeasures a new network and constructs an edit in that network's coordinates; copying the fixed weight diff instead gives negligible gains.

## Evidence
- SCAN: 257 weights changed, unseen command compositions 0.0% to 99.8% exact match. BabyAI: new pickup action from 8 demonstrations, 98.4% success.
- ImageNet corruption robustness: 4 programs give 8.84-17.62 net points while preserving clean accuracy, beating 8 fine-tuning methods under matched examples, checks and retention.
- Rerun on 5 independently trained ViTs: 10 programs retain 83-110% of source-network gains on average. 6 second-round programs add contrast robustness (5.23-14.50 points) while keeping the earlier noise gain.
- Causal check: ablating the installed noise-correction gates removes the robustness gain; their selective activation preserves clean accuracy.

## Limits / what they didn't show
- The task knowledge and the goal come from the experimenter. Nothing self-originated; the network being edited has no say.
- Vision, SCAN and BabyAI scale: small ViTs, no language-model behaviors, no style or preference.
- Each program is written by a frontier LLM in a scaffolded session; the edited network does not read or write anything.
- Preservation is measured on chosen reference conditions; distributed side effects are not deeply probed.

## Relevance to taste-lab
- **T4 ([[self-weight-change-T4]]) and the consolidation row of [[self-weight-updates]]**: strongest evidence yet that weight edits can be *accumulated* without retraining. A taste loop that persists would need exactly this "succession" property.
- Prior-art check: **A no** (experimenter supplies the goal and knowledge). **B yes** (gradient-free weight edits, reusable and stackable) - but on small non-LM networks.
- **Novelty pressure, again**: second WSP-framework paper in the same month (after [[2026-takehi-weight-space-programming]] and the 8+ follow-ups flagged on 2026-11-19). Our angle stays taste + self-direction, never "WSP on X".
- Contrast for the review: WeightCode installs *capabilities the experimenter wants*; our persist step writes *preferences the model itself evaluated*. Same mechanism family, opposite direction source.

## Steal this
- The retention rule ("best candidate whose old-input loss stays inside a hard bound") as the non-regression gate for T3/T4 weight edits - same shape as GUARD (2611.23476) in [[anti-collapse-anchor]].
- Rerun-vs-copy as the test that a procedure, not a diff, is what transfers. If we ever consolidate a valence direction, rerunning the *procedure* on a new checkpoint beats copying the edit.
- Their check-split protocol (S_new, S_old counts, 8-check budget) as a cheap evaluation harness.

## Kaushik's notes
<!-- yours -->
