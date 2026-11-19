---
type: concept
tags: [self-modification, consolidation]
links: [[2025-zweiger-seal]], [[2026-takehi-weight-space-programming]], [[2026-fischetti-just-sort-it]]
---

# Self-directed weight updates

**Definition (plain):** The model itself decides what changes in its weights, as opposed to an external optimizer on a fixed dataset.

**The spectrum:**
| Mechanism | Gradient? | Who decides | Good for |
|---|---|---|---|
| Fast weights / self-referential nets (Schmidhuber '92, Irie '22) | no (learned rule) | the net, at runtime | in-context adaptation |
| Nested Learning / Hope (Google '25) | multi-timescale | architecture | continual memory |
| SEAL ([[2025-zweiger-seal]]) | yes (SFT/LoRA) | model writes the data | distributed changes, e.g. style |
| WSP ([[2026-takehi-weight-space-programming]]) | no | an LLM reads and edits weights | localized repairs |
| Rank-one steering consolidation (T5, ours) | no | valence direction baked in | making a taste direction persistent |

**Key insight:** WSP edits act like constant biases along a direction ([[2026-fischetti-just-sort-it]]), which is what a steering vector is. That may be the bridge from inference-time taste to persistent taste.

**Related:** [[anti-collapse-anchor]], [[neuromodulation-metalearning]]
