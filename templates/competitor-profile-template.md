# Competitor Profile Template

*The structure for a competitor profile in the Competitor Profiles database. Full formatting syntax, the emoji system and the mandatory inline markers all live in `language-guidelines.md` Part 1.*

---

## Reader-facing vs internal

**The page body must contain nothing that only makes sense to the people building the system.** No form labels, no build scaffolding. Those are editorial notes for us, and to a reader they are noise. The form is obvious from the sections present. The one grey line the body opens with is the scan context, not a form label.

**Do not write a header table in the page body.** Category, Website, LinkedIn, AI-native, Tier and Tier rationale are database properties on the row. Reproducing them in the body puts the same facts in two places and they drift.

**No company name in a section heading.** A fork inherits this template unchanged, and a heading carrying our company name is a defect it would have to edit. Write "Where we win", not our own name.

---

## The date rule (the trust rule)

Too many dates is the single biggest thing that destroys trust in a profile. A reader cannot tell current from historical, so the whole page reads as stale.

- **One authority date per page.** The last-scan date, once, grey italic, in the footer. Nowhere else as a page-level date.
- **Every point inside a section leads with its own date**, where it has one. Date first, then what changed, then why.
- **No trailing date-summary lines.** A signal-history section ends on its last row, then the divider. Do not add a grey "nothing found in month X" line above the footer. It reads as a second, competing timestamp.
- **One exception, the Signal history table**, which uses ISO dates so it sorts and parses consistently.

---

## The title-pair rule (applies everywhere)

Wherever a bold title introduces a paragraph, the title sits on its own line and its text sits on the very next line with no blank line between them. A blank line (empty-block) separates one item from the next, never the title from its own text.

This one pattern governs: changelog items, reality-check verdicts, callout lines, the positioning block, and the good-at / falls-short bullets. Tight pairs, space between pairs.

In Notion-flavored markdown:
- Title line, then text line, with a normal newline between (renders tight).
- An empty-block tag on its own line between items (renders as the gap).
- Inside a quote block, use bold-title then a br tag then text so the whole verdict stays one block.

---

## The chip grammar

Origin, certainty and verdict are written as inline-code chips, not prose and not bare symbols. Because each chip is self-labelling, the table needs no legend above it.

- **Origin:** `Self-declared` or `Independent`. Plain word, no emoji.
- **Certainty:** `✅ Confirmed` · `🟠 Reported` · `◽ Inferred`. Emoji carries the degree at a glance.
- **Verdict:** `🗣️ Talk` or `🔧 Implement`.

A cell reads: `Self-declared` `✅ Confirmed`. Notion inline code renders these as neutral grey chips; the emoji carries the colour signal, since inline code cannot take a background colour.

---

## Full shape, Tier 1

Section order, each header carrying its emoji from the Part 1 table. **Reality check sits second, directly after the changelog**, because it is the core of the analysis. What-they-claim and what-they-actually-do are the supporting proof and come after it.

| # | Section | Header |
|---|---|---|
| 1 | What changed since the last scan | `## 🔄 Changelog since last scan` |
| 2 | The gap between claim and evidence | `## 🤷 Reality check` |
| 2b | Where they are going, top tier by default, extendable by user setting | `## 🗺️ Bets reading` |
| 3 | Their claims, Layer 1 | `## 🗣️ What they claim` |
| 4 | Verified evidence, Layer 2 | `## 🔧 What they actually do` |
| 5 | Our documented advantage | Green or blue callout, 💚 icon, **Where we win** |
| 6 | Our exposure | Yellow callout, ⚠️ icon, **Do not fight here** |
| 7 | Dated log | `## 📈 Signal history` |
| 8 | Open items | **Open questions**, bold heading, then grey text |

**Decision callouts.** A decision that waits on a human (a tier move, a threat change, a baseline revision) appears as a callout just below the changelog. Open: red background, 🚩 icon, title and text as one block, three lines at most. Closed: grey background, ✅ icon, with the closing line "✅ Closed [date]: [decision]. [Decider]'s decision." A closed callout stays one cycle, then moves to the Working record.

