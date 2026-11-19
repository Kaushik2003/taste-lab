# Gaps & patterns

Updated 2026-11-20 · 38 papers, 2 read (the rest skimmed or unread) · metacognition and weight editing first

## Gaps

| Gap | Loop stage | Test | Closest work | Why it matters |
|---|---|---|---|---|
| No model has edited its **own** weights by reading them. Every weight-space editor is a larger outside model. | persist | self-reinforcing | [[WSP - a model reads and edits weights (Takehi 2026)]], [[Exploring WSP - small weight edits, uneven results (Hu 2026)]], [[WeightBench - models cannot yet patch models (Marasini 2026)]] | "Self-modification" in the review rests on outside editors. Without self-editing, the persist step of the loop is not metacognition. |
| No weight editor knows the limits of its own edits. On impossible vs hard edits, agents score at chance. | monitor, persist | none | [[WeightBench - models cannot yet patch models (Marasini 2026)]] | This is metacognition in weight space ("can I make this change?"). It is the cleanest new gap that joins our two topics. |
| No self-edit is chosen by the model's own evaluation. SEAL's reward is task score; WSP edits are chosen by benchmark score; steering-to-weights uses an experimenter's direction. | evaluate, persist | self-reinforcing | [[SEAL - models write their own training data (Zweiger 2025)]], [[TFTV - turn a steering vector into a weight edit (Perin 2026)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]] | The "taste reaches the weights" step has no prior art. It is also the step most exposed to collapse. |
| No paper shows a model reads an internal state that is absent from its input and its behavior, under strong controls (input-only probe, cross-model control, shuffled labels). | monitor | grounded | [[Models can report and control their own activations (Ji-An 2025)]], [[Models sometimes notice injected thoughts (Lindsey 2025)]], [[Training LMs to watch themselves (Wang 2026)]] | Grounded self-report is the core metacognition claim. Today it fails strong checks ([[Introspection claims fail basic checks (Singh 2026)]]). |
| Privileged self-access is shown only for **behavior** (what the model will do), never for an **evaluation** (is this good or bad). | monitor, evaluate | grounded | [[Training LMs to watch themselves (Wang 2026)]], [[Models predict themselves better than others do (Binder 2024)]] | Taste needs the evaluate step. Predicting your own output is not judging it. |
| No probe or trained self-monitor has been checked against answer consistency or typicality, except one study that found trained confidence reads consistency off the training data. | monitor | grounded | [[Trained confidence tracks consistency, not accuracy (Yax 2026)]], [[Models know when they are right (Zhang 2025)]], [[Few neurons predict right answers (Xu 2026)]] | A "good or bad" signal may only measure "typical for me". That is the prior that self-training sharpens. |
| No monitoring signal controls **learning** (learning rate, what to learn next). Monitoring controls generation only (early stop, backtracking). The one paper that lets a judgment pick what to learn uses a frozen outside model with human taste. | control | self-reinforcing | [[Neuromodulators set how the brain learns (Doya 2002)]], [[OMNI - models judge which tasks are interesting (Zhang 2023)]], [[Outside controller steers thinking modes (Karpf 2026)]] | The Doya-style controller in our frame has no language-model evidence. In the review it is still a metaphor. |
| No check that the model's self-report follows a change in its own weights, except for behavior predictions and one refusal edit (which the self-report did not follow). | monitor, persist | grounded | [[Models predict themselves better than others do (Binder 2024)]], [[One direction controls refusal (Arditi 2024)]] | After a self-edit, does the meta level update its model of the object level (Nelson and Narens principle 2)? Untested. |
| No internal signal is shown to track quality beyond correctness, for example readability among solutions that all pass. | evaluate | divergent | [[Value axis - model knows it is on track (Jiang 2026)]], [[Steer code readability inside the model (Gao 2026)]] | Every evaluation signal found so far is a correctness signal. Taste needs a signal that is not. |
| Stability of a model's taste across paraphrase, persona and context is measured once (one model, 80 pairs). | evaluate | stable | [[Models show research taste (Trehan 2026)]] | Stable is the least covered test (1 paper). |
| No evidence that a model's **own** taste (the own-model premium) grows with self-training. Measured model taste is shared across models. | evaluate, persist | divergent | [[Models share one taste for text (Zatuchin 2026)]], [[Hidden good-bad feeling changes choices (Berg 2026)]] | "Self-originated" needs drift away from the shared origin. No paper measures it. |
| No self-scored loop on a quality the outside checks do not measure runs many rounds without collapse. | persist | self-reinforcing | [[Self-reward only within the same test result (Wu 2026)]], [[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]], [[Learn to find interesting maths (Patel 2026)]] | Every working loop leans on a hard check or a frozen outside score. Style has no hard check. |
| Open-endedness of a self-training model (novel and learnable outputs) has never been measured with the model as its own observer. | persist | self-reinforcing | [[Open-ended means novel and learnable to an observer (Hughes 2024)]], [[Training on own outputs erases rare data (Shumailov 2024)]] | It would give a direct test of "sharpens without collapse". |

## Patterns

