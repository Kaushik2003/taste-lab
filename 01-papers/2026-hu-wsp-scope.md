---
type: paper
title: "Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations"
status: skimmed
arxiv: 2611.09382
url: https://arxiv.org/abs/2611.09382
authors: Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu (Shanghai AI Lab, Tongji, Fudan)
year: 2026
venue: preprint
relevance: 2
section: 5
tier: skim
tests: []
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, wsp, weight-editing, localization]
links: ["[[2026-takehi-weight-space-programming]]", "[[2026-marasini-weightbench]]", "[[2026-li-weightcode]]"]
---

# Exploring WSP: Capabilities, Generalization, Limitations

**One line:** 16 WSP editing trajectories, 7 benchmarks, Qwen3.5-0.8B/9B: edits are strikingly local (1,023 parameters -> +29.45 pts on MATH-500; up to +36.72 IFEval, +17.11 SciBench), transfer unevenly (math edit -> +12.18 GPQA, +20.10 SciBench, nothing on SciCode), and 6/16 trajectories keep the original weights when improvement can't be validated.

## Claim
WSP enables highly localized adaptation with real but inconsistent cross-task generalization; reliable intervention discovery is the bottleneck ([abs](https://arxiv.org/abs/2611.09382), [project](https://wsp-scope.github.io/)).

## Mechanism
Systematic trajectory study of an editing agent on two model scales; held-out full evaluations; validation-gated acceptance of edits.

## Evidence
- Locality: 1,023 parameters for +29.45 MATH-500; +4.42 GPQA, +36.72 IFEval, +17.11 SciBench single-task.
- Transfer: math-edited checkpoint gains on GPQA/IFEval/SciBench without further editing; zero on SciCode.
- Reliability: outcomes vary across trajectories; 6 of 16 retain original weights when validation fails.

## Limits / what they didn't show
- Small models (0.8B/9B); agent-driven edits, not self-edits; no account of what the edited parameters encode.

## Relevance to taste-lab
**The locality result T4 needs.** "1,023 parameters" strengthens the sparse-is-enough pattern ([[2026-xu-sparse-reward-subsystem]], [[2026-karpf-metacognitive-steering]]) at the weight level, and the validation-gated acceptance mirrors GUARD's non-regression gate ([[2026-zhang-guard]]): the field is converging on "edit only what you can verify". For the review: WSP is mechanism, not novelty - position per [[gaps]].
- Prior-art check: n/a (capability study).

## Steal this
- The retain-original-weights outcome as honest reporting: a no-edit result is a result.
- Cross-task transfer grid as the table format for any persist-claim evaluation.

## Kaushik's notes
<!-- yours -->
