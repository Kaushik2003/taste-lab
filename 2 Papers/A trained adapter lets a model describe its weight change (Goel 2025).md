---
type: paper
title: "Learning to Interpret Weight Differences in Language Models"
status: skimmed
arxiv: 2510.05092
url: https://arxiv.org/abs/2510.05092
authors: Avichal Goel, Yoon Kim, Nir Shavit, Tony T. Wang
year: 2025
venue: arXiv preprint (MIT)
relevance: 3
section: 5
tier: deep
tests: [grounded]
components: [monitoring, consolidation]
tags: [type/paper, section/5, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, weight-diff, introspection]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models describe behaviors they were trained into (Betley 2025)]]", "[[Models that change their own weights]]", "[[Adapters report side effects of fine-tuning (Yoshida 2026)]]", "[[2026-11-23 gap check]]"]
---
# Learning to interpret weight differences (Goel 2025), Diff Interpretation Tuning

**One line:** An extra adapter, trained on thousands of labeled weight changes, lets a fine-tuned model say in words how its weights were changed. Without the adapter the model cannot say it, and the adapter does not carry over to other kinds of change.

Read 2026-11-24: abstract, introduction, Sec. 4, Sec. 6.1. Sec. 5 and appendices not read.

## Evidence
- 4,760 synthetic rank-1 LoRA weight changes, each with a hidden topic behind a trigger phrase; a rank-16 adapter is trained on 4,660 and tested on 100 (Sec. 4).
- Scores on a 5-point scale, Qwen3-4B: the adapter scores 4.76 on hidden topics; simply asking the changed model "what topic were you trained on?" scores 1.21 (Table 6.1).
- Generalizes from rank-1 changes to higher ranks and partly to full fine-tuning (Sec. 4.2).
- No transfer across kinds of change: the topic adapter scores 1.25 on news-knowledge changes, the news adapter 1.22 on topics (Sec. 6.1, Table 6.1).

## Limits (authors, Sec. 6)
Two narrow settings, synthetic changes, small models (4B, 8B). The adapter may interfere with the change it reads.

## Relevance to taste-lab
For "does a model notice its own weight change": by default it does not (1.21 out of 5), but the ability can be trained for one kind of change. So the default report is the open measurement, and a trained reporter is the known upper bound.
