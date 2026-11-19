---
type: concept
tags: [type/concept, status/active, self-modification, consolidation]
links: ["[[SEAL - models write their own training data (Zweiger 2025)]]", "[[WSP - a model reads and edits weights (Takehi 2026)]]", "[[A simple sort replaces the anti-loop edit (Fischetti 2026)]]", "[[ThinkEdit - edit weights to think longer (Sun 2025)]]", "[[Steer2Edit - steering into small weight edits (Sun 2026)]]"]
---

# Self weight updates

**Definition (plain):** The model itself decides what changes in its weights, as opposed to an external optimizer on a fixed dataset.

**The spectrum:**
| Mechanism | Gradient? | Who decides | Good for |
|---|---|---|---|
| Fast weights / self-referential nets (Schmidhuber '92, Irie '22) | no (learned rule) | the net, at runtime | in-context adaptation |
| Nested Learning / Hope (Google '25) | multi-timescale | architecture | continual memory |
| SEAL ([[SEAL - models write their own training data (Zweiger 2025)]]) | yes (SFT/LoRA) | model writes the data | distributed changes, e.g. style |
| WSP ([[WSP - a model reads and edits weights (Takehi 2026)]]) | no | an LLM reads and edits weights | localized repairs |
| Rank-one steering consolidation (Q5, ours) | no | valence direction baked in | making a taste direction persistent |

**Key insight:** WSP edits act like constant biases along a direction ([[A simple sort replaces the anti-loop edit (Fischetti 2026)]]), which is what a steering vector is. That may be the bridge from inference-time taste to persistent taste.

**Related:** [[Anchor against collapse]], [[Neuromodulators as learning settings]]
