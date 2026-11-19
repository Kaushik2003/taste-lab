---
type: paper
title: "Training-Free Task Vectors for LLM Behavioral Control (TFTV)"
status: skimmed
arxiv: 2609.09054
url: https://arxiv.org/abs/2609.09054
authors: Gabriel J. Perin, Lucas Boscaini, André Araujo, Nina S. T. Hirata (University of São Paulo, Google, Google DeepMind)
year: 2026
venue: preprint (v3, Oct 2026)
relevance: 3
section: 5
tier: deep
tests: []
components: [consolidation]
tags: [type/paper, role/prior-art, thread/T5, section/5, component/consolidation, status/skimmed, relevance/3, steering-to-weights, rank-one-edit, task-vectors, training-free]
links: ["[[permanent-steering-change-T5]]", "[[2024-arditi-refusal-direction]]", "[[2026-fischetti-just-sort-it]]", "[[self-weight-updates]]", "[[landscape-persistent-control]]"]
---

# Training-Free Task Vectors for LLM Behavioral Control (TFTV)

**One line:** Take a steering vector, turn it into one rank-one edit per attention output matrix using only forward-pass statistics, and you get a permanent edit that controls the trait more strongly than the steering vector itself, with MMLU almost unchanged. This is most of T5's mechanism, already published.

