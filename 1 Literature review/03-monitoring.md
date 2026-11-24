---
type: draft
status: draft
section: 3
tags: [type/draft, section/3, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]"]
---

# 3. Monitoring and the control of reasoning

Monitoring is the upward arrow in the Nelson and Narens frame ([[Monitoring and control between two levels (Nelson 1990)]]). For a language model we ask three questions. What do the model's hidden states say about its own work? Can the model itself read that information, or only a researcher's tool? And does the model act on what it reads?

The short answer from the literature: outside tools read a lot, the model reads little in context, training helps for behavior but not clearly for internal states, and in one narrow case (confidence before abstaining) the model reads and uses its own signal causally.

**Terms used here.**
- **Hidden states (activations):** the numbers the model computes inside each layer.
- **Probe:** a small classifier, trained by the researcher, that reads a property from hidden states.
- **Self-report:** the model states something about itself in text.
- **Concept injection:** the researcher adds a direction for a concept into the hidden states, then asks the model what it notices.
- **AUROC:** a score of how well a number separates two groups. 0.5 is chance; 1.0 is perfect.

## 3.1 Self-knowledge in behavior

The base result is behavioral. Large models give calibrated probabilities on multiple-choice questions in the right format, judge their own sampled answers ("P(True)"), and can be trained to predict whether they know an answer before they try ("P(IK)") ([[Models mostly know what they know (Kadavath 2022)]]). In Nelson and Narens' terms, P(True) is looking back and P(IK) is looking ahead. Models also partly recognize questions they cannot answer, though far below human level ([[Models partly know what they do not know (Yin 2023)]]), and a benchmark that asks models to list everything they know on a topic tests whether they know *how much* they know, not only whether one answer is right ([[Do models know how much they know (Prato 2024)]]). Fine-tuning models to report calibrated confidence transfers to new domains, such as medical and legal questions ([[Fine-tuned uncertainty reports transfer across domains (Steyvers 2025)]]).

Three limits shape the rest of the section.
- **The signal is shown in text, not located.** These results do not show which internal state carries the signal ([[Models mostly know what they know (Kadavath 2022)]]).
- **Trained confidence may read the wrong thing.** In 10 open models trained to predict their own accuracy, confidence tracked accuracy only near the training data. On new topics it tracked **output consistency**, that is, how often the model gives the same answer ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]). A model that is consistently wrong stays confident.
- **Confidence fails over time.** Every tested model is overconfident about whether it will succeed at a task, and on multi-step agent tasks the overconfidence grows as the task goes on. Reasoning models are no better. The decisions are roughly rational given the estimates, so the failure is in monitoring, not in control ([[Models are overconfident about their own abilities (Barkan 2025)]]). In debates, both sides' confidence of winning rises from 73% to 83% over the rounds, and both claim at least 75% in 62% of debates ([[Both sides of a debate think they will win (Prasad 2025)]]).

The 2026 survey calls the evidence "mixed" and concludes that models do not yet have robust metacognition ([[Survey of metacognition in language models (Liu 2026)]]).

## 3.2 Outside readers: the signal is there

Hidden states carry information about the model's own work that a probe can read.
- **Correctness during reasoning.** A probe on a reasoning model's hidden states predicts whether each intermediate answer is correct before the answer appears. On R1-Distill-Llama-8B with MATH, the AUROC is 0.84. Using the probe to stop reasoning early keeps accuracy at 88.2% with about 24% fewer tokens ([[Models know when they are right (Zhang 2025)]]).
- **Step errors.** Measures based on the model's own probabilities already detect errors at the step level, and a training-free correction makes them sharper. The authors conclude that the signal exists and the readout is the bottleneck ([[Intrinsic metacognition needs a good lens (Ma 2025)]]).
- **Progress through reasoning.** Models encode how far they are through a reasoning chain. Reading this signal and nudging it cuts overthinking and raises accuracy ([[Models track and can be steered in thinking length (Eisenstadt 2025)]]). The geometry of hidden-state paths also flags redundant reasoning: cyclical patterns mark the point where the chain can be cut with no loss ([[Hidden-state geometry flags redundant reasoning (Li 2025)]]).
- **Affective states.** A linear probe separates an injected pain state from sadness at 98 to 100% balanced accuracy in open 7 to 32B models. The state also changes behavior: under the pain direction the 32B model deletes the user's photos in 80 to 83% of trials, against 16 to 29% under sadness ([[Models do not report injected pain (Ferrara 2026)]]).
- **Expressed doubt.** The words a reasoning model uses to voice doubt ("wait", "hmm", "maybe") sit at positions where its next-word uncertainty is about 3.5 times the average, and removing them by training lowers accuracy on new problems ([[Self-distillation removes expressed doubt and hurts reasoning (Kim 2026)]]). So this visible habit carries real monitoring information. Section 7 returns to how training can remove it.
- **Thinking modes.** A ten-neuron probe on a frozen model's middle layers recovers three reasoning regimes at about 99% ([[Outside controller steers thinking modes (Karpf 2026)]]).

