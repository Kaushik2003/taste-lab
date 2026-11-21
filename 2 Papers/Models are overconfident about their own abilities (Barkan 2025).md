---
type: paper
title: "Do Large Language Models Know What They Are Capable Of?"
status: skimmed
arxiv: 2512.24661
url: https://arxiv.org/abs/2512.24661
authors: Casey O. Barkan, Sid Black, Oliver Sourbut
year: 2025
venue: arXiv preprint
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring, controller]
tags: [type/paper, section/3, component/monitoring, component/controller, status/skimmed, relevance/2, role/prior-art, metacognition, overconfidence, capability-awareness, agents]
links: ["[[Models know when they know but do not act (Cao 2026)]]", "[[Agents left alone study themselves (Szeider 2025)]]"]
---

# Do Large Language Models Know What They Are Capable Of?

**One line:** Every tested LLM is overconfident about whether it will succeed at a task; worse, on multi-step agentic tasks the overconfidence *grows* as the task progresses, and reasoning models are no better than non-reasoning ones.

**Why it matters to us:** Capability awareness is the task-level version of confidence, and it is the input an agent needs for pursue/abandon decisions. The finding that decisions are near-rational *given* the estimate isolates the problem to monitoring, not control, which is exactly our decomposition.

Source: [arXiv 2512.24661](https://arxiv.org/abs/2512.24661) (31 December 2025). Abstract-level note.

## Claim
LLMs can predict their own task success only weakly: better than chance, but systematically overconfident, with no consistent improvement from scale or reasoning training ([abstract](https://arxiv.org/abs/2512.24661)).

## Mechanism
- Models estimate their probability of success before and during multi-step tasks, and decide whether to pursue tasks when failure is costly.
- In-context failure experience is provided to test whether estimates update.

## Evidence
- All tested LLMs overconfident; most discriminate better than chance ([abstract](https://arxiv.org/abs/2512.24661)).
- Overconfidence worsens over the course of multi-step agentic tasks for several frontier models.
- Reasoning LLMs comparable to or worse than non-reasoning LLMs.
- Decisions are approximately rational *given* the estimated probabilities; the estimates, not the decision rule, are the failure point.
- Some models update after in-context failure, others do not.

## Limits / what they didn't show
- Verbal probability estimates only; no probe of internal state.
- "Success" is defined per benchmark task; no open-ended or taste-like tasks.
- The Claude trend (larger = better discrimination) is an exception that needs replication.

## Relevance to taste-lab
**Relevance 2. Section 3.**
- Clean separation result: control (the pursue/abandon rule) is fine; monitoring (the success estimate) is what fails. Supports the architecture argument that improving the monitor, not the policy, is the lever.
- The worsening-over-time result matters for long-horizon taste work (a long editing loop is exactly a multi-step task).

## Steal this
- The rationality-given-estimate analysis: score the decision rule conditional on the estimate, to attribute failure to monitoring vs control.

## Kaushik's notes
<!-- yours -->
