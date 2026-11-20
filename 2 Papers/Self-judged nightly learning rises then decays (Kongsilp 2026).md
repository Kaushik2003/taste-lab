---
type: paper
title: "Learning through Discernment: when a small language model learns from user feedback on the job, and when it decays"
status: skimmed
arxiv: 2611.23716
url: https://arxiv.org/abs/2611.23716
authors: Sirisilp Kongsilp
year: 2026
venue: arXiv preprint
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor, consolidation]
tags: [type/paper, section/6, test/self-reinforcing, component/anchor, component/consolidation, status/skimmed, relevance/3, role/threat, question/Q3, self-judging, lora, continual-learning, collapse]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[Self-reward on code collapses to short code (Jin 2026)]]", "[[SEAL - models write their own training data (Zweiger 2025)]]", "[[Q3 Can self-learning avoid collapse]]", "[[Four tests for own taste]]"]
---

# Learning through Discernment

**One line:** A small model that fine-tunes itself each night on the attempts it judges good gets better for about a week, then loses almost all of it. A year of this never recovers.

**Why it matters to us:** This is the sharpen-then-collapse pattern of [[Self-reward sharpens then collapses (He 2026)]], now in a weight-level loop that runs for a year. It is direct evidence against Q3 (can self-learning avoid collapse?) when the model is its own judge.

Source: [arXiv 2611.23716](https://arxiv.org/abs/2611.23716) (18 Nov 2026). Full PDF read for Sections 1 to 5.1 through `pdftotext`. Code and data: [github.com/kratai-desci/research](https://github.com/kratai-desci/research/tree/discernment/discernment).

**Words used here:**
- **Life:** one run of the model over many simulated days. Each night it trains a LoRA adapter (a small add-on set of weights) on the day's accepted attempts.
- **Judge:** what decides which attempts become lessons. Options: the true outcome (oracle), the user's stated verdict, the model's own judgment (self), or a separate frozen "feedback sense" that reads the user's reaction.

## Claim
Without a true outcome, learning on the job holds up only when the judge keeps failures out of the lessons and the user can see the outcome. Self-judging improves and then decays ([abstract](https://arxiv.org/abs/2611.23716)).

## Mechanism
- Qwen3 0.6B and 1.7B, LoRA fine-tuned each night on attempts the judge accepts. 127 lives of up to one year on WebShop (online shopping tasks) and tau-squared-bench (customer service) (Sec. 3 to 4).
- Three versions of a separate feedback sense were built. Version 3 first asks whether the user gave a clear verdict at all.

## Evidence
- 14-day test, 5 seeds per judge, WebShop exam score 0 to 100: oracle 63.2, stated verdict 41.6, self 27.0, self plus user 23.1, no learning 14.2. Self-judging was not reliably above no learning (p = 0.12) (Sec. 5.1).
- Self-judging rose as fast as the oracle at first (55 by day 7), then every self-judged life fell below its own day-7 score by day 14 (Sec. 5.1).
- Year-long run: self-judging plus user peaked near day 6 (52), was back at its start (15) by day 14, and ended the year at 5. The oracle life stayed between 55 and 64 (Sec. 5.1).
- Across 97 lives, the share of failed attempts among the lessons predicted the outcome (Spearman rank correlation of minus 0.81) ([abstract](https://arxiv.org/abs/2611.23716)).

## Limits / what they didn't show
- Very small models (0.6B and 1.7B).
- What is learned is mostly one habit: press "Buy Now" before the step limit. "Collapse" means the model stopped buying (Sec. 5). So this is collapse of one behavior, not of taste or style.
- The self-judge is a verbal judgment, not a hidden-state readout.
- No diversity or entropy measure is the main outcome; the paper only suggests lopsided lessons "may also narrow the model".

## Relevance to taste-lab
**Relevance 3. Threat to Q3 and to the self-reinforcing test.**
- Section 6 can cite this as a second, independent, long-horizon case of rise-then-decay with a self-judge at the weight level.
- The one design that held (oracle, or a judge that keeps failures out and sees the outcome) matches our anchor: tests as a hard bound ([[Anchor against collapse]]). It also matches [[Self-reward only within the same test result (Wu 2026)]].
- The fail-share metric is a cheap early warning: if failed attempts creep into self-chosen lessons, decay follows.

## Steal this
- "Share of failures among the lessons" as a leading indicator of collapse in any self-training loop.
- Long-horizon lives with daily held-out exams, not a single end-point score.

## Harshit's notes
<!-- yours -->