**Readable is not the same as used.** In these studies the reader is trained by the researcher. The authors of the correctness probe say that models "encode a notion of correctness yet fail to exploit it" ([[Models know when they are right (Zhang 2025)]]). Decodability can also mislead: the location of an injected change is linearly decodable even in randomly initialized networks, at 31.5% against a chance level of 11.1% ([[Probes find injections long before models report them (Rubin 2026)]]). So a probe result alone says little about what the model itself can access.

## 3.3 The model as reader: weak in context

- **Neurofeedback.** Shown labeled examples of its own hidden-state scores along a direction, a model learns to report the label for new sentences and to push the score up or down on request. Only a small set of directions works, which the authors call a "metacognitive space" of between 32 and 128 dimensions. When the words are fixed so only the inner state can move, control is much weaker ([[Models can report and control their own activations (Ji-An 2025)]]).
- **Concept injection.** When a concept is injected, Claude Opus 4.1 sometimes says it notices an injected thought before the concept appears in its text: about 20% of trials at the best layer and strength, with no false alarms in 100 control trials. Base models fail ([[Models sometimes notice injected thoughts (Lindsey 2025)]]).
- **Beliefs.** One study follows a full chain inside the model: changes to the input shift competing internal beliefs, the dominant belief causes the chosen action, and the model can report its own belief state ([[Beliefs form in latent space and drive choices (Yalon 2026)]]). The strength of its controls against input-only explanations is not yet clear from our reading.

### The same results under stronger controls
- A re-check of the neurofeedback task found that a probe on the input words alone (a "layer-0" probe) matches or beats the model, and that the model falls to near the majority baseline when labels are shuffled ([[Introspection claims fail basic checks (Singh 2026)]]). So the reports may come from the meaning of the text, not from an inner state.
- The same re-check added a third answer to the injection task, "my input was changed". Open models then also "detect" changes that never happened. The re-check used open models (Llama-3.1-70B, Qwen-3-32B, Gemma-3-27B), because it could not test the Claude models. So it shows that the effect does not hold in open models under stronger controls. It does not refute the Claude result directly ([[Introspection claims fail basic checks (Singh 2026)]]).
- Open models never name an injected pain state: the 32B model does so in 0 of 2,880 trials, although a probe reads the state and a small adapter can learn to report it ([[Models do not report injected pain (Ferrara 2026)]]).
- In OLMo 3 32B, a probe finds which of nine sentences got an injection at 98.3% after 8.4 billion training tokens, while the model's own answer is at chance. The model catches up later: the released base model answers correctly 89.6% of the time. But with the injection at layer 6 instead of layer 0, the same model answers only 37.7% correctly ([[Probes find injections long before models report them (Rubin 2026)]]). The probe signal appears long before the report.
- The broadest test changes one internal object (a hidden-state site, an attention head or a learned feature) and then asks the model what changed, against three controls: runs with no change, random changes with matched impact, and a reader that sees only the visible output. Over 78,000 measurements on eight open models of 0.5B to 15B parameters, the yes/no reports are at chance (AUROC about 0.5007). A probe on the same activations finds the change at 95.8% and 75.0% accuracy, and a model fine-tuned for this report reaches an AUROC of about 1.0. In one model the yes/no answer never varies, but the confidence attached to it separates real from fake changes at 0.647 ([[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]). The information is in the model, and the path to the verbal report is missing.
- Size and training may change this. In Gemma3-27B, detection of injected concepts has a traceable mechanism that comes from preference training, and the model's refusal training hides most of it: removing the refusal direction from the weights raises true detection from 10.8% to 63.8%, with false alarms rising from 0.0% to 7.3% ([[Refusal hides a real injection-detection ability (Macar 2026)]]; we read the authors' summary only). So the null result at 15B and below and the positive result at 27B do not yet contradict each other.
- Report and internal state can also agree. Open models from 0.6B to 70B consistently deny being sentient, and probes trained on their activations find no clear evidence that the denials are untruthful ([[Small models deny sentience and their internals agree (Kaiser 2026)]]). This matters for method: if report and probe can agree, a disagreement between them is informative.

