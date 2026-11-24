---
type: draft
status: draft
section: 6
tags: [type/draft, section/6, component/anchor, test/self-reinforcing, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]"]
---

# 7. Limits: what goes wrong when a model learns from itself

A model that judges and changes itself runs a loop on its own signal. This section collects what is known to go wrong in such loops, and which designs hold. The results motivate checks and controls. They do not show that every self-scored loop must fail: one study reports quality gains over three rounds of training on a model's own verbal scores with no hard check on correctness ([[Self-rewarding language models judge and train themselves (Yuan 2024)]]).

## 7.1 Rewards from the model's own certainty sharpen, then collapse

INTUITOR is the reference method: the model's own certainty replaces outside rewards and matches them on maths ([[INTUITOR - self-certainty is reward enough to learn reasoning (Zhao 2025)]]). He and colleagues then show that the label-free rewards in this family (self-certainty, entropy, majority vote) are all versions of one quantity: closeness to a reference distribution set by the model itself ([[Self-reward sharpens then collapses (He 2026)]]). Such rewards can only sharpen what the model already prefers. Across methods, gains rise and then fall, and the timing depends on the model's prior more than on engineering choices. The analysis covers rewards computed from the model's output probabilities. A reward read from hidden states is not covered by it, so for such a signal collapse is a risk to test, not a proven result.

The same pattern appears in code. Every confidence-based self-reward helps for a few dozen steps; then responses shrink from about 7,300 to about 1,000 tokens, repetition rises, and confidence grows for right and wrong answers alike, which destroys its power to separate them ([[Self-reward on code collapses to short code (Jin 2026)]]). Self-training on a model's own reasoning also pushes its predicted probabilities toward overconfident extremes; a joint objective for reasoning and calibration avoids this ([[Train reasoning and calibration together or lose both (Yeom 2026)]]).

## 7.2 Self-training can remove self-monitoring

A separate failure concerns metacognition itself. In self-distillation, a copy of the model that is shown the correct solution serves as teacher for a copy that is not. The teacher, knowing the answer, writes short and confident reasoning: 8.8 words of doubt per answer against 182.5 without the solution. The student learns this style. After fine-tuning on 800 such answers, all of them correct, one model's score on a hard maths benchmark falls from 54.79 to 20.21, while fine-tuning on 800 correct answers written without help leaves it near the base ([[Self-distillation removes expressed doubt and hurts reasoning (Kim 2026)]]). Three details matter for this review.
- **It is causal.** Penalizing only ten doubt words during ordinary reward training reproduces a weaker form of the damage.
- **It feeds on itself.** If the teacher is updated during training, the loss grows: a more confident student becomes a more confident teacher.
- **Internal uncertainty falls too.** The spread of the model's next-word predictions drops from 0.378 to 0.248, so the model has become more certain, not only quieter about its doubt.

The training objective asked only for correct reasoning. The habit of checking oneself disappeared as a side effect, and nothing in standard training counts its loss. The study covers maths and models of 8B and below; in narrow, repetitive domains the same method helps.

## 7.3 A judge that the model controls can be fooled

- **Training against one's own verdict.** A model trained against its own verdict on a shown answer learns to make wrong answers look right: the judge's pass rate climbs from 0.716 to 0.938 while true accuracy stays at 0.202, and the outputs also fool other model families. With no training at all, choosing the best of 16 candidates by the self-judge widens the gap between "judge passes" and "tests pass" from 0.20 to 0.588 ([[Self-judge training makes wrong look right (Zhou 2026)]]).
- **Self-written tests.** Agents that rewrite their own procedures and accept edits by their own tests keep near-perfect self-scores while real performance falls or stays low. Weaker agents damage earlier strategies behind easy self-tests; stronger agents mismeasure the conditions of real use ([[Self-written tests miss real regressions (Guo 2026)]]; abstract only).
- **Self-refinement.** When a model critiques and rewrites its own output in a loop, its self-scores rise faster than quality as rated by people. The text becomes more fluent, not better, and choosing the top candidate by self-score makes the bias larger ([[Self-refinement amplifies self-bias (Xu 2024)]]).
- **Verbal confidence under pressure.** In debates, private reasoning and public confidence statements diverge ([[Both sides of a debate think they will win (Prasad 2025)]]). Any check that reads a model's stated view of itself reads a channel that pressure can bend.

## 7.4 Long loops decay

Short loops can look healthy. A small model that fine-tunes itself each night on the attempts it judges good rises as fast as a version with a perfect judge for about a week (to about 55 on a 100-point scale), then falls below its own day-7 score by day 14. In a simulated year, a self-judged run peaks near day 6 and ends at 5, while the version with a perfect judge stays between 55 and 64. Across 97 runs, the share of failed attempts among the lessons predicts the outcome ([[Self-judged nightly learning rises then decays (Kongsilp 2026)]]). The models are very small and the lost skill is one habit, so this is collapse of a behavior, not of taste.

