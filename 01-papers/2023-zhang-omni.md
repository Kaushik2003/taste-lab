---
type: paper
title: "OMNI: Open-endedness via Models of human Notions of Interestingness"
status: skimmed
arxiv: 2306.01711
url: https://arxiv.org/abs/2306.01711
authors: Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune (UBC / Vector Institute / Stochastic Labs / Maven)
year: 2023
venue: preprint
relevance: 3
section: 7
tier: deep
tests: []
components: [monitoring, controller]
tags: [type/paper, section/7, component/monitoring, component/controller, status/skimmed, relevance/3, open-endedness, interestingness, auto-curriculum, foundation-models]
links: ["[[intrinsic-motivation]]", "[[2026-patel-interesting-mathematics]]", "[[2025-liu-intrinsic-metacognitive-learning]]"]
---

# OMNI: Models of human Notions of Interestingness

**One line:** Open-ended learning drowns in learnable-but-boring tasks; use a foundation model as a Model of Interestingness (MoI) - it has internalized human notions of interesting from human text - to pick tasks that are both learnable and interesting. Beats uniform sampling and learning-progress-only baselines.

## Claim
The Achilles heel of open-endedness is quantifying interestingness, and FMs already carry it ([abs](https://arxiv.org/abs/2306.01711), [project](https://www.jennyzhangzt.com/omni/)).

## Mechanism
FM-as-MoI scores candidate tasks; task selection optimizes learnable AND interesting; framed as AI selecting its own next task (auto-curricula, AI-generating algorithms).

## Evidence
Improved open-ended learning vs uniform / learning-progress baselines in the studied environments [unverified: which environments and effect sizes].

## Limits / what they didn't show
- The interestingness model is frozen and external to the learner: human notions distilled in an FM, queried as an oracle. The agent never develops its own interestingness.
- Interestingness is verbalized judgment, not an internal signal of the learning agent.

## Relevance to taste-lab
**The open-endedness anchor for section 7 and the clearest statement of what we are NOT doing.** OMNI borrows taste from a frozen FM; the taste-lab question is whether an agent can grow its own evaluation signal ([[valence-readout]]) and survive doing so ([[self-training-collapse-T3]]). Patel's math loop ([[2026-patel-interesting-mathematics]]) sits between: FM-interestingness, but frozen and externally applied. The progression OMNI -> Patel -> us is the section's spine.
- Prior-art check: **A no. B no.**

## Steal this
- Learnable AND interesting as the two-axis task-selection picture for the auto-curriculum paragraph.
- FM-as-MoI as the baseline any self-developed taste signal must beat or differ from.

## Kaushik's notes
<!-- yours -->
