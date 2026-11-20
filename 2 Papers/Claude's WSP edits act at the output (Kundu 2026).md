---
type: paper
title: "Same Fix, Different Weights: Replicating Weight-Space Programming with Claude"
status: skimmed
arxiv: 2611.20953
url: https://arxiv.org/abs/2611.20953
authors: Subham Kundu
year: 2026
venue: arXiv preprint
relevance: 2
section: 5
tier: skim
tests: [self-reinforcing]
components: [consolidation]
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, status/skimmed, relevance/2, role/threat, question/Q4, weight-space-programming, replication, preregistered]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[A model rewrites its own weights (Fan 2026)]]", "[[Reading weights is mostly reading inputs (Goworek 2026)]]", "[[Exploring WSP - small weight edits, uneven results (Hu 2026)]]"]
---

# Same Fix, Different Weights

**One line:** A preregistered replication of weight-space programming with Claude Opus 5.5 matches the original's large math gain, but every edit acts at the output: it raises the sampling temperature and lowers the chance of the token "Wait".

**Why it matters to us:** It suggests that large WSP gains on loop-prone small models can come from shallow output changes, not from deep repairs. That weakens how strongly section 5 can describe what WSP edits do.

Source: [arXiv 2611.20953](https://arxiv.org/abs/2611.20953) (16 Nov 2026). Abstract only; full text not read.

## Claim
The core WSP results replicate with a different frontier model, but the mechanism of the math gain differs: output-level changes, not removal of an internal loop direction ([abstract](https://arxiv.org/abs/2611.20953)).

## Mechanism
- Ten preregistered experiments with untrained-network and permutation controls, and hand audits of every code cell.
- Reading tasks (name the game a policy plays, find copying heads) and writing tasks (edit failing policies, write networks from scratch, edit Qwen3.5-0.8B with a few forward passes).

## Evidence
- Qwen3.5-0.8B on MATH-500: 6.7% to 58.1% with 50 forward passes, a gain of 51.4 points (95% interval 47.9 to 55.0; original study 48.1%). GSM8K 11.6% to 68.2%; IFEval 22.2% to 54.2% ([abstract](https://arxiv.org/abs/2611.20953)).
- Every edit scaled the final norm (higher effective temperature) and moved the logits of "Wait" and the end-of-thinking token. Norm scaling alone reaches only 20.9 to 22.1% on MATH-500.
- On Gemma 3 270M, which rarely loops, no edit helped (minus 0.8 points), as in the original.
- Reading was mixed: answers about training data often followed priors.

## Limits / what they didn't show
- A small target model with a known loop fault. One author.

## Relevance to taste-lab
**Relevance 2. Section 5, threat to strong WSP claims.**
- Read with [[A simple sort replaces the anti-loop edit (Fischetti 2026)]] and [[Reading weights is mostly reading inputs (Goworek 2026)]]: three independent papers say current WSP gains are often loop fixes or output tweaks. Add the vision-language repair study (arXiv 2611.23615, Reading list), where repairs depend on a low-bit trace that the planted faults leave.
- It frames the self-rewriting result in [[A model rewrites its own weights (Fan 2026)]], which also fixes loops. Section 5 should say what kind of fault each WSP gain repairs.

## Steal this
- Untrained-network and permutation controls for any claim that a model "reads" weights.

## Harshit's notes
<!-- yours -->
