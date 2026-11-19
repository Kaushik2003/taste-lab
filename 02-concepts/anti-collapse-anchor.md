---
type: concept
tags: [type/concept, status/active, collapse, stability]
links: ["[[2026-he-unsupervised-rlvr-limits]]"]
---

# Anti-collapse anchor

**Problem:** Self-generated rewards sharpen the prior, then collapse ([[2026-he-unsupervised-rlvr-limits]]; Shumailov et al., Nature 2024).
A model chasing its own likes turns into a narrower copy of itself by default.

**Candidate anchors:**
- **Hard external checks:** tests must pass (code), so taste can only move style.
- **Novelty / diversity term:** OMNI-style interestingness, or a penalty on falling Rényi entropy.
- **Non-regression gate:** only promote an update if gains outweigh regressions on a pinned buffer (GUARD, 2611.23476).
- **Small-data regime:** intrinsic rewards stay safe in test-time training on small data (He et al.).

**Metrics to always log:** Model Collapse Step, Rényi entropies at orders 0/1/2/∞ (they cross at different points per 2611.08892), output type-token diversity.

**Related:** [[four-taste-tests]]
