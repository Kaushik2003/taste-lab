---
type: paper
title: "Towards Understanding the Cognitive Habits of Large Reasoning Models"
status: skimmed
arxiv: 2506.21571
url: https://arxiv.org/abs/2506.21571
authors: Jianshuo Dong, Yujia Fu, Chuanrui Hu, Chao Zhang, Han Qiu
year: 2025
venue: arXiv preprint
relevance: 2
section: 2
tier: skim
tests: [divergent]
components: [monitoring]
tags: [type/paper, section/2, test/divergent, component/monitoring, status/skimmed, relevance/2, role/prior-art, metacognition, reasoning, habits-of-mind, benchmark]
links: ["[[Metacognition - watch and control yourself]]"]
---

# Towards Understanding the Cognitive Habits of Large Reasoning Models

**One line:** Reasoning models have measurable cognitive habits: patterns like "Wait, did I miss anything?" appear consistently, vary by task, and differ in profile across model families. Some habits correlate with harmful outputs.

**Why it matters to us:** Habits are persistent, model-specific, behavior-shaping patterns: the behavioral surface of what we call a self-state's *style*. CogTest gives a 16-habit taxonomy and evidence that habit profiles are family signatures, which is the divergent test in behavioral clothing.

Source: [arXiv 2506.21571](https://arxiv.org/abs/2506.21571) (13 June 2025). Abstract-level note.

## Claim
Large reasoning models exhibit human-like cognitive habits, deploy them adaptively by task, and show family-specific habit profiles; some habits (e.g. Taking Responsible Risks) are associated with harmful responses ([abstract](https://arxiv.org/abs/2506.21571)).

## Mechanism
- CogTest: 16 cognitive habits from the Habits of Mind framework, 25 tasks each, with evidence-first extraction from the chain of thought.
- 16 models evaluated (13 reasoning, 3 non-reasoning).

## Evidence
- LRMs, unlike conventional LLMs, show human-like habits and adapt them to task type ([abstract](https://arxiv.org/abs/2506.21571)).
- Inter-family similarity (Qwen-3 and DeepSeek-R1 profiles cluster).
- Certain habits strongly associate with harmful generations.

## Limits / what they didn't show
- Habits are read off chain-of-thought text, which post-training heavily shapes; may reflect training data more than internal computation.
- Correlational link between habits and harmful outputs, not causal.
- No mechanism for how habits are stored or selected.

## Relevance to taste-lab
**Relevance 2. Section 2.**
- Behavioral-level evidence for model-specific stable style: the divergent test without probes.
- The habit-harm correlation is a safety hook: if style-level variables predict bad outputs, reading them early is a monitoring use case.
- Connects to the societies-of-thought view: internal multiplicity with characteristic voices is a description of the same phenomenon at the CoT level.

## Steal this
- CogTest's evidence-first extraction: require a quoted CoT span as evidence before counting a habit, to cut annotation noise.
- The 16-habit taxonomy as a checklist when characterizing a model's behavioral self-style.

## Kaushik's notes
<!-- yours -->
