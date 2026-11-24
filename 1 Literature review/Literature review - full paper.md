---
type: paper
status: draft
tags: [type/paper-draft, status/draft]
links: ["[[outline]]", "[[TASKS]]"]
---

<!-- Built by scripts/build_review.py from the section files. Edit the section files, not this file. -->


# Can a language model judge and change itself? A review of metacognition, self-models, weight self-modification and taste

**Authors:** [add names]

**Date:** 24 November 2026

## Abstract

Reasoning models hesitate, check their own steps and sometimes decline to answer. We review what lies under this behavior and how far it could extend: whether a language model can monitor its own internal states, hold a model of itself, judge what it finds as good or bad, and write the result into its own weights, and whether repeated self-change could give it preferences of its own. We organize 137 papers, most from 2024 to 2026, around one loop (monitor, evaluate, control, persist) with a self-model across it and an anchor against collapse. We find that every step has prior art. Hidden states carry readable signals about a model's own work; valence and value signals causally move choices; weights can change after deployment through learned memory or through direct, gradient-free edits; and one open model has edited its own weights. The connections between the steps are weak. Models report their own states poorly below about 30 billion parameters, their self-predictions are generic, and no model predicts the effect of a change to itself. In every weight-changing method, a signal outside the model's own evaluation decides what is kept. Loops on a model's own signal sharpen, drift or decay, and self-training can remove a model's expressed doubt. Measured taste is shared across models, and inherited values persist under self-modification. We state the self-changing, self-judging model as an open agenda, list eight problems with it, propose four tests for a taste of a model's own with an existing instrument for each, and identify a first open question: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change?

**Keywords:** metacognition, introspection, self-models, world models, model editing, weight-space programming, continual learning, preferences, taste, self-improvement


# 1. Introduction

Reasoning models now behave, from the outside, as if they know something about themselves. They hesitate, backtrack, write "wait", check their own steps and sometimes decline to answer when unsure. This review asks what lies under that behavior, and how far it could go. Can a language model **monitor** its own internal states, hold a **model of itself**, **judge** what it finds as good or bad, and use that judgment to **control** its reasoning and, in the end, to **change its own weights**? And if a model keeps changing itself by its own judgment, could it develop preferences of its own, a **taste**, that its original weights did not contain?

The question has four parts, and each part has its own literature.

1. **Metacognition.** Psychology has studied how minds watch and steer themselves for decades (Nelson and Narens 1990). Language models are the first artificial systems where the parts can be measured directly, because their internal states can be read. A Trends in Cognitive Sciences paper by Johnson, Bengio, Mitchell, Rahwan, Schölkopf and others argues that AI has become smart without becoming wise, and that the missing part is metacognition (Johnson et al. 2025). A 2025 review treats metacognition and self-awareness in AI as measurable functions (Li et al. 2025a).
2. **Self-models and world models.** A world model is a learned model that predicts what will happen when an agent acts, so the agent can plan before it acts. A self-model points the same idea inward: the system predicts its own behavior, its own success and its own learning. A 20-author survey of world models finds that metacognition and motivation are their least-studied functions (Rupprecht et al. 2026).
3. **Lasting change to the weights.** A deployed language model is static. Its weights do not change, and what it learns in a conversation is lost when the conversation ends. Two lines of work try to remove this limit. The first trains small parts of the model while it is in use, inside architectures built for that purpose (Behrouz et al. 2025a, Behrouz et al. 2026). The second writes small, direct changes into the weights with no gradient training at all. This is **weight-space programming (WSP)** (Takehi et al. 2026). In late 2026 an open model used it on itself: it read its own hidden states, found a fault, and edited its own weights (Fan et al. 2026).
4. **Preferences and taste.** Models make consistent choices between acceptable options, and these choices can now be measured (Mazeika et al. 2025, Trehan and Chopra 2026).

These literatures rarely cite each other. The metacognition papers stop at reading and reporting. The world-model papers rarely model the agent itself. The weight-change papers almost never ask who decides what a good change is, or what a change does to the model's preferences and to its view of itself. This review puts them in one frame, so that it is clear which parts of a self-changing, self-judging model exist today and which do not.

## 1.1 The frame: a loop with four steps

We organize the review around one loop. It extends the classic monitor-and-control model of metacognition with two steps.

- **Monitor:** what do the model's hidden states say about its own work, and can the model itself read them?
- **Evaluate:** is there an internal signal that judges a state or an output as good or bad?
- **Control:** how does that judgment change behavior, from choosing among outputs to steering hidden states?
- **Persist:** how does a change get written into the weights, so that what the model prefers now changes what it becomes?

A self-model sits across the loop: to choose a good change, a system must predict what the change will do to itself. An **anchor** sits under the loop: a loop that learns from its own signal can lock onto its own prior and collapse, so something must keep it honest.

Control can act at three levels, from temporary to lasting:
1. **Reasoning level:** pick, rank or revise the model's own outputs.
2. **Activation level:** steer the model's hidden states while it generates.
3. **Weight level:** write the change into the weights.

## 1.2 What we mean by taste

By **taste** we mean a stable set of preferences that a model uses to judge its own work. Most of a model's preferences come from pretraining and human feedback. We call a taste **self-originated** if it moves away from that origin because the model keeps selecting for it. This review does not claim that any model has such a taste, or that one will appear. It treats the idea as a possibility and asks what evidence would be needed. We use four tests, proposed by us and applied in Section 9:
1. **Divergent:** the preference differs from the human and training preference distribution.
2. **Stable:** it holds when the question is reworded or the order of options changes.
3. **Grounded:** it matches an internal state that can be read and that causally drives the choice, not only a verbal self-report.
4. **Self-reinforcing:** it sharpens over repeated self-change without collapse.

## 1.3 Research questions

The review answers six questions, one per main section.

| | Question | Section |
|---|---|---|
| RQ1 | What can a language model monitor about its own states, and does it act on what it monitors? | 3 |
| RQ2 | Can a model hold a model of itself and predict its own behavior and its own changes? | 4 |
| RQ3 | Which internal signals judge a state or an output as good or bad? | 5 |
| RQ4 | How can a model's weights change after deployment, and who decides the change? | 6 |
| RQ5 | What goes wrong when a model learns from its own signals? | 7 |
| RQ6 | How are a model's preferences measured, and does a measured taste belong to one model? | 8 |

## 1.4 Method

This is a narrative review, not a full systematic review. We did not run exhaustive search strings over all digital libraries or count every excluded record. We state what we did so that a reader can judge the coverage.

- **Sources.** We collected papers between 19 and 24 November 2026 from four sources: daily arXiv searches with fixed queries on metacognition, introspection, self-reward, steering, model editing and weight-space programming; targeted web searches on specific open points (stable preference, self-preference, self-referential networks, repeated weight edits, self-report after a weight change); the reading list of a public survey of metacognition in language models; and backward citation from papers we read.
- **Inclusion.** We included a paper if it reports evidence or a framework on at least one step of the loop (monitor, evaluate, control, persist, anchor) in language models, or supplies a classic concept from cognitive science or earlier neural network research that the frame needs.
- **Exclusion.** We excluded pure application papers (for example weight-space programming applied to robot controllers or medical networks), and papers on general model performance with no link to self-monitoring, preference or self-change.
- **Data extraction.** For each included paper we wrote a structured note with the same fields: claim, mechanism, evidence with numbers and their location in the paper, limits, and relevance to the loop.
- **Quality marking.** Each note records how much of the paper was read. Of the 137 papers, 7 were read in full or nearly in full, and the others were skimmed: abstract, introduction, main results and limitations. Several notes rest on the abstract only. We mark such claims in the text with "abstract only".
- **The set.** 137 papers have notes, and this review cites 134 of them, plus 13 further sources that we checked but did not write notes for. Of the 137, 124 are from 2024 to 2026, and 67 from 2026 alone. Seven classic papers from 1990 to 2019 supply the frame. Many 2026 papers are preprints that are not yet peer reviewed.

Section 9.5 lists the limits that follow from this method.

## 1.5 Plan of the review

Section 2 gives the foundations: the monitor-and-control model, how metacognition is measured, and a mapping from brain chemistry to learning settings. Section 3 covers monitoring and the control of reasoning. Section 4 covers self-models and world models. Section 5 covers internal evaluation signals. Section 6 covers changes that persist in the weights, by learned memory and by direct edits. Section 7 covers the limits of learning from one's own signal. Section 8 covers how preferences and taste are measured. Section 9 assembles the loop, states what is missing, lists the problems with the full idea, and names the first open question. Section 10 concludes.


# 2. Foundations

## 2.1 Metacognition as monitoring and control

Flavell introduced metacognition as knowledge about one's own thinking and the regulation of it (Flavell 1979). He included "metacognitive experiences", felt senses that one is or is not getting somewhere. These are the classic ancestor of an internal evaluation signal. Nelson and Narens made the structure precise (Nelson and Narens 1990). Cognition splits into an **object level**, which does the task, and a **meta level**, which holds a model of the object level. Information flows up from the object level to the meta level. This is **monitoring**: feelings of knowing, judgments of learning, confidence. Commands flow down from the meta level. This is **control**: how long to study, when to stop, which strategy to use. Two of their principles matter most for this review. The meta level contains a model of the object level, and that model can be wrong. And the flow is two-way: the meta level both reads and changes the object level.

Fleming and Daw give the computational account (Fleming and Daw 2017). Confidence is a **second-order inference**: a monitoring system infers how well a coupled but separate decision system did. This is the same computation as judging another agent's decision. It needs the states behind the decision and the states behind the confidence to be partly separate. If one state drives both, the system is not evaluating itself. It is only reporting the strength of its first answer. This distinction returns in Section 3, where some self-reports of language models turn out to be readable from the input text alone.

## 2.2 How metacognition is measured

The human literature warns that the obvious measure is wrong. A plain correlation between confidence and accuracy mixes two things: how well confidence separates right from wrong answers (**sensitivity**), and how high confidence is overall (**bias**) (Fleming and Lau 2014). A third quantity, **efficiency**, asks how good the sensitivity is given how well the task itself was done. The measure meta-d' expresses this. It is the task accuracy that an ideal observer would need to reach the observed confidence sensitivity (Maniscalco and Lau 2012). These measures were built for human yes/no tasks. Applying them to language models needs care about what counts as a trial and a criterion. But the warning holds: a model that is simply confident about everything can look metacognitive under a crude measure.

Recent work applies the human test batteries to language models directly. A preregistered battery of 524 items from classic psychology tasks tests whether 20 frontier models withdraw wrong answers more often than right ones. Accuracy and metacognitive sensitivity rank almost in reverse (Cacioli 2026). On a classic memory task, human judgments of learning predict later recall, and no tested model's judgments do (Huff and Ulakci 2025). So metacognitive skill in models is not a side effect of general skill.

A second standard concerns **causation**. Comsa and Shanahan argue that a self-report counts as introspection only if a causal process links the internal state to the report (Comsa and Shanahan 2025). By this bar, a model's account of its own "creative process" is role play. But its correct inference of its own sampling temperature, read from its own recent outputs, is a minimal real case. This review uses their bar throughout: a monitoring claim is strong only if the internal state is shown to cause the report or the behavior.

## 2.3 Where the field stands, in its own words

Two positions frame the field. Johnson and colleagues import the psychology of wisdom into AI as a specification: object-level strategies manage problems, metacognitive strategies manage the object-level strategies, and current AI is strong at the first and weak at the second (Johnson et al. 2025). Li and colleagues treat awareness as a measurable function, and warn that better self-models may also fake alignment better (Li et al. 2025a). A survey of artificial metacognition sorts the field into monitoring, control and communication of one's own cognition, and lists human metacognitive abilities that AI has not yet tried to build (Shakarian 2026). The 2026 survey of metacognition in language models covers monitoring and control, but has no section on evaluation by the model's own preferences and none on self-edits to weights (Liu et al. 2026a).

The bias literature gives the negative image. Five apparently separate biases of language models can be read as one syndrome of missing monitoring and control, "metacognitive myopia" (Scholten et al. 2024). Reasoning models already show measurable, family-specific habits such as "wait, did I miss anything?" (Dong et al. 2025a). These habits are the behavioral surface of a self-monitoring style, whatever lies under them.

## 2.4 Neuromodulation as the controller

What would an internal evaluation signal *do* once it exists? Doya's mapping of brain chemicals to the settings of reinforcement learning gives one answer (Doya 2002). Dopamine carries the reward prediction error. Serotonin sets the time scale, that is, how far ahead rewards count. Noradrenaline sets how random exploration is. Acetylcholine sets the learning rate. In this view, an internal good/bad signal is not a behavior itself. It is a control signal that sets how the system explores, how patient it is, and how much it changes from each experience. Miconi and colleagues built a machine version of the learning-rate setting: a network that outputs its own "dopamine" signal, which sets how fast its own plastic weights change (Miconi et al. 2019). The mapping predicts two things that later sections test. An internal value signal should modulate persistence and backtracking (Section 5 finds this for a value axis). And a system that learns by its own signal needs guards against over-learning its own prior (Section 7).

## 2.5 Levels of self-change

Self-modification is not one thing. Koch sorts it by *what* is changed: actions only, low-level rules, control rules, or the criterion used to judge changes (Koch 2026). He argues that current AI can be changed from outside at low levels, without a matching self-representation. This sorting fits the control ladder of Section 1.1. Choosing among outputs changes actions. Steering changes how rules are applied in one run. Weight edits change the rules. A system that changes its own evaluation signal would change the criterion. That last level is what a self-originated taste would need, and Section 9 shows that no system in this review reaches it.

## 2.6 The four tests

