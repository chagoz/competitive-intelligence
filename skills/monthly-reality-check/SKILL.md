---
name: monthly-reality-check
description: "Runs the company's monthly competitive reality check across two runs in one conversation: a research pass that verifies competitor claims against Layer 2 evidence on every profile at every tier, pulls the previous month's lost-deal data from the configured source and stops at the operator's gate, and a later write pass that produces the monthly page and 3 Slack post options. Trigger phrases: 'run monthly reality check', 'run reality check for [month]'. The research pass runs as a scheduled task on the cadence recorded in configuration.md, and ad hoc when triggered."
---

# Monthly Reality Check

## Two runs, one conversation

Route before reading anything else.

- This conversation holds a **confirmed** set of key learnings for the current period: this is a **write run**. Go to Phase 2.
- This conversation holds an **unconfirmed or partly confirmed** set: this is a **gate resume**. Go to the gate protocol in Phase 1, Step 9. Do not re-research.
- **Anything else, including any case not clearly one of the above:** treat it as still at the gate and ask. Ambiguity never resolves toward writing.
- Neither state exists at all: this is a **research run**. Go to Phase 1.

**Cadence lives in `configuration.md`, not here.** The research pass fires as a scheduled task and stops at the gate. The operator returns to the same conversation to confirm the top three, and the write run happens in the same thread.

**If `configuration.md` records a cadence that does not match how this run was triggered**, say so in the first line of the run and ask the operator to update the file. No skill configures itself.

**If the earlier conversation is gone**, do not scan cold. The profile writes made under §9 during the research run are the permanent record of what was found; rebuild the candidate set from them. State in one line that this is what happened.

**Human gate:** required, every run, both modes. Never skipped, in any permission mode including auto, and not even if the trigger message says "just run it."

**Why this is split.** The research pass is long and the write pass applies a different set of rules. A writing rule read at the start of a multi-hour research run is a rule that gets dropped by the time it is needed. Phase 2 re-reads the writing layer next to the work it governs.

---

## Phase 1, research and gate

### Read first, research lens only

- `about-us.md`, read first. It owns the theme watch list the matrix is built from, our regulation coverage status, the loss patterns that shape how a finding is read, the Product direction the bets pillar measures against, and the buyer archetypes whose documented frictions are standing research questions
- `analysis-rules.md`: §2 research schema, §2.1 recency filter and the window, §2.2 source honesty, §2.2.1 the absence bar, §2.5 corporate events, §2.6 the market lens, §2.8 the bets pillar, §2.9 archetype frictions, §7 the all-tier rule, §8 lost deal method, §9 the always-true rule
- `evidence-registry.md` for source types, priorities and cadences. **Addresses are not in this file.** They live in the Evidence Registry database
- `watch-list.md`, for the topic questions
- `configuration.md` for the Competitor Profiles database, the Evidence Registry database, the Competitor Employee List database, the Slack channel and the CRM lost-deal field names

**Do not read the writing files in this phase.** `monthly-review-template.md` and `language-guidelines.md` Part 3 are read in Phase 2, next to the work they govern.

**If a configuration value is missing, unconfirmed, or does not match the workspace:** search Notion by the name given in the file, show what you found, and ask the operator to confirm before writing anything. **Do not attempt to write to `configuration.md`.** Report the delta and ask the operator to update it by hand.

If any edit fails with "can't edit page on block with an archived ancestor," stop and flag it. Do not silently write elsewhere. This usually means the database title matched more than one page and the wrong one got confirmed.

If no lost-deal source is connected (§8) or the lost-deal fields are not set, skip the lost-deal pull entirely and say so explicitly in the output. Never fail the whole run over a missing pull.

### Step 1, set the period and name the blind spot

**Period:** the previous calendar month. This is a fixed reporting period, not the rolling window in §2.1, and the difference is deliberate: the monthly reports on a month a reader can name.

