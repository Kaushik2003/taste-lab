---
type: report
status: active
tags: [type/report, direction, critique]
links: ["[[2026-11-23 gap check]]", "[[gaps]]", "[[A model rewrites its own weights (Fan 2026)]]", "[[Four tests for own taste]]"]
---

# Direction critique, 2026-11-23

Harshit asked: is this the right direction, and is it a valid point for research later? Be brutal.

**Verdict.** The vision is fine as the motivation of the review. It is a bad first research project. Pick one small question inside it.

## What is wrong with the full idea as a project
1. **It stacks four unproven things.** Metacognition, a self-model, weight self-editing and taste. Each is contested. A project that needs all four to work will almost surely fail somewhere.
2. **The tool does not fit the target.** Weight-space programming has so far fixed local faults (reasoning loops), and a $0.90 optimizer beats the agent (Salloum 2026). A taste is probably spread over the network. The original WSP paper says it struggles with spread-out problems.
3. **"Cheaper than LoRA" is not true today.** A LoRA run on a small model costs a few dollars. The agent repair used 89.7 million tokens; Fan's sessions take hours of GPU time. The real arguments for direct edits are: no training data, small and inspectable changes, self-directed. Cost is not one.
4. **"Taste" can become unfalsifiable.** Drift can be called collapse; stability can be called inheritance. Current evidence says values persist or converge (Stroganov 2026, Liang 2026, Bhatia 2025).
5. **The self-model adds nothing, by current evidence.** Three papers find no advantage of self over other (Blandfort, Kocabay, Zeng).
6. **A "nobody combined these" gap is weak.** Not done does not mean worth doing. A good question has an interesting answer both ways.
7. **Scoop and hype.** Fan's group (six universities) names recursion as its next step. November 2026 has more than 10 WSP papers. A newcomer loses a race here.
8. **Thin base.** The key paper (Fan) has no random-direction baseline, a small gain, and edits withdrawn in 5 of 8 sessions. Our verdicts rest mostly on abstracts: 5 of 128 notes are full reads.

## Process problem
The direction was built by Claude sessions faster than the PI could read. 128 notes, 5 read. The PI cannot yet defend the idea. Reading must come before commitment.

## Directions, ranked
- **A (recommended first project): do direct weight edits move a model's preferences?** Apply known edits in sequence (direction removal, rank-one edits) to a small open model, and measure preference stability with existing instruments (Trhlik 2026, Mazeika 2025, Zatuchin 2026) plus a health signal (perplexity, Yang 2024). No self-editing needed. One GPU. An answer either way is useful: it tells whether edits can carry taste at all. [unverified: no search yet for prior work on preference or value change after model editing]
- **B (second): does an internal good/bad signal predict which edits help?** Rank candidate edits by a hidden-state readout (Berg 2026, Jiang 2026), compare with held-out gain. This is the evaluation step alone.
- **C (the vision, not a first project): the full loop.** Repeated self-edits, own judgment, outside veto, drift measured. Keep it as the framing of the review and as the long-term goal.

## What the review should do
Present C as the open agenda, state the eight problems above honestly, and end with A and B as the first questions. No experiment plans in the review.
