import re, sys, time, json, html, urllib.request
from pathlib import Path
ROOT = Path("/home/kzark/Documents/research/taste-lab")
OUT = Path(sys.argv[1])
paper = (ROOT/"1 Literature review"/"Literature review - full paper.md").read_text()
refs = paper.split("\n# References\n")[1]
ids = sorted(set(re.findall(r"arxiv\.org/abs/((?:\d{4}\.\d{4,5})|(?:cs/\d{7}))", refs)))
print("arxiv ids:", len(ids), flush=True)
def get(url, t=40):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research script)"})
    with urllib.request.urlopen(req, timeout=t) as r:
        return r.read().decode("utf-8", "ignore")
def strip(t):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<annotation.*?</annotation>", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", t)
log = {}
for n, i in enumerate(ids):
    safe = i.replace("/", "_")
    f = OUT/(safe + ".txt")
    if f.exists() and f.stat().st_size > 500:
        log[i] = "cached"; continue
    kind = "none"; text = ""
    try:
        page = get("https://arxiv.org/html/" + i)
        if "ltx_" in page and len(page) > 20000:
            body = page.split('class="ltx_bibliography"')[0]
            text = strip(body); kind = "full"
    except Exception as e:
        pass
    if kind == "none":
        try:
            page = get("https://arxiv.org/abs/" + i)
            m = re.search(r'citation_abstract" content="([^"]*)', page, re.S)
            if m: text = html.unescape(m.group(1)); kind = "abstract"
        except Exception as e:
            kind = "error"
    f.write_text(text); log[i] = kind
    if n % 10 == 0: print(n, i, kind, len(text.split()), flush=True)
    time.sleep(1.2)
(OUT/"_log.json").write_text(json.dumps(log, indent=1))
from collections import Counter
print(Counter(log.values()))
