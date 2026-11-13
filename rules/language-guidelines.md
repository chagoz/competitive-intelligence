# Language Guidelines

*How every Competitive Intelligence document is written and formatted. Apply without exception.*

*This file owns craft: voice, structure, formatting, the emoji system, inline markers, words to avoid. It does not own positioning. Which words carry the company's position, and how the company frames its own AI, live in `about-us.md`. The test: would a different company forking this system keep the rule? If yes, it is craft and belongs here. See the ownership rule in `README.md`.*

---

## PART 1, SYSTEM-WIDE

*Applies to every document type: Weekly Digest, Flash Report, Monthly page, Competitor Profiles.*

### Audience

Each document type states, in its own template, which readers it serves and what those readers need. **Who those readers are is self-knowledge and lives in `about-us.md`**, because a fork has different readers and should not inherit ours.

Two craft rules follow from having more than one reader group, and they are general:

**No single document serves every reader equally.** A document that tries to serve all of them serves none. State the slice.

**Where two reader needs conflict, resolve it with a light touch rather than by splitting the document.** A first-use gloss satisfies a reader meeting a concept for the first time without slowing down a reader who already knows it.

### The Slack message rule

The Slack post is not a teaser. It delivers the core message on its own, efficiently, so someone with thirty seconds gets the actual point of the week, not just curiosity about it. The linked document goes deeper, proof, nuance, full picture, it does not hold the headline hostage to earn a click.

Bad: "Big week for competitors. More inside."
Good: "Groundline's own users just handed us two sales talking points. Read more →"

No manufactured suspense. Short, driven, self-contained.

---

### Sentence shape

Separate from tone: this rule governs how a line is built, whatever the voice. A short line must still read as a sentence a person would say. Cutting words until only nouns and labels remain makes a line shorter and harder to understand. When text has to be short, keep the subject and the verb, say what it means for us first, and move the detail elsewhere.

Bad: "Pricing. Aggressive: three tiers, a free trial, annual discount."
Good: "Pricing is aggressive. They offer three tiers, a free trial and an annual discount."

System labels and tags travel as chips next to the text, never as the words of the text.

---

### THE EMOJI SYSTEM

**One symbol, one meaning, across every document.** If a new section needs a symbol that is not on this list, add it to this list rather than borrowing one that is already in use.

#### Section header emojis

Every section header carries one.

| Symbol | Means | Typical sections |
|---|---|---|
| 🔄 | What changed since last time | Changelog since last scan |
| 🎯 | The headline, what to remember | Three things to remember. **Only this.** |
| 🗺️ | The map, establishing terms before reporting | Strategy brief, vocabulary table |
| 🗣️ | Their words, Layer 1 | What they claim |
| 🔧 | Verified evidence, Layer 2 | What they actually do, what users say |
| 🤷 | The gap between claim and evidence | Reality check |
| 🕳️ | Market white space, where nobody is playing | Gap and opportunity sections |
| 🌐 | The category rather than a company | Market lens |
| 📈 | Dated log | Signal history |
| 💚 | Our documented advantage | Where we win |
| ⚠️ | Our exposure, or where not to fight | Where they are ahead |
| 🧭 | Where overlap sits and where it stops | Our angle, short-form profiles |
| ⚡ | What would move a tier | Escalation trigger |
| 🤝 | Partnership or ecosystem lens | Tier 3 entries |
| 🤖 | AI | Topic section |
| 📊 | Regulation | Topic section |
| 💥 | Competitor activity roundup | Competitor pulse, what is hot elsewhere |
| 💪 | Opportunities | Content angles, sales and product signals |
| 🔍 | Still open, still tracked | Follow-up tracker, open questions |
| 🌲 | Seasonal edition marker | Summer or forest edition |

**On 🔍 and 💥, deliberately widened rather than split.** Follow-up tracker and Open questions are the same family, things still live. Competitor pulse and What is hot elsewhere are the same family, activity across competitors. One symbol each.

**🌐 added September 2026.** The market lens had no symbol, so an edition borrowed 🔴, which is an inline marker meaning high threat. A symbol carrying two meanings breaks the rule the whole visual language rests on.

#### Inline markers, mandatory and never skipped

