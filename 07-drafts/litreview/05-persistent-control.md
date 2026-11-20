---
type: draft
status: draft
tags: [type/draft, litreview, section/5]
links: ["[[landscape-persistent-control]]", "[[self-weight-updates]]", "[[permanent-steering-change-T5]]"]
---

# 5. Persistent control

Control at the reasoning and activation levels is temporary: the preference dies with the context. The persist stage asks how a change gets written into the weights. The mechanisms now exist in two families - learned self-edits and closed-form edits - and this is the most crowded part of the landscape. What none of them does is take the direction from the model's own evaluation.

## 5.1 Learned self-edits

SEAL has the model write its own finetuning data and hyperparameters ("self-edits"), applies a LoRA/SFT update, and uses an outer RL loop to reward the self-edits that improve downstream performance ([[2025-zweiger-seal]]). This is genuine self-directed weight change, but the reward is external task performance: the model learns to learn, not what it likes. It is the mechanism for consolidating *distributed* changes such as style, with the evaluator swapped out.

## 5.2 Closed-form edits: steering directions written into weights

The second family starts from the observation that a behavior direction found in activation space can be made permanent without training. Arditi et al. showed a single direction mediates refusal across 13 chat models, and that projecting it out of every matrix writing to the residual stream removes the behavior exactly and permanently, with capabilities mostly intact ([[2024-arditi-refusal-direction]]); they also note that adding a direction at inference is a constant shift writable as a bias change, and that the model's self-report is not updated by the weight change - it still describes its old policy. ThinkEdit localizes "how long to think" to a direction and ablates it from about 4% of attention heads, lifting math accuracy mostly on problems the model used to under-think ([[2025-sun-thinkedit]]). Steer2Edit generalizes to additive edits: score every attention head and MLP neuron by alignment with a steering vector and write sparse closed-form rank-one edits into the best-aligned components, beating inference-time steering at matched utility across safety, truthfulness and reasoning length ([[2026-sun-steer2edit]]) - though with real utility costs against the base model (about 10 accuracy points in the reasoning-length case), and with reasoning length, the behavior nearest to style, landing mostly in MLP neurons rather than one head. TFTV derives a rank-one edit per attention output matrix from forward-pass statistics alone, controlling traits more strongly than the steering vector itself with MMLU nearly unchanged, and supports add, subtract and compose ([[2026-perin-training-free-task-vectors]]).

## 5.3 Weight-space programming

A parallel line skips directions entirely and lets a frontier LLM edit weights directly. Weight-space programming has the LLM read raw weights, localize a mechanism, and write targeted edits with no gradients - fixing repetitive reasoning loops in a 0.8B model (MATH-500 7.9% to 48.1% editing about 0.016% of weights) ([[2026-takehi-weight-space-programming]]). Fischetti's follow-up finds the anti-loop edit behaves like a nearly constant bias along one direction, and that a sort over 8 low-variance neurons matches the original LP-based edit ([[2026-fischetti-just-sort-it]]) - evidence that at least some weight edits *are* steering vectors baked in. WeightCode extends the paradigm from repair to installation: executable weight programs install new capabilities (unseen command compositions 0% to 99.8% exact match; 8.84-17.62 net points of corruption robustness), the retained program reruns on independently trained networks keeping 83-110% of the gain, and programs stack on earlier edits ([[2026-li-weightcode]]). Its retention rule - keep the best candidate whose old-input loss stays inside a hard bound - is the non-regression gate any repeated self-editing loop will need.

## 5.4 Where persistence stands

Writing a direction into weights is solved several times over, to the point that a thread proposing exactly this was killed as prior art ([[permanent-steering-change-T5]]). Three things remain undone. In every case, someone else picks the direction: experimenter contrast sets, an external judge, or a frontier agent - never the model's own evaluation of its own work. Nobody reports the recovery ratio: how much of an inference-time steering gain an edit keeps at matched strength. And nobody has run repeated self-chosen edits over time, which is where the collapse dynamics of Section 6 bite. The open cell is not the mechanism; it is the source of the direction.