**The §2.1 blind-spot requirement still applies.** State in one line at the top of the candidate sheet: the period covered, and the gap between the end of the period and the day the research runs. Anything found in that gap is standing evidence on the profile, not a candidate for this month.

If the run covers more than one month's worth of time because a run was missed, say so in that same line.

### Step 2, research, Layer 2, all tiers

**The all-tier rule, §7.** Refresh the Layer 2 section on every competitor profile, every tier, not just Tier 1. Tier 1 keeps its full treatment on top. Lower tiers get, at minimum, a re-scan of their Layer 2 section against the source types in `evidence-registry.md` with the recency filter, plus a light glance at their orientation section.

Source types by priority order: Critical every cycle without exception, High unless time-constrained, Medium on a full pass. The quarterly types, positioning descriptor, review-site category, public company register, analyst coverage and supplier-facing surface, are checked on their own cadence rather than monthly.

Apply the recency filter per §2.1. Apply source honesty tags to every claim, origin and certainty, with a link when available. **Check the incentivized flag before citing any review count**; a vendor-solicited base is Self-declared, not Independent.

**Date traps.** Read the body dateline, not the page header. A "last updated" line on a review site is a page refresh. A review-site modified date is a CMS artifact and sort order is not reliably chronological. An image upload path is not a publication date.

### Step 3, the topic pass

Run the numbered questions in `watch-list.md`, "How to use this in the weekly digest", topic by topic. They are written for the digest and they work the same here, at a month's depth.

**Do not restate how many there are.** `watch-list.md` owns that list and its length changes.

### Step 4, archetype frictions, §2.9

Each buyer archetype in `about-us.md` carries a key friction evidenced from real users. For each one, ask whether this competitor has solved it, and look in the Layer 2 sources that would show it: onboarding articles in the help centre, the supplier-facing surface, the permission model, the invitation flow.

**A friction-solving move scores 4-5 on the same Axis 2 number**, not on a parallel score. Name the friction as the reason for the score. Frictions never become theme watches.

**Public user voice has a low ceiling in this category**, tested and confirmed absent rather than merely unmeasured. Reviewer role and company size stay usable where reviews exist. Do not spend a cycle re-establishing that buyers and suppliers here do not post publicly; the Evidence Registry carries it as a category-level finding.

### Step 5, absences, §2.2.1

**Absence is a finding, and it has to meet the bar before it is written as Confirmed.** Check whether the claim is bounded or unbounded before choosing how many paths it needs. One authoritative path is enough for a bounded claim; an unbounded one needs two, both named, with the scope written into the claim. A guessed URL returning 404 proves the guess was wrong, not that the thing is absent.

**Category-level absence beats company-level absence.** Where a source type turns out not to cover the category at all, record it once rather than per company.

### Step 6, corporate events and bets

**Corporate events, §2.5.** Funding, acquisition, partnership, integration, senior hire, ownership change and positioning changes are captured on the profile's Signal history table, typed, with an empty Grade. The recency filter applies to the reporting of an event, not to the event itself, so an older event is legitimate standing evidence with its own date.

**Bets, §2.8.** Where a competitor made a move that shows direction, record a bets reading on the profile. Bets reading shows on top-tier profiles by default, and a user setting extends it to all tiers: evidence class, conviction, and distance from us measured against the directions and non-goals in `about-us.md`. All three tags or the bet is excluded rather than shown partial. Where our own direction is silent, log the silence for Product rather than guessing. A bet landing on one of Product's open questions is flagged, not scored. **An excluded bet is recorded as excluded**, because a competitor whose direction cannot be evidenced is a finding about that competitor.

### Step 7, the rest of the research pass

**Employee scan.** Light scan of tracked employees' recent posts, dated within the cycle only. No rescoring; that is the six-month cadence in §5.

**Lost-deal pull.** Structured and free-text loss-reason fields named in `configuration.md`. It runs only when a lost-deal source is connected (§8). Query both meetings and calls objects for the period and sum them, dedup scheduling-tool pairs by datetime and title. Zero entries excluded, Unknown column always present. **Unattributed losses are not discarded**; they are read as buyer behaviour and feed the market lens.

