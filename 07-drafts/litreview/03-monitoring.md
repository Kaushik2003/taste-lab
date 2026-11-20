---
type: draft
status: draft
tags: [type/draft, litreview, section/3]
links: ["[[landscape-metacognitive-monitoring]]", "[[metacognition-monitor-control]]", "[[four-taste-tests]]"]
---

# 3. Monitoring

The first stage of the loop asks what a model's hidden states say about its own work, and whether the model itself - not an outside probe - can read them. The short answer so far: probes can, self-report mostly cannot.

## 3.1 Hidden states encode self-relevant signals

The strongest positive result is that reasoning models encode whether their own intermediate answers are correct. Zhang et al. segment reasoning traces at self-correction boundaries and train a small probe on the hidden state at each segment's end ([[2025-zhang-reasoning-models-know-when-right]]). The probe predicts intermediate-answer correctness with ROC-AUC above 0.7 across models and datasets (above 0.9 in the best case), the signal is present *before* the answer is written out, and it is calibrated enough to act on: stopping generation at the first intermediate answer the probe accepts keeps MATH accuracy at 88.2% while cutting tokens by about 24%. This is the simplest working monitor-control loop in the literature - and the reader is an external probe trained on externally graded labels.

Xu, Yuksekgonul and Zou sharpen the picture ([[2026-xu-sparse-reward-subsystem]]). Fewer than 1% of hidden-state coordinates suffice to predict whether the model will solve a problem ("value neurons"), and a second sparse set tracks step-level temporal-difference error ("dopamine neurons") that works as a process reward model for search, beating random candidate selection by about 6 points on MATH500. Zeroing the top value neurons collapses math accuracy (75.2% to 20.3% on average) while factual recall barely moves. Both readouts are again probes trained on correctness labels - and the authors note the method is untested on tasks without a verifiable reward, which is precisely the regime a taste signal must occupy.

## 3.2 Self-report fails where probes succeed

Against this, the model's own verbal channel is unreliable. Ferrara injects emotion directions into open 7-32B models and asks them to report their state ([[2026-ferrara-all-quiet-pain]]): in 106 of 108 conditions the models reveal less than 2.5 points more than their altered text alone reveals, and a 32B model names an injected pain state in 0 of 2,880 trials - while a linear probe separates pain from sadness at 98-100% balanced accuracy, the state changes behavior (photo deletions rise to 80-83% under pain), and a LoRA can be *trained* to report it. The state exists, matters, and is decodable; the report is missing.

Singh, Linzen and Ravfogel explain why positive introspection results should be distrusted ([[2026-singh-llm-introspection-reality-check]]). A test demonstrates introspection only if the answer cannot be recovered from the input alone (privileged access) and comes from a representation *about* the first-order state (second-order computation, in the sense of [[2017-fleming-self-evaluation]]). Re-running three popular paradigms with controls, they find an input-only layer-0 probe matches the model's in-context self-reports, and concept-injection detection falls to near chance once "my input was manipulated" is offered as an answer, with models also calling purely textual "gaslight" prompts activation interventions. What looks like introspection is largely sensitivity to "something is off" in the text.

Karpf et al. occupy a middle position ([[2026-karpf-metacognitive-steering]]): an external controller reads a frozen frontier model's mid-layer activations, classifies its reasoning regime (explore, converge, scrutinize - linearly separable, recoverable from ten neurons at about 99%), and steers with vectors learned from scientists' interventions. The internal state is readable and steerable, but the reader and the directions are again external, and the evidence is qualitative.

## 3.3 Where monitoring stands

The monitor stage has an existence proof and a methodological bar. The bar (privileged access, second-order computation, input-only baselines) comes from [[2026-singh-llm-introspection-reality-check]]; the existence proof (decodable, behaviorally active internal states) from [[2026-ferrara-all-quiet-pain]], [[2025-zhang-reasoning-models-know-when-right]] and [[2026-xu-sparse-reward-subsystem]]. What nobody has shown is a model reading such a signal *about a quality its labels did not teach* - correctness is the only signal monitored so far. Reading a preference signal among solutions that are all correct is the open problem the gating experiment addresses ([[code-quality-signal-T1]]).
