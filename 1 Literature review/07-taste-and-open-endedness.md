---
type: draft
status: draft
section: 7
tags: [type/draft, section/7, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Taste and new ideas]]", "[[Four tests for own taste]]", "[[Anchor against collapse]]"]
---

# 7. Taste & open-endedness

"Taste" has recently become a measurable object rather than a metaphor. Three papers define the measurement landscape, and together they draw the boundary this review cares about: a measured taste can be divergent, stable, and still not be the model's own.

## 7.1 Measuring divergence and stability

Trehan and Chopra operationalize research taste as pairwise choice: a model sees an author's actual future-work direction against a plausible alternative from a neighboring paper, in both orders ([[Models show research taste (Trehan 2026)]]). The three-outcome split - author alignment, stable divergence (picks the non-author option in both orders), unstable choice (follows position) - separates content preference from position noise. Across 8 frontier models, stable divergence runs 15.0 to 36.2%, survives four prompt ablations (67 to 81% kept), and mostly cannot be explained by a similarity heuristic. This is the most direct published operationalization of the divergent and stable tests ([[Four tests for own taste]]), and it ports to code readability almost unchanged: two passing solutions, one preferred by human raters, shown in both orders. Its limit for present purposes is that it is purely behavioral - no internal signal - and, crucially, divergences are partly shared across models (mean inter-model agreement 61.9%).

## 7.2 Shared taste, not own taste

Zatuchin supplies the cross-model control ([[Models share one taste for text (Zatuchin 2026)]]). Re-analyzing generator-by-selector matrices (21,828 trials), the own-model premium - does a model prefer *its own* text over other models' text, after removing what every model likes - is +0.019 share points, p = 0.14, with 97% power to detect a 0.05 effect. Models strongly prefer model-written text over human text (GPT-4 descriptions chosen 77-95% by every selector vs 36% by humans), but the preference is one shared machine taste, not five personal ones. The statistic (the diagonal premium gamma with an exact permutation test) is the right instrument for the divergent test's ownership half: if a model's valence prefers code every model prefers, that is machine taste, not self-originated taste. In a self-training loop, a *growing* gamma over rounds is a direct measure of drift away from the shared origin.

## 7.3 Taste as an open-ended driver

The predecessor result is OMNI ([[OMNI - models judge which tasks are interesting (Zhang 2023)]]): open-ended learning drowns in learnable-but-boring tasks, and a frozen foundation model used as a Model of Interestingness - human notions of interesting distilled from human text - beats uniform sampling and learning-progress-only baselines at picking what to learn next. Taste as auto-curriculum works; the taste is borrowed from a frozen external model.

Patel et al. build the closest working loop to the target architecture ([[Learn to find interesting maths (Patel 2026)]]). A computable interestingness score - expected proof length relative to statement description length - serves both as an RL reward and as a gate on which of the system's own theorems enter its premise library. Over 6 self-expanding rounds, mathlib overlap falls from 91.9% to 30.6% without collapse, interestingness promotion beats no-pruning, random and longest-proof baselines on blind judged quality, diversity and redundancy, and Lean verification keeps every step correct. The caveat is the one this review turns on: the taste is a fixed external formula plus a separately trained predictor. It never changes, so the loop shows a *fixed* taste can drive open-ended movement away from origin - not that a *self-scored* loop is safe, which Section 6's collapse results put in doubt. Its transferable parts are the promotion-gate ablation design and "library overlap" as a drift metric.

## 7.4 Can taste itself be trained?

Two 2026 results bracket the question. Tong et al. train taste directly with Reinforcement Learning from Community Feedback: a Scientific Judge learns from citations, generalizes to future-year papers, other metrics and unseen fields, and a Scientific Thinker trained against it proposes higher-potential ideas than baselines ([[Scientific taste can be trained from community feedback (Tong 2026)]]). Taste is trainable as a capability. But IdeaTaste measures the distance to human communities: LLM proposals from a frozen 2025 snapshot match what fields actually published in 2026 at about 26% of human level on citations and 18% on ideas, and the failure is not finding the community's directions but converting them into the concrete approaches it pursues ([[IdeaTaste - models fall short of human research taste (Zhong 2026)]]). More context and larger populations do not close the gap. Read together: models absorb the shared directions (the machine prior, Section 7.2) and miss exactly where individual taste operates. Utility engineering adds that the preferences themselves are coherent systems emerging with scale, not noise ([[Model values form coherent utilities that can be steered (Mazeika 2025)]]) - so there is something stable to own, even if current instruments cannot attribute it to one model.

## 7.5 Where taste measurement stands

The field can now measure divergence, stability and ownership, and can run a fixed-taste open-ended loop. The missing combination is all four tests at once: a taste read from the model's own activations (not verbal choice), shown to diverge from humans *and* from the shared machine prior, sharpening under self-training behind an external anchor. A second caution is specific to the testbed: readability may be a convergent axis where diverging from expert judgment simply means being wrong, so the divergent test must be paired with the ownership statistic rather than read alone.
