---
type: paper
title: "Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families"
status: skimmed
arxiv: 2607.17427
url: https://arxiv.org/abs/2607.17427
authors: Aleksander Fafuła
year: 2026
venue: arXiv preprint
relevance: 3
section: 5
tier: deep
tests: [divergent, stable]
components: [consolidation, evaluation]
tags: [type/paper, section/5, test/stable, component/consolidation, status/skimmed, relevance/3, role/prior-art, abliteration, side-effects, preferences]
links: ["[[Field map - Changes that stay in the weights]]", "[[One direction controls refusal (Arditi 2024)]]", "[[Models that change their own weights]]", "[[Task context moves model preferences (Trhlik 2026)]]", "[[2026-11-23 gap check]]"]
---
# Abliteration is not a scalpel (Fafuła 2026)

**One line:** Removing the refusal direction from a model's weights also changes how it decides on a task with nothing to refuse: both tested models become more optimistic, and their stated confidence moves in opposite directions.

Read 2026-11-24: key findings, Sec. 4.5, Sec. 5.1, 5.2, 5.5, conclusion. Method and result tables not read.

## Mechanism
21,600 up-or-down calls on 60 Warsaw Stock Exchange stocks over 18 weeks, replayed through a frozen pipeline. Base and edited versions of Gemma-4-26B and Qwen3-30B, same edit author, same prompt, full-precision weights. The base models never refuse on this task, so any difference is a side effect.

## Evidence
- Edited models bet on the upside more often: +12.2 percentage points (Gemma) and +7.4 (Qwen). This was the preregistered endpoint.
- Edited models justify themselves at greater length and use fewer uncertainty words (exploratory).
- Stated confidence goes down in Gemma and up in Qwen, with non-overlapping intervals.
- Stated and acted uncertainty come apart: the edited Gemma states more uncertainty but changes its stance no more often (Sec. 4.5).
- No arm shows real trading skill.
- Two artifacts were caught: a quantization mismatch and a stale chat template each produced false effects.

## Limits (author, Sec. 5.5)
One edit method, one task, one language (Polish), one persona. The optimism could be a general positivity shift; "distinguishing the two needs a non-financial disposition battery". No mechanism.

## Relevance to taste-lab
Closest prior work to "do direct weight edits move a model's preferences". It shows the effect for one edit and one task, and the author names the missing parts: a broad preference battery, a second edit method, a mechanism. It also warns that quantized weights can fake such effects, and that stated and acted dispositions must be measured separately.
