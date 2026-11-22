---
type: experiment
id: exp01
thread: Q1
status: spec
tags: [type/experiment, question/Q1, status/spec]
links: ["[[Q1 Does the model sense code quality]]", "[[08-synthesis]]"]
---

# exp01: Valence probe vs. code readability

## Status and maintained specification

**Proposed specification only. Execution remains parked.** The maintained protocol is now [Section 8.1 of the literature review](../../1%20Literature%20review/08-synthesis.md#81-q1-protocol-readable-signal-causal-use-then-a-decision), also at [[08-synthesis]]. It separates blind readability prediction (Stage A), fixed-text causal choice checks (Stage B), and the later Q2 selection experiment.

This pointer replaces the older short plan rather than maintaining two conflicting protocols. The old three-rater, approximately 400-judgment estimate was not a powered design. The new proposal uses at least five blind raters, problem-level splits and uncertainty, length/log-perplexity/comment baselines, supervised input-only and readability comparators, and norm- plus disruption-matched causal controls. The approximately 50-problem run is a pilot; the confirmatory sample needs a power simulation.

The original Q1 hypothesis (partial correlation at least 0.4) and stop line (below 0.2 in two families) are distinguished from the stricter incremental/random-direction criteria and interval-based rules proposed in Section 8.1. Those proposals, checkpoint choices, task counts and rater feasibility still need a research-owner decision before execution. No compute allocation or experiment run is approved by this specification.

## Next action

Review Section 8.1 and settle its pre-registration choices when experiments resume. Do not generate candidates, recruit raters or run interventions while Q1 is parked.

## Log

- 2026-11-22: Consolidated the protocol in Section 8.1 of the literature review. Replaced the stale short plan with this pointer; no experiment, training or compute purchase was performed.

## Results

No results yet.
