---
type: draft
status: draft
section: 3
tags: [type/draft, section/3, component/monitoring, test/grounded, status/draft]
links: ["[[outline]]", "[[gaps]]", "[[matrix]]", "[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]"]
---

# 3. Monitoring and the control of reasoning

Monitoring is the upward arrow in the Nelson and Narens frame. The main finding of this section is a gap between presence and access. Information about a model's own work is in its hidden states, the numbers it computes inside each layer, and outside tools read it well. The model itself reports it poorly, uses it in one narrow case, and gains from training mostly for predictions of its own behavior.

## 3.1 Signals in behavior and in hidden states

The base result is behavioral. Large models gave calibrated probabilities on multiple-choice questions and could be trained to predict whether they knew an answer before they tried ([[Models mostly know what they know (Kadavath 2022)]]). Such confidence can read the wrong thing: in ten open models trained to predict their own accuracy, confidence on new topics tracked how often the model gave the same answer, so a model that was consistently wrong stayed confident ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]). The 2026 survey of the field called the evidence "mixed" ([[Survey of metacognition in language models (Liu 2026)]]).

Inside the model the signal is clearer. A probe is a small classifier that a researcher trains to read a property from hidden states. A probe on a reasoning model predicted whether each intermediate answer was correct before the answer appeared, with an AUROC of 0.84 on one maths benchmark (AUROC scores how well a number separates two groups; 0.5 is chance and 1.0 is perfect) ([[Models know when they are right (Zhang 2025)]]). The words a reasoning model uses to voice doubt ("wait", "hmm", "maybe") sat at positions where its next-word uncertainty was about 3.5 times the average, and training them away lowered accuracy on new problems ([[Self-distillation removes expressed doubt and hurts reasoning (Kim 2026)]]). Readable does not mean used, however. The researcher trained the reader, and the authors of the correctness probe wrote that models "encode a notion of correctness yet fail to exploit it".

## 3.2 The model as reader: weak in context

Two results suggested that a model can read its own hidden states with no training. In a "neurofeedback" task, a model saw labeled examples of its own hidden-state scores along a direction and then reported the label for new sentences ([[Models can report and control their own activations (Ji-An 2025)]]). In concept injection, a researcher adds the direction for a concept to the hidden states and asks the model what it notices. Claude Opus 4.1 reported the injected thought in about 20% of trials at the best layer and strength, with no false alarms in 100 control trials ([[Models sometimes notice injected thoughts (Lindsey 2025)]]).

Stronger controls weakened both in open models. In a re-run of the neurofeedback task, a probe on the input words alone matched or beat the model, and the model fell to near the majority baseline when the labels were shuffled. With a third answer added to the injection task, "my input was changed", open models also "detected" changes that never happened ([[Introspection claims fail basic checks (Singh 2026)]]). The models were open ones, up to 70B (70 billion parameters), so the re-check does not refute the Claude result directly. Open models of 7B to 32B never named an injected pain state, in 0 of 2,880 trials for the 32B model, although a probe read the state at 98 to 100% ([[Models do not report injected pain (Ferrara 2026)]]). The broadest test changed one internal object and asked the model what had changed, against three controls: runs with no change, random changes with matched impact, and a reader given only the model's output text. In more than 78,000 measurements on eight open models of 0.5B to 15B, the reports were at chance (AUROC about 0.5007), while a probe on the same hidden states found the change at 95.8% and 75.0% accuracy ([[Models cannot tell a real internal change from a fake one (Ferrara 2026)]]). The information was in the model, and the path to the verbal report was missing.

