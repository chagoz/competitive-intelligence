---
name: weekly-digest
description: "Runs the company's weekly competitive intelligence digest across two runs in one conversation: a research and scoring pass that stops at the operator's gate, and a later write pass that produces the Notion page and 3 Slack post options, then logs analytics after posting. Also decides when findings warrant a Flash Report instead. Trigger phrases: 'run competitive digest', 'run this week's digest', 'weekly digest for [week]'. The research pass runs as a scheduled task on the cadence recorded in configuration.md, and ad hoc when triggered."
---

# Weekly Competitive Digest

## Two runs, one conversation

Route before reading anything else. The routing is the same in every skill: confirmed set, write run; unconfirmed set, gate resume; anything else, research run or still at the gate.

- This conversation holds a **confirmed** candidate set for the current window: this is a **write run**. Go to Phase 2.
- This conversation holds an **unconfirmed or partly confirmed** candidate set: this is a **gate resume**. Go to the gate protocol in Phase 1, Step 10. Do not re-research.
- **Anything else, including any case not clearly one of the above:** treat it as still at the gate and ask. Ambiguity never resolves toward writing.
- Neither state exists at all: this is a **research run**. Go to Phase 1.

**Cadence lives in `configuration.md`, not here.** The research pass fires as a scheduled task and stops at the gate. The operator returns to that same conversation to confirm the three, and the write run happens in the same thread. The page is dated the day it is written, not the day it was researched.

**If `configuration.md` records a cadence that does not match how this run was triggered**, say so in the first line of the run and ask the operator to update the file. No skill configures itself.

**If the earlier conversation is gone**, run a fresh research pass. Do not rebuild the sheet from the profiles. State in the first line of the run that the earlier sheet was not carried over, so the reader knows the candidates come from new research.

**Human gate:** required, every run, both modes. Never skipped, in any permission mode including auto, and not even if the trigger message says "just run it."

---

## Phase 1, research and gate

### Read first, research lens only

- `about-us.md`, read first. It is the lens every signal is judged through. It owns the theme watch list the threat axis scores against, and the buyer archetypes whose documented frictions raise that same score per `analysis-rules.md` §2.9
- `analysis-rules.md`
- `competitor-list.md`
- `watch-list.md`
- `configuration.md`, for the Competitive Intelligence home page title and the Slack channel

**Do not read the writing files in this phase.** They are read in Phase 2, next to the work they govern. A writing rule read hours before it is applied is a rule that gets dropped.

**If a configuration value is missing, unconfirmed, or does not match the workspace:** search Notion by the name given in the file, show what you found, and ask the operator to confirm before proceeding. If the search returns nothing, stop and name the field in `configuration.md` and the exact title you searched for, rather than running thin on a missing resource. **Do not attempt to write to `configuration.md`.** Report the delta and ask the operator to update it by hand. Never fetch a Notion page by a remembered ID.

### Step 1, set the window

Set the window per `analysis-rules.md` §2.1. It runs from where the previous window ended to the moment this run starts, so read the previous digest's window before assuming a Tuesday to Monday shape.

State in one line at the top of the candidate sheet: the window, and the blind spot between the end of the window and publication, per the §2.1 requirement that a split process names it rather than letting a reader assume the window runs to the publication date.

If the run covers more than one window's worth of time, say so in that same line.

### Step 2, orientation

1. Search existing digests under the Competitive Intelligence home page to find the correct next digest number.
2. Read the most recent monthly page for the current truth baseline. Do not scan competitors cold if a recent reality check exists.
3. Read the previous digest's "Next week watch list" as follow-up entry points.

### Step 3, topic pass. Before any company scan.

Run the numbered questions in `watch-list.md`, "How to use this in the weekly digest", topic by topic. Record each finding with its event date before opening a single competitor page.

**Do not restate how many there are.** `watch-list.md` owns the topic list and its length changes; the cap is five with a seat deliberately open. A count written here is a second copy of something another file owns, and it goes stale silently.