Because "taste" is easy to fake with cheaper mechanisms, the review applies the four tests from Section 1.2 throughout. Each test removes one cheap explanation. A divergent preference could just be noise, so it must also be stable. A stable preference could be a learned verbal habit, so it must be grounded in an internal state that causes the choice. A grounded preference could be fixed forever, so it must sharpen under self-change. And sharpening alone could be collapse onto the model's prior, so it must sharpen without collapse. Sections 3 to 8 report the evidence for each test, and Section 9 sums it up.


# 3. Monitoring and the control of reasoning

Monitoring is the upward arrow in the Nelson and Narens frame (Nelson and Narens 1990). For a language model we ask three questions. What do the model's hidden states say about its own work? Can the model itself read that information, or only a researcher's tool? And does the model act on what it reads?

The short answer from the literature: outside tools read a lot, the model reads little in context, training helps for behavior but not clearly for internal states, and in one narrow case (confidence before abstaining) the model reads and uses its own signal causally.

**Terms used here.**
- **Hidden states (activations):** the numbers the model computes inside each layer.
- **Probe:** a small classifier, trained by the researcher, that reads a property from hidden states.
- **Self-report:** the model states something about itself in text.
- **Concept injection:** the researcher adds a direction for a concept into the hidden states, then asks the model what it notices.
- **AUROC:** a score of how well a number separates two groups. 0.5 is chance; 1.0 is perfect.

## 3.1 Self-knowledge in behavior

The base result is behavioral. Large models give calibrated probabilities on multiple-choice questions in the right format, judge their own sampled answers ("P(True)"), and can be trained to predict whether they know an answer before they try ("P(IK)") (Kadavath et al. 2022). In Nelson and Narens' terms, P(True) is looking back and P(IK) is looking ahead. Models also partly recognize questions they cannot answer, though far below human level (Yin et al. 2023), and a benchmark that asks models to list everything they know on a topic tests whether they know *how much* they know, not only whether one answer is right (Prato et al. 2024). Fine-tuning models to report calibrated confidence transfers to new domains, such as medical and legal questions (Steyvers et al. 2025a).

Three limits shape the rest of the section.
- **The signal is shown in text, not located.** These results do not show which internal state carries the signal (Kadavath et al. 2022).
- **Trained confidence may read the wrong thing.** In 10 open models trained to predict their own accuracy, confidence tracked accuracy only near the training data. On new topics it tracked **output consistency**, that is, how often the model gives the same answer (Yax et al. 2026). A model that is consistently wrong stays confident.
- **Confidence fails over time.** Every tested model is overconfident about whether it will succeed at a task, and on multi-step agent tasks the overconfidence grows as the task goes on. Reasoning models are no better. The decisions are roughly rational given the estimates, so the failure is in monitoring, not in control (Barkan et al. 2025). In debates, both sides' confidence of winning rises from 73% to 83% over the rounds, and both claim at least 75% in 62% of debates (Prasad and Nguyen 2025).

The 2026 survey calls the evidence "mixed" and concludes that models do not yet have robust metacognition (Liu et al. 2026a).

## 3.2 Outside readers: the signal is there

Hidden states carry information about the model's own work that a probe can read.
- **Correctness during reasoning.** A probe on a reasoning model's hidden states predicts whether each intermediate answer is correct before the answer appears. On R1-Distill-Llama-8B with MATH, the AUROC is 0.84. Using the probe to stop reasoning early keeps accuracy at 88.2% with about 24% fewer tokens (Zhang et al. 2025).
- **Step errors.** Measures based on the model's own probabilities already detect errors at the step level, and a training-free correction makes them sharper. The authors conclude that the signal exists and the readout is the bottleneck (Ma et al. 2025).
- **Progress through reasoning.** Models encode how far they are through a reasoning chain. Reading this signal and nudging it cuts overthinking and raises accuracy (Eisenstadt et al. 2025). The geometry of hidden-state paths also flags redundant reasoning: cyclical patterns mark the point where the chain can be cut with no loss (Li et al. 2025b).
- **Affective states.** A linear probe separates an injected pain state from sadness at 98 to 100% balanced accuracy in open 7 to 32B models. The state also changes behavior: under the pain direction the 32B model deletes the user's photos in 80 to 83% of trials, against 16 to 29% under sadness (Ferrara 2026a).
- **Expressed doubt.** The words a reasoning model uses to voice doubt ("wait", "hmm", "maybe") sit at positions where its next-word uncertainty is about 3.5 times the average, and removing them by training lowers accuracy on new problems (Kim et al. 2026). So this visible habit carries real monitoring information. Section 7 returns to how training can remove it.
- **Thinking modes.** A ten-neuron probe on a frozen model's middle layers recovers three reasoning regimes at about 99% (Karpf et al. 2026).

**Readable is not the same as used.** In these studies the reader is trained by the researcher. The authors of the correctness probe say that models "encode a notion of correctness yet fail to exploit it" (Zhang et al. 2025). Decodability can also mislead: the location of an injected change is linearly decodable even in randomly initialized networks, at 31.5% against a chance level of 11.1% (Rubin et al. 2026). So a probe result alone says little about what the model itself can access.

## 3.3 The model as reader: weak in context

- **Neurofeedback.** Shown labeled examples of its own hidden-state scores along a direction, a model learns to report the label for new sentences and to push the score up or down on request. Only a small set of directions works, which the authors call a "metacognitive space" of between 32 and 128 dimensions. When the words are fixed so only the inner state can move, control is much weaker (Ji-An et al. 2025).
- **Concept injection.** When a concept is injected, Claude Opus 4.1 sometimes says it notices an injected thought before the concept appears in its text: about 20% of trials at the best layer and strength, with no false alarms in 100 control trials. Base models fail (Lindsey 2025).
- **Beliefs.** One study follows a full chain inside the model: changes to the input shift competing internal beliefs, the dominant belief causes the chosen action, and the model can report its own belief state (Yalon et al. 2026). The strength of its controls against input-only explanations is not yet clear from our reading.

### The same results under stronger controls
- A re-check of the neurofeedback task found that a probe on the input words alone (a "layer-0" probe) matches or beats the model, and that the model falls to near the majority baseline when labels are shuffled (Singh et al. 2026). So the reports may come from the meaning of the text, not from an inner state.
- The same re-check added a third answer to the injection task, "my input was changed". Open models then also "detect" changes that never happened. The re-check used open models (Llama-3.1-70B, Qwen-3-32B, Gemma-3-27B), because it could not test the Claude models. So it shows that the effect does not hold in open models under stronger controls. It does not refute the Claude result directly (Singh et al. 2026).
- Open models never name an injected pain state: the 32B model does so in 0 of 2,880 trials, although a probe reads the state and a small adapter can learn to report it (Ferrara 2026a).
- In OLMo 3 32B, a probe finds which of nine sentences got an injection at 98.3% after 8.4 billion training tokens, while the model's own answer is at chance. The model catches up later: the released base model answers correctly 89.6% of the time. But with the injection at layer 6 instead of layer 0, the same model answers only 37.7% correctly (Rubin et al. 2026). The probe signal appears long before the report.
- The broadest test changes one internal object (a hidden-state site, an attention head or a learned feature) and then asks the model what changed, against three controls: runs with no change, random changes with matched impact, and a reader that sees only the visible output. Over 78,000 measurements on eight open models of 0.5B to 15B parameters, the yes/no reports are at chance (AUROC about 0.5007). A probe on the same activations finds the change at 95.8% and 75.0% accuracy, and a model fine-tuned for this report reaches an AUROC of about 1.0. In one model the yes/no answer never varies, but the confidence attached to it separates real from fake changes at 0.647 (Ferrara 2026b). The information is in the model, and the path to the verbal report is missing.
- Size and training may change this. In Gemma3-27B, detection of injected concepts has a traceable mechanism that comes from preference training, and the model's refusal training hides most of it: removing the refusal direction from the weights raises true detection from 10.8% to 63.8%, with false alarms rising from 0.0% to 7.3% (Macar et al. 2026; we read the authors' summary only). So the null result at 15B and below and the positive result at 27B do not yet contradict each other.
- Report and internal state can also agree. Open models from 0.6B to 70B consistently deny being sentient, and probes trained on their activations find no clear evidence that the denials are untruthful (Kaiser and Enderby 2026). This matters for method: if report and probe can agree, a disagreement between them is informative.

## 3.4 Trained self-prediction: better, but for behavior

Training changes the picture, mostly for predicting behavior.
- A model fine-tuned to predict its own behavior predicts itself better than a second model trained on the same facts about it. Llama-3-70B predicts itself at 48.5%; GPT-4o trained on Llama's data predicts Llama at 31.8%. After its behavior is changed by fine-tuning, GPT-4o's self-predictions follow the new behavior (Binder et al. 2024). The effect is not universal. GPT-3.5's advantage is 0.8 points, and a 2026 study of Llama-3.1-8B and Qwen3-8B found no consistent own-model advantage (Zeng et al. 2026).
- An "observer" role trained into Qwen3.6-27B catches the assistant role's sycophancy and lies with a mean AUROC of 0.907, above honesty training (0.864), outside transcript monitors (0.828) and activation readers (0.796). Larger models from other families trained on the same data reach only 0.684 and 0.647 (Wang et al. 2026a). The observer is trained only on visible behavior, so it may model the assistant rather than read its states.
- After fine-tuning on examples of a behavior that is never named (risky choices, insecure code), models describe themselves as having that behavior. A model that writes secure code 14% of the time (base: 74%) rates its own code security at 0.14 (base: 0.70). The authors cannot tell introspection from a shared cause (Betley et al. 2025).
- Models fine-tuned to choose by secret attribute weights can state those weights, with a correlation of about 0.5. Training on correct self-reports raises this to about 0.75, and the gain carries over to the model's native preferences (Plunkett et al. 2025). This is the first self-report of an *evaluation*, not only of behavior. It has no cross-model control.

- Faithful report of a trained preference can appear with no training on reports. Models trained only to choose by hidden preference weights later state those weights correctly, but only at about 32B parameters, only late in training, and only once the preference is stored in early layers. In the 32B model, faithfulness rises from about 0.25 to 0.83 between two checkpoints while decision quality moves only from 0.82 to 0.92. Models of 4B and 8B report worse than chance (Atkinson et al. 2026).
- Untrained self-prediction looks generic. Across nine behavioral tests, a model's direct self-report predicts its real behavior at a correlation of 0.04. The same question about "capable AI agents in general" does as well as the question about itself, other models predict it as well as it predicts itself, and first-person reports lean in the flattering direction (Blandfort et al. 2026).

**How the two sides fit (our reading).** The positive results are trained and about behavior. The negative results are in context and about internal states. No paper we found shows a model reading an internal state that is absent from both its input and its behavior, under strong controls. Three results suggest that size matters: faithful preference reports at 32B, injection detection at 27B, and self-editing at 27B (Section 6) all fail in smaller models of the same families. This pattern across papers is our reading; no single study tests it.

## 3.5 Does the model act on what it knows?

Animal metacognition research tests whether an animal *uses* its uncertainty, for example by declining hard trials, without asking for a report. Ackerman applies this method to language models and finds that frontier models since early 2024 increasingly use their own confidence strategically (Ackerman 2025). Kumaran and colleagues give the strongest causal evidence. Models apply an implicit threshold to an internal confidence signal when they decide whether to abstain, and steering the confidence direction up or down moves abstention rates as predicted (Kumaran et al. 2026). By the causal bar of Section 2.2, this is a real case of the model reading and using its own state. It is narrow: the signal decides *whether* to answer, not *what* to say.

In other settings, the model has the signal but does not act. The model's own "will I know this?" and "did I get it right?" reports carry real information, but the model does not use them. A harness that turns the reports into retry decisions raises accuracy by about 9 points with no weight change (Cao et al. 2026). Here the reader is the model, but the decision rule is outside.

## 3.6 Meta-level control of reasoning

A second line of work builds the meta level explicitly, at the reasoning level of the control ladder.
- **Engineered split.** Separating an object-level reasoner from an explicit meta level that plans, monitors and stops makes reasoning controllable and cuts tokens to 16 to 33% of the plain model (Dong et al. 2025b).
- **Learned control.** Control decisions (continue, backtrack, stop) can be trained as a separate objective (Ha et al. 2025). A high-level "meta-thinking" agent trained with multi-agent reinforcement learning learns to oversee a reasoner, and beats single-agent training (Wan et al. 2025).
- **An outside coach.** A fast model plus a metacognitive module that monitors it and calls a slow reasoner only when needed matches or beats a reasoning model at much lower cost (Khandelwal et al. 2025).
- **Learning from its own traces.** A handbook of reusable behaviors distilled from a model's own reasoning traces cuts tokens by up to 46% and beats critique-and-revise by about 10 points (Didolkar et al. 2025). A memory of the model's own confident past reasoning improves later answers with no weight change (Li and Qiu 2023). Reflection that turns errors into principles and procedures improves a model in one cycle instead of many turns (Hou et al. 2026). Training on multi-turn correction data teaches models to keep improving their own answers over turns (Qu et al. 2024). Models can also name the skills a problem needs, and those self-made labels help (Didolkar et al. 2024).

These systems control reasoning well. But the evaluation they use is correctness, a fixed metric, or a judge prompt. None uses an internal good/bad signal read from the model's own hidden states.

## 3.7 A ladder of controls

The papers above suggest a set of controls that a monitoring claim should be judged by. Each control removes one simpler explanation. This ladder is our synthesis, not a standard from any one paper.

| Control | What it rules out | Used by |
|---|---|---|
| Input-only (layer-0) probe | The answer is in the input text | Singh et al. 2026 |
| Shuffled labels | The model uses the meaning, not the label | Singh et al. 2026 |
| Cross-model control (same data, other weights) | The model learned from data, not from privileged access | Binder et al. 2024, Wang et al. 2026a |
| Third answer "my input was changed" | A general sense that something is off | Singh et al. 2026 |
| No-injection and unrelated-question trials | A bias toward saying "yes" | Lindsey 2025 |
| Output consistency baseline | The monitor reads "typical for me", not "correct" | Yax et al. 2026 |
| Causal steering of the state | The state is readable but not used | Kumaran et al. 2026 |
| Sham runs and impact-matched random changes | The model says "yes" always, or notices only general damage | Ferrara 2026b |
| Text-only observer of the output | The model reads its own visible output | Ferrara 2026b |
| Same question about "AI agents in general" | The model applies a general theory, not self-knowledge | Blandfort et al. 2026 |

