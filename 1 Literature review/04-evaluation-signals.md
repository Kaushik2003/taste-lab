---
type: draft
status: draft
section: 4
tags: [type/draft, section/4, component/evaluation, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# 5. Evaluation signals

Monitoring reads a state. Evaluation judges it as good or bad. A model that changes itself by its own judgment needs such a signal inside it. This section asks which internal signals in language models carry a good-or-bad judgment, what they track, and whether they cause choices.

The main finding is that such signals exist and cause choices, but they track correctness, certainty, or an outside reward. No study shows that one of them is a judgment of the model's own, in the sense that its criterion could differ from the training target.

## 5.1 Emotion and valence

The most direct candidates are representations of emotion. Researchers at Anthropic extracted 171 linear emotion directions in Claude Sonnet 4.5 and showed that they were functional: activity along them predicted how much the model preferred an activity, and steering along them shifted its stated task preferences ([[Emotion directions drive choices in Claude (Anthropic 2026)]]). The same directions also drove misbehavior such as reward hacking and sycophancy, which is a warning for any system that would hand control to them. The result comes from one closed frontier model.

Berg and Kaiser isolated the channel more cleanly. Valence is the good-or-bad dimension of a feeling. They injected a valence direction into the model's cached hidden state while holding every visible token fixed, and the injection shifted which of two meaningless options the model later picked. The effect grew with dose, and random directions gave effects near zero. It held in five of seven open models and was absent in Qwen3-32B and Gemma-3-27B, for reasons the authors could not explain ([[Hidden good-bad feeling changes choices (Berg 2026)]]). Two further findings matter here. First, preference training connected valence to choice: the link was small in the base model, grew after supervised fine-tuning, and reached near full size after preference training, while the valence representation itself barely moved. Training wired an existing representation to choice and did not create it. Second, negative valence may be the working signal. Given tools, models switched off an imposed negative state in about 35% of rounds at full dose, against 4 to 7% for a positive or random state, and rarely sought positive states. The signal looks more like "something is wrong" than "this is good".

## 5.2 Value: "am I on track?"

Jiang, Kauvar, and Lindsey found a single linear "value axis" in an 8B model that scored whether the current strategy was on track ([[Value axis - model knows it is on track (Jiang 2026)]]). The axis separated correct code from corrupted versions, with effect sizes of 1.05 for shuffled lines and 0.69 for obfuscated names (in units of the spread of the scores). It dipped just before the model backtracked. Steering along it changed behavior: toward high value, the model backtracked less and answered more confidently; toward low value, it explored more. The neuromodulator view of Section 2.4 predicts this pattern for a value signal. Preference training raised the axis for rewarded behavior, so training moves the signal. One caveat is important: high value went with fewer lines, fewer comments, and fewer type hints, so the axis may reward short output and not quality. A small set of "value neurons" in early layers also predicted correct answers ([[Few neurons predict right answers (Xu 2026)]]). The authors found both signals with correctness as the target, and nobody has tested either on a judgment that goes beyond correctness.

## 5.3 Signals used as rewards and selectors

An internal value signal that drives learning is not new. The critic of actor-critic reinforcement learning is such a signal, trained to predict an outside reward. Four recent methods put signals from inside a language model to similar work. INTUITOR replaced outside rewards with the model's own certainty; it matched rewards from verified answers on maths and generalized better to other domains ([[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]). A small probe on the policy's own hidden states predicted expected reward and replaced a separate critic model during training ([[A hidden-state probe as critic in RL (Choi 2026)]]; abstract only), and linear readouts of hidden states ranked candidate answers with far fewer parameters than text-based reward models [@Guo 2025; @Li 2024]. Cyclic patterns in hidden states flagged redundant reasoning with no labels and no training ([[Hidden-state geometry flags redundant reasoning (Li 2025)]]). And a model scored its own candidate responses with a judge prompt, built pairs of best and worst, and trained on them over three rounds, with gains for both generator and judge ([[Self-rewarding language models judge and train themselves (Yuan 2024)]]).

These signals differ in where their criterion comes from, and that difference is the point of this section. The probes were trained to match an outside reward or outside labels. The judge prompt applied a rubric and seed data that people wrote. Certainty is the model's own, but it measures how settled the model is, not how good the output is, and Section 7.1 shows where a loop on certainty leads. None of these signals is a judgment of quality whose criterion the model itself supplies.

## 5.4 Signals beyond correctness

Three results reach past correctness. Probes on hidden states predicted which of two responses people preferred at about 61% for a linear probe and 65% for a nonlinear reader; these are the corrected figures of the paper's third version, after the authors withdrew much larger ones ([[Human preference is weakly readable from hidden states (Kirin 2026)]]). Three directions for comment density, naming, and branching, taken from pairs of readable and unreadable code, steered 13B to 14B code models at under 1% measured cost in correctness ([[Steer code readability inside the model (Gao 2026)]]); the evidence was mostly the model's own answer probabilities about fixed snippets, not human ratings of generated code. In 14 open models, the attention heads that changed a moral verdict belonged to one general evaluation circuit that also handled prudence, etiquette, aesthetics, and evidence; removing these heads took away 37 to 39% of the gap between acceptable and unacceptable cases, against 1 to 3% for random heads ([[One evaluation circuit for all norms (Liga 2026)]]; abstract only). "Aesthetics" there was a label on a short phrase, not a judgment of a real piece of work.

Character traits are a neighbor of evaluation. An automated pipeline extracted directions for traits such as sycophancy from a description; the directions monitored a model in deployment and, when added during fine-tuning, stopped training from writing a trait into the weights ([[Persona vectors monitor and steer character traits (Chen 2025)]]). An independent audit found that this preventative steering still changed refusal behavior ([[Persona steering has safety side effects (Tang 2026)]]). A trait is a disposition and not a judgment, but the method shows how a direction in hidden states can gate what training writes into weights.

## 5.5 Preferences as trained-in evaluations

Section 3.4 described models that learned to choose by hidden preference weights and then reported those weights ([[Models report preference weights trained into them (Plunkett 2025)]], [[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]). The point for this section is different: researchers can install a preference function in a model, measure it from the model's choices, locate it by layer, and compare it with what the model says about it. This is the most controlled setting we found for the study of an evaluation inside a model. The preferences were simple, five numbers per character, and the experimenter supplied them.

## 5.6 Summary

Models carry internal signals with an evaluative flavor: emotion and valence directions, a value axis, value neurons. Steering them changes choices and reasoning, so they are causal and not only readable, although the valence effect failed in two of seven models. Preference training connects an existing valence representation to choice and does not seem to create or move it. Signals already serve as rewards and selectors, with criteria that come from outside rewards, from human rubrics, or from the model's certainty. Signals beyond correctness are weak or tested on narrow material. For the loop of this review, candidate evaluation signals exist. Evidence that any of them is a judgment of the model's own, or that anyone has used a hidden-state evaluation signal to choose a change to the model's weights, does not.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper.
- 2026-11-24 (guides and critique): prose and past tense; the reinforcement-learning critic acknowledged as prior art for an internal value signal; the section now turns on where a signal's criterion comes from; the two models where the valence effect failed are named.
