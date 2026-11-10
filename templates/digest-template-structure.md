# Digest Template Structure

*The weekly digest page structure, section by section, with the reasoning behind each choice. Full formatting rules, the emoji system and the mandatory inline markers live in `language-guidelines.md`, Part 1 for system-wide and Part 2 for digest-specific voice. This document is the structural skeleton.*

---

## Page title

`Competitive Intelligence Digest #[N], [Date]`

*No em dashes, including in titles. Earlier digests used one and predate the rule.*

## Section order, with headers

| # | Section | Header |
|---|---|---|
| 1 | Opening subtitle | One line, grey italic, contextual emoji matching the week's theme |
| 2 | Three things to remember | `## 🎯 Three things to remember` |
| 3 | This week in AI | `## 🤖 This week in AI` |
| 4 | Regulation watch | `## 📊 Regulation watch` |
| 5 | Follow-up tracker | `## 🔍 Follow-up tracker` |
| 6 | Competitor pulse | `## 💥 Competitor pulse` |
| 7 | Opportunities | `## 💪 Opportunities` |
| 8 | Next week watch list | `## 🔍 Next week watch list` |
| 9 | Two closing lines | Grey italic |
| 10 | Credits line | Grey italic |

Seasonal editions add 🌲 to the opening subtitle rather than replacing a section header.

**Not every watch list topic gets its own section.** Topics 1 and 2 do, This week in AI and Regulation watch, because they are genuinely cross-cutting and company-agnostic, a reader shouldn't have to hunt through Competitor pulse to find them. Topics 3 and 4 (`watch-list.md`) are different in kind: a positioning shift or a friction removal is inherently about one company, so a finding surfaces naturally in that company's Competitor pulse entry, or in Three things to remember or Opportunities if it's strong enough to earn a slot. The topic pass still runs all four every week, per the digest skill's Step 3, this is about where a finding lands once found, not whether it gets looked for. Add a dedicated section only if a topic's findings start being genuinely cross-cutting rather than company-attributable.

**Section 2 is exactly three items and is called Three things to remember.** Not two, not four, and not renamed. If a quiet week genuinely yields only two, that is a signal about the week worth stating in the subtitle, not a reason to change the section.

**Section 4 is called Regulation watch.** Not Legislation watch. One name, so it is findable across editions.

## Inline markers, mandatory

*From `language-guidelines.md` Part 1. The single most commonly skipped part of the format.*

- Every competitor entry in the pulse carries both axes with both markers: `🔧 Implement · 🔴 High 4/5`.
- Every Follow-up tracker row carries its status and, where a verdict moved, the marker that moved.
- 🔥 on the sharpest signal of the week, highlighted sentence, followed by the So what for us callout.
- Quiet competitors get one grey line and no markers at all, because there is nothing to score.

A score written without its markers is unfinished. Check this last, before saving.

## Reasoning behind the order

Top 3 first because the fast reader (C-level) may read nothing else. AI and Regulation before Competitor Pulse because they are cross-cutting themes, not company-specific, and deserve their own scan pass rather than being buried inside a competitor's paragraph. Opportunities near the end but before the watch list, because it is the section the scanning reader (Product/Marketing) is actively hunting for, it needs to be findable without reading everything above it.

## What reads from what

- `language-guidelines.md` Part 1 for the emoji system, inline markers and all formatting. Part 2 for digest voice.
- `analysis-rules.md` for scoring, tier criteria, and the editorial gate
- The previous digest's follow-up tracker, to update status
- The latest monthly page, referenced and enriched, not restated in full
- The Competitor Profiles database, read rather than re-researched, and updated in the same session per the always-true rule

## When this is not the right shape

If findings consolidate around one topic with direct business consequences, this shape buries the point across eight sections. Use `templates/flash-report-template.md` instead.

---

*v3*
*v3 changes: added a note on where Topic 3 and 4 findings land, since `watch-list.md` grew to four topics after this document was last touched and only two of them had a named section. "Reality Check output" corrected to "the monthly page," the older document type this file hadn't caught up to. Header stamp removed, this file carried both a header and a footer stamp, the exact drift the one-stamp rule was written to stop.*
*v2 changes: emoji headers specified per section, which they previously were not in this document. Inline markers written in as mandatory. Section names fixed to one canonical form each after digest #9 drifted on two of them.*
