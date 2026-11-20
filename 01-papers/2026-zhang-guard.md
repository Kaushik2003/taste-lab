---
type: paper
title: "GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance"
status: skimmed
arxiv: 2611.23476
url: https://arxiv.org/abs/2611.23476
authors: Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, Chen-Yu Lee (Google Cloud)
year: 2026
venue: preprint
relevance: 3
section: 6
tier: deep
tests: []
components: [controller, consolidation]
tags: [type/paper, section/6, component/controller, component/consolidation, status/skimmed, relevance/3, self-improvement, non-regression, harness, forgetting]
links: ["[[self-training-collapse-T3]]", "[[anti-collapse-anchor]]", "[[2025-liu-intrinsic-metacognitive-learning]]"]
---

# GUARD: Stabilizing Recursive Self-Improvement

**One line:** Frozen model + editable harness (prompts, skills, tool rules, memory): self-editing without graders backfires because scalar scores conflate "newly broken" with "still unsolved". GUARD decomposes tasks into pre-execution self-checks, guides edits by directional regret, and gates promotion with a non-regression test (Soft-HURT) - improving without forgetting or memory bloat.

## Claim
Reference-free continual self-improvement is stable if each edit is graded against self-checks that pin mastered rules and isolate newly broken behaviors, and promoted only when gains outweigh regressions ([abs](https://arxiv.org/abs/2611.23476)).

## Mechanism
- Pre-execution self-checks per task; trajectories graded against them each round.
- Directional regret: prioritize what an edit newly broke over what was never solved.
- Critic-free group-relative fitness selects among parallel candidate edits.
- Soft-HURT gate: an edit is promoted only if gains outweigh regressions, with scoping to prevent over-triggering; guarantees non-regression on the gated buffer.
- Test time: one frozen harness, single pass.

## Evidence
- Benchmarks on memory, skill evolution, continual task streams and domain reasoning: consistent improvement without catastrophic forgetting or memory pollution, plus reduced deployment token usage [unverified: numbers not extracted].

## Limits / what they didn't show
- The harness is editable, the model is frozen: this is self-improvement of scaffolding, not of internal computation or taste.
- Self-checks are still behavior-level (task success); no internal signal involved.
- "Guarantee" is on the gated buffer, not on open-world drift.

## Relevance to taste-lab
**The engineering answer to T3 collapse in the harness regime.** Their diagnosis - reflection conflates regression with unsolved - is exactly why an unbounded self-signal collapses ([[2026-he-unsupervised-rlvr-limits]], [[2026-jin-intrinsic-rewards-code]]), and their fix is the external-check version of our [[anti-collapse-anchor]]. Cite in Limits as: collapse is being solved in the harness regime by non-regression gating; the open problem is doing it for internal signals and weights.
- Prior-art check: **A partial** (self-evaluated loop with a stability gate, but frozen weights and behavioral checks). **B no.**

## Steal this
- Directional regret (newly-broken vs never-solved) as a metric for our loop rounds - cheaper than full re-evaluation.
- The gated-buffer non-regression guarantee as the design pattern for exp01's anchor set.

## Kaushik's notes
<!-- yours -->
