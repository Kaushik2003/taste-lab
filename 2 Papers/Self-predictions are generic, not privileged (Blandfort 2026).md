---
type: paper
title: "Strangers to Themselves: What Language Models Say About Themselves Is Generic"
status: skimmed
arxiv: 2609.09899
url: https://arxiv.org/abs/2609.09899
authors: Phil Blandfort, Urja Pawar, et al.
year: 2026
venue: arXiv preprint
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, component/monitoring, status/skimmed, relevance/3, role/threat, self-prediction, introspection]
links: ["[[Field map - Models read their own state]]", "[[Models predict themselves better than others do (Binder 2024)]]", "[[Trained self-prediction without an own-model edge (Zeng 2026)]]", "[[2026-11-23 gap check]]"]
---
# Self-predictions are generic, not privileged (Blandfort 2026)

**One line:** When a model predicts its own behavior, it mostly applies a general theory of AI assistants, plus a flattering bias. Other models predict it as well as it predicts itself.

## Evidence (abstract)
- Nine behavioral evaluations. Direct self-report predicts the model's real behavior rates at r = +0.04; with the exact items shown, +0.24.
- The same question about "capable AI agents in general" does as well (+0.28). Other models' answers about themselves predict the target at least as well as its own.
- Frontier scale does not make gains self-specific.
- First-person framing shifts reports in the flattering direction (less harmful behavior).
- Fine-tuning on the model's own behavior record teaches narrow self-predictions, but it also changes the behavior being predicted and does not transfer broadly.

## Limits
Behavioral self-report, no hidden-state probes.

## Relevance to taste-lab
With [[Trained self-prediction without an own-model edge (Zeng 2026)]] and [[Models predict edit effects without a self advantage (Kocabay 2026)]], strong evidence that a "self-model" has no privileged access. For the gap: do not claim the self-model must be the model itself; an outside predictor may do as well. The flattering bias is a direct risk for a self-judging editor.