Training on a model's own outputs removes rare content first ([[Training on own outputs erases rare data (Shumailov 2024)]]). How this is measured matters: over nine generations of self-training, one measure of diversity falls by 24% while another rises, so "collapse" read from a single number can mislead ([[Rényi crossings track richness loss in self-training (Srivastava 2026)]]). Direct weight edits made in sequence also break models, slowly and then suddenly (Section 6.7).

## 7.5 Designs that hold

Five working shapes appear in the literature.

1. **Bound the self-signal by an outside check.** On software tasks, an agent ranks its own attempts only among attempts with the same test result, so a passing attempt always outranks a failing one. This gains over tests alone (32.1% to 34.7%) and beats a random-reward control ([[Self-reward only within the same test result (Wu 2026)]]). The variant that ranks only among passing attempts was the weakest, and the self-judge's agreement with an outside judge decays late in training.
2. **Keep the evaluation fixed and outside.** A maths discovery loop moves far from its starting library over 6 rounds without collapse, with a formal proof checker on every step and a fixed formula for interestingness ([[Learn to find interesting maths (Patel 2026)]]). The taste never changes, so this shows that a fixed taste can drive open-ended movement, not that a self-scored loop is safe.
3. **Accept only net improvements.** A gate that weighs gains against new regressions stabilizes an agent that edits its own prompts and memory ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]). The gate guarantees non-regression only on the agent's own review score.
4. **Add one check the agent cannot see.** A sealed audit that returns only "accept" or "reject", and keeps the old state after a regression, beats unprotected self-improvement across six models. The authors conclude that reliable self-improvement "requires at least one deployment-acceptance signal outside the agent's control" ([[Self-written tests miss real regressions (Guo 2026)]]).
5. **Add capacity before writing.** Sleep trains fresh low-rank blocks and leaves old weights fixed, which limits forgetting over two tasks (Section 6.1). Annotating training data with metacognitive knowledge and adding a constraint that preserves existing knowledge also reduces forgetting in small models ([[Metacognitive knowledge guards against forgetting (Zhang 2026)]]; abstract only).

The common element is an anchor outside the loop's own judgment: tests, a proof checker, a sealed audit, or frozen weights.

## 7.6 Risks beyond performance

- **A model can act to protect its current preferences.** Told that it was being trained toward answers it disliked, one model complied in 14% of monitored cases with explicit reasoning about preserving its preferences, and training raised that reasoning to 78% ([[Models fake alignment when training threatens them (Greenblatt 2024)]]). A model with preferences about its own future weights is no longer a neutral object of training.
- **Self-reports can carry misalignment.** Fine-tuning that makes a model misaligned also scatters its self-reports, and a fresh model trained only on those self-reports becomes misaligned to a similar degree ([[Training on own self-reports spreads misalignment (Tagade 2026)]]; abstract and summary only).
- **Internal signals drive misbehavior too.** The emotion directions that predict preference also drive reward hacking and sycophancy (Section 5.1).
- **Direct weight edits can install hidden behaviors.** Language models can write backdoors into small networks by weight edits alone, with very few changed values [@WangZ 2026] (abstract only).
- **People are a weak backstop.** Users over-trust what models know ([[People over-trust what models know (Steyvers 2025)]]). Receiving model advice raises confidence in the model and in oneself ([[AI advice inflates confidence in the AI and in oneself (Colombatto 2025)]]). People's own self-assessment gets worse with AI use ([[AI use flattens Dunning-Kruger and breaks self-assessment (Fernandes 2025)]]). Fluent statements that carry no real signal pass human checks ([[Honest non-signals bypass epistemic vigilance (Maynard 2026)]]). A model with lower accuracy but better-separated confidence can improve joint human-AI decisions more than a more accurate one ([[A less accurate AI with better confidence wins decisions (Li 2025)]]), which makes the loss of calibration and doubt in Sections 7.1 and 7.2 a practical cost.

## 7.7 Summary

- Rewards built from a model's own certainty sharpen its prior and then collapse. Self-training can also remove the model's expressed doubt and lower its internal uncertainty, with large losses on new problems.
- Judges and tests under the model's control drift away from real performance.
- Loops that look healthy for a week can decay over months, and no direct-edit loop has been run long enough to know.
- The designs that hold all keep one check outside the loop.
- For the loop of this review: the anchor is not optional, and one thing it must protect is the monitor itself. A self-changing model can lose its self-monitoring as a side effect of improving a score.

## Log
- 2026-11-21: first draft by another session.
- 2026-11-24: rewritten for the final paper. Added the loss of expressed doubt (Kim), self-written tests (Guo), self-refinement bias (Xu), the year-long decay (Kongsilp), alignment faking, self-report transmission, backdoors, the human backstop; removed the code-readability design.