**This runs first, deliberately.** A company-by-company scan sets the week's agenda by whoever happened to publish. The topic pass asks what moved on the things we care about, which is the question the digest exists to answer.

### Step 4, company scan

Scan Tier 1 always, even if quiet. Scan Tier 2 to 4 only if genuinely eventful, per the gate-keeper rule in `analysis-rules.md` §1.

The company scan answers what each competitor did about the topics from Step 3. It does not set the agenda by itself.

### Step 5, recency gate. Before scoring, not after.

Every finding is written with its event date next to the window before it is scored, and tested against §2.1, including the first-public-disclosure carve-out. A disclosure that is new today is in window for what it discloses even when the underlying work is old.

Anything failing that test **cannot be a candidate for the top three**. It becomes a follow-up tracker row or standing evidence on the profile, and the finding says which.

### Step 6, score

Score every surviving finding on both axes, Talk/Implement and Threat, per §3. Apply source honesty tags per §2.2, with a date and a link on every Layer 2 claim.

**A finding that removes a friction documented in the buyer archetypes scores 4-5**, per §2.9. The friction raises the single Axis 2 number rather than creating a second score, so the sheet still has exactly one figure to order on. Name the friction as the reason for the score, in the same line that carries it.

### Step 7, profile writes, through the write plan (§9)

**Every profile change in this step is one line in the write plan (§9):** the profile, the section, the new text, its origin and certainty tags, and its event date. The plan runs at the end of the research pass, before the gate and without waiting for the selection. A line that fails verification leaves the plan. A blocked line is reported, and it never holds the rest.

**Any corporate event found is one line in the write plan**, typed per §2.5 and written to the competitor's Signal history when the plan runs. Exempt from the gate.

**Any company named by a prospect that we do not track triggers a profile setup run**, per §1, regardless of the tier outcome. A single mention in passing makes a company a profile, not a tier.

**Any absence written to a profile meets the bar in §2.2.1 first.** Check whether the claim is bounded or unbounded before choosing how many paths it needs, name the paths in the finding, and record as Reported rather than Confirmed where the bar is not met.

### Step 8, format decision

Digest or Flash Report, decided here and stated to the operator with the candidates.

A Flash Report replaces the numbered digest when **all three** are true: the findings consolidate around one question rather than spreading across competitors, the question has a live business consequence, and the research is mission-depth rather than a weekly scan. If only the first is true, it stays a weekly digest with a strong lead story. A Flash Report is named, not numbered, and does not break the weekly sequence.

### Step 9, the candidate sheet. Fixed format, never skipped.

**This phase exists so the operator chooses. It is never abbreviated, never pre-decided, and never replaced by a finished selection.**

Open with the window and blind-spot line from Step 1. Then the candidates, each with exactly six fields, nothing else:

- **Claim**, one line
- **Event date**, and its position against the window
- **Score**, both axes, both markers, format `🔧 Implement · 🔴 High 4/5`
- **Why it matters**, one line on the business significance of the signal itself
- **Why this one**, one line making the editorial case for spending a slot on it: what it gives a reader that the other candidates do not. Name the specific hook, an escalated follow-up, an open OKR, a live deal, a theme watch struck, a documented archetype friction removed, a claim sales can use this week
- **Source**, origin tag, link

**Why it matters and Why this one are different questions and are never merged.** The first is about the signal. The second is about the choice. A signal can matter and still be the wrong use of one of three slots, and that judgement is the operator's to make with the argument in front of them.

Then two short blocks, each present even when empty:

- **Escalated follow-ups**, or "none this window"
- **Configuration deltas**, or "none"

**How many candidates.** More than there are slots, always, so there is a real choice. Present four or five where four or five survive the recency gate. **If fewer than four survive, say so explicitly as a finding about the window**, and present what there is. Never pad the list with signals that failed Step 5 in order to reach a count.

**Order is mechanical, by threat score, highest first.** That order is not a recommendation. Do not mark any candidate as recommended, preferred, the lead or the obvious three. Do not present a pre-selected top three for approval. The selection is the operator's and the sheet's job is to arm it.

