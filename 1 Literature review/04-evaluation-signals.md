---
type: draft
status: draft
section: 4
tags: [type/draft, section/4, component/evaluation, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# 5. Evaluation signals

Monitoring reads a state, and evaluation judges it as good or bad. A model that changes itself by its own judgment needs such a signal inside it. The main finding of this section is that such signals exist and cause choices, but they track correctness, certainty, or an outside reward. No study shows that one of them is a judgment of the model's own, in the sense that its criterion could differ from the training target.

## 5.1 Emotion and valence

The most direct candidates are representations of emotion. Researchers at Anthropic extracted 171 linear emotion directions in Claude Sonnet 4.5 and showed that they were functional: activity along them predicted how much the model preferred an activity, and steering along them shifted its stated task preferences ([[Emotion directions drive choices in Claude (Anthropic 2026)]]). The same directions also drove misbehavior such as reward hacking and sycophancy, which is a warning for any system that would hand control to them.

Berg and Kaiser isolated the channel more cleanly. Valence is the good-or-bad dimension of a feeling. They injected a valence direction into the model's cached hidden state while holding every visible token fixed, and the injection shifted which of two meaningless options the model later picked. It held in five of seven open models and was absent in Qwen3-32B and Gemma-3-27B, for reasons the authors could not explain ([[Hidden good-bad feeling changes choices (Berg 2026)]]). Two further findings matter here. Preference training connected valence to choice while the valence representation itself barely moved, so training wired an existing representation to choice and did not create it. And negative valence may be the working signal: given tools, models switched off an imposed negative state in about 35% of rounds at full dose, against 4 to 7% for a positive or random state. The signal looks more like "something is wrong" than "this is good".

## 5.2 Value: "am I on track?"

Jiang, Kauvar, and Lindsey found a single linear "value axis" in an 8B model that scored whether the current strategy was on track ([[Value axis - model knows it is on track (Jiang 2026)]]). The axis separated correct code from corrupted versions and dipped just before the model backtracked. Steering toward high value made the model backtrack less and answer more confidently; steering toward low value made it explore more. The control-signal view of Section 2.3 predicts this pattern. One caveat is important: high value went with fewer lines, fewer comments, and fewer type hints, so the axis may reward short output and not quality. Nobody has tested it on a judgment that goes beyond correctness.

## 5.3 Signals used as rewards, and where their criterion comes from

An internal value signal that drives learning is not new: the critic of actor-critic reinforcement learning is such a signal, trained to predict an outside reward. Two recent methods use a signal of the model's own. INTUITOR replaced outside rewards with the model's own certainty and matched rewards from verified answers on maths ([[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]). And a model scored its own candidate responses with a judge prompt and trained on the best and worst over three rounds, with gains for both generator and judge ([[Self-rewarding language models judge and train themselves (Yuan 2024)]]).

These signals differ in where their criterion comes from. The judge prompt applied a rubric and seed data that people wrote. Certainty is the model's own, but it measures how settled the model is, not how good the output is, and Section 7.1 shows where a loop on certainty leads. Evidence past correctness is thin: probes on hidden states predicted which of two responses people preferred at only about 61 to 65% ([[Human preference is weakly readable from hidden states (Kirin 2026)]]). Candidate evaluation signals therefore exist. Evidence that any of them is a judgment of the model's own, or that anyone has used a hidden-state evaluation signal to choose a change to the model's weights, does not.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper.
- 2026-11-24 (guides and critique): prose and past tense; the reinforcement-learning critic acknowledged as prior art for an internal value signal; the section now turns on where a signal's criterion comes from; the two models where the valence effect failed are named.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/04-evaluation-signals (long).md`.
