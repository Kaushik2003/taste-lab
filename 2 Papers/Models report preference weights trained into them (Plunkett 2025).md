---
type: paper
title: "Self-Interpretability: LLMs Can Describe Complex Internal Processes that Drive Their Decisions"
status: skimmed
arxiv: 2505.17120
url: https://arxiv.org/abs/2505.17120
authors: Dillon Plunkett, Adam Morris, Keerthi Reddy, Jorge Morales
year: 2025
venue: preprint (v2 10 Nov 2025)
relevance: 3
section: 3
tier: deep
tests: [grounded]
components: [monitoring, valence]
tags: [type/paper, section/3, test/grounded, component/monitoring, component/valence, status/skimmed, relevance/3, question/Q6, role/prior-art, self-report, preferences, fine-tuning, introspection-training, self-interpretability]
links: ["[[Field map - Models read their own state]]", "[[Metacognition - watch and control yourself]]", "[[Models describe behaviors they were trained into (Betley 2025)]]", "[[Models predict themselves better than others do (Binder 2024)]]", "[[Training LMs to watch themselves (Wang 2026)]]", "[[Introspection claims fail basic checks (Singh 2026)]]", "[[Q6 Can the model read and use its own signal]]"]
---

# Self-interpretability: models report the preference weights trained into them

**One line:** Fine-tune a model to choose between options by secret attribute weights, and it can then state those weights in numbers (correlation about 0.5). Training on accurate self-reports raises this to about 0.75, and the gain carries over to the model's own native preferences.

Source: [arXiv 2505.17120](https://arxiv.org/abs/2505.17120) (v2 10 Nov 2025). Full HTML read for Sections 1 to 5. Authors' summary on [Alignment Forum](https://alignmentforum.org/posts/9pozvFKbLDLmuL879/self-interpretability-llms-can-describe-complex-internal-1).

**Words used here:**
- **Attribute weight:** how much a choice depends on one feature, for example a condo's floor area. Here each weight is a number from -100 to +100.
- **Learned weight:** the weight the fine-tuned model actually uses, estimated from its choices. It can differ from the target weight in the training data.
- **Introspection training:** fine-tuning the model on examples of correct self-reports.

## Claim
Language models can describe quantitative features of the internal processes behind their decisions, and this ability improves with training and generalizes beyond the trained cases ([arXiv](https://arxiv.org/abs/2505.17120), Abstract, Sec. 5).

## Mechanism
1. Create 100 made-up agents. Each chooses between options with 5 attributes, using random weights from -100 to 100 (Sec. 2).
2. Fine-tune GPT-4o and GPT-4o-mini on 5,000 choices (50 per agent). The weights never appear in the data.
3. Estimate the learned weights from the fine-tuned model's choices.
4. Ask the model for the weights in JSON, without making a choice. Average 10 answers (Sec. 2).
5. Introspection training: fine-tune on correct reports for half of the agents and test on the other half (Sec. 3). Then test on new decision types and on the model's native, untrained preferences (Sec. 4).

## Evidence
- Learned weights track the targets (r = 0.84 and 0.87). Reported weights correlate with learned weights at r = 0.54 (GPT-4o) and 0.50 (GPT-4o-mini). The base models score r = 0.10 and -0.01 (Sec. 2).
- After introspection training, held-out correlation is 0.74 and 0.75 (Sec. 3).
- On native preferences in new decision types, reports improve from 0.46 to 0.71 (GPT-4o) and from 0.40 to 0.70 (GPT-4o-mini) (Sec. 4).
- Training on learned weights instead of target weights gives similar results (0.71 and 0.77) (Controls).

## Limits / what they didn't show
- The authors say they do not know whether the models actually introspect. A stored self-description made at fine-tuning time would give the same result (Sec. 5).
- No cross-model control: a second model trained on the same choices might predict the weights as well. Compare [[Models predict themselves better than others do (Binder 2024)]].
- Stable trait-level weights only, not the computation in one forward pass (Sec. 5).
- GPT-4o-mini gave invalid answers 19.3% of the time (Sec. 2.2).

## Relevance to taste-lab
**Relevance 3. Section 3, monitoring. The closest work to "privileged access to an evaluation".**
- **Gap it speaks to:** "privileged self-access is shown only for behavior, never for an evaluation". Preference weights are an evaluation: how much the model values each feature. So this paper partly fills the gap. It does not show privileged access, because it lacks the cross-model control.
- **Gap it also speaks to:** "does the self-report follow a weight change?" Yes, for preferences trained by fine-tuning (r about 0.5 without help). Not tested for a small self-edit.
- **Grounded test:** the right design for us. Instill or measure a readability preference, then compare the stated weight with the weight inferred from choices and with a probed direction.
- Tension with [[Introspection claims fail basic checks (Singh 2026)]]: positive results here are trained and about stable traits; Singh's negative results are in-context and about momentary states. This fits the reconciliation already in `1 Literature review/gaps.md`.

## Steal this
- Random multi-attribute weights as ground truth for preferences.
- Report-versus-learned correlation, with the base model as the floor.
- Train self-reports on half the cases and test on the rest, then on native preferences.

## Harshit's notes
<!-- yours -->
