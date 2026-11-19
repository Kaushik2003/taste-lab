---
type: experiment
id: exp01
thread: T1
status: spec
compute: 1–2× A100/H100 for 8B, 4× for 32B
tags: [type/experiment, thread/T1, status/spec]
links: ["[[code-quality-signal-T1]]"]
---

# exp01: Valence probe vs. code readability

## Question
Does an internal valence signal track code readability, beyond cheap confounds?

## Hypothesis + kill criterion
ρ(valence, expert readability) ≥ 0.4 after partialling out length, perplexity, and comment ratio. **Kill:** ρ < 0.2 in two model families.

## Setup
- **Models:** Qwen3.x-8B-Instruct (primary), Llama-3.x-8B (replication), Qwen 32B if stage A passes.
- **Data:** ~50 problems (HumanEval+/MBPP+/LiveCodeBench easy-medium). Sample 16 solutions per problem at T=1.0 and keep 8 that **pass all tests**. Add 2 deliberately "sloppy but correct" variants per problem (bad names, nesting, dead code) as known-bad anchors.
- **Readability labels:** blind pairwise ranking by 3 raters (you + 2 friends), plus an automated proxy (cognitive complexity, naming score) as secondary. Don't rely on an LLM judge alone because it shares the model's biases.
- **Valence directions:** replicate the emotion-concept extraction. Contrast prompts for positive vs. negative valence emotions (satisfaction/delight vs. disgust/frustration), take mean activation differences per layer, and pick the layer by held-out separability.
- **Readout:** project the model's activations *while reading* each solution (prompt: "Here is a solution: …") onto the valence direction. Average over solution tokens.
- **Controls (from [[2026-ferrara-all-quiet-pain]] OWMI):** random direction matched in norm; perplexity; length; a shuffled-label probe.

## Plan
- [ ] A1. Generate and filter solutions, build sloppy anchors (1 day)
- [ ] A2. Collect rankings, get ~400 pairwise judgments (2–3 days, the human part)
- [ ] A3. Extract valence directions, sanity-check on emotion text (1 day)
- [ ] A4. Readout + partial correlations + controls (1 day)
- [ ] A5. Also ask the model verbally "which do you prefer?" and compare to the probe, as a first look at the grounded test
- [ ] B. If ρ passes: causal check. Steer +valence while reading solution X and see whether its stated preference for X rises.

## Log
<!-- dated entries -->

## Results

## What it means for the thread
