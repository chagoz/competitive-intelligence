# Skills Index
 
*The five workflows that run this competitive intelligence system. Each has a corresponding skill file (SKILL.md) built for use in Claude, including Cowork. Full rules referenced by each skill live in `analysis-rules.md` and `language-guidelines.md`.*
 
---
 
## Status
 
All five are built as skills. Two of them, the Weekly Digest and the Monthly Reality Check, also run as scheduled tasks. The scheduled version researches and scores, then stops at the human gate; it never writes the page or posts to Slack. **The gate behaves identically in both modes and is never skipped**, including in auto permission mode and including when the trigger message says to just run it.
 
**Cadence is not restated here.** It lives in `configuration.md`, which owns where things run and when. A copy in two files is how the two versions start, and this one already went stale once.
 
**Two skills now run as two runs in one conversation**, a research pass that stops at the gate and a later write pass in the same thread. The weekly digest and the monthly reality check both work this way. The split exists because a writing rule read hours before it is applied is a rule that gets dropped, so Phase 2 re-reads the writing layer next to the work it governs and states each file's version before drafting.
 
**No skill hardcodes a Notion page ID, CRM field name, or Slack channel.** Every live Notion page or database is found by searching for its title and confirmed once. This is what makes the skills portable across Notion connections; hardcoded IDs from one workspace are meaningless in another.
 
**No skill configures itself.** Project knowledge is read-only at runtime, so a skill cannot write a confirmed value back into `configuration.md`. It reports the delta and asks for the file to be updated by hand. The human is the only writer, deliberately, so a configuration change is always visible.
 
**Every skill reads `about-us.md` first.** It is the lens every signal is judged through, and it owns the theme watch list the threat axis scores against, the regulation coverage status, the positioning vocabulary, the reader groups, the Product direction and non-goals the bets pillar measures distance against, and the buyer archetypes whose documented frictions raise that same threat score per §2.9.
 
**Four rules propagated across every skill, September 8, 2026.** The gate protocol, where partial agreement, modification, silence and ambiguity all resolve to still-at-the-gate and never to writing. The version-stamp attestation before drafting, taken from each file's footer, which is now the only stamp a file carries. The restate-before-write step, so a mis-route is visible before an artifact exists. And the bar on carrying method inline: window, absence bar, scoring, bets and frictions live in `analysis-rules.md` and are referenced, never restated.
 
**Section 1 was amended September 4, 2026.** A single mention of a company in passing makes it a profile, not a tier. Moving a tier takes a demonstrable active evaluation or a lost deal. Profile setup and the weekly digest both apply this.
 
## Where the skill files live
 
**The five skills below are installed as a plugin bundle, not as user skills.** They sit
under the plugins path in the skills directory, alongside their plugin manifest. The user
skills path holds a different set entirely.
 
*Recorded September 4, 2026, after a verification pass read a stale copy at the user path
and wrongly reported the skills as un-updated. The exact path is environment-specific and
deliberately not hardcoded. What matters is that the plugin bundle is the live set, and
anything found at the user path for these five is a snapshot rather than the source of truth.*
 
## The five skills
 
### 1. Weekly Digest
 
**Trigger:** "run competitive digest", "run this week's digest"
**Mode:** two runs in one conversation, research then write, on the cadence in `configuration.md`, plus ad hoc.
**Human gate:** required, every run, on the top 3 selection, closing only on a restatement the user agrees to.
**Reads:** `about-us.md`, `analysis-rules.md`, `language-guidelines.md` Parts 1 and 2, `competitor-list.md`, `watch-list.md`, `configuration.md`, the latest monthly page, the previous digest's follow-up tracker.
**Writes:** the digest page, 3 Slack post options, a Digest Impact Tracker entry after posting. Any corporate event or prospect-named company found is written to the profile through the §9 write plan at the end of the research pass, independently of the gate.
**Also owns:** the choice between a numbered digest and a Flash Report. A Flash Report replaces the digest only when the findings consolidate around one question, that question has a live business consequence, and the research is mission-depth. Named, not numbered, and it does not break the weekly sequence.
 
### 2. Monthly Reality Check
 
