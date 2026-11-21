---
type: paper
title: "Metacognitive Myopia in Large Language Models"
status: skimmed
arxiv: 2408.05568
url: https://arxiv.org/abs/2408.05568
authors: Florian Scholten, Tobias R. Rebholz, Mandy Hutter
year: 2024
venue: arXiv preprint
relevance: 2
section: 6
tier: skim
tests: []
components: [monitoring, controller]
tags: [type/paper, section/6, component/monitoring, component/controller, status/skimmed, relevance/2, role/prior-art, metacognition, bias, framework]
links: ["[[Metacognition - watch and control yourself]]", "[[Monitoring and control between two levels (Nelson 1990)]]"]
---

# Metacognitive Myopia in Large Language Models

**One line:** A framework paper: five seemingly separate LLM biases (redundancy susceptibility, base-rate neglect, frequency-based rules and more) are one syndrome, explained by the absence of monitoring and control over the input.

**Why it matters to us:** It is the human-cognition diagnosis running in reverse: the biases humans overcome *with* metacognition are the ones LLMs show *without* it. That is an argument that monitoring and control are the missing ingredient, not more data.

Source: [arXiv 2408.05568](https://arxiv.org/abs/2408.05568) (10 August 2024). Abstract-level note.

## Claim
A conglomerate of LLM biases is explained as metacognitive myopia: biased samples in the information environment produce five symptoms, and the two components of metacognition (monitoring and control) account for why humans resist and models do not ([abstract](https://arxiv.org/abs/2408.05568)).

## Mechanism
- Five symptoms: integration of invalid embeddings, susceptibility to redundant information, base-rate neglect, frequency-based decision rules, inappropriate higher-order inference for nested data.
- Proposed technical approximations of monitoring and control, e.g. hidden parallel reasoning histories that let the model evaluate risks of myopic inference before responding.

## Evidence
- Framework paper: synthesizes existing bias findings into the five-symptom structure ([abstract](https://arxiv.org/abs/2408.05568)). No new experiments.

## Limits / what they didn't show
- No empirical validation of the framework's causal claim; the five symptoms may have separate mechanical causes.
- The proposed remedies are sketches, not systems.

## Relevance to taste-lab
**Relevance 2. Section 6 (limits/failure modes).**
- Rhetorical structure worth reusing: enumerate failures, then show they are one missing capability, then propose the capability. That is the shape of our G5 argument.
- Warns that input-side monitoring (what to trust) is as absent as output-side monitoring (how well am I doing).

## Steal this
- The five-symptom table format for collapsing scattered failure modes into one diagnosis.
- "Hidden parallel reasoning histories" as a cited early sketch of a monitor channel.

## Kaushik's notes
<!-- yours -->
