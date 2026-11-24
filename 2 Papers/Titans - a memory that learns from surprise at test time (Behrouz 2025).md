---
type: paper
title: "Titans: Learning to Memorize at Test Time"
status: skimmed
arxiv: 2501.00663
url: https://arxiv.org/abs/2501.00663
authors: Ali Behrouz, Peilin Zhong, Vahab Mirrokni
year: 2025
venue: arXiv preprint (Google Research)
relevance: 2
section: 5
tier: skim
tests: [self-reinforcing]
components: [consolidation, control]
tags: [type/paper, section/5, test/self-reinforcing, component/consolidation, status/skimmed, relevance/2, role/prior-art, memory, test-time-learning, self-modification]
links: ["[[Field map - Changes that stay in the weights]]", "[[Models that change their own weights]]", "[[Nested Learning - a model that learns its own update rule (Behrouz 2025)]]", "[[Sleep - a model consolidates memories into its weights (Behrouz 2026)]]", "[[Neuromodulators as learning settings]]"]
---
# Titans: learning to memorize at test time (Behrouz 2025)

**One line:** A new architecture with a memory module whose own weights are updated while the model reads. What gets written is decided by "surprise": inputs that the memory predicts badly are stored more strongly.

Read 2026-11-24 at the user's request: abstract, Sec. 1, Sec. 3.1, Sec. 5.4, Sec. 6. Other experiments not read.

## Mechanism
- Three parts: attention as short-term memory; a neural long-term memory (a small MLP); and a persistent memory of fixed task parameters (Sec. 1).
- The long-term memory is trained **at test time**. Surprise is the gradient of an associative-memory loss for the incoming token. A momentum term carries past surprise, and a forgetting gate (weight decay) clears old content (Sec. 3.1).
- So the inner loop is gradient descent with momentum and weight decay on the memory's weights; the outer loop (normal training) learns how to memorize.

## Evidence
- Beats Transformers and recent recurrent models on language modeling, common-sense reasoning, genomics and time series, and scales past a 2M-token context (Abstract, Sec. 6).
- On BABILong, a small Titans model beats much larger models, including GPT-4 and Llama3.1-8B with retrieval (Sec. 5.4).

## Limits
- Only the memory module changes at test time; the rest of the weights are fixed.
- Needs a new architecture trained from scratch. Models are small (up to 760M in the memory-depth study).
- Surprise measures "unexpected", not "good or bad".

## Relevance to taste-lab
Prior art for "an internal signal decides what is written into the weights". Here the signal is surprise, a monitoring signal, and the write is a gradient step. It is the first step of the Google line Titans, then Nested Learning (Hope), then Sleep. Open after it: an evaluative signal (good or bad), and any measurement of what the stored changes do to the model's preferences.