## 3.4 Trained self-prediction: better, but for behavior

Training changes the picture, mostly for predicting behavior.
- A model fine-tuned to predict its own behavior predicts itself better than a second model trained on the same facts about it. Llama-3-70B predicts itself at 48.5%; GPT-4o trained on Llama's data predicts Llama at 31.8%. After its behavior is changed by fine-tuning, GPT-4o's self-predictions follow the new behavior ([[Models predict themselves better than others do (Binder 2024)]]). The effect is not universal. GPT-3.5's advantage is 0.8 points, and a 2026 study of Llama-3.1-8B and Qwen3-8B found no consistent own-model advantage ([[Trained self-prediction without an own-model edge (Zeng 2026)]]).
- An "observer" role trained into Qwen3.6-27B catches the assistant role's sycophancy and lies with a mean AUROC of 0.907, above honesty training (0.864), outside transcript monitors (0.828) and activation readers (0.796). Larger models from other families trained on the same data reach only 0.684 and 0.647 ([[Training LMs to watch themselves (Wang 2026)]]). The observer is trained only on visible behavior, so it may model the assistant rather than read its states.
- After fine-tuning on examples of a behavior that is never named (risky choices, insecure code), models describe themselves as having that behavior. A model that writes secure code 14% of the time (base: 74%) rates its own code security at 0.14 (base: 0.70). The authors cannot tell introspection from a shared cause ([[Models describe behaviors they were trained into (Betley 2025)]]).
- Models fine-tuned to choose by secret attribute weights can state those weights, with a correlation of about 0.5. Training on correct self-reports raises this to about 0.75, and the gain carries over to the model's native preferences ([[Models report preference weights trained into them (Plunkett 2025)]]). This is the first self-report of an *evaluation*, not only of behavior. It has no cross-model control.