One result keeps the question open. In Gemma3-27B, removing the refusal direction from the weights raised true detection of injected concepts from 10.8% to 63.8%, with false alarms rising from 0.0% to 7.3%, so refusal training had hidden most of a real ability ([[Refusal hides a real injection-detection ability (Macar 2026)]]; we read the authors' summary only).

## 3.3 Trained self-prediction: better, but for behavior

Training changes the picture, mostly for predictions of behavior. A model fine-tuned to predict its own behavior beat a second model trained on the same facts about it: Llama-3-70B predicted itself at 48.5%, and GPT-4o trained on Llama's data predicted Llama at 31.8% ([[Models predict themselves better than others do (Binder 2024)]]). Models can also describe a preference that training put into them. Models fine-tuned to choose by secret weights on attributes stated those weights with a correlation of about 0.5 ([[Models report preference weights trained into them (Plunkett 2025)]]). A follow-up showed that faithful reports can appear with no training on reports at all, but only at 32B, only late in training, and only once the preference was stored in early layers; models of 4B and 8B reported worse than chance ([[Self-report becomes faithful when preferences sit early (Atkinson 2026)]]).

Whether this is privileged access, meaning access that another model could not have, is contested. One study found no consistent own-model advantage in trained self-prediction ([[Trained self-prediction without an own-model edge (Zeng 2026)]]). Across nine behavioral tests, a model's untrained self-report predicted its real behavior at a correlation of 0.04, the same question about "capable AI agents in general" did as well, and first-person reports leaned in the flattering direction ([[Self-predictions are generic, not privileged (Blandfort 2026)]]). In 21 open models, answers about the model's own knowledge of language predicted its measured probabilities no better than the answers of a nearly identical model did [@Song 2025]. On the other side, a benchmark built to separate introspection from general knowledge found that frontier models predicted their own behavior better than peer models did [@Naphade 2026] (abstract only).

Our reading is as follows. The positive results come from training or from the largest models, and concern behavior or trained-in preferences. The negative results come from tests in context and concern internal states. Size may matter, because faithful preference reports, injection detection, and self-editing (Section 6.3) each appeared at 27B to 32B and failed in smaller models of the same families. The evidence does not support a threshold: a 70B model failed the stronger controls, a 32B model never named an injected state, and a hidden valence effect was absent in exactly the 32B and 27B models of one study (Section 5.1).

## 3.4 Acting on the signal

Does the model act on what it knows? The strongest causal evidence concerns abstention. Models applied an implicit threshold to an internal confidence signal when they decided whether to answer, and steering that signal up or down moved abstention rates as predicted ([[Models act on their own confidence (Kumaran 2026)]]). By the standard of Section 2.2, this is a real case of a model reading and using its own state, and a narrow one: the signal decided whether to answer, not what to say. Elsewhere the model has the signal and does not act: a harness that turned a model's own "did I get it right?" reports into retry decisions raised accuracy by about 9 points with no weight change ([[Models know when they know but do not act (Cao 2026)]]).

Systems that build a meta level explicitly control reasoning well. One engineered split of reasoner and meta level cut tokens to 16 to 33% of the plain model ([[An explicit meta-level makes reasoning controllable (Dong 2025)]]). Their evaluation is correctness, a fixed metric, or a judge prompt, and none uses a good-or-bad signal read from the model's own hidden states.

## 3.5 Ten controls for a monitoring claim

The studies above suggest a set of controls for judging any claim that a model monitors itself (Table 3). Each control removes one simpler explanation. The set is our synthesis; no single paper uses all ten.

**Table 3.** Ten controls for a claim that a model monitors itself.

| Control | Simpler explanation it removes | Used by |
|---|---|---|
| Probe on the input words alone | The answer is in the input text | [[Introspection claims fail basic checks (Singh 2026)]] |
| Shuffled labels | The model uses the meaning, not the label | [[Introspection claims fail basic checks (Singh 2026)]] |
| Second model trained on the same data | The model learned from data, not from privileged access | [[Models predict themselves better than others do (Binder 2024)]] |
| Third answer, "my input was changed" | A general sense that something is off | [[Introspection claims fail basic checks (Singh 2026)]] |
| Trials with no injection | A bias toward saying "yes" | [[Models sometimes notice injected thoughts (Lindsey 2025)]] |
| Baseline of answer consistency | The monitor reads "typical for me", not "correct" | [[Trained confidence tracks consistency, not accuracy (Yax 2026)]] |
| Causal steering of the state | The state is readable but not used | [[Models act on their own confidence (Kumaran 2026)]] |
| Random changes with matched impact | The model notices only general damage | [[Models cannot tell a real internal change from a fake one (Ferrara 2026)]] |
| Reader of the output text alone | The model reads its own visible output | [[Models cannot tell a real internal change from a fake one (Ferrara 2026)]] |
| Same question about "AI agents in general" | The model applies a general theory, not self-knowledge | [[Self-predictions are generic, not privileged (Blandfort 2026)]] |

## Log
- 2026-11-20: first draft and number checks ([[2026-11-20 number check]]).
- 2026-11-24: rewritten for the final paper with the newly read papers.
- 2026-11-24 (guides and critique): rewritten as connected prose in the past tense for what studies did. Added the calibration lineage, Song 2025, Naphade 2026 and MetaLoop; privileged access is now stated as contested; the "near 30B" pattern now carries its counter-evidence.
- 2026-11-24 (short version): cut to about half for a 10 to 12 page IEEE paper, at the user's request. The long text is in `Long version (23 pages)/03-monitoring (long).md`.