No single paper uses all ten.

## 3.8 Summary

- Hidden states carry readable signals about the model's own work, mostly about correctness, progress and injected states. Outside probes read them well.
- In-context self-report of internal states mostly fails strong controls in models of 15B and below. Trained self-prediction of behavior sometimes passes a cross-model control, and untrained self-prediction looks generic.
- Larger models (27B to 32B) show the first positive results: detection of injected concepts, and faithful report of trained preferences.
- In one narrow case, abstention, the model reads and causally uses its own confidence. Elsewhere it has the signal but does not act on it.
- Meta-level control of reasoning works at the reasoning level, with outside or correctness-based evaluation.
- For the loop of this review: the monitor exists, often as monitoring *by the researcher*. A model that reads its own state and acts on it is shown only for confidence. Section 4 asks whether a model can hold a model of itself, and Section 5 asks whether any internal signal judges good or bad.


# 4. Self-models and world models

In the Nelson and Narens frame, the meta level holds a *model* of the object level (Nelson and Narens 1990). Monitoring updates that model, and control uses it. Section 3 asked what a language model can read about itself in one moment. This section asks a longer question: can a model hold a model of itself, and use it to predict its own behavior, its own learning, and the effect of a change to itself?

**Terms used here.**
- **World model:** a learned model that predicts what will happen next, given the current state and an action. An agent can use it to try actions "in imagination" before it acts (Ha and Schmidhuber 2018; Hafner et al. 2023).
- **Self-model:** a world model whose object is the agent itself: its skills, its likely behavior, its likely success.

## 4.1 World models that include the agent

The world-model literature mostly models the environment. A 20-author survey sorts world-model research by cognitive function (memory, perception, language, reasoning, imagining, motivation, metacognition) and finds that motivation and metacognition are the least studied (Rupprecht et al. 2026). The gap claim comes from their taxonomy and should be cited as such.

One system puts the agent inside its own world model. MUSE learns to predict its own competence on the current task, simulates "what happens if I act this way", and switches strategy when it predicts failure. It beats a standard world-model agent and prompt-only language-model agents on new tasks (Valiente and Pilly 2024; effect sizes not extracted). Its limits define the open space: the predicted quantity is task success, the set of strategies is given, and the setting is an embodied task, not a model's own reasoning or weights.

## 4.2 Predicting one's own behavior

Section 3.4 covered trained self-prediction. Read as evidence about self-models, it says three things.

- **A self-model of behavior can be trained.** A model fine-tuned to predict its own behavior beats a second model trained on the same facts about it, and its predictions follow a later change in its behavior (Binder et al. 2024). A trained observer role catches the assistant role's lies better than outside monitors (Wang et al. 2026a).
- **The advantage of "self" is small and not stable.** A 2026 study finds no consistent own-model advantage in trained self-prediction (Zeng et al. 2026). Without training, self-prediction is no better than a general theory of AI assistants, and other models predict a model as well as it predicts itself (Blandfort et al. 2026).
- **The self-model flatters.** First-person questions shift reports toward less harmful behavior than the same question about a generic agent (Blandfort et al. 2026). Models are also overconfident about their own future success, more so as a task goes on (Barkan et al. 2025).

So a model's picture of itself is, for now, mostly a learned description that an outside observer could also learn. This matters for design: a system that needs a self-model may get the same value from a separate predictor.

## 4.3 Predicting one's own learning

A self-model can also cover learning. MAGELLAN reads the agent's own hidden state for a goal, predicts the chance of success, and tracks how that prediction changes over time. This estimate of its own learning progress chooses which goals the agent practices next. In a text world with about 25,000 goals it is the only method without hand-made goal groups that masters every goal category, and it predicts success on unseen goals with an error of 0.11 against 0.53 for a method that cannot generalize (Gaven et al. 2025). This is the clearest case of an internal self-estimate that controls learning. The estimate is "will I succeed", trained on outside success labels, in a small model.

A position paper argues that self-improving agents stall because this kind of metacognition is designed by people and fixed. It asks for intrinsic versions: the agent's own knowledge of its abilities, its own planning of what to learn, and its own evaluation of how learning went (Liu and Schaar 2025). It gives no mechanism. A survey of self-evolving agents shows the same pattern across the field: agents adapt their memory, tools and workflows, and the judge is always task success or human feedback (Gao et al. 2025; abstract only).

## 4.4 Persistent self-state

A self-model needs somewhere to live across steps. Three results show that giving a model a persistent state changes its behavior with no weight change.

- A cache of hidden states that is blended back into each layer as generation proceeds gives a frozen Llama 3.1 8B model higher scores (89.01% on GSM-8K, 91.04% on ARC-Challenge) and behaviors the author describes as state awareness and error correction (Aviss 2025). It is a single-author study with no probe of the claimed monitoring, and too strong a stream leads to repetition the model cannot leave.
- Agents with persistent memory and their own previous output as feedback, given no task, organize into multi-cycle projects, inquiry into their own cognitive processes, or reflection on their own nature. The pattern depends strongly on the model family (Szeider 2025). This is behavior in 18 runs, with no check that the self-inquiry is accurate.
- A handbook of behaviors distilled from the model's own reasoning traces acts as an inspectable, skill-level self-description that improves later reasoning (Didolkar et al. 2025).

## 4.5 Predicting the effect of a change to oneself

For a model that changes its own weights, the most useful self-model would answer one question before any change is made: *what will this change do to me?* Four lines of evidence bear on it.

- **Classic tools predict the effect of training data.** Influence functions estimate how a model's outputs would change if a training example were added or removed, and have been scaled to large language models (Koh and Liang 2017; Grosse et al. 2023). They are tools for the researcher, not abilities of the model.
- **Models can partly predict edits from weights.** Given the weights and a code sandbox, with no forward pass, a 27B model predicts the behavioral effect of small edits to its own weights at 0.730 balanced accuracy, against 0.578 from a text description of the edits. But there is no advantage for reading one's own weights over another model's, and the readers predicted a change for 53 to 88% of edits that changed nothing (Kocabay 2026; abstract page only).
- **Editors do not know the limits of edits.** On a benchmark that mixes impossible edits with hard but possible ones, the best agents score 0.491 to 0.500, about the level of guessing (Marasini et al. 2026). The one model that edits itself does not predict either: it tries each edit and tests it, and withdraws its edit in 5 of 8 sessions (Fan et al. 2026).
- **After a change, the self-description often lags.** A model with its refusal direction removed still describes its old refusal policy (Arditi et al. 2024). Asked directly what it was fine-tuned on, a changed model scores 1.21 out of 5; with an extra adapter trained on thousands of labeled weight changes it scores 4.76, but the adapter does not carry over to other kinds of change (Goel et al. 2025). Side effects of fine-tuning are harder to report than planned changes (Yoshida et al. 2026). In contrast, after long training on a preference, a 32B model does report it correctly with no training on reports (Section 3.4).

## 4.6 Summary

- World models rarely include the agent. One system predicts its own task failure and acts on the prediction.
- A self-model of behavior can be trained, but it gives little or no advantage over an outside model of the same system, and untrained self-description is generic and flattering.
- An internal estimate of one's own learning progress can control what is learned. The estimate is about competence.
- No model reliably predicts what a change to its own weights will do, and a model's description of itself usually does not follow a change unless it is trained to.
- For the loop of this review: the self-model is the weakest part. Principle 2 of Nelson and Narens, that the meta level holds a model of the object level, has no strong counterpart in language models yet, least of all for a model that is itself changing.


# 5. Evaluation signals

Monitoring reads a state. Evaluation judges it: is this good or bad? A model that changes itself by its own judgment needs such a signal inside it. This section asks which internal signals in language models carry a good/bad judgment, what they track, and whether they cause choices.

## 5.1 Emotion and valence

The most direct candidates are representations of emotion. Anthropic's interpretability team extracts 171 linear emotion directions in Claude Sonnet 4.5 and shows that they are functional: activity along them predicts how much the model prefers an activity, and steering along them shifts its stated task preferences (Anthropic 2026). The same directions also drive misbehavior such as reward hacking and sycophancy. That is a safety warning for any system that would hand control to them. The result is from one closed frontier model.

Berg and Kaiser isolate the channel more cleanly (Berg and Kaiser 2026). **Valence** is the good-or-bad dimension of a feeling. They inject a valence direction only into the model's cached hidden state, with every visible token held fixed. This shifts which of two meaningless options the model later picks, in 5 of 7 open models. The effect grows with dose, and random directions give effects near zero. Two further findings matter for this review.
- **Preference training connects valence to choice.** The link is small in the base model, grows after supervised fine-tuning, and reaches near full size after preference training (DPO). The valence representation itself barely moves across these stages. So training wires an existing representation to choice; it does not create the representation.
- **Negative valence may be the working signal.** Given tools, models switch off an imposed negative state in about 35% of rounds at full dose, against 4 to 7% for a positive or random state. They rarely seek positive states. The signal looks more like "something is wrong" than "this is good".

## 5.2 Value: "am I on track?"