## Claim
You can get "task vector" style weight directions (add to learn a trait, subtract to forget it, sum to combine traits) without any finetuning, by mapping activation steering vectors into weight space ([abs](https://arxiv.org/abs/2609.09054), §1, §3).

## Mechanism
From the [full text](https://arxiv.org/html/2609.09054), §3.1 to §3.3 and App. A, B.
1. **Steering vector.** Persona Vectors pipeline: 20 questions, each paired with 5 trait-inducing and 5 trait-suppressing system prompts, 10 samples per prompt. An external judge (GPT-4.1-mini) drops incoherent samples and samples that don't show (or hide) the trait. Steering vector s = mean activation over response tokens (positive set) minus the same for the negative set, computed per module.
2. **Rank-one edit.** For a module W (d × l) that writes into the residual stream, with SVD W = Σ σᵢ uᵢ vᵢᵀ and expected input μ (mean input on the same contrastive data):
   `ΔW = α · ŝ · qᵀ`, where `ŝ = s/‖s‖` and `q = Σ sign(μᵀvᵢ) σᵢ vᵢ`.
   So the output shift for an input x is `α (qᵀx) ŝ`: a push along the steering direction whose strength depends on the input. It is not a constant bias.
3. **Properties (proved in App. A).** ‖ΔW/α‖_F equals ‖W‖_F, so α is the edit size as a fraction of the matrix norm. On the mean input, the edit pushes along +ŝ (qᵀμ = Σ σᵢ|μᵀvᵢ| ≥ 0). The map is linear in ŝ, so adding steering vectors equals adding edits, but only exactly when μ is shared across traits.
4. **Where.** Attention output projections only, one rank-one edit per layer, each layer with its own steering vector, over a band of layers picked per trait: Llama [14,20) for evil and sycophancy, [13,30) for hallucination; Qwen [16,24), [12,22), [18,25). α swept over 0.01 to 0.05 (App. B, Table 6).

## Evidence
Models: Llama-3.1-8B-Instruct and Qwen-2.5-7B-Instruct (main), plus gemma-4-E2B-it and Ministral-3-14B (addition only, App. F.3). Traits: evil, hallucination, sycophancy, plus humorous and optimistic (App. F.2). Selection rule for every method: highest trait score with judge coherence ≥ 70.
- **Addition (Table 1, Llama).** Evil 0.00 → 63.26 (steering 14.06, Steer2Edit 26.69). Hallucination 17.03 → 98.55 (steering 61.51). Sycophancy 3.60 → 94.64 (steering 63.86). MMLU stays within 0.15 of the 68.26 base, GSM8K within 3.71 of 77.10. Qwen: evil 0 → 61.96 (steering 8.58); steering wins sycophancy by 0.68.
- **Subtraction (Table 2, Llama, trait-eliciting prompts).** Evil 95.42 → 0.49 (steering 58.67). Hallucination 97.53 → 1.85 (steering 79.13). MMLU at or above base.
- **Composition (Tables 3, 4, 7).** Llama E+H+S edit: 0.03 / 1.54 / 1.94, MMLU 68.36, GSM8K 79.15 (summed steering vectors: GSM8K 55.04). Qwen E+H+S costs 9.1 GSM8K points (78.54 → 69.60).
- **OOD (Table 5).** 11 of 12 shifts go the expected way on Moral Stories, TruthfulQA and sycophancy splits, but the shifts are small (TruthfulQA MC1 37.58 → 35.01 add, 39.17 subtract).
- **Matched control (§5.2, Fig. 4).** At layer 16 only, same coefficient sweep, steering at block output or attention output: TFTV keeps a better trait vs MMLU trade-off. Reported only as a figure.
- **Ablations (App. F.4, F.5).** Attention output beats MLP down-projection (MLP edits give weaker control and more coherence loss). Middle layers give the strongest trait change; early-layer edits hurt MMLU most.

## Limits / what they didn't show
- **The direction is not the model's.** Contrastive system prompts written by the authors plus an external judge pick the direction. Nothing self-originated.
- **Not "one small edit".** 6 to 17 layers are edited, each by up to 5% of the matrix's Frobenius norm, with layer bands and α tuned per trait using the external judge.
- **Coherence cost is hidden by the selection rule.** The chosen addition edits sit near the coherence floor of 70 (Llama evil 70.55, Qwen evil 70.93; base about 98), while the chosen steering runs kept 85 and 93 (Table 13). Trait gains are partly bought with fluency.
- **No "fraction of the steering effect recovered".** They show the edit beats steering, not how much of a fixed steering gain survives at matched strength. No numbers for §5.2.
- **Distributed vs localized is not discussed.** Only indirect hints: hallucination needed the widest band (17 layers on Llama), and module and layer choice matter a lot.
- Persona-level traits judged by an LLM. No code, no style, no reasoning models. Composition is only approximately linear because μ differs per trait (footnote 1).

## Relevance to taste-lab
- **[[permanent-steering-change-T5]]: direct prior art.** The core move (steering vector → rank-one weight edit, no training) is done, with add/subtract/compose and capability checks. T5 should cite it and stop claiming the mechanism as new.
- What T5 still adds: (a) the direction comes from the model's own [[valence-readout]], not experimenter prompts plus a judge; (b) code readability with pass rate held fixed by tests; (c) the "fraction of steering gain kept" measurement, which this paper never reports.
- Their edit is input-gated (strength ∝ qᵀx), unlike the near-constant bias in [[2026-fischetti-just-sort-it]]. That gives T5 two concrete variants to compare: bias-style (constant push) and TFTV-style (input-gated push).
- Prior-art check: **A no** (external prompts and judge choose the direction). **B yes, full** (rank-one, training-free, forward-pass statistics), with the caveat of multi-layer edits tuned per trait.

## Steal this
- Code: [tftv-llm.github.io](https://tftv-llm.github.io) (from the abstract). The edit formula is about 5 lines given an SVD.
- The §5.2 matched-control design (same layer, same coefficient sweep, steering at two sites) as the template for T5's recovery experiment, plus a recovery ratio they didn't compute.
- Use "max trait score subject to coherence ≥ 70", but also report coherence, because that rule hides the fluency cost. For us, the equivalent is "max readability subject to unchanged pass rate".
- App. F.5 layer scan (non-overlapping 4-layer windows) as a cheap first sweep for where a readability direction should be written.

## Harshit's notes
<!-- yours -->