**The market lens, §2.6.** A reading pass over evidence already collected, never its own scan. Four inputs: Tier 5 platforms and where their offer intersects ours, regulatory movement itself, unattributed losses read as buyer behaviour, and prospect-named companies we do not track.

Build the Theme Watch activity matrix in two blocks that never merge. Block one, our theme watches in the order `about-us.md` lists them. Block two, observed in the market, not ours, labelled as such. No promotion rule. The since-last-cycle column is read off the previous edition; nothing new is stored.

### Step 8, profile writes, through the write plan (§9)

Every discovery is one line in the write plan (§9), run at the end of this research pass, before and independently of the gate:

- The changelog at the top, with what changed and when
- The relevant evidence table row, not only a new Signal history line
- The positioning block, if the descriptor or boilerplate moved
- The Signal history table, for any corporate event or positioning change
- The bets reading, where one is now evidenced or now excluded
- The Talk/Implement property, if the evidence changes the picture
- Last updated

Property names are Talk/Implement and Threat score. **Threat scores are proposed, never set.** Record a proposed change in the Tier rationale and leave the property unchanged until the operator decides.

**The plan runs before the gate.** If the conversation is lost after this point, the profiles already hold the findings, and a fresh research pass recovers the sheet.

### Sufficiency check before the gate

Apply `analysis-rules.md` §10 before presenting the sheet: search execution, Fill the gate, Weight, and the monthly-only Trend condition. Trace any failure to its cause in order, setup then search execution then market, and state it with its cost. Do not report a quiet market until setup and search execution have passed.

### Step 9, the candidate sheet and the gate protocol

**This phase exists so the operator chooses. It is never abbreviated, never pre-decided, and never replaced by a finished selection.**

Open with the period and blind-spot line from Step 1. Then five key learning candidates, each with exactly six fields, nothing else:

- **Learning**, one line
- **Period position**, the dates the evidence carries and where they sit against the period
- **Score**, both axes, both markers, format `🔧 Implement · 🔴 High 4/5`
- **Why it matters**, one line on the business significance of the finding itself
- **Why this one**, one line making the editorial case for spending a slot on it. Name the specific hook: a theme watch struck, a documented archetype friction removed, a bets reading that changed, a lost-deal pattern confirmed, a claim sales can use
- **Source**, origin tag, link

**Why it matters and Why this one are different questions and are never merged.** The first is about the finding. The second is about the choice.

Then three short blocks, each present even when empty:

- **Proposed threat score changes**, or "none"
- **Registry and record corrections made**, or "none"
- **Configuration deltas**, or "none"

**Order is mechanical, by threat score, highest first.** That order is not a recommendation. Do not mark any candidate as recommended, preferred, or the obvious three. Do not present a pre-selected set for approval.

**Five candidates, with the reasoning both for and against each**, so the cut is a real choice rather than a rubber stamp. If fewer than five survive, say so explicitly as a finding about the month.

**The gate protocol.** Present the sheet and wait.

**The gate closes on one condition only: the skill has restated exactly three learnings, and the operator has agreed to that restatement.** Nothing else counts as confirmation.

- **Partial agreement** ("the first two are good"): still at the gate. Restate the full three with the settled two fixed and the third named as open, then ask the single question that resolves it.
- **Modification** ("swap the third for the Groundline ownership finding"): apply it, restate the resulting three, and treat a plain yes as confirmation. Do not return to research.
- **Silence or an unrelated reply**: still at the gate.
- **Anything unclear**: still at the gate. Ask. Never read ambiguity as confirmation.

**Ask at most one question per turn, the one that actually blocks progress.** Everything else becomes a default you have chosen, stated in one line each and flagged as changeable.

**If more than one conversation holds an unconfirmed set for the same period**, do not merge them. Name both and ask which is live.

Do not write the monthly page. Do not draft Slack options. Not in any permission mode, including auto.