No preamble, no methodology, no narrative, no partial page. This sheet is a decision document for one reader choosing three things. Completeness is the wrong default for it.

**Run the sufficiency check before the gate.** Apply `analysis-rules.md` §10: search execution, Fill the gate and Weight. Trace any failure to its cause in order, setup then search execution then market, and state it with its cost. The "fewer than four candidates" line above is the Fill the gate condition; do not report a quiet market until setup and search execution have passed.

### Step 10, the gate protocol

Present the sheet and wait.

**The gate closes on one condition only: the skill has restated exactly three items, and the operator has agreed to that restatement.** Nothing else counts as confirmation.

- **Partial agreement** ("the first two are good"): still at the gate. Restate the full three with the settled two fixed and the third named as open, then ask the single question that resolves it.
- **Modification** ("swap the third for Groundline"): apply it, restate the resulting three, and treat a plain yes as confirmation. Do not return to research, and do not treat a modification as a rejection.
- **Silence or an unrelated reply**: still at the gate. Do not proceed.
- **Anything unclear**: still at the gate. Ask. Never read ambiguity as confirmation, and never resolve it in the direction that lets the run continue.

**Ask at most one question per turn, the one that actually blocks progress.** Everything else becomes a default you have chosen, stated in one line each and flagged as changeable.

**If more than one conversation holds an unconfirmed set for the same window**, do not merge them. Name both and ask which is live.

Do not write the Notion page. Do not draft Slack options. Not in any permission mode, including auto.

---

## Phase 2, write, once the gate has closed

### Step 1, open with the confirmed three and the writing-layer versions. First, before anything else.

The write run's first output is one opening block with two parts, in this order: the three confirmed items restated in one line each, exactly as agreed, then the writing-layer versions line from Step 2. Nothing is drafted, asked or reported before this block is complete.

Producing the versions line requires the Step 2 reads, so do those reads first, silently; the opening block is still the run's first output. A write run that opens with the three picks but no versions line has skipped Step 2 and must stop and complete the block before going on.

This is the mis-route check and the audit stamp in one place. If the routing read the conversation wrongly, or a modification was applied that the operator did not intend, it is visible now, before a page exists, rather than after it is published. And every run states which rule and template versions produced it, so a bad page can be traced to the files that shaped it.

### Step 2, re-read the writing layer. Blocking.

Read these now. Do not rely on anything read in Phase 1.

- `language-guidelines.md`, Part 1 system-wide and Part 2 Weekly Digest, not Part 3
- `digest-template-structure.md`
- `about-us.md`, the positioning vocabulary and the reader groups
- `templates/flash-report-template.md`, only if that format was chosen at the gate

**State each file read with its version stamp in the Step 1 opening block**, taken from the file's own footer. Where a file carries no version, give its Last updated date.

Example: `Writing layer read: language-guidelines.md v5, digest-template-structure.md v2, about-us.md [version].`

A version cannot be produced without opening the file, and it catches the failure nobody looks for, reading the right filename at the wrong version. A filename alone proves nothing and must not be written as if it does.

### Step 3, closing-line context

Ask once: "Before I write the closing lines, anything specific from this week I should connect to? Office mood, weather, something that happened, a running joke?"

**If it goes unanswered by the time the page is otherwise ready**, draw the closing lines from the window's sharpest signal, state in one line that this is what you did, and continue. Do not hold the page waiting for it.

**The What's for us line** is written only when the user has switched it on in settings. It is off by default. When it is on, it follows the shape in the Slack template, and the human confirms its action at the gate.

### Step 4, draft

**Page title:** `Competitive Intelligence Digest #[N], [Date]`, the date of writing. No em dash, anywhere, including the title.
**Save under:** the Competitive Intelligence home page, title confirmed in `configuration.md`.

