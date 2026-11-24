#!/usr/bin/env python3
"""Draw Figure 1 of the literature review: the loop of four steps."""
from pathlib import Path
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "1 Literature review" / "figures" / "loop.png"
INK, SOFT, FILL, BAND = "#1f2933", "#52606d", "#f4f6f8", "#e4e9ee"

steps = [
    ("Monitor", "reads its own states", "Probes read the signals; the model acts on its confidence", "The model's own verbal report"),
    ("Evaluate", "judges good or bad", "Valence and value signals move choices", "A criterion that is the model's own"),
    ("Control", "steers its reasoning", "Meta-level control of reasoning", "Control by the model's own evaluation"),
    ("Persist", "writes to its weights", "Learned memory; direct edits", "A hidden-state signal that decides; a check of what changed"),
]

fig, ax = plt.subplots(figsize=(11, 5.6), dpi=200)
ax.set_xlim(0, 11); ax.set_ylim(0, 5.6); ax.axis("off")

def box(x, y, w, h, fc):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec=INK, lw=1.1))

def wrap(s, n):
    return "\n".join(textwrap.wrap(s, n))

# self-model band
box(0.4, 4.55, 10.2, 0.8, BAND)
ax.text(0.6, 5.08, "Self-model", fontsize=11, fontweight="bold", color=INK, va="center")
ax.text(2.0, 5.08, "predicts the effect of a change before the model makes it", fontsize=9.5, color=INK, va="center")
ax.text(0.6, 4.75, "Shown: trained prediction of one's own behavior.", fontsize=8.5, color=SOFT, va="center")
ax.text(4.9, 4.75, "Missing: prediction of a change to oneself", fontsize=8.5, color=SOFT, va="center", style="italic")

w, h, y0 = 2.25, 2.35, 1.65
xs = [0.4, 3.05, 5.7, 8.35]
for x, (name, sub, shown, missing) in zip(xs, steps):
    box(x, y0, w, h, FILL)
    ax.text(x + w / 2, y0 + h - 0.28, name, fontsize=12, fontweight="bold", color=INK, ha="center", va="center")
    ax.text(x + w / 2, y0 + h - 0.58, sub, fontsize=9, color=INK, ha="center", va="center")
    ax.plot([x + 0.15, x + w - 0.15], [y0 + h - 0.78, y0 + h - 0.78], color=SOFT, lw=0.6)
    ax.text(x + 0.14, y0 + h - 0.92, wrap("Shown: " + shown, 27), fontsize=8.3, color=SOFT, va="top")
    ax.text(x + 0.14, y0 + 0.72, wrap("Missing: " + missing, 27), fontsize=8.3, color=SOFT, va="top", style="italic")
for a, b in zip(xs[:-1], xs[1:]):
    ax.add_patch(FancyArrowPatch((a + w + 0.03, y0 + h / 2), (b - 0.03, y0 + h / 2), arrowstyle="-|>", mutation_scale=16, lw=1.4, color=INK))
# return arrow: the changed model is monitored again
ax.add_patch(FancyArrowPatch((xs[3] + w / 2, y0 - 0.03), (xs[0] + w / 2, y0 - 0.03), connectionstyle="bar,fraction=-0.055",
                             arrowstyle="-|>", mutation_scale=16, lw=1.4, color=INK))
ax.text(5.5, 1.22, "the changed model is monitored again", fontsize=8.8, color=INK, ha="center", va="center",
        bbox=dict(fc="white", ec="none", pad=1.5))

# anchor band
box(0.4, 0.15, 10.2, 0.75, BAND)
ax.text(0.6, 0.66, "Anchor", fontsize=11, fontweight="bold", color=INK, va="center")
ax.text(1.55, 0.66, "a check outside the loop", fontsize=9.5, color=INK, va="center")
ax.text(0.6, 0.34, "Shown: tests, proof checkers, sealed audits, frozen weights.", fontsize=8.5, color=SOFT, va="center")
ax.text(5.6, 0.34, "Missing: a check that protects the monitor itself", fontsize=8.5, color=SOFT, va="center", style="italic")

OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", facecolor="white")
print("wrote", OUT)
