---
name: ci-system-setup
description: "Setup skill, two phases. Phase 1, content: asks who the company is, competitors, watch list topics, and voice, then writes About Us, Competitor List, Watch List, and Language Guidelines, only for a genuinely new setup with no existing content, skipped automatically when these already exist (as they do for an existing company). Phase 2, architecture: checks whether the five required Notion pages and databases exist, and for any that don't, shows the proposed shape and builds it blank once confirmed. Never adds competitor data or digest content, that's the other skills' job. Trigger phrases: 'set up competitive intelligence system', 'build notion workspace', 'run workspace init'. Phase 1 runs once per company. Phase 2 is safe to re-run any time."
---

# Competitive Intelligence System Setup

*Two distinct jobs in one skill: getting the content right (who you are, competitors, watch list, voice) and getting the Notion structure right (the pages and databases everything else reads and writes to). A brand new fork usually needs both, in order. An already-populated workspace only needs the second.*

## Route first

- The phase is chosen at Step 0, and the choice is stated in the first line.
- If the earlier conversation is gone during Phase 1, start Phase 1 from its first question. Do not resume from remembered answers.
- If Phase 2 was interrupted, check what already exists before creating anything, and confirm each item again.

## Status

**Mode:** Phase 1 runs once, only when needed. Phase 2 runs once per new Notion connection, and is safe to re-run any time after that.
**Human gate:** every question in Phase 1 is asked, never assumed. Every item Phase 2 proposes to build gets shown and confirmed before creation, even on a re-run.

---

## Step 0, decide which phase to run

Before asking anything, check whether `about-us.md`, `competitor-list.md` and `watch-list.md` already exist in Project knowledge with real, specific content, not placeholders.

