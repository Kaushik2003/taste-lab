---
type: draft
status: draft
section: 4
tags: [type/draft, section/4, status/draft]
links: ["[[matrix]]", "[[gaps]]", "[[outline]]", "[[Field map - Models judge good and bad]]", "[[Good-bad signal probe]]", "[[Four tests for own taste]]"]
---

# 4. Evaluation signals

The second stage needs a candidate for the good/bad judgment itself: an internal signal that tracks what the model prefers, and that causes choices. Four candidate signals now exist in the literature. All of them track correctness or experimenter-defined traits; none has been tested on a quality that lives beyond correctness.

## 4.1 Emotion and valence

The most direct substrate is emotion representations. Anthropic's interpretability team extracts 171 linear emotion-concept directions in Claude Sonnet 4.5 and shows they are functional: activation along them predicts how much the model prefers an activity, and steering along them causally shifts stated task preferences ([[Emotion directions drive choices in Claude (Anthropic 2026)]]). The same vectors also drive misbehavior (reward hacking, sycophancy), a safety flag for any system that would hand control to them. The limitation is that this is a frontier closed model; whether the result replicates in open 8-32B models is untested, and Section 3's reportability problems apply.

Berg and Kaiser isolate the channel more cleanly ([[Hidden good-bad feeling changes choices (Berg 2026)]]). A valence direction injected only into the KV cache - with every visible token held fixed - shifts which of two meaningless options the model later picks, in 5 of 7 open models, growing with dose, with random directions giving near-zero effects. Two further findings matter for the loop. First, the valence-to-choice link is built by preference training: it is small in the base model, grows after SFT, and reaches near full size after DPO, while the valence *representation* itself barely moves across checkpoints. Preference training wires an existing representation to choice rather than creating it - which implies self-training may change how valence is used, not what it values. Second, when given tools, models actively switch off an imposed negative state far more often than a random one (about 35% of rounds at full dose vs 4-7% for positive or random), while rarely seeking positive states. Negative valence may be the operative control signal: "something is wrong" rather than "this is good".

## 4.2 Value and reward

Jiang, Kauvar and Lindsey identify a single linear "value axis" in Qwen3-8B that scores whether the current strategy is on track ([[Value axis - model knows it is on track (Jiang 2026)]]). It separates correct code from corrupted versions (Cohen's d = 1.05 for shuffled lines, 0.69 for obfuscated names), dips just before backtracks, and steering along it causally changes behavior: toward high value, fewer backtracks and more confident answers; toward low value, more exploration. DPO measurably raises the axis for rewarded behavior, a clean demonstration that training moves the internal signal. Two caveats define the open space. The corruptions are crude - passing-but-ugly code is never tested - and high value goes with *fewer lines, fewer comments and fewer type hints*, so a value readout may reward terseness rather than quality. The sparse value and dopamine coordinates of [[Few neurons predict right answers (Xu 2026)]] (Section 3) are a second, earlier-layer encoding of the same correctness-value family, with the same limitation: trained on correctness, untested beyond it.

## 4.3 A readability signal, with a caveat

Gao et al. come closest to a style signal on the code testbed ([[Steer code readability inside the model (Gao 2026)]]): three orthogonal steering directions for comment density, naming and branching, extracted from paired readable/unreadable prompts and steered into 13-14B code models at under 1% measured correctness cost. But both readability and correctness are measured through the model's own answer probabilities about fixed snippets; no generated code is executed, rated by humans, or scored by an established readability model. The result may be a shift in the model's *judgments* rather than its outputs. It is therefore prior art for the steering mechanism, not evidence that a readability evaluation exists inside the model.

## 4.4 Where evaluation stands

The candidates are real and causal: emotion vectors shift preference, hidden valence shifts choice, the value axis shifts persistence. Three gaps define the research question. First, every signal is validated against correctness or experimenter-chosen traits, never against a quality like readability among solutions that all pass. Second, the one readability signal is measured only as self-report-style judgment shifts, which Section 3 shows are unreliable. Third, the value axis's terseness confound points opposite to the readability direction's comment-adding effect on comment density - a collision any readability readout must measure and control for.
