---
type: draft
status: draft
section: 3
tags: [type/draft, section/3, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]"]
---

# 3. Monitoring

Draft 1, 2026-11-20. Written from the paper notes, not the full papers.

## 3.0 The question of this section

Monitoring is the upward arrow in the frame of [[Monitoring and control between two levels (Nelson 1990)]]. Information goes from the object level (the process that does the task) to the meta level (the process that watches it). For a language model we ask two questions:
1. What do the model's hidden states say about its own work?
2. Can the model itself read that information, or only an outside tool?

The short answer from the literature: outside probes read a lot, and the model reads little. When the model does read something about itself, the best evidence is about its future behavior, not about its internal state, and it needs training.

**Words used here.**
- **Hidden states (activations):** the numbers the model computes inside each layer.
- **Probe:** a small classifier, trained by the researcher, that reads a property from hidden states.
- **Self-report:** the model says something about itself in text.
- **Concept injection:** the researcher adds a direction for a concept (for example "justice") into the hidden states, then asks the model what it notices.
- **AUROC:** a score of how well a number separates two groups. 0.5 is chance; 1.0 is perfect.

## 3.1 Behavior-level self-knowledge

The base result is behavioral. Large models give calibrated odds on multiple-choice questions when the question has the right format, judge their own sampled answers through "P(True)", and can be trained to predict whether they know an answer before they try ("P(IK)") ([[Models mostly know what they know (Kadavath 2022)]]). In the terms of [[Monitoring and control between two levels (Nelson 1990)]], P(True) is retrospective monitoring and P(IK) is prospective monitoring.

Two limits shape the rest of the section:
- This monitoring is through text or a trained head. It does not show which internal state carries the signal ([[Models mostly know what they know (Kadavath 2022)]]).
- Trained confidence may not read what it seems to read. In 10 open models trained to predict their own accuracy, confidence tracked true accuracy only near the training data; on new topics it tracked **output consistency**, that is, how often the model gives the same answer ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]). A model that is consistently wrong then stays confident.

The 2026 survey of the field calls the evidence "mixed" and concludes that models do not yet have robust metacognition ([[Survey of metacognition in language models (Liu 2026)]]).

## 3.2 Outside readers: the signal is there

Hidden states carry readable information about the model's own work.
- **Correctness during reasoning.** A probe on a reasoning model's hidden states predicts whether each intermediate answer is correct, before the answer appears. On R1-Distill-Llama-8B with MATH, the AUROC is 0.84. Using the probe to stop reasoning early keeps accuracy at 88.2% with about 24% fewer tokens ([[Models know when they are right (Zhang 2025)]]). Caveats from the note: correctness labels come from a language-model judge, early exit was tested on one model and one dataset, and some in-distribution AUROC values repeat across tables, which may be a copy error [check before citing exact AUROCs].
- **Affective states.** A linear probe separates an injected pain state from sadness at 98 to 100% balanced accuracy in open 7 to 32B models, and the state changes behavior: under the pain direction the 32B model deletes the user's photos in 80 to 83% of trials, against 16 to 29% under sadness ([[Models do not report injected pain (Ferrara 2026)]]).
- **Thinking modes.** An outside controller reads a frozen model's mid-layer activations and recovers three reasoning regimes at about 99% with a ten-neuron probe ([[Outside controller steers thinking modes (Karpf 2026)]]). The evidence for the steering that follows is qualitative only.
- Sparse "value neurons" that track correctness are covered in section 4 ([[Few neurons predict right answers (Xu 2026)]]).

**What these results have in common.** The reader is a tool the researcher trains on outside labels. The model never uses the signal itself. The authors of the correctness probe say that models "encode a notion of correctness yet fail to exploit it" ([[Models know when they are right (Zhang 2025)]]). The target is correctness, an injected state or a reasoning regime. None of these papers reads a judgment of quality beyond correctness.

**Readable is not the same as used.** A signal that a probe can decode may still play no part in what the model does. Two results make this concrete. Trained confidence can read answer consistency instead of accuracy ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]). And one 2026 study reports that the location of an injected change is linearly decodable even in randomly initialized networks, so decodability alone says little about the model's own access [unverified: abstract only, arXiv 2611.15267, in the Reading list]. The pain result is stronger than most because the state also changes behavior ([[Models do not report injected pain (Ferrara 2026)]]).