**Changelog.** Opens with a one-line grey italic scan-context note. Then the top 3 things that moved this cycle, each a title-pair led by its date (date, then what changed, then why). If nothing moved, carry the previous 3 forward. If important new things came in, those replace the weakest. Close with a grey italic baseline note (no new signal / threat unchanged) if applicable. This section tells a reader what is current, so it carries the most weight. For a Tier 2 to 4 profile, a new change counts as moved only if it clears the eventfulness bar (`analysis-rules.md` §1, set in `configuration.md`); a continued or escalating move already being tracked is not re-gated, and Tier 1 logs movement regardless.

**Reality check.** Each gap is an H3, with a blank line between H3s so it scans. Four elements under each header, in this order, and nothing else:

1. **One grey line naming the divergence.** One or two clauses. Not a claim paragraph and an evidence paragraph, the divergence itself. If it takes more than two clauses, the gap is not yet understood well enough to publish.
2. **One thesis line**, one sentence, saying what the gap means for the reader in plain words. It gives the reasoning in brief and does not restate the sources. If it needs more than one sentence, the gap is not yet understood well enough to publish.
3. **The sources, as labelled links carrying their chips.** `Self-declared` `✅ Confirmed` then the source name, linked. The chips carry origin and certainty, so the grey line never restates them in words.
4. **The verdict**, quote block, title-pair form: bold Verdict title, br tag, one clause of consequence.
5. Nothing else.

**Why this is short.** Every gap already carries its evidence in the chips and the link. Restating who said it, when, and how sure we are, in prose above a line that says exactly that, is duplication that makes the section unreadable. A reader who wants the detail opens the source.

**What does not belong here.** Speculation about why a competitor's documents disagree, unless it changes what a seller does. And any gap whose verdict is about the limits of our own evidence rather than about them, for example "unassessable rather than absent". Those are coverage limits and they go in Open questions.

**What they claim.** Opens with the positioning block, below. Then the claims table, latest item first. Columns: Claim/Signal, Source, Origin & certainty (chips), Verdict/Notes. Show the top 5 by date. Older rows go in a details/summary toggle ("Older claims"), table indented one tab inside. No legend above the table; the chips self-label.

**What they actually do.** Same table shape, Layer 2 evidence, "Older signals" toggle.

**Bets reading.** Shown on top-tier profiles by default. A user setting extends it to all tiers. Each bet carries the three tags defined in `analysis-rules.md` §2.8: evidence class, conviction and distance from us. A bet missing a tag is excluded, not shown partial. Distance is named in one clause, as §2.8 requires.

**Where we win.** Coloured callout (green or blue), 💚. Specific, documented advantages only, each a title-pair. Every line survives a rebuttal. Keep it coloured, it is the cheering-up moment.

**Do not fight here.** Yellow callout, ⚠️. Not optional on a Tier 1 profile. A profile with only wins is a sales sheet, not intelligence. Title-pairs.

**Working record.** Signal history is the audit record. It sits in a toggle at the bottom of the profile, titled by what is inside, and nothing is deleted when a profile is rewritten. Anything the body no longer shows moves there.

**Open questions.** Bold heading, then grey text. Never buried as plain grey with no heading.

**Tracked employees.** Via the relation. Do not duplicate as text.

---

## The positioning block

Opens the What they claim section, before the claims table. Three lines maximum, in title-pair form.

> **Positioning**
> Currently: [descriptor, verbatim]. Previously: [descriptor, verbatim], last seen [date].
> [One line of reading, only where there is a gap or a change.]

Line 2 carries both descriptors verbatim, never paraphrased, since the comparison is the point. Where the change date is a range rather than a date, write the range: "last seen as X in March 2024, first seen as Y in June 2026". Do not pick a midpoint. Press cadence is irregular and false precision here is worse than an honest range.

Line 3 appears only when there is something to read: a gap between the descriptor and the boilerplate, or a change since the last check. No change means two lines and nothing else. Never write "no change" as a third line.

**Two fields, two speeds.** The descriptor is the one-line self-category in the lede of a press release, "X, the leader in Y, today announced". It moves first. The boilerplate is the standing About paragraph at the foot of the release. It moves late, and only on a decision. The distance between them is the finding: a gap means a shift in progress, alignment means a shift completed or none at all.

**What is not captured.** Homepage headline, navigation structure, product names, review-site category. Tested and dropped in September 2026: a homepage headline moves for search optimisation rather than positioning, navigation and product names are not reliably archivable, and review-site category has no retrievable history. The review-site category is recorded in the Evidence Registry database as a present-state fact and reaches the profile only as a reading, never as a field.