- **The reader is outside the model.** Probes and outside monitors read correctness and emotion signals well ([[Models know when they are right (Zhang 2025)]], [[Models do not report injected pain (Ferrara 2026)]], [[Few neurons predict right answers (Xu 2026)]]). When the model itself must report, it needs training ([[Models predict themselves better than others do (Binder 2024)]], [[Training LMs to watch themselves (Wang 2026)]]) or fails strong controls ([[Introspection claims fail basic checks (Singh 2026)]]).
- **Someone else chooses what goes into the weights.** A larger agent ([[WSP - a model reads and edits weights (Takehi 2026)]], [[Exploring WSP - small weight edits, uneven results (Hu 2026)]]), an experimenter's direction ([[TFTV - turn a steering vector into a weight edit (Perin 2026)]], [[Steer2Edit - steering into small weight edits (Sun 2026)]], [[ThinkEdit - edit weights to think longer (Sun 2025)]], [[One direction controls refusal (Arditi 2024)]]) or a task reward ([[SEAL - models write their own training data (Zweiger 2025)]]).
- **Large weight-editing gains are mostly repairs of one local fault.** The headline math gain came from fixing reasoning loops ([[WSP - a model reads and edits weights (Takehi 2026)]]), a simple fix replaces that edit ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]), and audited patching of language models mostly fails ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).
- **Every self-improvement loop that works has a hard outside check or a gate.** Tests bound the self-reward ([[Self-reward only within the same test result (Wu 2026)]]); a sandbox check plus a non-regression gate ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]); Lean proofs ([[Learn to find interesting maths (Patel 2026)]]); "keep the original unless validated" ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]); keeping 10% real data ([[Training on own outputs erases rare data (Shumailov 2024)]]).
- **Self-signals drift toward what the model already prefers.** Intrinsic rewards sharpen the prior and then collapse ([[Self-reward sharpens then collapses (He 2026)]]); code shrinks under self-reward ([[Self-reward on code collapses to short code (Jin 2026)]]); trained confidence reads consistency ([[Trained confidence tracks consistency, not accuracy (Yax 2026)]]); recursive training piles up typical outputs ([[Training on own outputs erases rare data (Shumailov 2024)]]).
- **The field's own map leaves out our two steps.** The 2026 survey has monitor and control, but no taste and no weight self-edits ([[Survey of metacognition in language models (Liu 2026)]]).

## Tensions

- **Privileged access: yes or no?** Trained observers and self-predictors beat other models trained on the same data ([[Training LMs to watch themselves (Wang 2026)]], [[Models predict themselves better than others do (Binder 2024)]]). But in-context self-report matches an input-only probe ([[Introspection claims fail basic checks (Singh 2026)]]). A possible reconciliation: the positive results are trained and about behavior; the negative ones are in-context and about internal states [our reading].
- **Metacognitive space.** [[Models can report and control their own activations (Ji-An 2025)]] finds a small space of reportable directions; [[Introspection claims fail basic checks (Singh 2026)]] reruns it and finds the input explains the report.
- **How well does weight-space programming work?** Large held-out gains with free forward passes and validation ([[Exploring WSP - small weight edits, uneven results (Hu 2026)]]) vs low patching scores under metered audits ([[WeightBench - models cannot yet patch models (Marasini 2026)]]).
- **Borrowed vs own taste.** Borrowed human taste helps an open-ended learner ([[OMNI - models judge which tasks are interesting (Zhang 2023)]]); our divergent test asks taste to move away from that origin; and open-endedness is defined as learnable to an observer, so a taste that moves too far from humans may stop counting as open-ended ([[Open-ended means novel and learnable to an observer (Hughes 2024)]]).
- **Self-graded gates.** GUARD guarantees non-regression only on its self-review score ([[GUARD - a gate stops self-edits from breaking things (Zhang 2026)]]), while training against one's own verdict inflates that verdict ([[Self-judge training makes wrong look right (Zhou 2026)]]).
- **Long loops without collapse.** A math loop moves far over 6 rounds without collapse ([[Learn to find interesting maths (Patel 2026)]]), against the sharpen-then-collapse result ([[Self-reward sharpens then collapses (He 2026)]]). Patel's taste score is frozen and outside, so the two do not test the same thing.
- **Harshit's notes:** none yet in any paper note or in `4 My notes/`, so no disagreements to report.

## Coverage by section

| Section | Papers | Read | Note |
|---|---|---|---|
| 1 Introduction | 0 | 0 | **Under 2.** Needs no new papers; draw on sections 2 and 8. |
| 2 Foundations | 6 | 0 | Was 0 this morning. Fleming and Daw (2017) still missing. Doya note is abstract only. |
| 3 Monitoring | 7 | 0 | Rubin 2026 (shallow injection reports) still to add. |
| 4 Evaluation signals | 5 | 0 | All signals are correctness signals. Xu 2026 is unread. |
| 5 Persistent control | 9 | 2 | Best covered. All editors are outside models. |
| 6 Limits | 6 | 0 | Strong on threats; one design that works (hard check plus gate). |
| 7 Taste & open-endedness | 5 | 0 | Stable test covered by one paper. |
| 8 Synthesis | 0 | 0 | Written in [[outline]]; no papers needed. |
| 9 Conclusion | 0 | 0 | **Under 2.** No papers needed. |

## Fill next

1. Note for "A Closer Look at Language Model Introspection" (arXiv 2611.15267): already scored 3, it sharpens the grounded gap.
2. Note for Fleming and Daw (2017), confidence as a second-order inference: the missing classic for section 2.
3. Search: a model that edits its **own** weights by reasoning (self weight-space programming, self-modifying networks after Irie 2022). If one exists, gap 1 shrinks.
4. Search: stability of model preferences across paraphrase and persona (the Stable test), beyond Trehan.
5. Read Zeng et al. 2026, cited by [[Training LMs to watch themselves (Wang 2026)]] for "trained self-prediction does not always show an own-model advantage" [unverified: not found yet].
