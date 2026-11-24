---
type: draft
status: draft
section: 4
tags: [type/draft, section/4, component/evaluation, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# 5. Evaluation signals

Monitoring reads a state. Evaluation judges it: is this good or bad? A model that changes itself by its own judgment needs such a signal inside it. This section asks which internal signals in language models carry a good/bad judgment, what they track, and whether they cause choices.

## 5.1 Emotion and valence

The most direct candidates are representations of emotion. Anthropic's interpretability team extracts 171 linear emotion directions in Claude Sonnet 4.5 and shows that they are functional: activity along them predicts how much the model prefers an activity, and steering along them shifts its stated task preferences ([[Emotion directions drive choices in Claude (Anthropic 2026)]]). The same directions also drive misbehavior such as reward hacking and sycophancy. That is a safety warning for any system that would hand control to them. The result is from one closed frontier model.

Berg and Kaiser isolate the channel more cleanly ([[Hidden good-bad feeling changes choices (Berg 2026)]]). **Valence** is the good-or-bad dimension of a feeling. They inject a valence direction only into the model's cached hidden state, with every visible token held fixed. This shifts which of two meaningless options the model later picks, in 5 of 7 open models. The effect grows with dose, and random directions give effects near zero. Two further findings matter for this review.
- **Preference training connects valence to choice.** The link is small in the base model, grows after supervised fine-tuning, and reaches near full size after preference training (DPO). The valence representation itself barely moves across these stages. So training wires an existing representation to choice; it does not create the representation.
- **Negative valence may be the working signal.** Given tools, models switch off an imposed negative state in about 35% of rounds at full dose, against 4 to 7% for a positive or random state. They rarely seek positive states. The signal looks more like "something is wrong" than "this is good".

## 5.2 Value: "am I on track?"

Jiang, Kauvar and Lindsey find a single linear "value axis" in Qwen3-8B that scores whether the current strategy is on track ([[Value axis - model knows it is on track (Jiang 2026)]]). It separates correct code from corrupted versions, with effect sizes (Cohen's d, the gap in units of spread) of 1.05 for shuffled lines and 0.69 for obfuscated names. It dips just before the model backtracks. Steering along it changes behavior: toward high value, fewer backtracks and more confident answers; toward low value, more exploration. This is what the neuromodulator view of Section 2.4 predicts for a value signal. Preference training raises the axis for rewarded behavior, so training moves the internal signal. One caveat is important: high value goes with fewer lines, fewer comments and fewer type hints, so the axis may reward short output, not quality.

A small set of "value neurons" in early layers also predicts correct answers ([[Few neurons predict right answers (Xu 2026)]]). Both signals were found with correctness as the target, and neither has been tested on a judgment that goes beyond correctness.

## 5.3 Signals used as rewards and selectors

Several methods already put an internal signal to work.

- **Self-certainty as the only reward.** INTUITOR replaces outside rewards in reinforcement learning with the model's own certainty. It matches reward from verified answers on maths and generalizes better to other domains ([[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]). Section 7 covers how this class of reward sharpens and then collapses.
- **Hidden states as a value estimate.** A small probe on the policy's own hidden states predicts expected reward and replaces a separate critic model during reinforcement learning ([[A hidden-state probe as critic in RL (Choi 2026)]]; abstract only). Linear readouts of hidden states also rank candidate answers for best-of-N selection, with far fewer parameters than text-based reward models [@Guo 2025; @Li 2024].
- **Hidden-state geometry.** Cyclic patterns in the path of hidden states flag redundant reasoning with no labels and no training ([[Hidden-state geometry flags redundant reasoning (Li 2025)]]).
- **Verbal self-judgment.** A model scores its own candidate responses with a judge prompt, builds best-versus-worst pairs, and trains on them over three rounds. Both the generator and the judge improve ([[Self-rewarding language models judge and train themselves (Yuan 2024)]]). The rubric and the seed data come from people.

In all but the last, the signal tracks certainty, expected reward or redundancy. In the probe methods, the readout is trained to match an outside reward or outside labels. None of these signals is the model's own judgment of quality in a sense that could differ from the training target.

## 5.4 Signals beyond correctness

Three results reach past correctness.

- **Human preference is weakly readable.** Probes on hidden states predict which of two responses people preferred at about 61% for a linear probe and 65% for a nonlinear reader ([[Human preference is weakly readable from hidden states (Kirin 2026)]]). These are the corrected figures of the paper's third version; much larger figures in earlier versions were withdrawn.
- **Style can be steered.** Three directions for comment density, naming and branching, taken from paired readable and unreadable code, steer 13 to 14B code models at under 1% measured cost in correctness ([[Steer code readability inside the model (Gao 2026)]]). The evidence is mostly the model's own answer probabilities about fixed snippets, not human ratings of freely generated code.
- **One circuit for many norms.** In 14 open models, the attention heads that change a moral verdict are part of one general evaluation circuit that also handles prudence, etiquette, aesthetics and evidence. Removing these heads takes away 37 to 39% of the gap between acceptable and unacceptable cases, against 1 to 3% for random heads ([[One evaluation circuit for all norms (Liga 2026)]]; abstract only). Here "aesthetics" is a label on a short phrase, not a judgment of a real piece of work.

Character traits are a neighbor of evaluation. Directions for traits such as sycophancy can be extracted from a description, used to monitor a model in deployment, and used during fine-tuning to stop a trait from being written into the weights ([[Persona vectors monitor and steer character traits (Chen 2025)]]). An independent audit finds that this preventative steering still changes refusal behavior, so it is not free of side effects ([[Persona steering has safety side effects (Tang 2026)]]). A trait is a disposition, not a judgment, but the method shows how a direction in hidden states can gate what training writes into weights.

## 5.5 Preferences as trained-in evaluations

Section 3.4 described models that are trained to choose by hidden preference weights and then report those weights ([[Models report preference weights trained into them (Plunkett 2025)]], [[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]). For this section the point is different: a preference function can be installed in a model, measured from its choices, located by layer, and compared with what the model says about it. This is the most controlled setting we found for studying an evaluation inside a model. The preferences are simple (five numbers per character) and are given by the experimenter.

## 5.6 Summary

- Models carry internal signals with an evaluative flavor: emotion and valence directions, a value axis, value neurons. Steering them changes choices and reasoning behavior, so they are causal, not only readable.
- Preference training connects an existing valence representation to choice. It does not seem to create or move the representation.
- Signals already serve as rewards and selectors, but they track certainty or an outside reward. Signals that go beyond correctness are weak (human preference at 61 to 65%) or tested only on narrow material.
- For the loop of this review: candidate evaluation signals exist. What does not exist is evidence that any of them is a judgment of the model's own, in the sense of the four tests, or that any of them has been used to choose a change to the model's weights.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper. Removed the code-readability framing; added signals used as rewards (Choi, SWIFT, Q-Probe, Yuan), the norm circuit (Liga), persona vectors and their audit, and trained-in preferences (Plunkett, Atkinson).