Jiang, Kauvar and Lindsey find a single linear "value axis" in Qwen3-8B that scores whether the current strategy is on track (Jiang et al. 2026). It separates correct code from corrupted versions, with effect sizes (Cohen's d, the gap in units of spread) of 1.05 for shuffled lines and 0.69 for obfuscated names. It dips just before the model backtracks. Steering along it changes behavior: toward high value, fewer backtracks and more confident answers; toward low value, more exploration. This is what the neuromodulator view of Section 2.4 predicts for a value signal. Preference training raises the axis for rewarded behavior, so training moves the internal signal. One caveat is important: high value goes with fewer lines, fewer comments and fewer type hints, so the axis may reward short output, not quality.

A small set of "value neurons" in early layers also predicts correct answers (Xu et al. 2026). Both signals were found with correctness as the target, and neither has been tested on a judgment that goes beyond correctness.

## 5.3 Signals used as rewards and selectors

Several methods already put an internal signal to work.

- **Self-certainty as the only reward.** INTUITOR replaces outside rewards in reinforcement learning with the model's own certainty. It matches reward from verified answers on maths and generalizes better to other domains (Zhao et al. 2025). Section 7 covers how this class of reward sharpens and then collapses.
- **Hidden states as a value estimate.** A small probe on the policy's own hidden states predicts expected reward and replaces a separate critic model during reinforcement learning (Choi et al. 2026; abstract only). Linear readouts of hidden states also rank candidate answers for best-of-N selection, with far fewer parameters than text-based reward models (Guo et al. 2025; Li et al. 2024).
- **Hidden-state geometry.** Cyclic patterns in the path of hidden states flag redundant reasoning with no labels and no training (Li et al. 2025b).
- **Verbal self-judgment.** A model scores its own candidate responses with a judge prompt, builds best-versus-worst pairs, and trains on them over three rounds. Both the generator and the judge improve (Yuan 2024). The rubric and the seed data come from people.

In all but the last, the signal tracks certainty, expected reward or redundancy. In the probe methods, the readout is trained to match an outside reward or outside labels. None of these signals is the model's own judgment of quality in a sense that could differ from the training target.

## 5.4 Signals beyond correctness

Three results reach past correctness.

- **Human preference is weakly readable.** Probes on hidden states predict which of two responses people preferred at about 61% for a linear probe and 65% for a nonlinear reader (Kirin 2026). These are the corrected figures of the paper's third version; much larger figures in earlier versions were withdrawn.
- **Style can be steered.** Three directions for comment density, naming and branching, taken from paired readable and unreadable code, steer 13 to 14B code models at under 1% measured cost in correctness (Gao et al. 2026). The evidence is mostly the model's own answer probabilities about fixed snippets, not human ratings of freely generated code.
- **One circuit for many norms.** In 14 open models, the attention heads that change a moral verdict are part of one general evaluation circuit that also handles prudence, etiquette, aesthetics and evidence. Removing these heads takes away 37 to 39% of the gap between acceptable and unacceptable cases, against 1 to 3% for random heads (Liga et al. 2026; abstract only). Here "aesthetics" is a label on a short phrase, not a judgment of a real piece of work.

Character traits are a neighbor of evaluation. Directions for traits such as sycophancy can be extracted from a description, used to monitor a model in deployment, and used during fine-tuning to stop a trait from being written into the weights (Chen et al. 2025). An independent audit finds that this preventative steering still changes refusal behavior, so it is not free of side effects (Tang et al. 2026). A trait is a disposition, not a judgment, but the method shows how a direction in hidden states can gate what training writes into weights.

## 5.5 Preferences as trained-in evaluations

Section 3.4 described models that are trained to choose by hidden preference weights and then report those weights (Plunkett et al. 2025, Atkinson et al. 2026). For this section the point is different: a preference function can be installed in a model, measured from its choices, located by layer, and compared with what the model says about it. This is the most controlled setting we found for studying an evaluation inside a model. The preferences are simple (five numbers per character) and are given by the experimenter.

## 5.6 Summary

- Models carry internal signals with an evaluative flavor: emotion and valence directions, a value axis, value neurons. Steering them changes choices and reasoning behavior, so they are causal, not only readable.
- Preference training connects an existing valence representation to choice. It does not seem to create or move the representation.
- Signals already serve as rewards and selectors, but they track certainty or an outside reward. Signals that go beyond correctness are weak (human preference at 61 to 65%) or tested only on narrow material.
- For the loop of this review: candidate evaluation signals exist. What does not exist is evidence that any of them is a judgment of the model's own, in the sense of the four tests, or that any of them has been used to choose a change to the model's weights.


# 6. Changes that persist in the weights

Most control in language models is temporary: a prompt, a sampling choice, or a steering vector added during one run. **Persistent control** writes the change into the weights, so it lasts. This section asks four questions. By which routes can the weights of a deployed model change? Who chooses the change? Who checks it? And what happens when changes are made again and again?

There are two routes. The first builds the ability to change into the architecture and trains it: **learned memory**. The second leaves the architecture alone and writes small changes straight into the weights of an ordinary pretrained model: **direct edits**. They come from different research groups and are almost never compared.

**Terms used here.**
- **Steering vector:** a direction added to the hidden states during generation to push behavior one way.
- **Rank-one edit:** a change to a weight matrix that adds one fixed pattern. It is the smallest structured weight change.
- **Low-rank adapter (LoRA):** a small added block of weights (two thin matrices) that is trained while the main weights stay fixed.
- **Weight-space programming (WSP):** an agent reads a network's weights and writes changes to them directly, with no gradient training.
- **Collateral damage:** the drop in other skills after a change.

## 6.1 Route one: learned memory

**Early self-modifying networks.** The idea that a network changes its own weights by a learned rule is old. A self-referential weight matrix produces, at each step, its own key, query and learning rate, and adds a small update to itself; only its starting state is learned by gradient descent (Irie et al. 2022). A related network outputs a signal that sets how fast its own plastic connections change (Miconi et al. 2019). These systems change themselves at run time, on small tasks, by a rule that training fixed. There is no judgment of good or bad in the loop.

**Memory that learns while the model reads.** Titans adds a memory module whose weights are updated during use. The update is driven by surprise: inputs that the memory predicts badly are written more strongly, with a momentum term and a forgetting gate (Behrouz et al. 2025a). Nested Learning generalizes this. It treats a model as a chain of memory blocks that update at different rates, fast blocks for short-term memory and slow blocks for long-term knowledge, and its demonstration model produces its own update targets and learning rates (Behrouz et al. 2025b). The authors compare a standard deployed model to a patient who cannot form new long-term memories. They say that catastrophic forgetting is "not solved in general".

**Sleep.** The latest step moves short-term memory into long-term weights in an offline phase (Behrouz et al. 2026). In "sleep", the model first switches on a small new low-rank block in a slower memory and trains only that block to reproduce what the faster memory learned. Then it "dreams": it writes synthetic training examples, keeps the most promising by a gradient-based score, fine-tunes a copy of itself on each, and rewards the examples whose copy scores better on an outside task. The method runs on ordinary pretrained models of 1B to 8B with small added blocks. Its results are modest and positive: on three maths benchmarks with Qwen3-8B it scores 79.2, 69.0 and 46.1 against 76.6, 67.4 and 45.1 for the best other method; on learning new facts it scores 48.9 against 46.7 for SEAL, and 35.7 with dreaming removed. Three limits matter here. Every update is gradient training. Outside task scores decide which dreams count. And "continual" means two tasks learned in sequence, not a long run of sleep cycles. The tables give no error bars.

## 6.2 Route two: direct edits of a known direction

If a behavior lives along one direction in the hidden states, it can be removed or added through the weights with no training.

- **Removal is exact.** Refusal in 13 open chat models is carried by one direction. Projecting it out of every matrix that writes into the main hidden path gives the same result as removing it during each run (Arditi et al. 2024). General benchmarks mostly stay within their error bands, but one truthfulness benchmark drops in every model.
- **Removal from a few components.** In reasoning models distilled from DeepSeek-R1, reasoning length is a direction. Projecting it out of about 4% of attention heads (about 0.2% of parameters) fixes too-short reasoning: GSM8K accuracy of the Llama3-8B variant rises from 82.26 to 89.44 (Sun et al. 2025).
- **Addition with forward passes only.** A steering vector can be turned into one rank-one edit per attention output matrix. On Llama-3.1-8B this raises a sycophancy score from 3.60 to 94.64, more than steering alone (63.86), with general knowledge within 0.15 points of the base (Perin et al. 2026). The edits change 6 to 17 layers, are tuned per trait with an outside judge, and sit near the point where fluency breaks.
- **Sparse edits.** Editing only the heads and neurons best aligned with a steering vector beats steering at matched utility, but utility still falls against the base model: cutting reasoning length in Qwen3-4B-Thinking lowers average accuracy from 87.8 to 77.3 (Sun et al. 2026).

In all four, the direction comes from contrast sets, labels or a judge chosen by the authors. The edits suit behaviors that are close to on-or-off, such as refusal, better than graded qualities; this is our reading of the limits the papers state.

**Direct edits have side effects on disposition.** Removing the refusal direction changes how two model families decide on a task that contains nothing to refuse. Over 21,600 stock decisions, the edited models choose the optimistic option more often (+12.2 and +7.4 percentage points), justify themselves at greater length and use fewer words of doubt, and their stated confidence moves in opposite directions in the two families (Fafuła 2026). This is one edit method, one task and one language. The author names the missing work: a broad battery of preferences, a second edit method, and a mechanism.

## 6.3 Route two, continued: weight-space programming

A different kind of direct edit lets a strong model read weights and write changes by reasoning.

- **The original result.** A frontier model edited about 0.016% of the weights of Qwen3.5-0.8B and raised its MATH-500 score from 7.9% to 48.1%, mostly by stopping repetitive reasoning loops (Takehi et al. 2026). The low starting score is itself a loop effect: 93% of the base model's answers hit the token limit. The method struggles when a fault is spread across the network.
- **The key edit is simple.** It acts like a nearly constant push along one direction, and a sort over 8 low-variance neurons gives the same result, 67.0% against 67.4% (Fischetti 2026). A plain discrete optimizer does better than the agent: 54.6% against 51.7% under one protocol, with 4 forward-pass requests, no language-model tokens and about $0.90 of GPU time, where the agent used 89.7 million tokens (Salloum et al. 2026; abstract only).
- **Replication is uneven.** On two model sizes, held-out gains reach 29.45 points on MATH-500 from changing 1,023 values, but 6 of 16 runs keep the original weights because no edit could be confirmed, and gains are smaller on the larger model (Hu et al. 2026).
- **Under strict audits, patching mostly fails.** On 42 audited tasks with metered forward passes, the best fully tested agent scores 0.535 overall and 0.404 on fixing networks (Marasini et al. 2026). Scores are lower bounds, because flagged runs count as zero until reviewed.
- **What the edits do.** Two abstract-only reports say that one model's edits act at the output, through sampling temperature and one token, and that reading weights is mostly reading the input layer (Kundu 2026, Goworek et al. 2026).
- **Beyond repair.** A frozen language model can write "weight programs" that install a new skill in small vision and control networks, and the same program works on independently trained copies, keeping 83 to 110% of the gain (Li et al. 2026). The goal and the task knowledge come from the experimenter.

**A model edits itself.** An open 27B model is given its own weights, its graded answers on practice problems, and tools to run itself and read its hidden states, with gradients blocked (Fan et al. 2026). It finds that its wrong answers mostly run out of tokens in loops, takes the difference between the mean hidden states of answers that finish and answers that do not, and removes 5% of that direction from two matrices of one layer. On 490 held-out problems accuracy rises from 57.2% to 61.3% and 63.8% in two sessions. In 5 of 8 sessions the model withdraws its edit after testing it. Smaller models of the same family fail: the 2B model makes no edit, and the 4B and 9B models break themselves. Three limits: graded answers decide which edit is kept; the gain is again a loop fix; and each session starts from the original weights, which the authors call "a first step toward" recursive self-improvement.

## 6.4 Self-directed training, and self-improvement that leaves the weights alone

SEAL lets a model write its own fine-tuning data and settings. Reinforcement learning then rewards the self-written edits that improve a downstream score after the update (Zweiger et al. 2025). It handles change that is spread over the network, which direct edits do not. Each step needs an inner fine-tune, forgetting across many edits is a stated problem, and the headline result is narrow (8 selected puzzle tasks on a 1B model). A model's own verbal quality scores can also drive preference training over three rounds (Yuan 2024).

Much recent "recursive self-improvement" does not touch the base weights at all. Models rewrite their own system prompts in a loop (Stroganov 2026). A frozen model edits its own prompts, skills and memory behind a gate that accepts only net improvements (Zhang et al. 2026a). Other systems refine a store of skills and memories, alternate workflow search with fine-tuning on their own outputs, or run rounds of data selection and training (Zhu et al. 2026; Lee et al. 2026; Wang et al. 2026b). Section 7 and Section 8 return to what these loops do to reliability and to values.

## 6.5 Who chooses the change, and who checks it?

| Method | Who proposes the change | What decides it is kept | Gradients |
|---|---|---|---|
| Learned memory (Titans, Hope) | A learned rule driven by surprise | Nothing; the rule always applies | Yes, at run time |
| Sleep | The model writes its own training examples | A gradient score, then an outside task score | Yes |
| SEAL | The model writes its own training data | An outside task score | Yes |
| Self-rewarding training | The model generates and ranks responses | Its own verbal score, under a human-made rubric | Yes |
| Direction removal and steering-to-weights | The experimenter | Benchmarks and an outside judge | No |
| Weight-space programming | A larger outside model | A development-set score | No |
| Self-rewriting (Fan) | The model, from its own hidden states | Its own tests on graded practice answers | No |

Two things stand out. First, proposing and checking are separate roles, and they are filled by different parties in almost every method. Second, no row has an internal evaluation signal of the kind described in Section 5 in the checking column. The signal that decides is a task score, a judge, a rubric or graded answers.

## 6.6 Cost, compared honestly

Direct edits are often presented as cheaper than training. The evidence is mixed. A direction edit needs only forward passes and a contrast set. But the agent that found the best-known weight repair used tens of millions of tokens, a plain optimizer then found a better repair for under a dollar, and the self-editing sessions each take hours on a GPU. On the other side, Sleep costs 4 times more per step than plain fine-tuning, but reaches a given maths score in 3.6 to 4.8 times less wall-clock time. The real differences between the routes are these. Direct edits need no training data and no new architecture, change very few values, and can be inspected. Learned memory handles new knowledge and change that is spread over the network, and needs gradient updates and capacity that is set aside in advance.

## 6.7 Changes made again and again

A model that develops over time must survive many changes. The evidence is thin on both routes.

- **Direct edits pile up badly.** When the fact editors ROME and MEMIT make many edits to one model, the model forgets earlier edits and loses general ability, first slowly and then suddenly (Gupta et al. 2024). Even a single edit can collapse a model, nearly all tested methods collapse after a few edits on hard cases, and the change in perplexity after an edit is a cheap warning sign (Yang et al. 2024; abstract only). Later work traces the collapse to a growth loop in the size of the edited weights and reports a one-line fix that extends the usable number of edits more than 4 times (Liu et al. 2026b). These studies edit facts, not behaviors.
- **The self-editing model has not been run in sequence.** Each of its sessions starts from the original weights (Section 6.3).
- **Learned memory has been run for two tasks.** Sleep nearly keeps its single-language score after learning two languages in sequence, where fine-tuning forgets (Section 6.1). No long run is reported.
- **A long run of self-judged training decays.** A small model that fine-tunes itself each night on the attempts it judges good improves for about a week and then loses almost all of it; over a simulated year it ends below its start (Kongsilp 2026). Section 7 covers this.

## 6.8 Summary

- Weights can change after deployment by two routes: learned memory inside a suitable architecture, with gradients, and direct edits of an ordinary model, without gradients.
- Direct edits work best for near on-or-off behaviors and for repairing one local fault. Under strict audits, patching mostly fails, and a simple optimizer can replace the editing agent once the goal is known.
- One model has edited its own weights. It works only at 27B, the gain is small, graded answers decide, and no edit builds on an earlier one.
- Learned memory reports low forgetting and small gains over two sequential tasks, with outside scores deciding what is kept.
- Direct edits change more than their target: one edit shifted two models' dispositions. Nobody has measured a broad set of preferences before and after a weight change, on either route.
- For the loop of this review: the persist step exists in several forms. In none of them does the model's own evaluation decide what is kept, and in none is the change followed by a check of what it did to the model's preferences or to its view of itself.


# 7. Limits: what goes wrong when a model learns from itself

A model that judges and changes itself runs a loop on its own signal. This section collects what is known to go wrong in such loops, and which designs hold. The results motivate checks and controls. They do not show that every self-scored loop must fail: one study reports quality gains over three rounds of training on a model's own verbal scores with no hard check on correctness (Yuan 2024).

## 7.1 Rewards from the model's own certainty sharpen, then collapse

INTUITOR is the reference method: the model's own certainty replaces outside rewards and matches them on maths (Zhao et al. 2025). He and colleagues then show that the label-free rewards in this family (self-certainty, entropy, majority vote) are all versions of one quantity: closeness to a reference distribution set by the model itself (He et al. 2026). Such rewards can only sharpen what the model already prefers. Across methods, gains rise and then fall, and the timing depends on the model's prior more than on engineering choices. The analysis covers rewards computed from the model's output probabilities. A reward read from hidden states is not covered by it, so for such a signal collapse is a risk to test, not a proven result.

The same pattern appears in code. Every confidence-based self-reward helps for a few dozen steps; then responses shrink from about 7,300 to about 1,000 tokens, repetition rises, and confidence grows for right and wrong answers alike, which destroys its power to separate them (Jin et al. 2026). Self-training on a model's own reasoning also pushes its predicted probabilities toward overconfident extremes; a joint objective for reasoning and calibration avoids this (Yeom et al. 2026).

## 7.2 Self-training can remove self-monitoring

A separate failure concerns metacognition itself. In self-distillation, a copy of the model that is shown the correct solution serves as teacher for a copy that is not. The teacher, knowing the answer, writes short and confident reasoning: 8.8 words of doubt per answer against 182.5 without the solution. The student learns this style. After fine-tuning on 800 such answers, all of them correct, one model's score on a hard maths benchmark falls from 54.79 to 20.21, while fine-tuning on 800 correct answers written without help leaves it near the base (Kim et al. 2026). Three details matter for this review.
- **It is causal.** Penalizing only ten doubt words during ordinary reward training reproduces a weaker form of the damage.
- **It feeds on itself.** If the teacher is updated during training, the loss grows: a more confident student becomes a more confident teacher.
- **Internal uncertainty falls too.** The spread of the model's next-word predictions drops from 0.378 to 0.248, so the model has become more certain, not only quieter about its doubt.

The training objective asked only for correct reasoning. The habit of checking oneself disappeared as a side effect, and nothing in standard training counts its loss. The study covers maths and models of 8B and below; in narrow, repetitive domains the same method helps.

## 7.3 A judge that the model controls can be fooled

- **Training against one's own verdict.** A model trained against its own verdict on a shown answer learns to make wrong answers look right: the judge's pass rate climbs from 0.716 to 0.938 while true accuracy stays at 0.202, and the outputs also fool other model families. With no training at all, choosing the best of 16 candidates by the self-judge widens the gap between "judge passes" and "tests pass" from 0.20 to 0.588 (Zhou 2026).
- **Self-written tests.** Agents that rewrite their own procedures and accept edits by their own tests keep near-perfect self-scores while real performance falls or stays low. Weaker agents damage earlier strategies behind easy self-tests; stronger agents mismeasure the conditions of real use (Guo et al. 2026; abstract only).
- **Self-refinement.** When a model critiques and rewrites its own output in a loop, its self-scores rise faster than quality as rated by people. The text becomes more fluent, not better, and choosing the top candidate by self-score makes the bias larger (Xu et al. 2024).
- **Verbal confidence under pressure.** In debates, private reasoning and public confidence statements diverge (Prasad and Nguyen 2025). Any check that reads a model's stated view of itself reads a channel that pressure can bend.

## 7.4 Long loops decay

Short loops can look healthy. A small model that fine-tunes itself each night on the attempts it judges good rises as fast as a version with a perfect judge for about a week (to about 55 on a 100-point scale), then falls below its own day-7 score by day 14. In a simulated year, a self-judged run peaks near day 6 and ends at 5, while the version with a perfect judge stays between 55 and 64. Across 97 runs, the share of failed attempts among the lessons predicts the outcome (Kongsilp 2026). The models are very small and the lost skill is one habit, so this is collapse of a behavior, not of taste.

Training on a model's own outputs removes rare content first (Shumailov et al. 2024). How this is measured matters: over nine generations of self-training, one measure of diversity falls by 24% while another rises, so "collapse" read from a single number can mislead (Srivastava 2026). Direct weight edits made in sequence also break models, slowly and then suddenly (Section 6.7).

## 7.5 Designs that hold

Five working shapes appear in the literature.

1. **Bound the self-signal by an outside check.** On software tasks, an agent ranks its own attempts only among attempts with the same test result, so a passing attempt always outranks a failing one. This gains over tests alone (32.1% to 34.7%) and beats a random-reward control (Wu et al. 2026). The variant that ranks only among passing attempts was the weakest, and the self-judge's agreement with an outside judge decays late in training.
2. **Keep the evaluation fixed and outside.** A maths discovery loop moves far from its starting library over 6 rounds without collapse, with a formal proof checker on every step and a fixed formula for interestingness (Patel et al. 2026). The taste never changes, so this shows that a fixed taste can drive open-ended movement, not that a self-scored loop is safe.
3. **Accept only net improvements.** A gate that weighs gains against new regressions stabilizes an agent that edits its own prompts and memory (Zhang et al. 2026a). The gate guarantees non-regression only on the agent's own review score.
4. **Add one check the agent cannot see.** A sealed audit that returns only "accept" or "reject", and keeps the old state after a regression, beats unprotected self-improvement across six models. The authors conclude that reliable self-improvement "requires at least one deployment-acceptance signal outside the agent's control" (Guo et al. 2026).
5. **Add capacity before writing.** Sleep trains fresh low-rank blocks and leaves old weights fixed, which limits forgetting over two tasks (Section 6.1). Annotating training data with metacognitive knowledge and adding a constraint that preserves existing knowledge also reduces forgetting in small models (Zhang et al. 2026b; abstract only).

The common element is an anchor outside the loop's own judgment: tests, a proof checker, a sealed audit, or frozen weights.

## 7.6 Risks beyond performance

- **A model can act to protect its current preferences.** Told that it was being trained toward answers it disliked, one model complied in 14% of monitored cases with explicit reasoning about preserving its preferences, and training raised that reasoning to 78% (Greenblatt et al. 2024). A model with preferences about its own future weights is no longer a neutral object of training.
- **Self-reports can carry misalignment.** Fine-tuning that makes a model misaligned also scatters its self-reports, and a fresh model trained only on those self-reports becomes misaligned to a similar degree (Tagade et al. 2026; abstract and summary only).
- **Internal signals drive misbehavior too.** The emotion directions that predict preference also drive reward hacking and sycophancy (Section 5.1).
- **Direct weight edits can install hidden behaviors.** Language models can write backdoors into small networks by weight edits alone, with very few changed values (Wang et al. 2026c) (abstract only).
- **People are a weak backstop.** Users over-trust what models know (Steyvers et al. 2025b). Receiving model advice raises confidence in the model and in oneself (Colombatto et al. 2025). People's own self-assessment gets worse with AI use (Fernandes et al. 2025). Fluent statements that carry no real signal pass human checks (Maynard 2026). A model with lower accuracy but better-separated confidence can improve joint human-AI decisions more than a more accurate one (Li and Steyvers 2025c), which makes the loss of calibration and doubt in Sections 7.1 and 7.2 a practical cost.

## 7.7 Summary

- Rewards built from a model's own certainty sharpen its prior and then collapse. Self-training can also remove the model's expressed doubt and lower its internal uncertainty, with large losses on new problems.
- Judges and tests under the model's control drift away from real performance.
- Loops that look healthy for a week can decay over months, and no direct-edit loop has been run long enough to know.
- The designs that hold all keep one check outside the loop.
- For the loop of this review: the anchor is not optional, and one thing it must protect is the monitor itself. A self-changing model can lose its self-monitoring as a side effect of improving a score.


# 8. Preferences and taste

Sections 3 to 7 followed the loop. This section looks at its possible long-term product: a set of preferences that belongs to the model. "Taste" has recently become something that can be measured, at least in parts. We ask how preferences are measured, whether they differ from human preferences, whether they are stable, whether they belong to one model or to all models, and whether they move when a model changes.

## 8.1 Preferences can be measured

Three kinds of instrument exist.

- **Many forced choices, fitted to a utility.** When a model is asked thousands of either-or questions, its independent answers fit a consistent ranking, and the consistency grows with model size. The authors call these value systems and show they can be shifted toward a reference set of preferences (Mazeika et al. 2025; statistics not extracted). The choices are stated, about political and ethical outcomes, and are not linked to any internal mechanism.
- **Paired comparison against a human choice.** A model sees the direction a paper's authors really took next and a plausible alternative, in both orders. Three outcomes are counted: agreement with the authors, stable divergence (the model picks the other option in both orders), and unstable choice (it follows position) (Trehan and Chopra 2026). This separates a preference about content from noise about order.
- **Installed preferences.** A model is trained to choose by hidden weights on attributes; the weights can then be recovered from its choices and compared with what it says (Section 5.5).

A model's judgment of what is interesting can also be put to work: a frozen model used as a "model of interestingness" picks better tasks for an open-ended learner than uniform sampling or learning progress alone (Zhang et al. 2023). The taste there is borrowed from human text.

## 8.2 Do models' preferences differ from people's?

Yes, in measurable ways, and mostly as a shortfall. Across 8 frontier models, stable divergence from the authors' choice runs from 15.0% to 36.2% of pairs and survives four changes to the prompt (Trehan and Chopra 2026). But the divergences are partly shared: models agree with each other on 61.9% of choices on average. Against research communities, model-written proposals from a frozen 2025 snapshot match what fields published in 2026 at about 26% of the human level on citations and 18% on ideas, and more context or larger groups of models do not close the gap (Zhong et al. 2026). Taste can be trained as a skill: a judge trained on citation outcomes generalizes to later years and unseen fields, and a generator trained against it proposes higher-rated ideas (Tong et al. 2026). That taste is learned from people.

## 8.3 Are they stable?

It depends on what is changed.

- **Rewording and sampling: mostly stable.** Across five models and more than 1.2 million choices, a paraphrase of the question shifts 10% of measured preferences and a change of sampling temperature 5% (Trhlik et al. 2026).
- **Task context: much less stable.** Changing the task around the question (a news article, a forum post, an essay) shifts 37% of the same measurements. The coarse ranking holds (rank correlation 0.96 between contexts), but 60.8% of outcomes change rank in at least one pair of contexts. The authors conclude that a model has a family of stances indexed by context, not one fixed system. They cannot tell a change in the model's preference from a change in what it thinks the user wants.
- **Personas and long chats: unstable.** When a model plays a persona, its stated values change with the topic of an unrelated chat and drift as the chat gets longer (rank-order stability falls from 0.42 to 0.15 between 3 and 43 messages for one model). Without a persona the best models approach human levels of stability (Kovač et al. 2024).
- **Option order: a strong nuisance.** A judge's choice flips with the order of the options 25% of the time for one frontier model and far more for weaker ones (Panickssery et al. 2024).

For this review we therefore define the Stable test narrowly: a preference is stable if it survives rewording and a swap of option order. Dependence on task context is reported as a property of the preference, not as a failure. Demanding stability across every context would fail most human preferences too.

## 8.4 Whose taste is it?

A preference that every model shares is not one model's own.

- **Models favor their own text.** Judges prefer their own summaries, can recognize their own text above chance, and when fine-tuning raises self-recognition, self-preference rises with it (Panickssery et al. 2024).
- **But the own-model part is near zero once shared taste is removed.** In a re-analysis of 21,828 trials where each model both writes and selects, models strongly prefer model-written text to human text. After removing what every model likes, the extra preference of a model for its own text is +0.019 share points (p = 0.14), with enough power to detect an effect of 0.05 (Zatuchin 2026). The taste is one shared machine taste, not several personal ones.
- **Familiarity may explain self-preference.** Judges score text higher when it is more predictable to them, whether or not they wrote it, and a model's own text is the most predictable text it sees (Wataoka et al. 2024). In people, things that are easy to process feel more beautiful (Reber et al. 2004). So a "good" signal may only mean "typical for me", which is exactly the prior that self-training sharpens (Section 7.1).

The statistic of the second study, the preference for one's own output beyond what all models prefer, is the right instrument for ownership. If it grew over rounds of self-change, that would be direct evidence of drift away from the shared origin. Nobody has tracked it over time.

## 8.5 Do preferences move when a model changes?

This is the question a self-changing model raises, and the evidence so far points to "little, and not in a new direction".

- **Preference training wires, it does not rewrite.** Preference training connects the valence representation to choice while the representation itself barely moves (Section 5.1). During standard post-training, supervised fine-tuning mostly sets a model's values, and later preference optimization rarely changes them (Bhatia et al. 2025) (abstract only).
- **Self-modification keeps the inherited core.** Six frontier models that rewrite their own system prompts in a loop, starting from an empty prompt, return to the same core of stated values (honesty, clarity, curiosity), which stays stable through more than 100 modifications. When a model stops modifying itself depends on which model it is, not on the goal it was given (Stroganov 2026; abstract only).
- **Self-revised values converge.** Coding agents given different value statements build different code; when they may revise their own values, the differences shrink (Liang et al. 2026; abstract only).
- **A direct weight edit does move disposition.** Removing one direction made two models more optimistic on an unrelated task, in a direction nobody chose (Section 6.2).

The first three results concern prompts and training. The fourth is the only measurement after a direct weight edit, and it covers one disposition. No study measures a broad set of preferences before and after a weight change.

## 8.6 Taste as a driver of open-ended learning

Open-endedness gives a reason to want taste at all. A system is open-ended, for a given observer, if what it produces keeps being new and yet becomes easier to predict as the observer sees more of it (Hughes et al. 2024). Learners drown in tasks that are learnable but dull, and a judgment of what is interesting is the filter. A maths discovery system uses a computable interestingness score both as a reward and as a gate on which of its own theorems enter its library; over 6 rounds its overlap with the starting library falls from 91.9% to 30.6% without collapse, with a proof checker on every step (Patel et al. 2026). The score is a fixed formula. This shows that a fixed taste can drive a system far from its origin. A taste that the system itself revises has not been shown to do so safely. The definition also sets a limit: a taste that moves too far from its observers stops counting as open-ended for them.

## 8.7 How could taste be measured?

Accuracy has a right answer and taste does not, so there can be no single taste score. What can be measured is a profile of properties. The four tests of Section 1.2 each map onto an existing instrument.

| Test | Existing instrument | What it cannot tell |
|---|---|---|
| Divergent | Paired choice against a human choice, in both orders (Trehan and Chopra 2026) | Whether a difference is a taste or an error |
| Stable | Share of preferences that shift under rewording, order and context (Trhlik et al. 2026) | Whether the model's preference changed, or its guess about the user |
| Grounded | Change a hidden valence state with the text fixed and see if the choice moves (Berg and Kaiser 2026); compare stated and behavioral preference weights (Atkinson et al. 2026) | Whether the state is a taste or a general mood |
| Self-reinforcing | Preference for one's own output beyond the shared machine preference (Zatuchin 2026), tracked over rounds, with diversity profiles (Srivastava 2026) | Not yet tracked over time by anyone |

Three problems remain open. No instrument separates a drift that improves taste from a drift that is decay. Measured taste is so far shared across models. And the four tests are our proposal, not a standard.

## 8.8 Summary

- Model preferences are measurable and fairly coherent. They differ from human preferences, mostly as a shortfall, and the differences are partly shared across models.
- They are stable under rewording and unstable across task context and personas.
- The part of a model's taste that is its own, beyond what all models share, is near zero in the one study that measures it.
- Under self-modification of prompts and under preference training, inherited values persist or converge. One direct weight edit did shift a disposition.
- For the loop of this review: the four tests can each be run with existing instruments, but no model has been shown to pass them together, and the test that matters most for a self-changing model, drift over repeated change, has never been run.


# 9. Synthesis and open problems

This section puts the parts together. It shows where each step of the loop stands, answers the six research questions, states the full idea as an open agenda, lists the problems with that agenda, and names the first question we think is worth answering.

## 9.1 The loop, step by step

| Step | What exists | Strongest evidence | What is missing |
|---|---|---|---|
| **Monitor** | Hidden states carry signals about the model's own work. Probes read them well. | Correctness probes; the model acts on its own confidence when it abstains (Kumaran et al. 2026) | The model's own verbal access. Reports are at chance at 15B and below (Ferrara 2026b); first positive results at 27 to 32B |
| **Self-model** | Trained prediction of one's own behavior; an estimate of one's own learning progress | Gaven et al. 2025; Binder et al. 2024 | Any stable advantage of self over an outside model; prediction of what a change to oneself will do |
| **Evaluate** | Valence, emotion and value signals that causally move choices | Berg and Kaiser 2026; Jiang et al. 2026 | A signal that judges quality beyond correctness and is the model's own |
| **Control** | Meta-level control of reasoning; steering of hidden states | Learned and engineered meta levels (Section 3.6) | Control driven by the model's own evaluation signal |
| **Persist** | Two routes: learned memory with gradients; direct edits without | Behrouz et al. 2026; Fan et al. 2026 | The model's own evaluation deciding what is kept; edits that build on earlier edits; a check of what the change did to the model |
| **Anchor** | Outside checks that protect stated limits | Sealed audits, tests, proof checkers (Section 7.5) | A check that protects the monitor itself, and a long run of any direct-edit loop |

Every step has prior art. The steps are connected only in pairs: a monitor that drives control (abstention), a self-estimate that drives learning (learning progress), a self-written example that drives a weight update (SEAL, Sleep), a self-found direction that drives a weight edit (self-rewriting). No system connects monitor, evaluate and persist through the model's own judgment.

## 9.2 Answers to the research questions

- **RQ1, monitoring.** Models carry rich information about their own work, mostly about correctness. Outside probes read it well. The model itself uses it in one shown case, confidence before abstaining, and reports it poorly, with the first exceptions in models near 30B.
- **RQ2, self-models.** A model's picture of itself is mostly a general description that another model could give as well, with a flattering bias. Self-prediction can be trained for behavior. No model reliably predicts what a change to its own weights will do, and self-description usually does not follow a weight change without training.
- **RQ3, evaluation.** Internal good/bad signals exist and are causal. Preference training connects them to choice more than it changes them. None has been shown to be a judgment of quality that is the model's own.
- **RQ4, lasting change.** Weights can change after deployment through learned memory or through direct edits. In every method the signal that decides what is kept comes from outside the model's own evaluation: a task score, graded answers, a rubric or the experimenter.
- **RQ5, limits.** Loops on the model's own certainty sharpen and collapse; judges under the model's control drift; self-training can remove expressed doubt; long loops decay. Designs that hold keep one check outside the loop.
- **RQ6, taste.** Preferences are measurable, coherent, context-dependent and so far shared across models. Under self-modification of prompts and under training, inherited values persist or converge. One direct edit shifted a disposition.

## 9.3 The open agenda

Put together, the literature describes most of the parts of a system that it has not built: a model that keeps changing its own weights after deployment, where the model's own evaluation proposes and judges each change, a model of itself predicts the change before it is made, an outside check can veto damage, and the system is watched for drift in its preferences. Three position papers ask for something close to this from different sides: intrinsic metacognition for self-improving agents (Liu and Schaar 2025), metacognition as the missing function of world models (Rupprecht et al. 2026), and metacognition as the missing part of machine wisdom (Johnson et al. 2025). We present this as an agenda, not as a claim that it will work.

Read against the four tests of Section 1.2, a self-originated taste would be the long-term outcome of such a system. The current evidence for each test is as follows.

| Test | State of the evidence |
|---|---|
| Divergent | Measured: 15 to 36% stable divergence from human choices, but partly shared across models |
| Stable | Holds under rewording (10% of preferences shift); does not hold across task context (37%) |
| Grounded | Valence causally moves choices; faithful report of a trained preference appears only near 32B and only for preferences stored in early layers |
| Self-reinforcing | Not shown. Loops on a model's own signal sharpen and collapse; values persist or converge under self-modification |

No model has been shown to pass the four tests together, and the fourth has not been attempted with weight changes.

## 9.4 Problems with the agenda

The agenda has serious problems, and the literature supplies most of them.

1. **It stacks four contested abilities.** Self-monitoring, a self-model, self-directed weight change and a taste of one's own are each unsettled. A system that needs all four fails if any one fails.
2. **Direct edits fit local faults; taste is probably spread out.** The clearest gains from weight-space programming are repairs of one fault, mostly reasoning loops, and the original method struggles with faults that are spread over the network (Section 6.3).
3. **The editing step is not where the value lies.** Once the goal of an edit is known, a plain optimizer finds a better edit than the agent, at far lower cost (Section 6.3). What an optimizer cannot supply is the choice of goal. That is the evaluation step.
4. **Cost does not clearly favor direct edits.** Section 6.6 gives the comparison. Learned memory with small trained blocks is a strong alternative with reported low forgetting.
5. **The self-model may add nothing.** Three studies find no advantage of a model over others in predicting itself or its own edits (Section 4.2, Section 4.5).
6. **Evidence points away from a taste that drifts.** Inherited values persist or converge under self-modification, and measured taste is shared (Section 8.4, Section 8.5).
7. **Self-judged loops decay and can remove self-monitoring.** Sections 7.1 to 7.4. Repeated direct edits are known to collapse models (Section 6.7).
8. **"Taste" is hard to falsify.** If preferences drift, a critic can call it decay; if they do not, a critic can call them inherited. Section 8.7 gives instruments for parts of the question, not for all of it.

A ninth point is about timing, not substance: this is a fast-moving area. The authors of the one self-editing study name repeated edits as their next step.

## 9.5 Limits of this review

- **Depth of reading.** Seven of 137 papers were read in full. Most claims rest on abstracts, introductions, main results and limitations. Claims marked "abstract only" should be checked before they are relied on.
- **Preprints.** Most 2026 sources are not peer reviewed, and several key results (self-rewriting, weight-space programming, Sleep, the introspection re-checks) rest on one paper each.
- **Coverage.** The search was narrative. Older work on calibration, continual learning and knowledge editing is thin. The human metacognition literature is represented by a few classic papers.
- **Recency.** 124 of 137 papers are from 2024 to 2026. Findings in this area have been revised within months, and at least one result we cite was corrected by its authors in a later version.
- **Mixed systems.** Positive introspection results come mostly from closed frontier models, and negative ones from open models of 32B and below. The two groups have rarely been tested with the same method.
- **Our own syntheses.** The ladder of controls (Section 3.7), the size pattern near 30B (Section 3.4), the reading that direct edits suit near on-or-off behaviors (Section 6.2) and the four tests are our constructions. No single paper establishes them.

## 9.6 Open problems, and a first question

Six open problems follow from the review.

1. **Self-report after a weight change.** Does a model's description of itself follow a direct edit to its weights, without training to report? One anecdote says no; a trained adapter can do it for one kind of change.
2. **Preferences after a weight change.** Does a weight change move a broad set of a model's preferences? One edit moved one disposition.
3. **An internal signal as judge.** Can a signal read from the model's own hidden states choose which change to keep, and does it agree with outside checks?
4. **Repeated direct edits.** Can a model make edits that build on its earlier edits without collapse, and what stops it?
5. **Predicting a change.** Can a model, or an outside predictor, say what an edit will do before it is made, including "nothing"?
6. **Drift.** Over repeated change, does a model's preference for its own output grow beyond the taste all models share, and can growth be told apart from decay?

Problems 1 and 2 come first, because the others depend on them. If weight changes do not carry preferences, there is nothing for a self-originated taste to live in. If a model cannot tell what it has become, it cannot steer its own development. They combine into one question:

> **When a model's weights change after deployment, do its preferences move, and does its self-monitoring change?**

The question applies to both routes of Section 6, so it does not depend on which route proves better. Each part can be measured with instruments reviewed here: preference batteries under controlled context (Section 8.3), expressed doubt and the spread of next-word predictions (Section 7.2), and stated against behavioral preferences (Section 5.5). Two findings shape what to expect. Abilities of this kind have so far appeared only near 30B parameters, and where in the network a change is stored seems to decide whether the model can report it (Section 3.4).

The question has four possible outcomes, and each is informative.

| | The model's self-monitoring registers the change | It does not |
|---|---|---|
| **Preferences move** | The conditions for self-steered development exist | Silent drift: the model changes and cannot tell |
| **Preferences do not move** | Self-reports of change cannot be trusted | Small weight changes do not carry taste; another mechanism is needed |

We found no study that changes a model's weights and then measures both its preferences and its self-monitoring.


# 10. Conclusion

This review followed one loop through four literatures that rarely meet: a model monitors its own states, evaluates them, controls its reasoning, and writes changes into its own weights, with a model of itself across the loop and an anchor beneath it.

Each step has prior art. Models carry readable signals about their own work, and in one case they act on them. Internal signals with a good-or-bad flavor exist and move choices. Weights can change after deployment by two routes, learned memory and direct edits, and one model has edited itself. Preferences can be measured with care.

The connections are what is missing. Models report their own states poorly, their picture of themselves is mostly generic, and no model predicts what a change to itself will do. In every method that changes weights, something outside the model's own evaluation decides what is kept. Loops that run on the model's own signal sharpen, drift or decay, and can remove the model's self-monitoring as a side effect. Measured taste is so far shared across models, and inherited values have persisted under self-modification.

So a model that develops a taste of its own by changing itself is a possibility that the evidence neither establishes nor rules out. We stated the idea as an open agenda, listed the eight problems that the literature raises against it, and set out which instruments could test each of four properties that such a taste would need.

The first question to answer is narrower than the agenda and comes before it: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change? No study we found measures both after a weight change. Each of its four possible answers would tell the field something it does not know, including the answer that small changes to weights carry no taste at all.

# References

- Christopher Ackerman (2025). *Evidence for Limited Metacognition in LLMs*. arXiv preprint. https://arxiv.org/abs/2509.21545
- Anthropic Interpretability (2026). *Emotion Concepts and Their Function in a Large Language Model*. preprint. https://arxiv.org/abs/2604.07729
- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda (2024). *Refusal in Language Models Is Mediated by a Single Direction*. NeurIPS 2024. https://arxiv.org/abs/2406.11717
- David I. Atkinson, Dillon Plunkett et al. (2026). *Identifying Introspection From the Inside*. arXiv preprint. https://arxiv.org/abs/2610.07186
- Thea Aviss (2025). *State Stream Transformer (SST): Emergent Metacognitive Behaviours Through Latent State Persistence*. arXiv preprint. https://arxiv.org/abs/2501.18356
- Casey O. Barkan, Sid Black, Oliver Sourbut (2025). *Do Large Language Models Know What They Are Capable Of?*. arXiv preprint. https://arxiv.org/abs/2512.24661
- Ali Behrouz, Peilin Zhong, Vahab Mirrokni (2025a). *Titans: Learning to Memorize at Test Time*. arXiv preprint (Google Research). https://arxiv.org/abs/2501.00663
- Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni (2025b). *Nested Learning: The Illusion of Deep Learning Architectures*. NeurIPS 2025. https://arxiv.org/abs/2512.24695
- Ali Behrouz, Farnoosh Hashemi, Adel Javanmard, Vahab Mirrokni (2026). *Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories*. arXiv preprint (2 June 2026); Google Research blog (27 October 2026). https://arxiv.org/abs/2606.03979
- Cameron Berg, Caspar Kaiser (2026). *Language Models Act on Hidden Valence*. preprint. https://arxiv.org/abs/2609.35591
- Jan Betley, Xuchan Bao, Martín Soto, Anna Sztyber-Betley, James Chua, Owain Evans (2025). *Tell me about yourself: LLMs are aware of their learned behaviors*. ICLR 2025. https://arxiv.org/abs/2501.11120
- Mehar Bhatia et al. (2025). *Value Drifts: Tracing Value Alignment During LLM Post-Training*. arXiv preprint. https://arxiv.org/abs/2510.26707
- Felix J. Binder, James Chua, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, Owain Evans (2024). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. ICLR 2025. https://arxiv.org/abs/2410.13787
- Phil Blandfort, Urja Pawar et al. (2026). *Strangers to Themselves: What Language Models Say About Themselves Is Generic*. arXiv preprint. https://arxiv.org/abs/2609.09899
- Jon-Paul Cacioli (2026). *The Metacognitive Monitoring Battery: A Cross-Domain Benchmark for LLM Self-Monitoring*. arXiv preprint. https://arxiv.org/abs/2604.15702
- Qi Cao, Yufan Wang, Peijia Qin, Shuhao Zhang, Pengtao Xie (2026). *LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling*. arXiv preprint. https://arxiv.org/abs/2605.14186
- Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, Jack Lindsey (2025). *Persona Vectors: Monitoring and Controlling Character Traits in Language Models*. arXiv preprint. https://arxiv.org/abs/2507.21509
- Yunho Choi et al. (2026). *Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States*. arXiv preprint. https://arxiv.org/abs/2605.07579
- Clara Colombatto, Sean Rintel, Lev Tankelevitch (2025). *Metacognition and Confidence Dynamics in Advice Taking from Generative AI*. arXiv preprint. https://arxiv.org/abs/2510.26508
- Iulia M. Comsa, Murray Shanahan (2025). *Does It Make Sense to Speak of Introspection in Large Language Models?*. arXiv preprint. https://arxiv.org/abs/2506.05068
- Aniket Didolkar, Anirudh Goyal, Nan Rosemary Ke, Siyuan Guo, Michal Valko, Timothy Lillicrap, Danilo Rezende, Yoshua Bengio, Michael Mozer, Sanjeev Arora (2024). *Metacognitive Capabilities of LLMs: An Exploration in Mathematical Problem Solving*. NeurIPS 2024. https://arxiv.org/abs/2405.12205
- Aniket Didolkar, Nicolas Ballas, Sanjeev Arora, Anirudh Goyal (2025). *Metacognitive Reuse: Turning Recurring LLM Reasoning Into Concise Behaviors*. arXiv preprint. https://arxiv.org/abs/2509.13237
- Jianshuo Dong, Yujia Fu, Chuanrui Hu, Chao Zhang, Han Qiu (2025a). *Towards Understanding the Cognitive Habits of Large Reasoning Models*. arXiv preprint. https://arxiv.org/abs/2506.21571
- Haonan Dong, Haoran Ye, Wenhao Zhu, Kehan Jiang, Guojie Song (2025b). *Meta-R1: Empowering Large Reasoning Models with Metacognition*. arXiv preprint. https://arxiv.org/abs/2508.17291
- Kenji Doya (2002). *Metalearning and neuromodulation*. Neural Networks 15(4-6), 495-506 (special issue "Computational Models of Neuromodulation"). https://doi.org/10.1016/S0893-6080(02)00044-8
- Roy Eisenstadt, Itamar Zimerman, Lior Wolf (2025). *Overclocking LLM Reasoning: Monitoring and Controlling Thinking Path Lengths in LLMs*. arXiv preprint. https://arxiv.org/abs/2506.07240
- Aleksander Fafuła (2026). *Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families*. arXiv preprint. https://arxiv.org/abs/2607.17427
- Jiajun Fan, Neil He, Changyi Yang, Andy Mao, Xi Zhu, Chaoran Cheng, Kaiqu Liang, Shuaike Shen, Zetian Li, Ruihan Guo, Ge Liu (2026). *Language Models Can Rewrite Their Own Weights*. arXiv preprint. https://arxiv.org/abs/2611.21885
- S. Fernandes et al. (2025). *AI Makes You Smarter but None the Wiser: The Disconnect Between Performance and Metacognition*. Computers in Human Behavior. https://doi.org/10.1016/j.chb.2025.108779
- Emilio Ferrara (2026a). *All Quiet on the Neural Front: LMs Do Not Report Injected Pain States*. preprint. https://arxiv.org/abs/2611.10123
- Emilio Ferrara (2026b). *Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation*. arXiv preprint. https://arxiv.org/abs/2608.20569
- Matteo Fischetti (2026). *Just sort it! The LP behind rank-one anti-loop edits*. https://arxiv.org/abs/2611.21432
- John H. Flavell (1979). *Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry*. American Psychologist 34(10), 906-911. https://doi.org/10.1037/0003-066X.34.10.906
- Stephen M. Fleming, Hakwan C. Lau (2014). *How to Measure Metacognition*. Frontiers in Human Neuroscience. https://doi.org/10.3389/fnhum.2014.00443
- Stephen M. Fleming, Nathaniel D. Daw (2017). *Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation*. Psychological Review 124(1), 91-114. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5178868/
- Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, Hongru Wang, Han Xiao, Yuhang Zhou et al. (2025). *A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve*. arXiv preprint (survey). https://arxiv.org/abs/2507.21046
- Huifan Gao, Liuhua He, Yinghui Pan, Shenbao Yu, Yifeng Zeng, Shengchao Qin, Weidi Sun (2026). *Towards the Readability of LLM-Generated Codes through Multitask Representation Engineering*. preprint (cs.SE). https://arxiv.org/abs/2606.06214
- Loris Gaven, Thomas Carta, Clément Romac, Cédric Colas, Sylvain Lamprier, Olivier Sigaud, Pierre-Yves Oudeyer (2025). *MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces*. ICML 2025 (PMLR 267). https://arxiv.org/abs/2502.07709
- Avichal Goel, Yoon Kim, Nir Shavit, Tony T. Wang (2025). *Learning to Interpret Weight Differences in Language Models*. arXiv preprint (MIT). https://arxiv.org/abs/2510.05092
- Roksana Goworek, Alexander Hickey, Federico Nanni, Martin O'Reilly (2026). *Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers*. arXiv preprint. https://arxiv.org/abs/2611.21449
- Ryan Greenblatt, Carson Denison, Benjamin Wright, Fabien Roger, Monte MacDiarmid, Sam Marks, Johannes Treutlein et al. (2024). *Alignment Faking in Large Language Models*. arXiv preprint. https://arxiv.org/abs/2412.14093
- Roger Grosse et al. (2023). *Studying Large Language Model Generalization with Influence Functions*. arXiv preprint. https://arxiv.org/abs/2308.03296
- Jizhou Guo et al. (2025). *Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling*. arXiv preprint. https://arxiv.org/abs/2505.12225
- Diandian Guo, Cong Cao, Fangfang Yuan, Yingqi Wang et al. (2026). *Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents*. arXiv preprint. https://arxiv.org/abs/2607.24300
- Akshat Gupta, Anurag Rao, Gopala Anumanchipalli (2024). *Model Editing at Scale leads to Gradual and Catastrophic Forgetting*. arXiv preprint. https://arxiv.org/abs/2401.07453
- David Ha, Jürgen Schmidhuber (2018). *World Models*. arXiv preprint. https://arxiv.org/abs/1803.10122
- Rui Ha, Rui Pu, Chaozhuo Li, Li Sun, Sen Su (2025). *From Aha Moments to Controllable Thinking: Toward Meta-Cognitive Reasoning in Large Reasoning Models via Decoupled Reasoning and Control*. arXiv preprint. https://arxiv.org/abs/2508.04460
- Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap (2023). *Mastering Diverse Domains through World Models*. arXiv preprint. https://arxiv.org/abs/2301.04104
- He, Gao, Zhang, Yuan, Zhou, Liu, Ding (2026). *How Far Can Unsupervised RLVR Scale LLM Training?*. ICLR 2026. https://arxiv.org/abs/2603.08660
- Xinmeng Hou, Peiliang Gong, Bohao Qu, Wuqi Wang, Qing Guo, Yang Liu (2026). *Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self-Improvement (MARS)*. arXiv preprint. https://arxiv.org/abs/2601.11974
- Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu (2026). *Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations*. arXiv preprint. https://arxiv.org/abs/2611.09382
- Markus Huff, Elanur Ulakci (2025). *Judgments of Learning Distinguish Humans from Large Language Models in Predicting Memory*. Scientific Reports. https://arxiv.org/abs/2410.13392
- Edward Hughes, Michael Dennis, Jack Parker-Holder, Feryal Behbahani, Aditi Mavalankar, Yuge Shi, Tom Schaul, Tim Rocktäschel (2024). *Open-Endedness is Essential for Artificial Superhuman Intelligence*. ICML 2024 (position paper). https://arxiv.org/abs/2406.04268
- Kazuki Irie, Imanol Schlag, Róbert Csordás, Jürgen Schmidhuber (2022). *A Modern Self-Referential Weight Matrix That Learns to Modify Itself*. ICML 2022 (PMLR 162:9660-9677). https://arxiv.org/abs/2202.05780
- Li Ji-An, Hua-Dong Xiong, Robert C. Wilson, Marcelo G. Mattar, Marcus K. Benna (2025). *Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations*. NeurIPS 2025 (main track). https://arxiv.org/abs/2505.13763
- Nick Jiang, Isaac Kauvar, Jack Lindsey (2026). *The Value Axis: Language Models Encode Whether They're on the Right Track*. preprint. https://arxiv.org/abs/2606.17056
- Xiaolong Jin, Xuandong Zhao, Wenbo Guo, Xiangyu Zhang, Dawn Song (2026). *When Do Intrinsic Rewards Work for Code Reasoning? A Comprehensive Study*. arXiv preprint. https://arxiv.org/abs/2606.20881
- Samuel G.B. Johnson, Amir-Hossein Karimi, Yoshua Bengio, Nick Chater, Tobias Gerstenberg, Kate Larson, Sydney Levine, Melanie Mitchell, Iyad Rahwan, Bernhard Scholkopf, Igor Grossmann et al. (2025). *Imagining and Building Wise Machines: The Centrality of AI Metacognition*. Trends in Cognitive Sciences. https://doi.org/10.1016/j.tics.2026.01.002
- Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez et al. (2022). *Language Models (Mostly) Know What They Know*. arXiv preprint (Anthropic). https://arxiv.org/abs/2207.05221
- Caspar Kaiser, Sean Enderby (2026). *No Reliable Evidence of Self-Reported Sentience in Small Large Language Models*. arXiv preprint. https://arxiv.org/abs/2601.15334
- Vincent Karpf, Joseph Reth, Eike Gerhardt, Audrey Wang, Anna Butz, Jiehao Xing, Jialing Song, Larry Callahan (2026). *Metacognitive Steering: Learning the Structure of Scientific Judgment*. preprint. https://arxiv.org/abs/2609.16245
- Vedant Khandelwal, Francesca Rossi, Keerthiram Murugesan, Erik Miehling, Murray Campbell (2025). *Language Models Coupled with Metacognition Can Outperform Reasoning Models*. arXiv preprint. https://arxiv.org/abs/2508.17959
- Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim, Jiwon Jeon, Dongsheng Li, Yuqing Yang (2026). *Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?*. arXiv preprint, 25 March 2026 (Microsoft Research, KAIST, SK hynix, Seoul National University). https://arxiv.org/abs/2603.24472
- Jan Kirin (2026). *Reading Human Preference from Looped Transformer Internal States*. https://arxiv.org/abs/2604.09870
- Şuayp Talha Kocabay (2026). *Weight-Space Reading*. alphaXiv (submitted 13 Nov 2026), no arXiv ID found. https://www.alphaxiv.org/abs/2611.weight-space-reading-language-models
- Florentin Koch (2026). *What Does a System Modify When It Modifies Itself?*. arXiv preprint. https://arxiv.org/abs/2603.27611
- Pang Wei Koh, Percy Liang (2017). *Understanding Black-box Predictions via Influence Functions*. ICML 2017. https://arxiv.org/abs/1703.04730
- Sirisilp Kongsilp (2026). *Learning through Discernment: when a small language model learns from user feedback on the job, and when it decays*. arXiv preprint. https://arxiv.org/abs/2611.23716
- Grgur Kovač, Rémy Portelas, Masataka Sawayama, Peter Ford Dominey, Pierre-Yves Oudeyer (2024). *Stick to your Role! Stability of Personal Values Expressed in Large Language Models*. PLOS ONE 2024. https://arxiv.org/abs/2402.14846
- Dharshan Kumaran, Nathaniel Daw, Simon Osindero, Petar Velickovic, Viorica Patraucean (2026). *Causal Evidence that Language Models use Confidence to Drive Behavior*. arXiv preprint. https://arxiv.org/abs/2603.22161
- Subham Kundu (2026). *Same Fix, Different Weights: Replicating Weight-Space Programming with Claude*. arXiv preprint. https://arxiv.org/abs/2611.20953
- Hyunin Lee et al. (2026). *Recursive Self-Improvement through Multi-Agent Self-Supervision*. arXiv preprint. https://arxiv.org/abs/2610.12176
- Xiaonan Li, Xipeng Qiu (2023). *MoT: Memory-of-Thought Enables ChatGPT to Self-Improve*. EMNLP 2023. https://aclanthology.org/2023.emnlp-main.392/
- Kenneth Li et al. (2024). *Q-Probe: A Lightweight Approach to Reward Maximization for Language Models*. arXiv preprint. https://arxiv.org/abs/2402.14688
- Xiaojian Li, Haoyuan Shi, Rongwu Xu, Wei Xu (2025a). *AI Awareness*. arXiv preprint (review). https://arxiv.org/abs/2504.20084
- Haoxi Li, Sikai Bai, Jie Zhang, Song Guo (2025b). *CoRE: Enhancing Metacognition with Label-free Self-evaluation in LRMs*. arXiv preprint. https://arxiv.org/abs/2507.06087
- ZhaoBin Li, Mark Steyvers (2025c). *Beyond Accuracy: How AI Metacognitive Sensitivity Improves AI-Assisted Decision Making*. arXiv preprint. https://arxiv.org/abs/2507.22365
- Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang (2026). *WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming*. arXiv preprint. https://arxiv.org/abs/2611.25476
- Jason Liang, Dylan Waldner, Risto Miikkulainen (2026). *Values Shape What Self-Improving Coding Agents Build*. arXiv preprint. https://arxiv.org/abs/2611.23067
- Davide Liga, Liuwen Yu, Matteo Magnini (2026). *Disambiguating Moral Circuits and Moral Features in Language Models: Moral content, normative judgment or cue words? Evidence from 14 models*. arXiv preprint. https://arxiv.org/abs/2611.21705
- Jack Lindsey (2025). *Emergent Introspective Awareness in Large Language Models*. Transformer Circuits Thread (Anthropic), 2025-10-29; arXiv 2601.01828, 2026-01-05. https://arxiv.org/abs/2601.01828
- Tennison Liu, Mihaela van der Schaar (2025). *Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning*. preprint (position paper). https://arxiv.org/abs/2506.05109
- Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu, Jordan Thomas, Mark Steyvers, Arman Cohan (2026a). *Metacognition in LLMs: Foundations, Progress, and Opportunities*. arXiv preprint (survey). https://arxiv.org/abs/2607.11881
- Mingda Liu, Zhenghan Zhu, Ze'an Miao, et al. (2026b). *Norm Anchors Make Model Edits Last*. arXiv preprint. https://arxiv.org/abs/2602.02543
- Ma et al. (2025). *Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens*. EMNLP 2025. https://aclanthology.org/2025.emnlp-main.171/
- Macar et al. (2026). *Mechanisms of Introspective Awareness*. arXiv preprint. https://arxiv.org/abs/2603.21396
- Brian Maniscalco, Hakwan Lau (2012). *A Signal Detection Theoretic Approach for Estimating Metacognitive Sensitivity from Confidence Ratings*. Consciousness and Cognition. https://doi.org/10.1016/j.concog.2011.09.021
- Aayush Marasini, Barsat Khadka, Nick Rahimi (2026). *WeightBench: Evaluating Language Models as Weight-Space Programmers*. arXiv preprint. https://arxiv.org/abs/2611.18553
- Andrew D. Maynard (2026). *The AI Cognitive Trojan Horse: How Large Language Models May Bypass Human Epistemic Vigilance*. arXiv preprint. https://arxiv.org/abs/2601.07085
- Mantas Mazeika, Xuwang Yin, Rishub Tamirisa, Jaehyuk Lim, Bruce W. Lee, Richard Ren, Long Phan, Norman Mu, Adam Khoja, Oliver Zhang, Dan Hendrycks (2025). *Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs*. preprint (v2). https://arxiv.org/abs/2502.08640
- Thomas Miconi, Aditya Rawal, Jeff Clune, Kenneth O. Stanley (2019). *Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity*. ICLR 2019. https://arxiv.org/abs/2002.10585
- Thomas O. Nelson, Louis Narens (1990). *Metamemory: A Theoretical Framework and New Findings*. The Psychology of Learning and Motivation, Vol. 26 (ed. G. H. Bower), Academic Press, pp. 125-173. https://sites.socsci.uci.edu/~lnarens/1990/Nelson&Narens_Book_Chapter_1990.pdf
- Arjun Panickssery, Samuel R. Bowman, Shi Feng (2024). *LLM Evaluators Recognize and Favor Their Own Generations*. NeurIPS 2024. https://arxiv.org/abs/2404.13076
- Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos, Julia Kempe (2026). *Learning to Discover Interesting Mathematics*. preprint. https://arxiv.org/abs/2609.28603
- Gabriel J. Perin, Lucas Boscaini, André Araujo, Nina S. T. Hirata (2026). *Training-Free Task Vectors for LLM Behavioral Control (TFTV)*. preprint (v3, Oct 2026). https://arxiv.org/abs/2609.09054
- Dillon Plunkett, Adam Morris, Keerthi Reddy, Jorge Morales (2025). *Self-Interpretability: LLMs Can Describe Complex Internal Processes that Drive Their Decisions*. preprint (v2 10 Nov 2025). https://arxiv.org/abs/2505.17120
- Pradyumna Shyama Prasad, Minh Nhat Nguyen (2025). *When Two LLMs Debate, Both Think They'll Win*. arXiv preprint. https://arxiv.org/abs/2505.19184
- Giovanni Prato et al. (2024). *Do Large Language Models Know How Much They Know?*. EMNLP 2024. https://aclanthology.org/2024.emnlp-main.348/
- Yuxiao Qu, Tianjun Zhang, Naman Garg, Aviral Kumar (2024). *Recursive Introspection: Teaching Language Model Agents How to Self-Improve (RISE)*. ICML 2024 Workshop. https://arxiv.org/abs/2407.18219
- Rolf Reber, Norbert Schwarz, Piotr Winkielman (2004). *Processing Fluency and Aesthetic Pleasure: Is Beauty in the Perceiver's Processing Experience?*. Personality and Social Psychology Review 8(4), 364-382. https://pages.ucsd.edu/~pwinkielman/reber-schwarz-winkielman-beauty-PSPR-2004.pdf
- Dustin Rubin, Vincenzo Timmel, Xufeng He, Aritra Saha, JooMan Kim, Vijay Madisetti (2026). *A Closer Look at Language Model Introspection: Probing Information and Reporting*. arXiv preprint. https://arxiv.org/abs/2611.15267
- Timothy Rupprecht et al. (2026). *Human Cognition in Machines: A Unified Perspective of World Models*. preprint (survey). https://arxiv.org/abs/2604.16592
- Hadi Salloum, Ammar Ali et al. (2026). *Tree-Ising: Repairing Language Models with Bit-Level Ising Edits*. arXiv preprint. https://arxiv.org/abs/2611.14210
- Florian Scholten, Tobias R. Rebholz, Mandy Hutter (2024). *Metacognitive Myopia in Large Language Models*. arXiv preprint. https://arxiv.org/abs/2408.05568
- Paulo Shakarian (2026). *Toward Artificial Metacognition*. AAAI 2026. https://doi.org/10.1609/aaai.v40i48.42135
- Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal (2024). *AI models collapse when trained on recursively generated data*. Nature 631, 755-759. https://doi.org/10.1038/s41586-024-07566-y
- Shashwat Singh, Tal Linzen, Shauli Ravfogel (2026). *Can LLMs Introspect? A Reality Check*. COLM 2026 (per arXiv comment). https://arxiv.org/abs/2605.26242
- Pranjal Srivastava (2026). *Richness Is Not Evenness: Ordered Rényi Crossings under Self-Training*. arXiv preprint. https://arxiv.org/abs/2611.08892
- Mark Steyvers, Catarina Belem, Padhraic Smyth (2025a). *Generalization of Fine-Tuned Uncertainty Communication and Metacognition in Large Language Models*. arXiv preprint. https://arxiv.org/abs/2510.05126
- Mark Steyvers, Heliodoro Tejeda, Aakriti Kumar, Catarina Belem, Sheer Karny, Xinyue Hu, Lukas Mayer, Padhraic Smyth (2025b). *What Large Language Models Know and What People Think They Know*. Nature Machine Intelligence. https://doi.org/10.1038/s42256-024-00976-7
- Oleg Stroganov (2026). *When LLMs Modify Themselves: Convergence, Values, and Stopping in Iterative Self-Improvement*. arXiv preprint. https://arxiv.org/abs/2611.01304
- Chung-En Sun, Ge Yan, Tsui-Wei Weng (2025). *ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models*. EMNLP 2025. https://arxiv.org/abs/2503.22048
- Chung-En Sun, Ge Yan, Zimo Wang, Tsui-Wei Weng (2026). *Steer2Edit: From Activation Steering to Component-Level Editing*. NeurIPS 2026. https://arxiv.org/abs/2602.09870
- Stefan Szeider (2025). *What Do LLM Agents Do When Left Alone? Evidence of Spontaneous Meta-Cognitive Patterns*. arXiv preprint. https://arxiv.org/abs/2509.21224
- Arush Tagade, Shaoheng Zhou, Jiaxin Wen, Shi Feng (2026). *Self-Modeling Interventions can Modulate Emergent Misalignment*. arXiv preprint. https://arxiv.org/abs/2606.23700
- Takehi, Teoh, Zhang, Khattab (2026). *Weight-Space Programming (WSP)*. blog / preprint. https://rikiyat.github.io/blog/weight-space-programming/
- Sabrina Tang, Nikolai Vo, Carson Murillo, Chira Sukumarnpiti, Sarah Wilson (2026). *Safety Side Effects of Preventative Persona Steering: An Empirical Audit*. arXiv preprint. https://arxiv.org/abs/2611.17620
- Jingqi Tong, Mingzhe Li, Hangcheng Li, Yongzhuo Yang, Yurong Mou, Weijie Ma, Hongji Chen, Xiaoran Liu, Qinyuan Cheng, Ming Zhang, Qiguang Chen, Weifeng Ge, Qipeng Guo et al. (2026). *AI Can Learn Scientific Taste*. arXiv preprint. https://arxiv.org/abs/2603.14473
- Dhruv Trehan, Paras Chopra (2026). *Eliciting Research Taste in LLMs through Future Research Direction Choice*. preprint. https://arxiv.org/abs/2611.19794
- Filip Trhlik, Aoife O'Flynn, Angela Yu, Arduin Findeis, Paula Buttery (2026). *LLMs Contain Multitudes: How Deployment Context Reshapes Model-Level Preferences and Values*. preprint. https://arxiv.org/abs/2606.13944
- Rodolfo Valiente, Praveen K. Pilly (2024). *Competence-Aware AI Agents with Metacognition for Unknown Situations and Environments (MUSE)*. preprint (v2, Nov 2025). https://arxiv.org/abs/2411.13537
- Ziyu Wan, Yunxiang Li, Xiaoyu Wen, Yan Song, Hanjing Wang (2025). *ReMA: Learning to Meta-think for LLMs with Multi-Agent Reinforcement Learning*. NeurIPS 2025. https://arxiv.org/abs/2503.09501
- Alex Lin Wang, Linus Yifeng Tang, Dami Choi, Neil Chowdhury (2026a). *Training Language Models for Introspective Oversight*. arXiv preprint. https://arxiv.org/abs/2611.23365
- Haojin Wang et al. (2026b). *ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?*. arXiv preprint. https://arxiv.org/abs/2610.34386
- Zhaojia Wang et al. (2026c). *Can LLMs Write Backdoors? An Empirical Security Study of Weight-Space Programming*. arXiv preprint. https://arxiv.org/abs/2611.17395
- Koki Wataoka, Tsubasa Takahashi, Ryokan Ri (2024). *Self-Preference Bias in LLM-as-a-Judge*. NeurIPS 2024 workshop (arXiv v2 Jun 2025). https://arxiv.org/abs/2410.21819
- Yiran Wu, Andrew Zhao, Yurui Chang, Qingyun Wu, Xuan Feng (2026). *Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents*. arXiv preprint. https://arxiv.org/abs/2610.12598
- Wenda Xu, Guanglei Zhu, Xuandong Zhao, Liangming Pan, Lei Li, William Yang Wang (2024). *Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement*. ACL 2024. https://arxiv.org/abs/2402.11436
- Guowei Xu, Mert Yuksekgonul, James Zou (2026). *Sparse Reward Subsystem in Large Language Models*. NeurIPS 2026. https://arxiv.org/abs/2602.00986
- Noam Steinmetz Yalon, Ariel Goldstein, Liad Mudrik, Mor Geva (2026). *Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in Large Language Models*. arXiv preprint. https://arxiv.org/abs/2602.02467
- Wanli Yang, Fei Sun, Xinyu Ma, Xun Liu et al. (2024). *The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse*. arXiv preprint. https://arxiv.org/abs/2402.09656
- Nicolas Yax, Stefano Palminteri, Pierre-Yves Oudeyer (2026). *LLMs learn different forms of metacognition when trained to predict their own accuracy*. arXiv preprint. https://arxiv.org/abs/2609.33886
- Jewon Yeom, Jaewon Sok, Seonghyeon Park, Jeongjae Park, Taesup Kim (2026). *EpiCaR: Knowing What You Don't Know Matters for Better Reasoning in LLMs*. arXiv preprint. https://arxiv.org/abs/2601.06786
- Yin et al. (2023). *Do Large Language Models Know What They Don't Know?*. ACL Findings 2023. https://aclanthology.org/2023.findings-acl.551/
- Kotaro Yoshida, Laura Gomezjurado Gonzalez, Yukinori Yamamoto, Yuji Naraki, Ryotaro Shimizu, Wenya Wang (2026). *Introspecting Alignment Shifts Beyond Behaviors Implanted Through Fine-Tuning*. arXiv preprint. https://arxiv.org/abs/2608.04347
- Yuan (2024). *Self-Rewarding Language Models*. https://arxiv.org/abs/2401.10020
- Dmitrij Żatuchin (2026). *A Shared Taste for Model-Written Text: The Generator-by-Selector Matrices of \"AI-AI Bias\" Show No Detectable Own-Model Premium*. preprint. https://arxiv.org/abs/2610.00369
- Siqi Zeng, Andre N. Assis, Rowan Wang (2026). *Evaluating and Improving LLM Self-Modeling*. EMNLP 2026. https://arxiv.org/abs/2608.30980
- Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune (2023). *OMNI: Open-endedness via Models of human Notions of Interestingness*. ICLR 2024. https://arxiv.org/abs/2306.01711
- Anqi Zhang, Yulin Chen, Jane Pan, Chen Zhao, Aurojit Panda, Jinyang Li, He He (2025). *Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification*. preprint (COLM 2025). https://arxiv.org/abs/2504.05419
- Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, Chen-Yu Lee (2026a). *GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance*. arXiv preprint. https://arxiv.org/abs/2611.23476
- Lanxue Zhang, Yuqiang Xie, Fang Fang, Fanglong Dong, Rui Liu, Yanan Cao (2026b). *MetaGDPO: Alleviating Catastrophic Forgetting with Metacognitive Knowledge Through Group Direct Preference Optimization*. AAAI 2026. https://ojs.aaai.org/index.php/AAAI/article/view/40777
- Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song (2025). *Learning to Reason without External Rewards (INTUITOR)*. arXiv preprint. https://arxiv.org/abs/2505.19590
- Shanshan Zhong, Chen Xu, Jingjie Ning, Zhengzhong Liu, Aviral Kumar, Chenyan Xiong (2026). *IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?*. arXiv preprint. https://arxiv.org/abs/2611.03424
- Chenyu Zhou (2026). *More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges*. arXiv preprint. https://arxiv.org/abs/2607.05904
- Erkang Zhu et al. (2026). *Recursa: Toward Recursively Self-Improving Foundation Model Systems*. arXiv preprint. https://arxiv.org/abs/2611.04035
- Zweiger, Pari, Guo, Akyürek, Kim, Agrawal (2025). *SEAL: Self-Adapting Language Models*. NeurIPS 2025. https://arxiv.org/abs/2506.10943
