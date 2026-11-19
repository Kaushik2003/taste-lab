---
type: paper
title: "Language Models (Mostly) Know What They Know"
status: skimmed
arxiv: 2207.05221
url: https://arxiv.org/abs/2207.05221
authors: Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, et al. (36 authors, last Jared Kaplan)
year: 2022
venue: arXiv preprint (Anthropic)
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, calibration, self-knowledge, self-evaluation, foundations]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Models know when they are right (Zhang 2025)]]", "[[Training LMs to watch themselves (Wang 2026)]]"]
---

# Language Models (Mostly) Know What They Know

**One line:** Large models give well-calibrated odds on multiple-choice questions, can judge whether their own sampled answer is true, and can be trained to predict whether they know an answer before they try.

**Why it matters to us:** This is the classic "self-knowledge" result for language models. It is retrospective and prospective monitoring in the sense of [[Monitoring and control between two levels (Nelson 1990)]], measured only by behavior, with correctness as the target.

Source: [arXiv 2207.05221](https://arxiv.org/abs/2207.05221) (v1 11 Jul 2022, v4 latest). Abstract plus the first 8 pages of the PDF (summary, setup, Figs. 1 to 3) read.

**Words used here:**
- **Calibrated:** when the model says 70%, it is right about 70% of the time.
- **P(True):** the model writes an answer, then is asked "is this answer true?". P(True) is the probability it gives to "True".
- **P(IK):** "probability that I know". A small extra output (a value head) trained to predict, from the question alone, if the model will answer correctly.
- **AUROC:** a score of how well a number separates two groups (here right vs wrong). 0.5 is chance, 1.0 is perfect.
- **Out of distribution (OOD):** test data from a different task than the training data.

## Claim
1. Larger models are well calibrated on varied multiple-choice and true/false questions, if the question has the right format ([arXiv](https://arxiv.org/abs/2207.05221)).
2. So models can judge their own open-ended answers through P(True). This works, is calibrated, and gets better with scale.
3. Self-evaluation improves when the model first sees several of its own samples ("brainstorming") before judging one.
4. Models can be trained to predict P(IK) without seeing any answer. P(IK) partly transfers to new tasks, but its calibration on new tasks is poor.
5. P(IK) rises when relevant source text or a hint is in the context.

## Mechanism
- **Models:** a series of 800M, 3B, 12B and 52B parameter models (PDF p. 6). Some tests also use RLHF chat policies.
- **Self-evaluation tasks:** TriviaQA, Lambada, Arithmetic, GSM8k and Codex HumanEval (code). The model samples an answer at temperature 1, then judges it.
- **Ground truth for P(IK):** the fraction of temperature-1 samples for a question that are correct.
- **P(IK) training:** a value head trained on TriviaQA, then tested on Arithmetic, Python function synthesis and Lambada (Fig. 2).

## Evidence
- Calibration improves with model size across BIG-Bench tasks (Figs. in Sec. 3; exact values are in figures only [unverified]).
- RLHF policies look miscalibrated at first. A simple temperature change makes them fairly well calibrated on several tests (PDF p. 3, Fig. 9).
- The 52B model separates its own right and wrong samples on the five tasks (Fig. 1). The paper reports AUROC per task in Figs. 10 and 11; we did not copy the values [unverified].
- P(IK) trained on TriviaQA has real power to separate known from unknown questions on new tasks, but is not calibrated there (Fig. 2).

## Limits / what they didn't show
- All monitoring is through the model's text output or a trained head. It does not show which internal state carries the signal, or whether the model "reads" it (no grounded test in the strict sense).
- The target is always correctness. Nothing about quality beyond right and wrong, such as style or taste.
- P(IK) needs supervised training on labels from the model's own samples. It is learned self-prediction, close to the "observer" idea in [[Training LMs to watch themselves (Wang 2026)]].
- The monitoring is never used to control generation or learning in this paper. The authors only suggest it as groundwork for honesty.
- Models from 2022, one model family, not public weights.

## Relevance to taste-lab
**Relevance 3.** Foundations section: this is the base result that models have usable self-knowledge about correctness.
- **Monitor stage:** shows prospective (P(IK)) and retrospective (P(True)) monitoring both exist. Later probe papers ([[Models know when they are right (Zhang 2025)]]) read the same kind of signal from hidden states.
- **Gap it leaves:** monitoring of "is it good?" when "is it right?" is fixed. That is the gap for taste ([[Gaps in the field]]).
- **Threat:** none directly. But it sets a high bar: a new monitoring paper must show something more than calibrated self-evaluation of correctness.

## Steal this
- P(True) with brainstorming: let the model see several of its own candidates before it judges one. This is a cheap reasoning-level control baseline.
- Ground-truth P(IK) as the fraction of correct samples: a clean way to label "does the model know" without human raters.

## Harshit's notes
<!-- yours -->
