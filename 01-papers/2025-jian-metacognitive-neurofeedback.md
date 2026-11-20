---
type: paper
title: "Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations"
status: skimmed
arxiv: 2505.13763
url: https://arxiv.org/abs/2505.13763
authors: Li Ji-An, Hua-Dong Xiong, Robert C. Wilson, Marcelo G. Mattar, Marcus K. Benna
year: 2025
venue: preprint (v2, Oct 2025)
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/3, component/monitoring, component/controller, status/skimmed, relevance/3, neurofeedback, metacognition, activations, control]
links: ["[[landscape-metacognitive-monitoring]]", "[[metacognition-monitor-control]]", "[[2026-lindsey-emergent-introspective-awareness]]"]
---

# Metacognitive Monitoring & Control of Internal Activations (Ji-An et al.)

**One line:** A neuroscience-inspired neurofeedback paradigm: via in-context learning, LLMs can report on and control their own activation patterns - but only along a low-dimensional "metacognitive space", a small subset of their neural space, gated by semantic interpretability and variance explained.

## Claim
LLMs have quantifiable, limited metacognition over their own activations: report and control abilities scale with in-context examples, direction interpretability, and variance explained ([abs](https://arxiv.org/abs/2505.13763)).

## Mechanism
- Neurofeedback via ICL: examples teach the model to report or steer specific activation directions; performance quantifies metacognitive access.
- The reportable/controllable directions form a "metacognitive space" of much lower dimensionality than the full neural space.

## Evidence
Abilities depend on number of in-context examples, semantic interpretability of the direction, and variance explained by it [unverified: effect sizes not extracted].

## Limits / what they didn't show
- In-context elicitation, not persistent architecture: the ability lives in the prompt regime.
- Which directions are semantically interpretable is a property of current probes; the "space" may grow with better readouts.
- Safety framing (obfuscation of oversight) dominates; capability framing (using the channel for self-improvement) unexplored.

## Relevance to taste-lab
**The ceiling theorem for any internal readout.** "Models can monitor only a small, interpretable, high-variance subset of their activations" predicts exactly where a valence readout can live and explains why sparse probes work ([[2026-xu-sparse-reward-subsystem]]). If taste is in the metacognitive space, exp01 succeeds; if not, no verbal self-report of taste can work either. Cite beside [[2026-lindsey-emergent-introspective-awareness]] as the quantified version of the same capacity.
- Prior-art check: **A partial** (monitor + control of own activations, but prompt-elicited, no evaluation signal, no loop). **B no.**

## Steal this
- The three gating factors (examples, interpretability, variance explained) as design constraints for the valence probe.
- "Metacognitive space" as the term for where our readout must live.

## Kaushik's notes
<!-- yours -->
