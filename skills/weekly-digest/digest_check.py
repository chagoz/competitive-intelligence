import re, sys, argparse
p = argparse.ArgumentParser()
p.add_argument("mode", choices=["sheet", "payload"])
p.add_argument("file")
p.add_argument("--topics", default="", help="topic names from the watch list, comma separated")
p.add_argument("--teams", default="", help="team names from the about-us file, comma separated")
p.add_argument("--sections", default="", help="section headings the payload must contain, separated by |")
a = p.parse_args()
t = open(a.file, encoding="utf-8").read()
err = []
def need(ok, msg):
    if not ok: err.append(msg)
for i, line in enumerate(t.splitlines(), 1):
    need(chr(8212) not in line, f"em dash on line {i}")
teams = [x.strip() for x in a.teams.split(",") if x.strip()]
topics = [x.strip() for x in a.topics.split(",") if x.strip()]
if a.mode == "sheet":
    need(re.search(r"^Window: .*\d{1,2}:\d{2}.* to .*\d{1,2}:\d{2}", t, re.M), "window line missing or not written as timestamps")
    for topic in topics:
        need(re.search(re.escape(topic), t, re.I), f"no line for topic '{topic}'")
    cands = re.split(r"^[A-Z]\. ", t, flags=re.M)[1:]
    for n, c in enumerate(cands, 1):
        for f in ["Event date:", "Score:", "Source:"]:
            need(f in c, f"candidate {n}: field '{f}' missing")
        need(re.search(r"Source: \[(Self-declared|Independent, verified)\].*https?://", c), f"candidate {n}: source needs origin tag and URL")
if a.mode == "payload":
    for h in [x.strip() for x in a.sections.split("|") if x.strip()]:
        need(h in t, f"section missing: {h}")
for s in re.findall(r"🌟 What's for us:?\s*(.+)", t):
    m = re.search(r"\(([^)]+)\), because", s)
    need(m and (not teams or m.group(1) in teams), f"What's for us line needs 'Action (Team), because proof' with a team from the list: {s[:60]}")
print("PASS" if not err else "FAIL\n- " + "\n- ".join(err))
sys.exit(1 if err else 0)
