---
type: paper
title: "Learning to Reason without External Rewards (INTUITOR)"
status: skimmed
arxiv: 2505.19590
url: https://arxiv.org/abs/2505.19590
authors: Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song
year: 2025
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [controller, consolidation]
tags: [type/paper, section/6, test/self-reinforcing, status/skimmed, relevance/3, role/prior-art, intrinsic-reward, rlif, self-certainty, rlvr, unsupervised]
links: ["[[Self-reward sharpens then collapses (He 2026)]]", "[[Self-reward on code collapses to short code (Jin 2026)]]", "[[Anchor against collapse]]", "[[Self-reward only within the same test result (Wu 2026)]]"]
---
# Learning to Reason without External Rewards / INTUITOR (Zhao et al., 2025)

**One line:** Replace the external reward in GRPO with the model's own confidence ("self-certainty") and nothing else: INTUITOR matches GRPO with verifiable rewards on math benchmarks and generalizes *better* to out-of-domain code generation, with no gold solutions or test cases.

## Claim
Reinforcement learning from internal feedback (RLIF) is viable: a model's intrinsic signal, used as its sole reward, can drive effective learning across domains.

## Mechanism
- RLIF framework: learn from intrinsic signals, no external rewards or labeled data.
- INTUITOR: self-certainty (the model's own confidence over its answer) as the only reward inside GRPO.
- Fully unsupervised: no gold solutions, no test cases.

## Evidence
- Matches GRPO (with verifiable rewards) on mathematical benchmarks; better generalization to out-of-domain code generation [unverified: margins, model sizes].

## Limits / what they didn't show
- Self-certainty is a correctness-adjacent signal, not a quality judgment: nothing here says a model can reward *style* where no ground truth exists.
- Run lengths are benchmark-scale; the sharpen-then-collapse dynamics of [[Self-reward sharpens then collapses (He 2026)]] appear over longer horizons, and He shows monotone transforms of cross-entropy to an anchor (which self-certainty is) sharpen the prior first.
- Reward hacking a confidence reward is one meta-level up: the model can raise confidence without raising quality.

## Relevance to taste-lab
**The intrinsic-reward baseline the review has to beat or cite first.** It is the strongest evidence *for* the loop (intrinsic signals can teach reasoning) and the cleanest target for the collapse critique (the signal is still correctness-flavored). The taste question sits one step beyond: can a signal that is *not* correctness - a readability preference - drive the same learning without collapse? That is exactly the self-reinforcing test.
- Prior-art check: **A partial** (intrinsic reward drives learning; the reward is confidence, not taste). **B no.**

## Steal this
- Self-certainty as the control arm: our valence reward must beat a self-certainty reward at matched budget, or the taste claim adds nothing.
- OOD-generalization metric (math trained, code tested) as the transfer test for a trained taste signal.

## Kaushik's notes
<!-- yours -->