**If they exist with real content** (an existing company's case): skip Phase 1 entirely, say so plainly, and go directly to Phase 2.

**If they do not exist, or are template shells:** run Phase 1 first, then Phase 2 once Phase 1's output is confirmed.

Never run Phase 1 "just in case." Asking someone to re-answer who their company is when that document already exists and is correct is exactly the friction this check avoids.

---

## PHASE 1, content

*Only runs per Step 0.*

### The four setup questions, asked in sequence

1. **Who is your company?** Category, value drivers, differentiators, ICP, priorities, and the theme watches, the dimensions along which a competitor move becomes strategically relevant. Do not proceed until this is answered; everything downstream scores against it.
2. **Who are your competitors, organised by tier?** Ask what Tier 1 means for their business specifically. The reference definition is "we have lost deals to them, or they are named by prospects in active evaluations". Check whether that gate-keeper rule fits or needs adapting. Note that Tier 5 is the platforms their category sits on rather than a competitor set.
3. **What are your watch list topics?** Two to four maximum, more creates noise. Ask what the primary competitive battleground is right now, and what external forces most affect their buyers. Ask each topic to state its own noise floor.
4. **What is your language or copy reference?** Existing brand voice docs, tone examples, words to avoid. If they have nothing, offer to derive a starting point from content they already like.

### Phase 1 output

Four new reference documents, written in the structure of the existing templates but populated entirely with the new user's answers, never with any existing company's content as a default or placeholder.

**Point them at the ownership rule in `README.md`.** Positioning belongs to About Us, craft belongs to Language Guidelines. A copy in two files is how the two versions start.

### Sufficiency check at the end of setup

Run the setup check from `analysis-rules.md` §10 against the four documents: the Search setup tests and the input map, inputs only. State every input that fails or is missing with the condition it weakens and the run it affects. A skip is never silent. The Evidence Registry is empty on a fresh setup and is disclosed as a known thin input, not a blocker: it fills run by run as profiles are set up.

### Gotchas, Phase 1

- A guessed answer speeds setup now and persists in every later run. Ask every question.
- Copying another company's competitors, watch list or voice into a new workspace is the failure this phase exists to prevent.
- Phase 1 does not run again once these documents exist.

---

## PHASE 2, architecture

*Structure only, never content.*

**Is:** checks for six required Notion items, creates whichever are missing, blank, matching the shapes below. Reports their titles so the human can record them in `configuration.md`.

**Isn't:** content. This phase never adds a competitor, a digest, an evidence source, or any row of real data.

**Safe to re-run.** Every check looks for what already exists before proposing to create anything.

**Does not write `configuration.md`.** Project knowledge is read-only at runtime. Report what was found or created and ask the human to update the file. **No skill configures itself.**

### Before this phase

Read `configuration.md`, plus the shape references: `competitor-profile-template.md`, `evidence-registry.md`, `skills-index.md`.

### The six items, checked one at a time

For each: search Notion for the title given in `configuration.md`. If found, confirm it matches the expected type and move on. Do not touch it, do not migrate or merge anything into it, even if an old or oddly-named version exists alongside. If not found, show the proposed shape and wait for confirmation before creating.

**1. Competitive Intelligence home page**
Type: page. Shape if creating: a hub page with a short description and placeholder links to the four items below.

**2. Competitor Profiles**
Type: database. Propose these properties, wait for confirmation:
Name (title) · Category (text) · Website (URL) · LinkedIn (URL) · AI-native (checkbox) · Tier (select: 1-5) · Tier rationale (text) · Talk/Implement (select) · Threat score (select: 1-5) · Last updated (date) · Tracked Employees (relation to Competitor Employee List)

Zero rows on creation. The tables inside each row, What they claim, What they actually do, Signal history, are page content written per-row by Competitor Profile Setup and the Monthly Reality Check. Do not model them as properties.

**3. Competitor Employee List**
Type: database. Shape: Name (title) · Company (relation to Competitor Profiles) · Role (text) · Seniority score (select: 1-3) · LinkedIn activity score (select: 1-3) · Combined score (formula or number) · LinkedIn URL (URL) · Last reviewed (date). Zero rows.

**4. Digest Impact Tracker**
Type: database. Shape: Digest (title) · Date posted (date) · Channel (text) · Link to digest (URL) · Slack message link (URL) · Total reactions (number) · Reactions 24h (number) · Reactions 1 week (number) · Emoji breakdown (text) · Reactors (text) · Thread replies (number) · Total page comments (number) · Page comments 24h (number) · Page comments 1 week (number) · Commenters (text) · Notion views 24h (number) · Notion views 1 week (number) · Measurement status (select: Awaiting 24h, Awaiting 1 week, Complete, No Slack link) · Actions (relation to Digest Actions). Zero rows.

*Channel is not optional. Channel choice is editorial and varies by edition, so engagement cannot be read without knowing where a post actually went.*

*Measurement status drives the sweep and is not decoration. Awaiting 24h is set when a row is created. No Slack link is a designed failure path, not an error state.*

*Reactors and Commenters hold names as text. They exist so a segment read is possible by eye without the system holding a segment table, which would be one company's org chart living inside a forkable system.*

*Only two fields cannot be filled by API: the two Notion view counts. Everything else, including page comments and commenters, is machine-readable. Do not describe the whole tracker as manual.*

**5. Digest Actions**
Type: database. Shape: Action (title) · Type (select: Commitment, Request, Question, Correction) · Surface (select: Notion page comment, Slack thread, Slack DM, Meeting) · Section (text) · Person (person) · Raised (date) · Link (URL) · Status (select: Open, In progress, Landed, Dropped) · Outcome (text) · Digest (relation to Digest Impact Tracker). Zero rows.

*This is the database that answers what the digest caused, which engagement counts cannot. It was missing from this skill until September 8, 2026, so a fork would have inherited a measurement layer that could count attention and never record a consequence.*

*Status and Outcome are human entry only, by design. No automation can know whether the work happened, and no future session should infer either from activity elsewhere.*

*Section anchors an action to a block of the digest. It is the field that answers whether the digest is getting better, rather than whether it is being read.*

*Surface includes Slack DM and Meeting deliberately. That is where the response usually happens, and neither is machine-readable, so rows are added by hand. An empty table is a finding about the habit, not about the digest.*

**6. Evidence Registry**
Type: database. Shape: Company (relation to Competitor Profiles) · Source type (select: Help centre, G2, Capterra, TrustRadius, Careers/Job board, Press/Newsroom, LinkedIn, Product pages, Pricing page, Positioning descriptor, Review-site category, Public company register, Analyst coverage, Supplier-facing surface) · **Source URL** (URL) · Priority (select: Critical, High, Medium) · Check frequency (select: Weekly, Monthly, Quarterly) · Last checked (date) · Notes (text). Zero rows.

*The URL field is named **Source URL**, not URL. Notion treats a property literally named URL as reserved and requires a prefix on every write. This is a known defect; do not recreate it.*

If an old page or database with a similar name already exists: leave it exactly as it is. Create the new one alongside and flag the old item's existence in your output, but do nothing to it.

### Confirmation flow, per item

1. Show the proposed type and full field list.
2. Wait for explicit confirmation. Never create on an assumption, even when the shape is copied from a template file.
3. On confirmation, create it blank.
4. Report its title and type so the human can record it in `configuration.md`.
5. Move to the next item. Do not batch-confirm all six unless explicitly asked.

### Phase 2 output

A short status table: item, found or created, type, any old or stray item flagged for awareness but left untouched. Plus the list of values the human needs to add to `configuration.md`. Nothing else.

### Gotchas, Phase 2

- An existing page or database is never touched, read into, merged or archived, even one that looks like an old version of what this phase builds.
- Each item is confirmed before it is created, including on a re-run.
- No content or row is added in this phase, and `configuration.md` is never written by the skill.

---

## What this skill never does, either phase

Does not run on a schedule. Does not guess at content to save time. Does not touch existing Notion items it was not asked to build. Does not write competitor data, digest content, or any row-level information. That boundary is what keeps this skill safe to re-run.
---

*v4*
*v4 changes: §10 sufficiency setup check added at the end of Phase 1, inputs only, disclosing thin inputs with their cost.*
*v3 changes: route-first added, stating how the phase is chosen and what a lost conversation does. The two do-not lists are replaced by gotchas. The never section is kept, since it states the hard boundary.*
