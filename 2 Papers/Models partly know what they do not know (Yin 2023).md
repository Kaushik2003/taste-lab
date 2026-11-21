---
type: paper
title: "Do Large Language Models Know What They Don't Know?"
status: skimmed
arxiv:
url: https://aclanthology.org/2023.findings-acl.551/
authors: Yin et al. [unverified: full author list]
year: 2023
venue: ACL Findings 2023
relevance: 2
section: 3
tier: skim
tests: []
components: [monitoring]
tags: [type/paper, section/3, status/skimmed, relevance/2, role/prior-art, metacognition, self-knowledge, knowledge-boundary, dataset]
links: ["[[Models mostly know what they know (Kadavath 2022)]]", "[[Metacognition - watch and control yourself]]"]
---
# Do Large Language Models Know What They Don't Know? (Yin et al., 2023)

**One line:** The SelfAware dataset of unanswerable questions (five categories) plus answerable counterparts, and an automated uncertainty-detection method, measure whether models know the edge of their own knowledge. They partly do.

## Claim
Self-knowledge - recognizing unanswerable or unknowable questions - is measurable as its own ability, separable from task performance, and current models show it only partially.

## Mechanism
- SelfAware: unanswerable questions from five diverse categories paired with answerable counterparts.
- Automated detection of uncertainty expressions in responses as the self-knowledge measure.

## Evidence
- Models vary in recognizing unanswerability; self-knowledge does not track task accuracy [unverified: numbers].

## Limits / what they didn't show
- Detection leans on surface uncertainty language, which a model can produce without any internal readout - the [[Introspection claims fail basic checks (Singh 2026)]] critique applies.
- 2023-era models; the knowledge boundary has moved.

## Relevance to taste-lab
The knowledge-boundary line is the oldest behavioral form of the monitor. Cite in section 3 as the starting point of the "knows what it knows" thread that Kadavath, Binder and the trained-readout papers extend. For the architecture claim: boundary knowledge that lives only in output habits is exactly what a persistent self-state should internalize.
- Prior-art check: **A partial** (behavioral boundary sense, no internal readout). **B no.**

## Steal this
- Unanswerable-vs-answerable pairing as a control set for any self-report evaluation.

## Kaushik's notes
<!-- yours -->
