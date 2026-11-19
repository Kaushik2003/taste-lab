---
type: paper
title: "LLMs learn different forms of metacognition when trained to predict their own accuracy"
status: skimmed
arxiv: 2609.33886
url: https://arxiv.org/abs/2609.33886
authors: Nicolas Yax, Stefano Palminteri, Pierre-Yves Oudeyer
year: 2026
venue: arXiv preprint
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, component/monitoring, status/skimmed, relevance/3, role/threat, calibration, self-knowledge, metacognition, foundations]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Models know when they are right (Zhang 2025)]]", "[[Survey of metacognition in language models (Liu 2026)]]"]
---

# LLMs learn different forms of metacognition when trained to predict their own accuracy

**One line:** When you train a model to predict if it will be right, it learns two things: near the training data it tracks real accuracy, but on new topics it tracks only how consistent its answers are. So it stays confident when it is consistently wrong.

**Why it matters to us:** It shows that a trained self-monitoring signal can look calibrated and still read the wrong thing. That is a direct warning for any "the model knows its own quality" claim, including ours.

Source: [arXiv 2609.33886](https://arxiv.org/abs/2609.33886) (v1 27 Sep 2026, v2 read). Full HTML read for Sections 2 and 3. Many correlation values are in math markup that did not render; we give only readable numbers.

**Words used here:**
- **Metacognitive monitoring:** knowing what you know.
- **Verbalized confidence:** the model states how sure it is.
- **Output consistency:** how often the model would give the same answer to the same question. 1 means always the same, 0 means spread evenly over options.
- **Probe:** a small linear readout added on top of the model's last hidden numbers, trained to give one number.
- **QLoRA:** cheap fine-tuning of a compressed model with small add-on weights.

## Claim
Trained confidence reflects two different signals: true accuracy on questions close to the training data, and output consistency on questions far from it. Consistency tracking appears early in training and transfers across datasets; accuracy tracking appears later and stays local ([arXiv abstract](https://arxiv.org/abs/2609.33886)).

## Mechanism
- 10 open models: Qwen2.5-7B (base and instruct), Qwen3.5-9B (base and chat), Llama-2-7b-chat, Llama-3.2-3B-Instruct, phi-4, Mistral-7B-Instruct-v0.3, Ministral-3-3B and 8B (Sec. 2).
- Task: factual multiple choice with no chain of thought (MMLU-Pro with 4 or 10 options, MedMCQA, and two math sets). Train and test splits share no topic category.
- "Accuracy" per question is the probability the model gives to the correct option.
- Training: QLoRA plus a linear probe to one number, following [[Models mostly know what they know (Kadavath 2022)]].
- Analysis: correlate trained confidence with true accuracy and with output consistency, per dataset and per question.

## Evidence
- Before training, verbalized confidence is about uncorrelated with accuracy. After training it correlates strongly, for every model and dataset (Sec. 3.1).
- On MedMCQA, Qwen3.5-9B's trained confidence is U-shaped against accuracy but almost linear against consistency (Sec. 3.2, Fig. 2).
- On the math test set, which sits between training categories, confidence tracks accuracy almost perfectly (Sec. 3.2).
- Models trained on math track accuracy on math, but switch to tracking consistency on MMLU-Pro and MedMCQA. Models trained on MMLU-Pro or MedMCQA track consistency everywhere (Sec. 3.3, Fig. 3).
- Exact correlation values did not render in our copy [unverified].

## Limits / what they didn't show
- Multiple-choice recall only, no reasoning. Open-ended or code tasks may behave differently.
- Models up to about 14B (phi-4) [unverified size]; no frontier models.
- Consistency is a strong proxy for accuracy on easy questions, so the two signals are hard to separate except where the model is consistently wrong.

## Relevance to taste-lab
**Relevance 3.** Section 2 (calibration and self-knowledge), and a threat for section 3.
- **Threat to monitoring claims:** a probe or trained head that "knows when it is right" may just read consistency. Probe papers such as [[Models know when they are right (Zhang 2025)]] should be checked for this confound in the review.
- **For taste:** a "good or bad" readout on code could likewise track how typical or self-consistent the code is, not its quality. Consistency is close to the model's own prior, which is exactly what self-training sharpens ([[Self-reward sharpens then collapses (He 2026)]]).
- **Grounded test:** the right test is the case where consistency and the target come apart (consistently wrong, or consistently ugly).

## Steal this
- Output consistency as a baseline every self-monitoring signal must beat.
- Category-disjoint splits plus distance-to-training analysis to tell local from general monitoring.

## Harshit's notes
<!-- yours -->
