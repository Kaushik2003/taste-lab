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
Local cron, catch-up style. Cron calls the script every hour, and it runs once per day, the first time the
laptop is awake. It exits early if today's digest already exists, and a lock in `/tmp` stops two runs overlapping.
```bash
crontab -e
# hourly at :17
17 * * * * cd ~/Documents/research/taste-lab && PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin TASTE_LAB_ACCOUNT=laptop-scout ./scripts/scout.sh >> 00-inbox/scout.log 2>&1
```
Cron starts with a bare PATH, so the line adds `~/.local/bin`, where `claude` lives on this machine (`which claude`).
Keep `PATH=` and `TASTE_LAB_ACCOUNT=` after the `cd`: put in front of `cd`, they only apply to `cd` and never reach the script.

Or push to GitHub and run it as a scheduled cloud task that commits the digest. Ask Claude to set that up.

## Using multiple Claude accounts
The repo is the only memory shared across accounts (see "Session protocol" in `CLAUDE.md` and `00-inbox/HANDOFF.md`).
- Set `TASTE_LAB_ACCOUNT=<label>` (e.g. `personal`, `work`, `laptop-scout`) in `.env` or your shell so commits carry a
  `Session-Account:` trailer and you can tell later which account did what. `cp .env.example .env` to start;
  API keys for any future fetchers go there too. A value set in the shell or the cron line wins over `.env`.
- Keep `06-patterns/` and thread framing (promoting, killing, rewording threads) on your personal account.
  Other accounts can scout, ingest, and draft, but they don't set direction.

## Current state
- Threads: see `03-threads/` (T1 valence probe validity is the gating experiment)
- Experiment 01 spec: `04-experiments/exp01-valence-probe/spec.md`
- Reading queue: `00-inbox/reading-queue.md`
- Target: ICML 2027 workshop (~late May 2027)