**Trigger:** "run monthly reality check", "run reality check for [month]"
**Mode:** two runs in one conversation, research then write, on the cadence in `configuration.md`, covering the previous calendar month, plus ad hoc.
**Human gate:** required, on the top 3 key learnings selection, closing only on a restatement the user agrees to.
**Reads:** `about-us.md`, including the Product direction the bets pillar measures against, `analysis-rules.md`, `evidence-registry.md` for source types, `monthly-review-template.md`, `language-guidelines.md` Parts 1 and 3, `configuration.md`, the Evidence Registry database, the Competitor Profiles database, the Competitor Employee List, CRM lost-deal data.
**Writes:** every affected Competitor Profiles entry, all tiers, through the §9 write plan at the end of the research pass, per the all-tier rule in §7 and the always-true rule in §9. Then, once the top 3 are selected, **one monthly page** holding the review, the market lens and the working record in a toggle. Then 3 Slack post options for the review and a tracker row.
 
*One page per month, not a pair of sibling pages. The Theme Watch activity matrix and the lost-deal table are sections inside the working record toggle, not separate documents.*
 
### 3. Competitor Profile Setup
 
**Trigger:** "set up competitor profile for [name]". Also triggered automatically by any company a prospect names that we do not already track, per §1, before and regardless of the tier review.
**Mode:** ad hoc only, once per new competitor, never scheduled.
**Human gate:** required, on tier placement and employee list validation, closing only on a restatement the user agrees to. A wrong tier persists in a database with a rationale attached, which is why this gate carries the same protocol as the two cadence skills.
**Reads:** `about-us.md`, `analysis-rules.md`, `competitor-profile-template.md`, `evidence-registry.md`, `configuration.md`.
**Writes:** a new Competitor Profiles entry, new Evidence Registry database rows including absent source types recorded with their search trail, proposed employee list candidates.
 
### 4. Competitive Mission
 
**Trigger:** open-scope, e.g. "research Competitor X for the upcoming RFI"
**Mode:** always ad hoc, on demand, never scheduled by definition.
**Human gate:** scope clarification required if the request is vague, including depth per company and a stopping rule. Never fabricate your own side of a comparison; flag the gap instead.
**Reads:** `about-us.md`, `analysis-rules.md`, `evidence-registry.md`, `configuration.md`, relevant Competitor Profiles entries.
**Writes:** a standalone page opening with a scope block, structure determined by the mission's own needs, or the Flash Report shape where the mission consolidates around one question. Anything new learned is written back to the profile in the same session.
**Also owns:** scoping before research. The question in one sentence, depth per company stated as a source count, a stopping rule agreed upfront, and the intended reader. A mission asking about direction uses the bets pillar in §2.8 rather than inventing a framing.
 
### 5. CI System Setup
 
**Trigger:** "set up competitive intelligence system"
**Mode:** Phase 1 once per company, first-time only. Phase 2 safe to re-run any time. Never scheduled.
**Human gate:** the entire skill is a human gate. Every Phase 1 answer is asked, never assumed. Every Phase 2 item is shown and confirmed before creation.
**Reads:** for Phase 1, nothing pre-existing. For Phase 2, `configuration.md` and the shape references.
**Writes:** a new user's own About Us, Competitor List, Watch List and Language Guidelines, populated entirely from their answers. Then the five blank Notion items.
 
*Phase 2 is not the same thing as confirming `configuration.md` on an already-populated workspace. If your content documents already exist with real answers, the first run of any of the other four skills will skip straight to confirming Notion structure, via the search-and-confirm step built into each of them, rather than asking you to answer the Phase 1 questions again.*
 
---
 
## Known gaps in this layer
 
**The daily impact sweep has no skill file.** It runs as a scheduled task, filling Slack reaction and reply counts at the 24 hour and one week marks. Its logic lives in the task rather than in a skill anyone can read or fork.
 
**Notion page view counts are manual.** Notion does not expose them through its API. The sweep is instructed never to guess them and to flag rows where they are missing.
 
---
 
*[Your name] x Claude · September 8, 2026*
*September 8, 2026: cadence removed from this file and deferred to configuration.md, after the table here went stale against a changed schedule. The weekly digest and the monthly reality check both became two runs in one conversation. The gate protocol, the version attestation, the restate-before-write step and the no-inline-method rule propagated across all five skills. Buyer archetypes added to what About Us owns.*