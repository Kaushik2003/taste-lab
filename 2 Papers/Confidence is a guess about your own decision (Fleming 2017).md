---
type: paper
title: "Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation"
status: skimmed
arxiv:
url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5178868/
doi: 10.1037/rev0000045
authors: Stephen M. Fleming, Nathaniel D. Daw
year: 2017
venue: Psychological Review 124(1), 91-114
relevance: 3
section: 2
tier: deep
tests: [grounded]
components: [monitoring]
tags: [type/paper, section/2, test/grounded, component/monitoring, status/skimmed, relevance/3, role/prior-art, metacognition, confidence, error-detection, bayesian, foundations, cognitive-science]
links: ["[[Metacognition - watch and control yourself]]", "[[Field map - Models read their own state]]", "[[Monitoring and control between two levels (Nelson 1990)]]", "[[Models mostly know what they know (Kadavath 2022)]]", "[[Trained confidence tracks consistency, not accuracy (Yax 2026)]]", "[[Four tests for own taste]]"]
---

# Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation

**One line:** Confidence is not read straight off the signal that made the decision. It is a separate inference about that decision, the same kind of guess you would make about another person's choice.

**Why it matters to us:** It gives the review a precise word for what a model's meta level does. It also says when self-evaluation can come apart from performance, and why the model's own action is useful evidence for it.

Source: [PubMed Central PMC5178868](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5178868/), full text read (introduction, model sections, error detection, action effects, discussion). DOI [10.1037/rev0000045](https://doi.org/10.1037/rev0000045).

**Words used here:**
- **First-order model:** one internal signal drives both the choice and the confidence in it.
- **Second-order model:** two signals, linked but different. One drives the choice. The other is used to *infer* how good the choice was.
- **Correlation ρ (rho):** how strongly the two signals move together. At ρ = 1 they are the same signal.
- **Metacognitive sensitivity:** how well confidence separates right answers from wrong ones. Measured as meta-d′, compared with task accuracy d′.

## Claim
Self-evaluation is a "second-order" inference on a coupled but distinct decision system. The same maths explains confidence and error detection, and why metacognition can be worse or better than task performance (abstract).

## Mechanism
1. A stimulus produces two noisy internal samples: one for acting (X_act) and one for confidence (X_conf). They are drawn from a joint Gaussian with correlation ρ.
2. The agent acts on X_act.
3. To rate confidence, the agent uses X_conf, its own action, and what it knows about how the two signals relate. It infers the probability that the action was right.
4. This is the same computation an observer would use to judge another actor. First-order models are a special case (ρ = 1 or no confidence noise) (Figure 1 and model sections).

## Evidence
- Simulation only, plus a fit to published data. Error detection (confidence below 0.5) appears when ρ is below 1 and the confidence signal is precise. As ρ nears 1, error detection disappears (Figure 4).
- Prediction: confidence rated after the choice separates right from wrong better than confidence rated before it, because the action carries information. A published anagram study (Siedlecka et al. 2016) matches this for sensitivity; the drop in mean confidence was not significant (Figure 6).
- Meta-d′ > d′ ("better than performance") appears when the confidence signal is less noisy than the decision signal. Pooled human datasets show this often (Figure 8).

## Limits / what they didn't show
- A computational-level account (what is computed, not how neurons do it). No new experiment of their own.
- Two-choice perceptual tasks. Not about preferences or open-ended work.
- Nothing about language models.

## Relevance to taste-lab
**Relevance 3.** Section 2 (foundations).
- It turns [[Monitoring and control between two levels (Nelson 1990)]] into a formal model: the meta level holds its own signal, linked to but not the same as the object level's.
- It explains the results in section 3. A probe can read the decision signal while the model's self-report, which uses a different signal, does not ([[Models do not report injected pain (Ferrara 2026)]]). Confidence can track something other than accuracy ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]).
- **Grounded test** ([[Four tests for own taste]]): "self-evaluation is like judging another actor" is the human version of the cross-model control in [[Models predict themselves better than others do (Binder 2024)]]. If a model's taste report is a second-order inference, a second model with the same view could make it too.
- **Evaluate stage:** a taste signal that is separate from the generation signal is what lets a model notice that its own output is bad. A first-order readout (ρ near 1) could not flag its own mistakes.

## Steal this
- The first-order vs second-order distinction, as a frame for section 2.
- The "rate before vs after acting" prediction: a model's evaluation of a solution should get sharper after it has committed to the solution, if it uses its own action as evidence.
- meta-d′ / d′ as a sensitivity measure that does not mix up accuracy and confidence.

## Harshit's notes
<!-- yours -->
