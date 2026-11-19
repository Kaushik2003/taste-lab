---
type: paper
title: "AI models collapse when trained on recursively generated data"
status: skimmed
arxiv:
url: https://doi.org/10.1038/s41586-024-07566-y
doi: 10.1038/s41586-024-07566-y
authors: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal
year: 2024
venue: Nature 631, 755-759
relevance: 3
section: 6
tier: deep
tests: [self-reinforcing]
components: [anchor]
tags: [type/paper, section/6, test/self-reinforcing, component/anchor, status/skimmed, relevance/3, role/threat, model-collapse, synthetic-data, self-training]
links: ["[[Field map - Limits of self-learning]]", "[[Anchor against collapse]]", "[[Self-reward sharpens then collapses (He 2026)]]", "[[Self-reward on code collapses to short code (Jin 2026)]]", "[[Four tests for own taste]]"]
---

# AI models collapse when trained on recursively generated data

**One line:** If each new model trains on text made by the last one, the rare parts of the original data disappear first, and over many rounds the model narrows toward a small, low-variety output.

**Why it matters to us:** It is the classic statement of "model collapse". Any loop where a model learns from what it prefers to generate is a version of this setup.

Source: [Nature 631, 755-759](https://doi.org/10.1038/s41586-024-07566-y) (published 25 July 2024, open access). Full text read from the [Edinburgh repository PDF](https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf).

**Words used here:**
- **Model collapse:** a slow loss of the original data distribution when models learn from model-made data.
- **Tails of a distribution:** the rare cases.
- **Perplexity:** how surprised a model is by text. Lower means the text is more typical for the model.
- **Generation (here):** one round: train a model, then use its output as training data for the next.

## Claim
Using model-made content in training without care causes lasting defects: the tails of the original distribution vanish. This happens in language models, variational autoencoders and Gaussian mixture models ([Nature](https://doi.org/10.1038/s41586-024-07566-y)).

## Mechanism
- **Early collapse:** the model starts to lose the tails. **Late collapse:** it converges to a distribution with little likeness to the original and much less variance.
- Three errors add up over generations: statistical approximation error (finite samples; the main cause), functional expressivity error (the model cannot represent the true distribution), and functional approximation error (the learning method is imperfect).
- **Language model test:** OPT-125m fine-tuned on wikitext2. Each generation makes a dataset of the same size (64-token continuations, five-way beam search) and the next model trains on it. Five runs per setting.

## Evidence
- The model fine-tuned on real wikitext2 reaches perplexity 34 (zero-shot was 115).
- With no original data kept (5 epochs), task perplexity worsens from about 20 to 28 points over generations.
- Keeping 10% of the original data each generation (10 epochs) gives only minor loss.
- In both settings, low-perplexity samples pile up over generations: the model makes more and more of what it already finds typical, and less of the rare.
- Generated text shows repeated phrases in later generations (Example 1 in the paper).

## Limits / what they didn't show
- Small model (125M), few generations (up to 9), and full replacement of data each round. Later work argues that accumulating real data alongside synthetic data avoids collapse [unverified: not read here; for example Gerstgrasser et al. 2024].
- No selection: the model trains on all its outputs, not on outputs it prefers. A preference filter could speed collapse or slow it; the paper does not test that.
- Beam search, not sampling, which already narrows outputs.

## Relevance to taste-lab
**Relevance 3.** Section 6, the base threat for the self-reinforcing test ([[Four tests for own taste]]).
- **Mechanism matches our risk:** self-training on preferred outputs pushes toward what the model already finds typical. That is the same "sharpen the prior" story as [[Self-reward sharpens then collapses (He 2026)]], seen at the data level.
- **Anchor evidence:** keeping 10% real data nearly stops the damage. That supports a fixed outside anchor in any self-training loop ([[Anchor against collapse]]).
- **Measure to copy:** track the tails (rare outputs), not only the average score. A taste that "sharpens" may just be a loss of tails.

## Steal this
- The early vs late collapse split as words for the review.
- Perplexity histograms over generations: watch for mass piling up at low perplexity.
- "Keep a fixed share of original data" as the simplest anchor baseline.

## Harshit's notes
<!-- yours -->