*This is the part most likely to get dropped under time pressure, and it is the part that carries the most reading value. A verdict without its marker is an unfinished verdict.*

| Symbol | Means |
|---|---|
| 🔴 | High threat, 4 to 5 |
| 🟡 | Moderate threat, 3 |
| ⚪ | Low threat, 1 to 2 |
| 🗣️ | Verdict: Talk, announced or claimed, nothing verified as shipped |
| 🔧 | Verdict: Implement, verified as running or shipped |
| 🔥 | Flame-level signal, the sharpest thing in the document |
| 🚩 | Decision awaiting a human |
| ✅ | Decision closed and recorded |
| ✏️ | Correction made after publication |
| 🗑️ | Retired or superseded |
| ✅ | Certainty: Confirmed, high confidence regardless of origin |
| 🟠 | Certainty: Reported, credible but not fully verified |
| ◽ | Certainty: Inferred, our own read stated as opinion |

**Where inline markers are required, without exception:**

- Every **Verdict** cell in a claims table. Write `🗣️ Talk` or `🔧 Implement`, never the bare word.
- Every **Verdict** line in a reality check gap block.
- Every entry in a **Signal history**, on the talk or implement grade.
- Every **two-axis score** wherever it is displayed. Format: `🔧 Implement · 🔴 High 5/5`. Both axes, both markers, always together.
- Every **gate or decision** state, 🚩 open or ✅ closed.

**One exemption, corporate events.** A Signal history row typed Funding, Acquisition, Partnership, Integration, Senior hire, Ownership change or Positioning has no talk-versus-implement state, so its Grade cell is left empty. An empty Grade on such a row is correct and complete, not an unfinished verdict. Every other row still carries its marker. Full definition: `analysis-rules.md` §2.5.

**Never use an inline marker as a section header.** The threat circles in particular read as a score, and a reader who sees one in a heading will read the whole section as scored. If a section needs a symbol, take it from the section table above or add one.

**Origin tags stay as text**, `[Self-declared]` and `[Independent, verified]`. Deliberately not symbols. That distinction carries too much weight to compress into a glyph a reader might misread at a glance.

**Note on the databases.** Competitor Profiles carries Talk/Implement and Threat score as select properties whose chip colours already provide the visual coding in the table view. Do not duplicate the emoji into the select option names. Inline markers are for page bodies and documents, where there is no chip.

---

### Notion formatting pre-flight

Run before writing any Notion content, no exceptions:

- Grey italic on all subtitles and legend lines
- "So what for us" / impact callouts use a blue callout, action-required icon
- **Section header emoji on every header, from the table above. Never an inline marker.**
- **Inline markers applied everywhere the list above requires them. Check this last, it is the one that gets skipped.**
- Two-axis scores always shown together, never collapsed, both with markers
- Source honesty tag on every Layer 2 claim, linked when available
- Dates on every Layer 2 citation, no evidence presented as new without its date visible
- OKR tags: blue inline text inside callouts, grey inline text outside. Max 3 per document.
- Flame-level sentence: highlight the key sentence only
- Quiet competitors: entire section in grey, no scoring, no bullets, one line
- Visual language legend placed directly above any colour or symbol system, no exceptions
- No em dashes anywhere, scan before saving
- TOC block reminder, cannot be inserted via API in Notion

If any item is unchecked, the document is not finished.

### Colour registers

| Colour | Meaning | Used on |
|---|---|---|
| Blue callout | Impact / action | "So what for us" and monthly impact statements |
| Blue inline text | OKR signal inside a callout | OKR tags inside blue callouts |
| Grey inline text | Low urgency / meta | Subtitles, quiet sections, legends |
| Yellow highlight | New signal, flag for attention | Key sentence, unverified flags |
| Red callout, 🚩 | A decision waiting on a human | Open tier, threat or baseline decisions on a profile |
| Grey callout, ✅ | A decision that is closed and past | Closed decisions on a profile, kept one cycle |

### Visual language legend rule

Any table, matrix, or element using colour codes or symbols gets a grey italic legend directly above it, before the element, not below. Reading order: know the code, then read the table.

Example score legend: 🗣️ Talk (announced, not shipped) · 🔧 Implement (verified, shipped) · 🔴 High (4-5) · 🟡 Moderate (3) · ⚪ Low (1-2)

