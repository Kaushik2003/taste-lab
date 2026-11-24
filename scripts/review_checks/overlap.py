import re, sys, json
from pathlib import Path
ROOT = Path("/home/kzark/Documents/research/taste-lab")
SRC = Path(sys.argv[1]); N = int(sys.argv[2]) if len(sys.argv) > 2 else 8
paper = (ROOT/"1 Literature review"/"Literature review - full paper.md").read_text()
body = paper.split("\n# References\n")[0]
body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
def toks(t):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", t.lower().replace("’", "'"))
bt = toks(body)
# positions of words that sit inside double quotes in the review (quoted material is allowed)
quoted = set()
pos = 0
for part_i, part in enumerate(re.split(r'"', body)):
    n = len(toks(part))
    if part_i % 2 == 1:
        quoted.update(range(pos, pos + n))
    pos += n
grams = {}
for i in range(len(bt) - N + 1):
    grams.setdefault(tuple(bt[i:i+N]), []).append(i)
log = json.loads((SRC/"_log.json").read_text()) if (SRC/"_log.json").exists() else {}
hits = {}   # review position -> source
per_src = {}
for f in sorted(SRC.glob("*.txt")):
    st = toks(f.read_text(errors="ignore"))
    seen = set()
    for j in range(len(st) - N + 1):
        g = tuple(st[j:j+N])
        if g in grams:
            for i in grams[g]:
                seen.add(i)
    if seen:
        per_src[f.stem] = seen
        for i in seen: hits.setdefault(i, f.stem)
covered = set()
for i in hits:
    covered.update(range(i, i + N))
unq = covered - quoted
print("review words:", len(bt), "| sources:", len(list(SRC.glob('*.txt'))), "| full text:", sum(1 for v in log.values() if v in ("full","cached")), "| abstract only:", sum(1 for v in log.values() if v == "abstract"))
print("%d-word sequences shared with a source: %d of %d (%.2f%%)" % (N, len(hits), len(bt)-N+1, 100*len(hits)/(len(bt)-N+1)))
print("review words inside a shared sequence: %d (%.2f%%); outside quotation marks: %d (%.2f%%)" % (len(covered), 100*len(covered)/len(bt), len(unq), 100*len(unq)/len(bt)))
# passages: merge consecutive positions
starts = sorted(hits)
passages = []
cur = None
for i in starts:
    if cur and i <= cur[1] + 1 and hits[i] == cur[2]:
        cur[1] = i
    else:
        if cur: passages.append(cur)
        cur = [i, i, hits[i]]
if cur: passages.append(cur)
passages.sort(key=lambda p: -(p[1]-p[0]))
print("passages:", len(passages))
for a, b, s in passages[:int(sys.argv[3]) if len(sys.argv) > 3 else 40]:
    words = bt[a:b+N]
    q = sum(1 for k in range(a, b+N) if k in quoted)
    print("%3d words | %s | %s%s" % (len(words), s, " ".join(words)[:230], "  [in quotes]" if q > len(words)*0.6 else ""))
