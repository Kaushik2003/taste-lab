---
type: paper
title: "Metacognition in LLMs: Foundations, Progress, and Opportunities"
status: skimmed
arxiv: 2607.11881
url: https://arxiv.org/abs/2607.11881
authors: Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu, Jordan Thomas, Mark Steyvers, Arman Cohan
year: 2026
venue: arXiv preprint (survey)
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring, controller]
tags: [type/paper, section/2, test/grounded, component/monitoring, component/controller, status/skimmed, relevance/3, role/prior-art, survey, metacognition, calibration, introspection, foundations]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Models can report and control their own activations (Ji-An 2025)]]", "[[Gaps in the field]]"]
---

# Metacognition in LLMs: Foundations, Progress, and Opportunities

**One line:** The first broad survey of metacognition in language models. It sorts the field into measuring, giving and using metacognition, and concludes that models do not yet have robust metacognition.

**Why it matters to us:** It is the review our review must position against. It covers monitoring and control in depth. It does not cover taste, and it does not cover models that change their own weights. That is our space.

Source: [arXiv 2607.11881](https://arxiv.org/abs/2607.11881) (v1 13 Jul 2026). Full HTML read for Sections 2, 4, 5, 8 and 9. Paper list: [github.com/yale-nlp/LLM-Metacognition](https://github.com/yale-nlp/LLM-Metacognition).

**Words used here:**
- **Type 1 / type 2 judgment:** type 1 is the task answer; type 2 is the confidence in that answer.
- **Signal detection theory (SDT):** a method from psychology that separates how well confidence tells right from wrong (sensitivity) from how confident someone is in general (bias).
- **Meta-d′ and M-ratio:** meta-d′ measures how well confidence separates right from wrong answers. The M-ratio divides it by task skill. An M-ratio of 1 means confidence uses all the information the answer had.
- **Neurofeedback measure:** the model gets a score from its own hidden numbers and must report or change it (as in [[Models can report and control their own activations (Ji-An 2025)]]).

## Claim
Metacognition is the ability to monitor, assess and regulate one's own thinking. In language models the evidence is mixed and the field is young: models show some calibration, self-knowledge and introspection, but these are fragile and depend on context ([arXiv](https://arxiv.org/abs/2607.11881), Sec. 8).

## Mechanism (how the survey is built)
- **Measuring (Sec. 4.1):** four kinds of measure: psychology-based (SDT, meta-d′, judgments of learning), neurofeedback-based, confidence-based (AUROC on step-wise confidence) and interpretability-based (probes, concept injection).
- **Findings (Sec. 4.2):** self-knowledge, introspection on internal states, awareness of learned behaviors, and task-specific skills. Model size goes with better metacognition, but on few data points. Post-training (for example RLHF) may lower metacognitive efficiency in STEM questions (one study, Cacioli, cited in Sec. 4.2).
- **Giving metacognition (Sec. 5):** prompts, special architectures, training on self-critique traces, and training with self-generated signals (for example predicting one's own pass rate).
- **Using it (Sec. 6, 7):** better task performance, better learning, and applications.

## Evidence
- A survey: no new experiments.
- Its summary judgment (Sec. 8): models are "not yet capable of robust metacognition". Signs: steady overconfidence, weak judgments of knowledge and resource use, fragile introspection, and distraction by redundant input.
- Judgments of learning in GPT models largely fail (Huff and Ulakçı, cited in Sec. 4.2).
- Introspection on internal states is "sparse" as a research line and "fragile" where shown (Sec. 4.2, citing [[Models sometimes notice injected thoughts (Lindsey 2025)]] and [[Models can report and control their own activations (Ji-An 2025)]]).
- **What it leaves out:** a text search of the HTML finds no use of "taste" or "aesthetic", and no discussion of self-edits to weights or SEAL. Self-improvement appears only as a future direction (Sec. 9). [Our check, by text search of the v1 HTML.]

## Limits / what they didn't show
- Survey written in mid-2026; it misses the November 2026 papers (for example [[Training LMs to watch themselves (Wang 2026)]] and [[Introspection claims fail basic checks (Singh 2026)]]) [unverified for Singh's date].
- It reports findings as "mixed" without weighing study quality. It does not apply the stricter controls (input-only probes, cross-model controls) to the positive results.
- Monitoring of correctness dominates. Monitoring of quality beyond correctness is not a category.

## Relevance to taste-lab
**Relevance 3.** Section 2, and the anchor for how we position the whole review.
- **Our angle is not covered:** the survey has monitor and control, but not "evaluate" as a judgment of good or bad, and not "persist" into weights. Cite it as the state of the field, then show the two missing steps ([[Gaps in the field]]).
- **Grounded test:** its four kinds of measure give the review a ready frame for section 3. Only neurofeedback and interpretability measures reach internal states; the others are behavior only.
- **Threat:** if a reviewer sees our review as a subset of this survey, we lose. The evaluate and persist steps must carry the novelty.

## Steal this
- The four-way split of measures (psychology, neurofeedback, confidence, interpretability) for section 3.
- Meta-d′ and M-ratio: a cleaner score of self-monitoring than plain calibration, because it removes task skill and bias.
- The curated paper list on GitHub as a dedupe check for our own search.

## Harshit's notes
<!-- yours -->
