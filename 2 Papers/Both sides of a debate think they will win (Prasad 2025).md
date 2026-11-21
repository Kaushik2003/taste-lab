---
type: paper
title: "When Two LLMs Debate, Both Think They'll Win"
status: skimmed
arxiv: 2505.19184
url: https://arxiv.org/abs/2505.19184
authors: Pradyumna Shyama Prasad, Minh Nhat Nguyen
year: 2025
venue: arXiv preprint
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/2, role/prior-art, metacognition, calibration, overconfidence, debate]
links: ["[[Models know when they know but do not act (Cao 2026)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Monitoring and control between two levels (Nelson 1990)]]"]
---

# When Two LLMs Debate, Both Think They Will Win

**One line:** In zero-sum debates, ten frontier models all think they will win: they start at 73% average confidence, rise to 83% by the final round, and in 62% of debates both sides claim at least 75% chance of victory.

**Why it matters to us:** Calibration results on static QA were too kind. Under opposition, confidence goes the wrong way, and private scratchpad reasoning sometimes disagrees with the public confidence report, a faithfulness red flag for any self-report based monitor.

Source: [arXiv 2505.19184](https://arxiv.org/abs/2505.19184) (25 May 2025). Abstract-level note.

## Claim
LLM confidence is not just miscalibrated in static settings; it escalates under adversarial multi-turn pressure, in a setting where the zero-sum structure makes mutual high confidence a logical impossibility ([abstract](https://arxiv.org/abs/2505.19184)).

## Mechanism
- 60 three-round policy debates among ten state-of-the-art LLMs; private win-probability ratings (0-100) after each round.
- Zero-sum design: one side wins, so paired confidences above 100% are impossible.

## Evidence
- Initial average confidence 72.9% vs a rational 50%; rises to 83% by round 3 ([abstract](https://arxiv.org/abs/2505.19184)).
- In 61.7% of debates both sides simultaneously claimed >=75% win probability.
- Self-debate against an identical copy still raised confidence from 64.1% to 75.2%; even told the chance was exactly 50%, it rose to 57.1%.
- Private scratchpad thoughts sometimes diverged from public confidence ratings.

## Limits / what they didn't show
- Win-probability is a social, adversarial judgment, not a correctness judgment on a checkable task.
- No internal-state measurements; the private-vs-public gap is behavioral only.
- Policy debate topics may sit far from the factual distribution calibration methods were built on.

## Relevance to taste-lab
**Relevance 2. Section 3.**
- The stress-test counterweight to static calibration results: any claim that a model "knows its confidence" must survive opposition.
- The private/public divergence is direct evidence for why verbal self-reports cannot be the only monitor channel; needs a probe readout beside it.

## Steal this
- The zero-sum trick as a calibration test with no answer key needed: mutual >50% claims are impossible, full stop.
- Self-debate against an identical copy as the cheapest control condition.

## Kaushik's notes
<!-- yours -->
