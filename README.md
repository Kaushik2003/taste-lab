# taste-lab

A research repo for **self-originated taste in reasoning models**: metacognition, valence, and self-directed
weight updates. You and Claude work in it together. Plain markdown + git, so it opens in Obsidian or works fine without it.

## Setup (10 min)

```bash
# 1. put it somewhere and make it a repo
cd ~/research && unzip taste-lab.zip && cd taste-lab
git init && git add -A && git commit -m "init taste-lab"

# 2. Claude Code (if not installed)
npm install -g @anthropic-ai/claude-code
claude            # run once in this folder to log in; it auto-reads CLAUDE.md

# 3. optional: open the folder as an Obsidian vault for graph view + wikilinks

# 4. test the paper fetcher (no dependencies, Python 3.9+)
python3 scripts/fetch_arxiv.py --days 7
```

## The loop

**Daily (Claude, automated, ~5 min of your time)**
1. `scripts/scout.sh` runs on cron → fetches new arXiv papers matching `research.yaml` → Claude triages
   → writes `05-digests/YYYY-MM-DD.md` + drafts notes for papers that score ≥2.
2. You read the digest (top 3 + a surprise pick + one question for you). Reply by jotting in `06-patterns/`.

**When you study (you)**
- `/explain <concept>` makes Claude tutor you on something, grounded in the notes.
- Write your own intuitions in `06-patterns/`, rough. This is where your human pattern-finding goes.
  Claude reads it and points its scouting there, but never edits it.

**Weekly (together, ~1 hr)**
- `/weekly` → Claude synthesizes the week, updates thread statuses, proposes next actions.
- `/connect` → non-obvious links across papers/concepts/your patterns.
- `/critique <thread>` → red-team before you commit compute to anything.
- You promote/kill threads and pick the next experiment.

## Division of labor
| Claude is better at | You are better at |
|---|---|
| reading 50 abstracts/day | noticing which one *matters* |
| summarizing, linking, deduping | taste: picking the bet |
| red-teaming, finding counter-evidence | weird cross-domain analogies (games, art, building) |
| writing experiment boilerplate | deciding what result would change your mind |
| keeping the "what would kill this" list honest | ambition |

## Automating the scout
Local cron (laptop must be awake):
```bash
crontab -e
# every day 8:17am
17 8 * * * cd ~/research/taste-lab && ./scripts/scout.sh >> 00-inbox/scout.log 2>&1
```
Or push to GitHub and run it as a scheduled cloud task that commits the digest. Ask Claude to set that up.

## Current state
- Threads: see `03-threads/` (T1 valence probe validity is the gating experiment)
- Experiment 01 spec: `04-experiments/exp01-valence-probe/spec.md`
- Reading queue: `00-inbox/reading-queue.md`
- Target: ICML 2027 workshop (~late May 2027)