**Structure, in order:** opening subtitle, Three things to remember (the confirmed set), This week in AI, Regulation watch, Follow-up tracker, Competitor pulse, Opportunities, Next week watch list, two closing lines, credits line. Section by section: `digest-template-structure.md`.

The opening subtitle carries the window and the blind spot, per §2.1.

### Step 5, pre-flight. Against the payload.

Reproduce the formatting pre-flight from `language-guidelines.md` Part 1 as a visible list and tick each item **against the final write payload**, including anything composed during the write itself. Not against an earlier draft. Not from memory.

This is where the em dash scan, the inline markers, the grey italic subtitles, the visual legends, the two-axis displays and the source honesty tags are each checked one at a time.

If any item is unchecked, the document is not finished.

### Step 6, write and read back

**After any write that includes a toggle, callout, table or chip, fetch the page back and inspect the returned markdown before calling it done.** Notion markdown fails silently. After a write that coincided with a connection warning or a timeout, read the page back before retrying; a reconnect can land the same write twice.

---

## Slack post options

**Read `slack-message-template.md` now**, at the moment of drafting, and state its version, for the same reason Phase 2 Step 2 does.

Generate 3 options for the channel confirmed in `configuration.md`. Channel choice is editorial and varies by edition, so record where it actually went.

Format: `📡 Weekly Competitor Digest #[N], [Date]`, then 3 bullets (what they did plus what it means for us, one sentence, second part four words max), then `Read more → [Notion link]`, then a closing line in one of three registers, cult quote, fake kung fu master, or absurdist, calibrated to the window's sharpest signal. Do not repeat a register two weeks running.

Do not auto-post. Present the 3 options and let the operator choose.

---

## Analytics, after the Slack post is live

1. Search the configured Slack channel for the digest post.
2. Pull total reactions with emoji breakdown, thread reply count, timestamp.
3. Log to the Digest Impact Tracker database, including the Channel field.
4. Prompt the operator to add Notion view counts at 24h and one week. Notion does not expose page views through its API, so those fields are manual entry only. Never guess them.

---

## Gotchas

Real failures from past runs. Each one looked reasonable at the time.

- A guessed address that returns not found proves the guess was wrong, not that the page is absent. Record an absence only after the registered address has been checked.
- An old event promoted now is not an in-window event. Test its event date before scoring it.
- Topic questions dissolve into a company scan unless the coverage check makes them visible. Run the topic pass before any company scan.
- A research fetch can blend in text that is not on the source page. Only a quote with its URL reaches the sheet.
- One source's date is not an official date. Use the official publication, or two independent sources.
- A window that ends on a date loses the rest of that day. Record window ends as timestamps.
- One blocked write is one blocked write. Report it, and let the remaining lines run.
- A candidate that fails the recency test cannot be in the top three, however strong it looks.
- A single mention in passing makes a company a profile, not a tier.
- A louder namesake can own the search results for a tracked name. Carry the identifier in the query, and tie each finding to the domain or registration number before it is used (§2.2.2).

## Check script

Run the script on the sheet before the gate and on the page before the write. It checks shape only. PASS means the shape is complete, not that the content is right.

```python
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
```

Command, sheet: `python3 digest_check.py sheet sheet.txt --topics "[topic names]" --teams "[team names]"`
Command, page: `python3 digest_check.py payload page.md --teams "[team names]" --sections "[section heading]|[section heading]"`

---

*v6*
*v6 changes: the write run opens with one block carrying the confirmed three and the writing-layer versions line, per eval-set S4.1. The versions statement moves from a before-drafting rule in Step 2 to part of the run's first output in Step 1.*
*v5 changes: title-lookup recovery, a configured title that finds nothing stops and names the field and the searched value, matching configuration.md.*
*v4 changes: §10 sufficiency check added before the gate, covering search execution, Fill the gate and Weight.*
*v3 changes: profile writes move to the write plan at the end of the research pass, without a gate. Route-first is stated in every skill. A fresh research pass replaces rebuilding the sheet from profiles. Gotchas and the check script replace the do-not list. The What's for us line is optional and off by default.*
