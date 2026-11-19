---
type: concept
tags: [type/concept, status/active, neuroscience, metalearning, controller]
links: ["[[Good-bad signal probe]]", "[[Neuromodulators set how the brain learns (Doya 2002)]]"]
---

# Neuromodulation as metalearning (Doya 2002)

**Definition (plain):** Doya, "Metalearning and neuromodulation" (Neural Networks, 2002), maps brain neuromodulators to RL meta-parameters:
- **Dopamine** → reward prediction error (what was better or worse than expected)
- **Serotonin** → time scale / discount (patience)
- **Noradrenaline** → randomness of action selection (exploration temperature)
- **Acetylcholine** → learning rate (how much to update from this experience)

**Why it matters for us:** This is the controller in the architecture, and the formal version of "learning at its own rate".
Valence + surprise + confidence set the per-experience learning rate, the exploration temperature, and which adapter to update.
Emotions act as control knobs on learning, not as decoration.

**Steal:** Lifelong RL via neuromodulation (arXiv 2408.08446) for implementation patterns.

**Related:** [[Models that change their own weights]], [[Anchor against collapse]], paper note [[Neuromodulators set how the brain learns (Doya 2002)]]