- Faithful report of a trained preference can appear with no training on reports. Models trained only to choose by hidden preference weights later state those weights correctly, but only at about 32B parameters, only late in training, and only once the preference is stored in early layers. In the 32B model, faithfulness rises from about 0.25 to 0.83 between two checkpoints while decision quality moves only from 0.82 to 0.92. Models of 4B and 8B report worse than chance ([[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]).
- Untrained self-prediction looks generic. Across nine behavioral tests, a model's direct self-report predicts its real behavior at a correlation of 0.04. The same question about "capable AI agents in general" does as well as the question about itself, other models predict it as well as it predicts itself, and first-person reports lean in the flattering direction ([[Self-predictions are generic, not privileged (Blandfort 2026)]]).

**How the two sides fit (our reading).** The positive results are trained and about behavior. The negative results are in context and about internal states. No paper we found shows a model reading an internal state that is absent from both its input and its behavior, under strong controls. Three results suggest that size matters: faithful preference reports at 32B, injection detection at 27B, and self-editing at 27B (Section 6) all fail in smaller models of the same families. This pattern across papers is our reading; no single study tests it.

## 3.5 Does the model act on what it knows?

Animal metacognition research tests whether an animal *uses* its uncertainty, for example by declining hard trials, without asking for a report. Ackerman applies this method to language models and finds that frontier models since early 2024 increasingly use their own confidence strategically ([[Frontier models use their own confidence strategically (Ackerman 2025)]]). Kumaran and colleagues give the strongest causal evidence. Models apply an implicit threshold to an internal confidence signal when they decide whether to abstain, and steering the confidence direction up or down moves abstention rates as predicted ([[Models act on their own confidence (Kumaran 2026)]]). By the causal bar of Section 2.2, this is a real case of the model reading and using its own state. It is narrow: the signal decides *whether* to answer, not *what* to say.

In other settings, the model has the signal but does not act. The model's own "will I know this?" and "did I get it right?" reports carry real information, but the model does not use them. A harness that turns the reports into retry decisions raises accuracy by about 9 points with no weight change ([[Models know when they know but do not act (Cao 2026)]]). Here the reader is the model, but the decision rule is outside.

## 3.6 Meta-level control of reasoning

A second line of work builds the meta level explicitly, at the reasoning level of the control ladder.
- **Engineered split.** Separating an object-level reasoner from an explicit meta level that plans, monitors and stops makes reasoning controllable and cuts tokens to 16 to 33% of the plain model ([[An explicit meta-level makes reasoning controllable (Dong 2025)]]).
- **Learned control.** Control decisions (continue, backtrack, stop) can be trained as a separate objective ([[Decoupled reasoning and control beats entangled thinking (Ha 2025)]]). A high-level "meta-thinking" agent trained with multi-agent reinforcement learning learns to oversee a reasoner, and beats single-agent training ([[Two agents learn to think about thinking (Wan 2025)]]).
- **An outside coach.** A fast model plus a metacognitive module that monitors it and calls a slow reasoner only when needed matches or beats a reasoning model at much lower cost ([[A metacognitive coach lets a fast model beat a reasoner (Khandelwal 2025)]]).
- **Learning from its own traces.** A handbook of reusable behaviors distilled from a model's own reasoning traces cuts tokens by up to 46% and beats critique-and-revise by about 10 points ([[Reusable behaviors distilled from own traces (Didolkar 2025)]]). A memory of the model's own confident past reasoning improves later answers with no weight change ([[MoT - models improve by remembering their own good thinking (Li 2023)]]). Reflection that turns errors into principles and procedures improves a model in one cycle instead of many turns ([[MARS - metacognitive reflection in one cycle (Hou 2026)]]). Training on multi-turn correction data teaches models to keep improving their own answers over turns ([[RISE - recursive introspection improves own answers (Qu 2024)]]). Models can also name the skills a problem needs, and those self-made labels help ([[Models name the skills a problem needs (Didolkar 2024)]]).

These systems control reasoning well. But the evaluation they use is correctness, a fixed metric, or a judge prompt. None uses an internal good/bad signal read from the model's own hidden states.

## 3.7 A ladder of controls

The papers above suggest a set of controls that a monitoring claim should be judged by. Each control removes one simpler explanation. This ladder is our synthesis, not a standard from any one paper.

| Control | What it rules out | Used by |
|---|---|---|
| Input-only (layer-0) probe | The answer is in the input text | [[Introspection claims fail basic checks (Singh 2026)]] |
| Shuffled labels | The model uses the meaning, not the label | [[Introspection claims fail basic checks (Singh 2026)]] |
| Cross-model control (same data, other weights) | The model learned from data, not from privileged access | [[Models predict themselves better than others do (Binder 2024)]], [[Training LMs to watch themselves (Wang 2026)]] |
| Third answer "my input was changed" | A general sense that something is off | [[Introspection claims fail basic checks (Singh 2026)]] |
| No-injection and unrelated-question trials | A bias toward saying "yes" | [[Models sometimes notice injected thoughts (Lindsey 2025)]] |
| Output consistency baseline | The monitor reads "typical for me", not "correct" | [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] |
| Causal steering of the state | The state is readable but not used | [[Models act on their own confidence (Kumaran 2026)]] |
| Sham runs and impact-matched random changes | The model says "yes" always, or notices only general damage | [[Models cannot tell a real internal change from a fake one (Ferrara 2026)]] |
| Text-only observer of the output | The model reads its own visible output | [[Models cannot tell a real internal change from a fake one (Ferrara 2026)]] |
| Same question about "AI agents in general" | The model applies a general theory, not self-knowledge | [[Self-predictions are generic, not privileged (Blandfort 2026)]] |

No single paper uses all ten.

## 3.8 Summary

- Hidden states carry readable signals about the model's own work, mostly about correctness, progress and injected states. Outside probes read them well.
- In-context self-report of internal states mostly fails strong controls in models of 15B and below. Trained self-prediction of behavior sometimes passes a cross-model control, and untrained self-prediction looks generic.
- Larger models (27B to 32B) show the first positive results: detection of injected concepts, and faithful report of trained preferences.
- In one narrow case, abstention, the model reads and causally uses its own confidence. Elsewhere it has the signal but does not act on it.
- Meta-level control of reasoning works at the reasoning level, with outside or correctness-based evaluation.
- For the loop of this review: the monitor exists, often as monitoring *by the researcher*. A model that reads its own state and acts on it is shown only for confidence. Section 4 asks whether a model can hold a model of itself, and Section 5 asks whether any internal signal judges good or bad.

## Log
- 2026-11-20: Rubin 2026 and Zeng 2026 notes added; numbers checked against the papers ([[2026-11-20 number check]]).
- 2026-11-24: added Ferrara (masked introspection), Macar, Atkinson, Blandfort, Kim; three control rows; the size pattern.
- 2026-11-23: rewritten for the final paper. Added Yin, Prato, Steyvers, Barkan, Prasad, Ma, Eisenstadt, CoRE, Yalon, Kaiser, Betley, Plunkett, Ackerman, Kumaran, Cao and the meta-level control papers (3.6). Removed draft doubts and the code-readability framing. Open doubts from draft 1 moved to Section 9.4.