**History.** A descriptor change is written to Signal history typed Positioning. The block says where they are now, the table says when it moved. Neither repeats the other.

---

## Signal history, all tiers

*The audit record. One table, most recent first, on every profile regardless of tier. Replaces the graded-bullet format used before September 4, 2026.*

| Date | Type | What happened | Grade | Source |
|---|---|---|---|---|
| 2026-08-19 | Acquisition | Acquired a carbon accounting platform | | `Self-declared` `✅ Confirmed` company newsroom |
| 2026-08-18 | Signal | Reviewers report the supplier portal could be more intuitive | 🔧 Implement | `Self-declared` `✅ Confirmed` G2 |

**Columns.**

*Date*, ISO format, most recent first. This is the exception to the prose date style elsewhere on the page, made so the table sorts and parses consistently.

*Type*, one of eight, closed: **Funding · Acquisition · Partnership · Integration · Senior hire · Ownership change · Positioning · Signal.** Signal is the catch-all for everything that is not a corporate event or a positioning change. Anything that does not fit one of the seven stays a Signal rather than earning a new type. Full definition: `analysis-rules.md` §2.5.

*What happened*, one clause. Not a paragraph. If it needs more, the detail belongs in the reality check or the changelog, not here.

*Grade*, `🗣️ Talk` or `🔧 Implement` with its marker. **Left empty on the seven non-Signal types**, which have no talk-versus-implement state. An empty Grade there is correct and complete, not an unfinished verdict.

*Source*, origin and certainty chips followed by the source name, linked where public.

**All tiers.** The medium form gains this section as its last standing section, same header, same table, same rules. Tier 5 is the single exception: two short paragraphs, no headers, so an event there is written into the prose.

**No trailing summary line.** The section ends on the last table row, then the divider.

---

## Medium form, Tier 2 to 4

Six sections, same beats as Tier 1 compressed to lines. No dual-axis scoring in the body (database properties carry it). No wins / ahead split; the essential version lives in section 4.

Opens with one grey italic scan-context line. No form label.

| # | Section | Header | What it holds |
|---|---|---|---|
| 0 | What changed since the last scan | `## 🔄 Changelog since last scan` | Same rule as Tier 1, compressed. One grey italic scan-context line, then up to three title-pairs led by their date, then the impact callout if there is one. |
| 1 | What they are | `## 🧭 What they are` | Orientation. Category, base, size or funding, who they sell to. One or two lines. Durable, light re-verify each cycle. |
| 2 | What they claim | `## 🗣️ What they claim` | The positioning block, then their positioning in their own words, source-tagged. One or two lines. |
| 3 | What's actually true | `## 🔧 What's actually true` | The Layer 2 outside view, dated, source-honesty tagged. Reality-check-owned, refreshed monthly for all tiers. If nothing this cycle: "No in-window signal, baseline only." in grey. |
| 4 | Where they touch us | `## ⚖️ Where they touch us` | Lead with the discovery in a title-pair (the key angle), then good-at and fall-short bullet blocks. The line a seller actually needs. |
| 5 | What would change the picture | `## ⚡ What would change the picture` | The escalation trigger, one concrete line. |
| 6 | Dated log | `## 📈 Signal history` | The same table as Tier 1. Added September 2026, because a corporate event at a Tier 2 or 4 company had nowhere to go. |

**The changelog is not optional on the medium form.** It was missing from v5 and earlier, so medium-form profiles carried their newest findings inside whichever section happened to fit. A reader could not tell what was current. Same section, same emoji, same rule as Tier 1, just shorter.

**Section 3 is reality-check-owned, all tiers, monthly.** Re-scanned against the source types in `evidence-registry.md` with the recency filter each cycle; the footer date moves. Sections 1, 2, 4, 5 change only on a real shift, though section 1 gets a light glance each cycle.

**Where they touch us structure.** Lead with the single sharpest read as a title-pair, for example "The threat is a price anchor, not feature parity." Then two labelled bullet blocks, **They are good at:** (short, incisive, but explanatory enough to be useful) and **Where they fall short:** (short, incisive).

**Callouts on medium form.** An escalation or gate note is a coloured callout at the very top: red background for an active escalation, yellow for a closed gate. Title-pair inside, condensed to the verdict plus the load-bearing facts only, three lines not five. The rest of the reasoning goes in the body, not the callout.

