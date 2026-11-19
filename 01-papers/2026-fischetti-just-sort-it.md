---
type: paper
title: "Just sort it! The LP behind rank-one anti-loop edits"
status: skimmed
arxiv: 2611.21432
url: https://arxiv.org/abs/2611.21432
authors: Matteo Fischetti
year: 2026
relevance: 2
section: 5
tier: skim
components: [consolidation]
tags: [type/paper, section/5, component/consolidation, status/skimmed, relevance/2, weight-space-programming, rank-one-edit]
links: ["[[landscape-persistent-control]]", "[[self-weight-updates]]"]
---

# Just sort it! The LP behind rank-one anti-loop edits

**One line:** The WSP anti-loop edit is W' = W + u vᵀ. You can replace the LP that picks v with a simple sort over 8 low-variance neurons and match performance. The edit behaves like a nearly constant bias along u.

## Evidence
Qwen3.5-0.8B on 1,000 problems: sorted edit 67.0% vs LP edit 67.4% vs unedited 9.5%. The difference is inside a pre-declared non-inferiority margin.

## Relevance to taste-lab
If a WSP edit is basically "a constant push along a direction", then it is a **steering vector baked into the weights**.
→ **T5:** a valence/taste steering direction found at inference time could be made permanent with a rank-one edit.
That's gradient-free consolidation of taste with no training loop.
