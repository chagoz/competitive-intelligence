import re, sys, argparse
p = argparse.ArgumentParser()
p.add_argument("file")
p.add_argument("--teams", default="", help="team names from the about-us file, comma separated")
p.add_argument("--sections", default="", help="section headings the page must contain, separated by |")
a = p.parse_args()
t = open(a.file, encoding="utf-8").read()
err = []
def need(ok, msg):
    if not ok: err.append(msg)
for i, line in enumerate(t.splitlines(), 1):
    need(chr(8212) not in line, f"em dash on line {i}")
for h in [x.strip() for x in a.sections.split("|") if x.strip()]:
    need(h in t, f"section missing: {h}")
teams = [x.strip() for x in a.teams.split(",") if x.strip()]
for s in re.findall(r"🌟 What's for us:?\s*(.+)", t):
    m = re.search(r"\(([^)]+)\), because", s)
    need(m and (not teams or m.group(1) in teams), f"What's for us line needs 'Action (Team), because proof' with a team from the list: {s[:60]}")
for line in t.splitlines():
    if re.search(r"^\*\*Bet[^*]*\*\*", line):
        need(all(k in line for k in ["Evidence class", "Conviction", "Distance"]), f"bet missing a tag: {line[:60]}")
print("PASS" if not err else "FAIL\n- " + "\n- ".join(err))
sys.exit(1 if err else 0)