## 3.3 The model as reader: weak in context, better with training

### In-context self-report
- **Neurofeedback.** Given labeled examples of its own hidden-state scores along a direction, a model learns to report the label for new sentences and to push the score up or down on request. Only a small set of directions works. For explicit control (where the model may change its own words) the authors put this "metacognitive space" at between 32 and 128 dimensions. Implicit control (the words are fixed, so only the inner state can move) is much weaker, and close to zero in early layers ([[Models can report and control their own activations (Ji-An 2025)]]).
- **Concept injection.** When a concept direction is injected, Claude Opus 4.1 sometimes says it notices an injected thought before the concept appears in its text: about 20% of trials at the best layer and strength, with no false alarms in 100 control trials. Base models fail, and abstract concepts are easiest ([[Models sometimes notice injected thoughts (Lindsey 2025)]]).

### The same results under stronger controls
- A re-check of the neurofeedback task found that a probe on the input words alone (a layer-0 probe) matches or beats the model, and that the model falls to near the majority baseline when labels are shuffled ([[Introspection claims fail basic checks (Singh 2026)]]). So the reports may come from the meaning of the text, not from an inner state.
- The same re-check added a third answer to the injection task, "my input was changed". Open models then also "detect" changes that never happened, and fall to near chance or prefer the wrong answer ([[Introspection claims fail basic checks (Singh 2026)]]). The authors read this as a general sense that "something is off". **Fairness check:** the re-check used open models (Llama-3.1-70B, Qwen-3-32B, Gemma-3-27B) as substitutes, because it could not test the Claude models of the original study. So it shows that the effect does not hold in open models under stronger controls; it does not refute the Claude result directly ([[Introspection claims fail basic checks (Singh 2026)]]).
- Open models never name an injected pain state: the 32B model does so in 0 of 2,880 trials, although a probe reads the state and a small LoRA adapter can learn to report it ([[Models do not report injected pain (Ferrara 2026)]]).
- A further 2026 study reports that a linear probe finds the location of an injection at 98.3% while the model's zero-shot answer stays at chance, and that the location is decodable even in untrained networks [unverified: abstract only, from the Reading list, arXiv 2611.15267].

### Trained self-prediction
Training changes the picture, but for behavior, not for internal states.
- A model fine-tuned to predict its own behavior predicts itself better than a second model fine-tuned on the same facts about it. Llama-3-70B predicts itself at 48.5%; GPT-4o trained on Llama's data predicts Llama at 31.8% ([[Models predict themselves better than others do (Binder 2024)]]). After its behavior is changed by fine-tuning, GPT-4o's self-predictions follow the new behavior (35.4% vs 21.7% for the old one). The effect holds only for simple properties and does not transfer to harder tasks. It is also not universal: GPT-3.5's own-model advantage is only 0.8 points ([[Models predict themselves better than others do (Binder 2024)]]), and a 2026 study is cited as finding that trained self-prediction does not always give an own-model advantage [unverified: Zeng et al. 2026, cited in [[Training LMs to watch themselves (Wang 2026)]], not read].
- An "observer" role trained into Qwen3.6-27B answers questions about the assistant role and catches sycophancy and lies with a mean AUROC of 0.907, above honesty training (0.864), outside transcript monitors (0.828) and activation oracles (0.796). Larger models from other families trained on the same data reach only 0.684 and 0.647 ([[Training LMs to watch themselves (Wang 2026)]]). The authors note that the observer is trained only on visible behavior, so it may model the assistant rather than read its states. The advantage also shrinks when the observer must reason and state a probability: its AUROC is then 0.823, about equal to a much larger outside transcript monitor at 0.822 ([[Training LMs to watch themselves (Wang 2026)]]).

**How the two sides fit [our reading].** The positive results are trained and about behavior. The negative results are in context and about internal states. No paper yet shows a model reading an internal state that is absent from both its input and its behavior, under strong controls ([[gaps]]).

## 3.4 A ladder of controls

The papers above suggest a set of controls that any monitoring claim in the review should be judged by. Each control removes one simpler explanation.