Example source legend: Self-declared = competitor's own words · Independent, verified = third party with no incentive to favour them

Apply this rule to: tables with emoji columns, scoring matrices, follow-up tracker status columns, any custom visual language introduced in a document.

*One exception, the chip grammar in `competitor-profile-template.md`. Those chips are self-labelling, so a legend above them adds noise rather than clarity.*

### Recency filter

Only evidence dated within the current research cycle presents as new. Older evidence stays in the standing profile, referenced, not repeated. Full rule: `analysis-rules.md` §2.1, including the corporate events exemption in §2.5.

Bad: "Users report the setup is slow." (no date, reads as current)
Good: "A March 2026 G2 review flagged setup speed. No newer reviews raise it."

### Source honesty

Every claim tagged Self-declared (competitor's own words) or Independent, verified (third party, no incentive to favour them), dated, linked when available. Full rule: `analysis-rules.md` §2.2.

Bad: "Groundline delivers 180% ROI."
Good: Self-declared, Groundline website, citing an unlocated analyst study: "180% ROI, 8-month breakeven."

### Words to avoid

| Avoid | Use instead |
|---|---|
| Leverage | Use |
| Holistic | Specific alternative |
| End-to-end | Name the actual scope |
| Seamless | Describe what actually happens |
| Empower | Name the concrete action |
| Synergy | Avoid entirely |
| AI-powered / AI-driven | Describe what the AI actually does |
| Game-changer | Describe the actual change |
| Leading (self-declared) | Use specific proof points |

No em dashes. Anywhere. Ever.

*Words whose meaning depends on the company's own position, and the rules governing them, live in `about-us.md`.*

### AI language

Describe what the AI does. Never echo competitor hype.

Bad: "Their cutting-edge AI transforms compliance workflows."
Good: "Their AI parses bills of materials and extracts material data."

*This is craft, and it applies to writing about anyone's AI. How the company positions its own AI is a position, not craft, and lives in `about-us.md`.*

### Scoring system, two axes, always shown together

Full model: `analysis-rules.md` §3.

Axis 1, is it real? 🗣️ Talk (announced only) vs 🔧 Implement (verified shipped).
Axis 2, does it matter? 🔴 High (4-5), 🟡 Moderate (3), ⚪ Low (1-2). Independent of Axis 1, a pure announcement can still be High if it strikes a core theme watch.

Always displayed together with both markers, never collapsed into one number.

---

## PART 2, WEEKLY DIGEST

*Reader slice: fast readers who need proof and understanding in the same glance, deeper experts who need the source and date on every claim, and scanners hunting for opportunity. Reader groups are defined in `about-us.md`.*

### Voice and structure

Direct, fast, built for a Slack-speed read. Event and source first, "so what for us" last. This is an internal working document, the reader wants the point fast, not softened.

Example: "Groundline launched a Help Center. So what for us: continuous visibility should already be part of our sales conversation."

One idea per sentence. No compound sentences. Split at commas connecting independent thoughts.

Plain regulation names. Every regulation gets a one-line plain language gloss on first use.

Short is the default. 100 words max per competitor section on a quiet week. Longer only for a direct threat.

Enrichment, not repetition. References and acts on reality check findings, does not re-explain them at the same depth.

Bad: restating the full gap story at reality-check depth inside the digest.
Good: "Groundline's two user-confirmed gaps (see the August monthly page) are worth surfacing in sales conversations this week."

### Section emojis

Use the system-wide table in Part 1. The digest's standing sections map as follows: 🎯 Three things to remember · 🗺️ any vocabulary or map section · 🤖 This week in AI · 📊 Regulation watch · 🔍 Follow-up tracker · 💥 Competitor pulse · 💪 Opportunities · 🔍 Next week watch list · 🌲 seasonal editions.

Section subtitles always grey italic.

### Competitor sections, three formats

**Active competitor:**
```
### [Company name]
[Company] was [very active / active] in [period]. They mainly talked about [theme].
🗣️ Talk · 🔴 High [score]/5   OR   🔧 Implement · 🟡 Moderate [score]/5
[Bullet points, 3 max, each carrying a source honesty tag if citing Layer 2 evidence]
```

**Quiet competitor:** entire section grey, one line: "No significant update in [period]."

**Flame-level signal:** 🔥 marker, highlight the key sentence, then the "So what for us" callout.

### "So what for us" block

Only on high-threat flagged signals. Fixed title, never varied. Blue callout, two to three sentences, OKR tag on the last line.

### Closing

Two closing lines, grey italic, last before signature. Double divider between every Tier 1 profile.

### Slack bullet formula

Each bullet: what they did plus what it means for us, one sentence. Second part four words max.

### Flash Report

When findings consolidate around one topic with direct business consequences, the edition is renamed a Flash Report rather than numbered. Keeps the Digest's speed and directness, still Slack-bound, but given the higher stakes, holds a slightly more measured tone, closer to "here's what we found and why it matters" than a routine quick take. Full structure: `templates/flash-report-template.md`.

---

## PART 3, THE MONTHLY PAGE

*Reader slice: fast readers making a strategic read rather than a weekly pulse check, plus company-wide readers who may be meeting a concept for the first time. The proof bar is higher than the digest's. Reader groups are defined in `about-us.md`.*

*Structure: `monthly-review-template.md`.*

### Voice, observation not instruction

The reader is Product, Sales, or C-level. The goal is to nurture a decision, not hand one down. No imperative verbs opening an item (Investigate, Decide, Confirm, Publish). Open with what was observed, let the implication sit there rather than stating the conclusion for the reader.

Bad: "Investigate the Lindab and AXA feedback as a product signal, not a messaging problem."
Good: "Two buyers, two deals, the same doubt. Lindab and AXA independently raised versions of the same concern this quarter, one on effort reduction, one on methodology reliability, both claims we lead with."

### Structure, reversed from the Digest

Impact first, proof at the close. Shape: impact statement, one or two sentences of context, then a proof line, source-honesty tagged, dated and linked.

Bad: leading with the event ("Groundline hired a Chief Strategy and Innovation Officer") and ending with why it matters.
Good: leading with the implication ("Two competitors are quietly repositioning above us") and closing with the named hire and date as the proof.

### Altitude rule

Every claim answers "what does this mean for the business or buyer," not "what does the feature do." If the sentence can't complete that in one clause, it stays in the working record instead.

Bad: "No in-platform supplier dialogue."
Good: "Buyers are asking for something we already offer and a Tier 1 competitor doesn't, worth confirming this is said explicitly in sales conversations."

### Sufficiency, trend condition

The trend check is the monthly-only condition of the sufficiency check (`analysis-rules.md` §10). If there isn't enough reality check history for a genuine time comparison, don't stretch two points into a trend. Run a dedicated fresh search against the theme watch list itself, topic by topic, not company by company, to establish an honest current-state baseline instead.

Bad: calling two reality checks a "four-month view."
Good: "Two reality checks exist so far, not enough for a trend line. This section reflects a fresh baseline search instead."

### Market lens voice

Same observational register as the rest of Part 3. An observation drawn from the not-ours block of the matrix says so in the sentence. Never present a market theme as one of our theme watches.

### Opportunities section

Numbered, divider between each item. Team code-tag kept, decoupled from any directive verb. Frame as observation plus why it matters, never as an instruction.

---

*v7*
*v7 changes: the Data-sufficiency gate renamed to the sufficiency trend condition, pointing to `analysis-rules.md` §10.*
*v6 changes: Part 1 gains Sentence shape, kept separate from tone, after the compressed-line rule. Colour registers gain the red open-decision and grey closed-decision callouts, following profile template v8.*
*v5 changes: the audience pool moved out to About Us, since our readership is self-knowledge and a fork has different readers; the two craft rules that follow from having several readers stay here. 🌐 added for the market lens, after an edition borrowed the high-threat marker as a section header, with an explicit rule against reusing inline markers in headings. Corporate events exemption added to the inline marker list. Words to avoid and AI language now state that positioning-bearing vocabulary lives in About Us. Part 3 retitled from Quarterly Review to the monthly page and pointed at its template.*
*v4 changes: certainty chips added to the inline-markers table.*
*v3 changes: the emoji system moved from Part 2 to Part 1 so it governs every document type, and inline markers made an explicit mandatory pre-flight item.*
