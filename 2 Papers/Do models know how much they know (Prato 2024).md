---
type: paper
title: "Do Large Language Models Know How Much They Know?"
status: skimmed
url: https://aclanthology.org/2024.emnlp-main.348/
authors: Giovanni Prato, et al.
year: 2024
venue: EMNLP 2024
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/3, component/monitoring, status/skimmed, relevance/2, role/prior-art, knowledge-boundary, benchmark]
links: ["[[Models partly know what they do not know (Yin 2023)]]", "[[LLM judgments of learning do not predict memory (Huff 2025)]]"]
---

# Do Large Language Models Know How Much They Know?

**One line:** A benchmark that asks models to enumerate everything they know on a topic, testing whether they recall too much, too little, or the right amount - knowledge-quantity awareness, not just answer-level confidence.

**Why it matters to us:** Most boundary work asks "is this answer right"; Prato asks "how much do I hold on this topic" - a different monitoring variable, closer to the self-model a persistent architecture would need (what domains am I strong in). Section 3's instrument inventory gains a quantity axis.

Source: [ACL Anthology 2024.emnlp-main.348](https://aclanthology.org/2024.emnlp-main.348/) (EMNLP 2024). Abstract-level note.

## Claim
LLMs can be tested on whether they recognize the scope of their own knowledge by asking them to enumerate all information they possess on specific topics; the property emerges unevenly ([abstract](https://aclanthology.org/2024.emnlp-main.348/)).

## Mechanism
- Benchmark: enumerate-all-you-know per topic; scoring for excessive, insufficient, or precise recall against the required information.

## Evidence
- Findings show the emergence of this knowledge-quantity awareness varies across models ([abstract](https://aclanthology.org/2024.emnlp-main.348/)).

## Limits / what they didn't show
- "All information on a topic" is fuzzy to score; the ground-truth boundary of a topic is annotator-defined.
- Enumeration ability confounds with verbosity and recall capacity, not only metacognition.
- Factual topics only.

## Relevance to taste-lab
**Relevance 2. Section 3.**
- Adds the quantity/scope axis to the monitoring taxonomy (answer-level confidence, abstention, success prediction, and now scope of knowledge).
- A scope judgment is exactly what an auto-curriculum loop (MAGELLAN-style) consumes: what do I know a lot vs little about.

## Steal this
- The excessive/insufficient/precise trichotomy as a scoring scheme for any scope-of-knowledge probe.

## Kaushik's notes
<!-- yours -->
