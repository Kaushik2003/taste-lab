---
type: paper
title: "ReMA: Learning to Meta-think for LLMs with Multi-Agent Reinforcement Learning"
status: skimmed
arxiv: 2503.09501
url: https://arxiv.org/abs/2503.09501
authors: Ziyu Wan, Yunxiang Li, Xiaoyu Wen, Yan Song, Hanjing Wang
year: 2025
venue: NeurIPS 2025
relevance: 3
section: 5
tier: deep
tests: []
components: [controller]
tags: [type/paper, section/5, component/controller, status/skimmed, relevance/3, role/prior-art, metacognition, learned-control, multi-agent, rl]
links: ["[[Decoupled reasoning and control beats entangled thinking (Ha 2025)]]", "[[An explicit meta-level makes reasoning controllable (Dong 2025)]]", "[[A survey of self-evolving agents (Gao 2025)]]"]
---

# ReMA: Learning to Meta-think with Multi-agent RL

**One line:** Split the model into a high-level meta-thinking agent (plans, oversight) and a low-level reasoning agent (execution), and train both with aligned multi-agent RL: the meta level *learns* to supervise, and beats single-agent RL on competition math and judge benchmarks.

**Why it matters to us:** The strongest existing version of learned selection: the monitor/controller is not prompted or pipelined, it is *trained* as its own agent with its own objective aligned to the reasoner's. This is the architectural shape our claim generalizes from two agents back into one self-state.

Source: [arXiv 2503.09501](https://arxiv.org/abs/2503.09501) (12 March 2025; NeurIPS 2025). Abstract-level note.

## Claim
Meta-thinking (monitoring, evaluating, controlling one's own reasoning) is better acquired by a dedicated high-level agent trained with multi-agent RL than by asking a single agent to do both ([abstract](https://arxiv.org/abs/2503.09501)).

## Mechanism
- Two hierarchical agents: meta-thinking agent generates strategic oversight and plans; reasoning agent executes.
- Iterative RL with aligned objectives so the two learn to collaborate; extends to multi-turn interaction.

## Evidence
- Outperforms single-agent RL baselines on competitive-level math and LLM-as-a-Judge benchmarks ([abstract](https://arxiv.org/abs/2503.09501)).

## Limits / what they didn't show
- Two agents = two forward passes' worth of parameters serving one cognition; a single-model internalization is not demonstrated.
- The meta agent's oversight is text-level (plans and instructions), not an internal-state readout of the reasoner.
- Correctness and judge tasks; nothing evaluative or open-ended.

## Relevance to taste-lab
**Relevance 3. Section 5.**
- The learned-selection leg of G5 in its clearest form: oversight trained, not scripted.
- The open problem ReMA leaves: collapse the two agents into one model with an internal meta level without losing the trained specialization - that is precisely an architecture-level metacognition question.
- Cite with MERA and Meta-R1 as the "learned vs engineered meta level" spectrum.

## Steal this
- Aligned-objective MARL as the training scheme for a separate evaluator head.
- Their single-agent vs two-agent ablation as the experiment template for "is a dedicated meta level worth it".

## Kaushik's notes
<!-- yours -->
