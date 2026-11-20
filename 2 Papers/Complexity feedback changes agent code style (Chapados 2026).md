---
type: paper
title: "Metrics-in-the-Loop: Complexity Feedback Reshapes Agent-Written Code"
status: skimmed
arxiv: 2611.23817
url: https://arxiv.org/abs/2611.23817
authors: Nicolas Chapados, Jean-François Gagné, Nouha Dziri
year: 2026
venue: arXiv preprint
relevance: 2
section: 1
tier: skim
tests: []
components: [controller, anchor]
tags: [type/paper, section/1, component/controller, component/anchor, status/skimmed, relevance/2, question/Q2, code-quality, coding-agents, cyclomatic-complexity, testbed]
links: ["[[Field map - Models judge good and bad]]", "[[Steer code readability inside the model (Gao 2026)]]", "[[Self-reward on code collapses to short code (Jin 2026)]]", "[[Q2 Can the model steer its own code]]", "[[Anchor against collapse]]"]
---

# Complexity feedback changes agent code style

**One line:** Coding agents that get short in-run messages about functions that are too complex write less tangled code, and the code stays as correct on held-out tests.

**Why it matters to us:** It shows the core idea of our testbed in practice: with tests holding correctness fixed, a quality signal can move code style alone. Here the signal is an outside metric, not the model's own.

Source: [arXiv 2611.23817](https://arxiv.org/abs/2611.23817) (18 Nov 2026). Abstract only; full text not read.

**Words used here:**
- **Cyclomatic complexity:** a count of independent paths through a function. Higher means more branches and harder code.
- **Erosion:** the authors' measure of how much complexity piles up in a few places.

## Claim
Cheap code metrics injected into an agent's context during a run redirect it before weaknesses build up ([abstract](https://arxiv.org/abs/2611.23817)).

## Mechanism
- After each code-changing turn, a message names changed functions above a complexity limit, or changed lines not covered by tests.
- Three long-horizon coding benchmarks and four strong models, with ablations.

## Evidence
- Complexity feedback significantly reduces erosion without changing held-out correctness ([abstract](https://arxiv.org/abs/2611.23817)). Effect sizes are not in the abstract [unverified].

## Limits / what they didn't show
- The quality signal is a fixed outside metric. No model preference, no human readability rating.
- Inference-time only, no weight change.

## Relevance to taste-lab
**Relevance 2. Section 1 (why code readability is the testbed), and Question 2 (can the model steer its own code?).**
- Evidence that style can move with correctness held by tests.
- A natural baseline for any self-signal: does the model's own readout beat a plain complexity metric?

## Steal this
- Erosion and complexity limits as cheap secondary measures of code quality.

## Harshit's notes
<!-- yours -->
