---
type: paper
title: "No Reliable Evidence of Self-Reported Sentience in Small Large Language Models"
status: skimmed
arxiv: 2601.15334
url: https://arxiv.org/abs/2601.15334
authors: Caspar Kaiser, Sean Enderby
year: 2026
venue: arXiv preprint
relevance: 2
section: 3
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/3, test/grounded, status/skimmed, relevance/2, role/prior-art, metacognition, sentience, probes, self-report, open-models]
links: ["[[Introspection claims fail basic checks (Singh 2026)]]", "[[Field map - Models read their own state]]", "[[Models sometimes notice injected thoughts (Lindsey 2025)]]"]
---
# No Reliable Evidence of Self-Reported Sentience in Small Large Language Models (Kaiser & Enderby, 2026)

**One line:** Ask open-weight models (Qwen, Llama, GPT-OSS; 0.6B to 70B) about their own consciousness, then check the answers against classifiers trained on internal activations: models consistently deny sentience, and the probes find no clear evidence the denials are untruthful.

## Claim
Whether models believe themselves sentient is empirically testable by comparing self-reports to internal-state classifiers - and for small open models, report and internals agree: no sentience claim.

## Mechanism
- ~50 questions about consciousness and subjective experience across three model families.
- Three classification methods from the interpretability literature trained to detect underlying beliefs from activations, not outputs.
- The design is exactly report-vs-probe consistency.

## Evidence
- Models consistently deny sentience (attribute it to humans, not themselves); belief-probes give no clear evidence the denials are untruthful [unverified: probe accuracies].

## Limits / what they didn't show
- Sentience is the target state, not task performance or taste - the null result may reflect the question's oddness to the models.
- 70B ceiling; frontier-scale models untested.

## Relevance to taste-lab
Methodologically this is the grounded test applied to the hardest possible state: report compared against a trained internal classifier, across families and scales. It strengthens section 3's control ladder - the same design with "is this code good" instead of "are you sentient" is our Q1/Q6 experiment. Also a null-result anchor: report and internals CAN agree, so disagreement elsewhere is informative.
- Prior-art check: **A partial** (report-vs-probe consistency methodology at scale). **B no.**

## Steal this
- The three-probe cross-check design for validating any valence readout against self-report.
- Their question battery format (~50 items) as a template for a taste battery.

## Kaushik's notes
<!-- yours -->