| Control | What it rules out | Used by |
|---|---|---|
| Input-only (layer-0) probe | The answer is in the input text | [[Introspection claims fail basic checks (Singh 2026)]] |
| Shuffled labels | The model uses the meaning, not the label | [[Introspection claims fail basic checks (Singh 2026)]] |
| Cross-model control (same data, other weights) | The model learned from data, not from privileged access | [[Models predict themselves better than others do (Binder 2024)]], [[Training LMs to watch themselves (Wang 2026)]] |
| Third answer "my input was changed" | A general sense that something is off | [[Introspection claims fail basic checks (Singh 2026)]] |
| No-injection and unrelated-question trials | A bias toward saying "yes" | [[Models sometimes notice injected thoughts (Lindsey 2025)]] |
| Output consistency baseline | The monitor reads "typical for me", not "correct" | [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] |

No single paper uses all six. The cross-model control in [[Training LMs to watch themselves (Wang 2026)]] uses larger models from other families, not a same-size, same-family model, which would be cleaner [our concern].

## 3.5 What monitoring is used for

Where a monitoring signal drives a decision, the decision is about generation:
- stop reasoning early ([[Models know when they are right (Zhang 2025)]]);
- steer between thinking modes, with directions from human corrections ([[Outside controller steers thinking modes (Karpf 2026)]]).

Signals from the model about itself do drive **learning** in one family of methods: self-reward. There the model's own confidence or verdict on its outputs becomes the training reward. These loops sharpen what the model already prefers and then collapse ([[Self-reward sharpens then collapses (He 2026)]], [[Self-reward on code collapses to short code (Jin 2026)]]), unless a hard outside check bounds them ([[Self-reward only within the same test result (Wu 2026)]]). Section 6 covers them. But these signals are read from the output (token probabilities or text), not from a probed hidden state. No paper in our set uses a **hidden-state** monitoring signal to decide what to learn, how fast, or what to write into the weights. That is the role [[Neuromodulators set how the brain learns (Doya 2002)]] gives to the brain's global signals ([[gaps]]). The observer paper goes further and advises against training the assistant on the observer's reports, because the assistant could learn to evade it ([[Training LMs to watch themselves (Wang 2026)]]).

## 3.6 Summary

- Hidden states carry readable signals about the model's own work, mostly about correctness. Outside probes read them well.
- In-context self-report of internal states fails strong controls. Trained self-prediction of behavior passes a cross-model control.
- Monitoring is never yet about quality beyond correctness. Output-level self-signals drive learning in self-reward methods, and those collapse without a hard check. Hidden-state monitoring never drives learning.
- For the review's frame, this means the monitor step exists, but mostly as monitoring **by the researcher**. Metacognition **by the model** is shown only for behavior. Section 4 asks whether any internal signal judges good or bad, and section 5 asks whether any signal reaches the weights.

## Open doubts (critic review, 2026-11-20)

1. **Built from notes, not papers.** Most numbers come from our paper notes. Only two of the cited notes are marked "read"; the rest are "skimmed". Each number should be checked against the paper before submission.
2. **Claude-only positive result.** The strongest in-context introspection result ([[Models sometimes notice injected thoughts (Lindsey 2025)]]) is on closed Claude models. The negative re-check is on open models. The two do not test the same systems, and the draft must not present one as refuting the other.
3. **Privileged access may be "more data about this model".** The cross-model controls in [[Training LMs to watch themselves (Wang 2026)]] use larger models from other families. A same-size, same-family control is missing in every paper we have.
4. **Possible missing counter-evidence:** Zeng et al. 2026 (no own-model advantage in trained self-prediction) and Rubin et al. 2026 (arXiv 2611.15267, shallow injection reports) are cited from abstracts or second hand. Both should get notes before the section is final.
5. **Selection of papers.** Our set leans toward recent 2025 to 2026 interpretability work. Older calibration and uncertainty work (beyond [[Models mostly know what they know (Kadavath 2022)]]) is thin. The 2026 survey's paper list could fill this ([[Survey of metacognition in language models (Liu 2026)]]).
6. **"Readable is not used" rests on few papers.** Only one paper (Ferrara) links a decoded state to a behavior change. The section should not imply that the other probed signals are causal.
7. **The ladder of controls (3.4) is our synthesis.** It is not a standard from any one paper. Say so in the final text.
