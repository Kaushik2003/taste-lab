---
type: paper
title: "Learning to Discover Interesting Mathematics"
status: skimmed
arxiv: 2609.28603
url: https://arxiv.org/abs/2609.28603
authors: Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos, Julia Kempe (FAIR at Meta; CERMICS ENPC; NYU)
year: 2026
venue: preprint
relevance: 2
section: 7
tier: skim
tests: [self-reinforcing]
components: [anchor, consolidation]
tags: [type/paper, section/7, test/self-reinforcing, component/anchor, component/consolidation, status/skimmed, relevance/2, question/Q3, interestingness, open-endedness, compression, novelty, self-expanding-library, lean]
links: ["[[Anchor against collapse]]", "[[Field map - Taste and new ideas]]", "[[Q3 Can self-learning avoid collapse]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[Models that change their own weights]]", "[[Four tests for own taste]]"]
---

# Learning to Discover Interesting Mathematics

**One line:** A simple, computable interestingness score (how long the proof is relative to how short the statement is) is used both as an RL reward and as a gate on which of the system's own theorems it keeps building on, and it pushes the system away from known mathematics while a proof checker keeps everything correct.

## Claim
"Easy to state, hard to prove" can be measured from proof structure alone, with no human judgment. This score correlates with how much a theorem later helps the rest of the library, and optimizing it produces new, verified, less derivative theorems ([arXiv 2609.28603](https://arxiv.org/abs/2609.28603), abstract, Sec. 3).

## Mechanism
- **Difficulty model V(T | P).** Expected proof length (Lean lines) of theorem T given premises P. Trained on about 100k mathlib (theorem, premises, proof) triples built by "premise expansion" (unrolling dependencies). Qwen3.6-27B fine-tuned with GRPO for 350 steps; the reward enforces matching the true length, a Bellman-style composition rule, and "more premises never makes it harder" (Sec. 2, Eq. 1 to 4).
- **Interestingness I(T | P) = 100 · V(T | P) / L(T | P),** where L is the description length of the statement plus any definitions not already available in P. Dividing by L stops "glue many theorems together" from scoring high (Sec. 3.1, Eq. 5 and 6).
- **Utility U0(T) = number of direct users x proof length.** An after-the-fact measure of how much a theorem compresses the library (Sec. 3.2, Eq. 7).
- **RL conjecturer.** Qwen3.6-27B, 75 GRPO steps, reward = 0.25 + log(1 + I/100) for valid, relevant, non-trivial statements. Hard gates: Lean must compile it, it must use the given premises, and simple tactics (rfl, simp, tauto...) must not close it (Sec. 3.3, App. C.1.2).
- **Self-expanding library.** Each round: Claude 4.6 proposes 400 statements, a semantic filter removes duplicates, Claude Code proves them in Lean, and the 10 with the highest verified interestingness are promoted into the premise set for the next round. 6 rounds (Sec. 3.4).

## Evidence
- Intrinsic interestingness and extrinsic utility correlate on mathlib: Spearman ρ = 0.756, excluding theorems with no users (Sec. 3.2, Fig. 3).
- The trained 27B difficulty model is better calibrated than GPT-5.5 and Claude Opus 4.6 on 4,615 held-out prompts (Fig. 1).
- RL raises mean verified interestingness from 1.76 (base) to 7.58, higher in all 8 areas (2.10x combinatorics to 8.72x number theory). It also beats Opus 4.6 prompted to be interesting (Sec. 3.3, Fig. 4).
- Share of generated statements judged substantially or fully already in mathlib falls from 91.9% (base) and 92.5% (Claude) to **30.6%** (Fig. 5).
- In the 6-round loop, interestingness promotion beats no pruning, random, and longest-proof promotion. Blind judge ranks its statement first 60% of the time (vs 8 to 19%), cohort quality 3.40 vs 2.40 to 2.60, diversity 2.10 vs 1.20 to 1.30 (out of 5), redundancy 28% vs 50 to 53% (App. D, Tables 3 and 4).

## Limits / what they didn't show
- The taste is a fixed, hand-written formula plus a separately trained predictor. It never changes during the loop, so this is "steer by a fixed taste", not "develop a taste".
- Only 6 rounds and 10 theorems per round. Even the best rule has low absolute diversity (2.10 of 5) and 28% redundancy. The authors say long-running loops need extra diversity and de-duplication mechanisms (Sec. 4).
- Quality and diversity are judged by Claude 4.6, the same model family that proposes and proves in the loop.
- Proof length in lines is partly a style artifact (automation tactics shorten proofs) (Sec. 4).
- No test of whether the new theorems help prove later results.
- I did not find a public code release [unverified].

## Relevance to taste-lab
- **Closest working loop to Q3.** Hard external check (Lean) + taste-gated promotion of the system's own outputs + RL on a taste reward, and the output moves away from its origin (mathlib overlap 91.9% → 30.6%) without collapsing in 6 rounds. This is the shape of [[Q3 Can self-learning avoid collapse]], with our tests playing the role of Lean.
- **Difference that matters.** Their signal is external and frozen. Ours is the model's own valence, which changes as it learns. Per [[Self-reward sharpens then collapses (He 2026)]], a self-scored reward is the case that collapses; a fixed external formula may avoid that. So this paper does not show our loop is safe; it shows a structural metric is a good *anchor*.
- **Novelty term for [[Anchor against collapse]].** "Overlap with the existing library" (judge rubric, 5 levels) is a usable drift metric. For code: overlap with a reference corpus of solutions, or near-duplicate rate against the base model's samples.
- **Code analog of the score** (my idea, not from the paper): behavior per unit of description, e.g. tests passed or functionality covered per token or per AST node, as a compression-style readability prior to check valence against in Q1. Compare [[Field map - Taste and new ideas]] on Schmidhuber's compression progress.
- **Prior-art check.** A: partial. The system uses an evaluation signal to steer what it generates (RL) and what it learns from (promotion), but the signal is external (formula + separate 27B predictor), not the model's own internal state. B: no.

## Steal this
- The promotion-rule ablation design (keep all / random / longest / interestingness), with a blind four-way ranking and cohort diversity + redundancy scores. Drop-in for Q3 arms.
- The "library overlap" rubric (App. C.2.3) as a drift and novelty metric.
- Hard triviality gates before any taste reward (compile, relevance, "closed by simple tactics" = 0). Code analog: must pass tests, must differ from the reference by more than formatting.

## Harshit's notes
<!-- yours -->