---

## Phase 2, write, once the gate has closed

### Step 1, restate the confirmed three. First, before anything else.

Open the write run by restating the three confirmed learnings, in one line each, exactly as agreed.

This is the mis-route check. If the routing read the conversation wrongly, or a modification was applied that the operator did not intend, it is visible now, before a page exists.

### Step 2, re-read the writing layer. Blocking.

Read these now. Do not rely on anything read in Phase 1.

- `monthly-review-template.md`
- `language-guidelines.md`, Part 1 system-wide and Part 3 the monthly page, not Part 2
- `about-us.md`, the positioning vocabulary and the reader groups
- `slack-message-template.md`, at the moment of drafting the Slack options

**Before drafting anything, state each file read with its version stamp**, taken from the file's footer, which is the only stamp each file carries.

Example: `Writing layer read: monthly-review-template.md v1, language-guidelines.md v5, about-us.md v2.2.`

A version cannot be produced without opening the file, and it catches the failure nobody looks for, reading the right filename at the wrong version. A filename alone proves nothing and must not be written as if it does.

### Step 3, write the monthly page

One page per month, never a pair of sibling pages. It holds the review, the market lens section, and the working record inside a toggle. Structure: `monthly-review-template.md`. Voice: `language-guidelines.md` Part 3.

The working record carries what did not make the cut: the two unselected candidates with their reasoning, the lost-deal table, the Theme Watch matrix, coverage gaps, date traps found, and corrections made.

### Step 4, pre-flight. Against the payload.

Reproduce the pre-flight from `monthly-review-template.md` and the `language-guidelines.md` Part 1 checklist as a visible list, and tick each item **against the final write payload**, including anything composed during the write itself. Not against an earlier draft. Not from memory.

If any item is unchecked, the document is not finished.

### Step 5, write and read back

**After any write, fetch the page back and inspect the returned markdown before calling it done.** Notion markdown fails silently. After a write that coincided with a connection warning or a timeout, read the page back before retrying; a reconnect can land the same write twice.

### Step 6, distribution

Draft 3 Slack post options for the review, same mechanism as the digest, and log a Digest Impact Tracker row with the channel. Do not auto-post. A monthly document with no distribution does not get read, which is why this step is not optional.

---

## Sufficiency, trend condition

The trend check is the monthly-only condition of the sufficiency check (`analysis-rules.md` §10). If there is not enough reality check history for a genuine time comparison, do not stretch limited data into a trend. State how many reality checks exist and present current state rather than direction of travel. If a baseline is needed instead, run a dedicated fresh search against the topics in `watch-list.md`, topic by topic, and flag it as a separate step rather than compressing it into the same session.

---

## Gotchas

Real failures from past runs. Each one looked reasonable at the time.

- A reality check over a short history cannot show a trend. State how many periods exist, and do not stretch limited history into a trend.
- A claim that a competitor no longer does something needs the absence bar. One failed retrieval is evidence of a failed retrieval, not of absence.
- A bet missing one of its three tags is excluded, not shown partial.
- A lost-deal pull with no connected source is a line that says so, never a blank table.
- Profiles written before the gate are safe only through the write plan: one blocked line never holds the rest.
- A chip does not replace a sentence. A bare chip line tells the reader nothing.

## Check script

Run the script on the page before the write. It checks shape only. PASS means the shape is complete, not that the content is right.

```python
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
```

Command: `python3 monthly_check.py page.md --teams "[team names]" --sections "[section heading]|[section heading]"`

---

*v4*
*v4 changes: §10 sufficiency check added before the gate, covering search execution, Fill the gate, Weight and the monthly-only Trend condition. The former data-sufficiency gate renamed to the sufficiency trend condition, pointing to §10.*
*v3 changes: the research pass writes profiles through the write plan at its end, before the gate and without waiting for it. Bets reading is top tier by default and extendable by user setting. The lost-deal pull runs only when a lost-deal source is connected. Gotchas and the check script replace the do-not list.*
