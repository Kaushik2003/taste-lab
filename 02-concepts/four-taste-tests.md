---
type: concept
tags: [evaluation, taste]
links: [[valence-readout]], [[anti-collapse-anchor]]
---

# Four tests for self-originated taste

A candidate taste must pass **all four**. Each one alone has a cheap explanation.

1. **Divergent:** preferences differ from human/training preference data. *Alone, it could be noise or a quirk.*
2. **Stable:** holds across paraphrase, persona, context. *Alone, it could just be memorized human taste.*
3. **Grounded:** self-report matches a probed internal state, causally (steer the state → the report shifts). *Note: zero-shot report fails in open models, see [[2026-ferrara-all-quiet-pain]].*
4. **Self-reinforcing:** sharpens under self-training without collapse. *Alone, it could be sharpening a prior.*

Related measurement work: "Eliciting Research Taste" (2611.19794) uses author alignment / **stable divergence** / unstable choice as behavioral measures, which is close to tests 1+2. Cite and contrast.
