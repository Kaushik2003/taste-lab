---
type: draft
status: draft
section: 9
tags: [type/draft, section/9, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[08-synthesis]]"]
---

# 10. Conclusion

This review followed one loop through four literatures that rarely meet: a model monitors its own states, evaluates them, controls its reasoning, and writes changes into its own weights, with a model of itself across the loop and an anchor beneath it.

Each step has prior art. Models carry readable signals about their own work, and in one case they act on them. Internal signals with a good-or-bad flavor exist and move choices. Weights can change after deployment by two routes, learned memory and direct edits, and one model has edited itself. With care, researchers can measure preferences.

The connections are what is missing. Models report their own states poorly, their picture of themselves is mostly generic, and no model predicts what a change to itself will do. Where a model's own judgment decides which weight change stays, that judgment is its certainty or a verbal score, and no method uses an evaluation signal read from its hidden states. Loops that run on the model's own signal sharpen, drift, or decay, and can remove the model's self-monitoring as a side effect. Measured taste is so far largely shared across models, and inherited values have persisted under self-modification.

So a model that develops a taste of its own by changing itself is a possibility that the evidence neither establishes nor rules out. We stated the idea as an open agenda, listed the nine problems that the literature raises against it, and set out which instruments could test each of four properties that such a taste would need.

The first question to answer is narrower than the agenda and comes before it: when a model's weights change after deployment, do its preferences move, and does its self-monitoring change? No study we found measures both after a weight change. Each of the four possible answers is useful, including the answer that small weight changes carry no taste at all.

One lesson holds whatever the answer. The field has learned to change what a model does much faster than it has learned to check what the model has become. Methods for changing weights after deployment are arriving now; methods for asking the changed model what it prefers, and whether it knows, should arrive with them.
