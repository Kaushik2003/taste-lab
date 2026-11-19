"""Set Obsidian graph color groups, forces, excluded files and property types.

Usage: python3 scripts/obsidian_graph_setup.py [vault_dir]   (default: repo root)
Close the graph view (or Obsidian) first, because Obsidian rewrites graph.json while it is open.
"""
import json, sys, pathlib

o = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent) / ".obsidian"

g = json.loads((o / "graph.json").read_text())


def c(q, hexs):
    return {"query": q, "color": {"a": 1, "rgb": int(hexs, 16)}}


# First match wins, so the most specific groups come first.
g["colorGroups"] = [
    c("tag:#role/threat", "e5484d"),        # papers that threaten the thesis
    c("path:03-questions", "f76b15"),         # open research questions
    c("path:04-experiments", "ffc53d"),
    c("tag:#type/landscape", "8e4ec6"),     # section hub notes
    c("path:02-concepts", "30a46c"),
    c("path:01-papers", "3e63dd"),
    c("path:06-patterns", "d6409f"),        # Harshit's layer
    c("path:00-inbox OR path:05-digests OR file:HOME", "8b8d98"),
]
g.update({"collapse-color-groups": False, "repelStrength": 12, "linkDistance": 220,
          "centerStrength": 0.5, "linkStrength": 1, "showArrow": False, "textFadeMultiplier": -1})
(o / "graph.json").write_text(json.dumps(g, indent=2))

a = json.loads((o / "app.json").read_text())
a["userIgnoreFilters"] = ["_templates/", "CLAUDE.md", "scripts/"]
(o / "app.json").write_text(json.dumps(a, indent=2))

(o / "types.json").write_text(json.dumps({"types": {
    "links": "multitext", "tests": "multitext", "components": "multitext",
    "tags": "tags", "aliases": "aliases"}}, indent=2))
print("ok")