**Promotion rule.** A Tier 2 genuinely competing on our core drivers can earn the full Tier 1 template. Medium form is the floor, not a ceiling.

Tier 3 may use `## 🤝` for the partnership angle in place of section 5. Tier 5 gets two short paragraphs, no headers, and is read into the market lens rather than scored.

---

## Inline markers, mandatory

*From `language-guidelines.md` Part 1.*

- Every verdict chip in a table: `🗣️ Talk` or `🔧 Implement`.
- Every reality-check verdict line: same, in the quote block.
- Every Signal history row typed Signal carries its grade marker. The seven other types carry none, deliberately.
- Certainty chips wherever origin is given: `✅ Confirmed` · `🟠 Reported` · `◽ Inferred`.
- 🔥 on the sharpest signal, if there is one.
- 🚩 for a gate awaiting a human, ✅ once closed.
- 🗑️ on a retired entry, kept not deleted.
- Never an inline marker as a section header.

Threat scores are **not** restated in the page body. The database property and its chip colour carry them. Talk/Implement is restated in the body because it applies per claim.

---

## Two checks after every write, both reported

**These are different checks and passing one does not imply the other.** A page can render perfectly and still break every formatting rule the system has. That failure happened on September 4, 2026: a profile was read back, confirmed as rendered, and shipped carrying a 600-word unstructured changelog, no grey scan line, no colour register and section emoji used as prose prefixes.

**Check one, does it render.** Notion markdown fails silently: a bad block type writes "successfully" but renders as raw text. After any write that includes a toggle, callout, table, chip or column, **fetch the page back and inspect the returned markdown before calling it done.** Look for escaped tags, orphaned summary lines, runaway indentation, or a span wrapped around a link, which splits into several spans.

**Check two, does it comply.** Run the pre-flight in `language-guidelines.md` Part 1 against what came back, and **state which items passed rather than asserting the page is done.** The items that get skipped most: grey italic on every subtitle and legend line, inline markers everywhere the list requires them, a section emoji on every header and never an inline marker, two-axis scores shown together with both markers, and no em dashes.

**After a write that coincided with a connection warning or a timeout, read the page back before retrying.** A reconnect can land the same write twice, and a timeout is not proof that nothing was written.

---

*v10*
*v10 changes: a continued or escalating tracked move is not re-gated by the eventfulness bar.*
*v9 changes: wire the eventfulness bar, a Tier 2 to 4 competitor's change is reportable only when it clears the bar in `configuration.md`, defined in `analysis-rules.md` §1.*
*v8 changes: reality check gains one thesis line per gap, in option C form. Decision callouts added, red when open and grey when closed. Bets reading added as an optional section, top tier by default and extendable by user setting, using the tags in analysis-rules.md §2.8. Signal history moves to a Working record toggle. The At a glance brief and the reader model are not yet in this template and are logged for later.*
*v7 changes: the medium form gains the changelog as a standing section, numbered 0 so the existing section numbers do not shift. It was already present on live medium-form profiles and absent from the template, which is the wrong way round for a rule.*
*v6 changes: the Reality check rule cut to four elements, one grey line naming the divergence, chipped source links, a one-clause verdict and nothing else, after a rehearsal showed the prose claim-and-evidence lines duplicated what the chips and links already carried. Coverage limits and speculation moved out to Open questions. The rendering checklist split into two checks, renders and complies, with the compliance pre-flight reported item by item rather than assumed, after a profile shipped rendering correctly and breaking most of the formatting rules.*
*v5 changes: Signal history became one table on every profile, all tiers, with a closed eight-value Type column carrying corporate events and positioning changes, and an empty Grade on the seven non-Signal types. Positioning block added to What they claim, two press fields with the gap between them as the finding. Section 5 renamed from a company-specific name to "Where we win", so a fork does not inherit our name as a heading. Medium form gained Signal history as a sixth section. Read-back rule extended to cover timeouts.*
*v4 changes: one-date trust rule; title-pair rule; chip grammar; reality check moved to second position; top-5 tables with older rows in a toggle; certainty chips; reader-facing vs internal rule; good-at / fall-short structure; rendering checklist.*
*v3 changes: Short shape replaced by five-section Medium form.*
*v2 changes: header table removed from body. Emoji headers per section. Inline markers mandatory.*
