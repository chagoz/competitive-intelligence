*[Your name] x Claude — September 9, 2026*

*How the competitive intelligence system was reworked across 4, 8 and 9 September 2026. Written for retelling and for the next session's context, not as a record of findings. The findings live on the audit page, which owns them. This page owns the method: what reversed, what went wrong, and what the work was actually like.*

## What this was

It started as an audit. An external Product Vision brief arrived asking nine competitors' worth of strategic questions, and rather than answer it, the decision was to use it as a test case: what does the system already cover, how well, and what would have to change.

The audit found twenty-three problems. Fixing them turned into a rework of every layer: fourteen reference documents, six skill files, twenty-five competitor profiles, two Notion databases and a schema.

**The headline number is not the twenty-three findings.** It is that giving existing evidence a shape produced twelve findings the system could not previously state, from research that had already been done. Almost none of it came from new searching.

---

## What changed, by layer

**The rulebook.** `analysis-rules.md` went from v1.6 to v1.12. It gained corporate events, the market lens, the persona schema, the bets pillar, the window definition, the absence bar and the friction rule. Two of those were migrated in from a skill that had been carrying them inline.

**The lens.** `about-us.md` went from v1.0 to v2.2. It took ownership of the theme watch list, which had drifted to nine themes against the rulebook's eleven, and gained Product direction, buyer archetypes and a corrected loss-pattern section. The correction mattered more than the additions: the dominant loss mode, buyer-internal causes at twice the value of product-fit losses, was absent from the section that owns loss modes.

**The profiles.** All twenty-five converted to a new template. Signal history became a typed table, positioning blocks were added, and bets readings were written for every scoreable profile. Three companies were added, taking the tracked set from twenty-two to twenty-five.

**The skills.** Rewritten twice. Once on 4 September, then again on 8 September after the maintainer rewrote the weekly digest into two runs in one conversation and that pattern proved worth propagating.

**The databases.** The Evidence Registry went from 58 rows to 108, with a schema fix the live database had never received. A fifth database was found that no document named.

---

## Decisions that reversed

*The useful part. A log that only contains what worked teaches nothing about how to do it again.*

**A new database for corporate events, rejected.** The first proposal was a dedicated database. The maintainer pushed back: the system is a context layer for human reading and agent digging, nobody would query it, and more files means more maintenance. The argument that had been made for it, that it would solve the market-level gap, was wrong anyway, because a corporate event is always company-indexed. It became a typed column on a table that already existed.

**Archive snapshots for positioning history, tested and dropped.** The plan was four fixed capture dates of homepage headline and navigation labels. The maintainer challenged whether a headline says anything, since it moves for search optimisation. Testing on a real company showed the press descriptor and the standing boilerplate were far sharper, moved at different speeds, and the gap between them was the finding. Homepage headline was dropped entirely.

**Keyword mapping over press bodies, tested against the alternative and parked.** It would have produced a cloud dominated by awards and event announcements. The one-line self-category in a press lede answered the same question precisely and with a date.

**A new object for market-level findings, avoided.** The Theme Watch activity matrix was already the system's only market-level object, indexed by theme rather than company. It needed extending, not replacing. The proposal to give it its own research sources was also dropped, because it implied new scanning; four inputs already collected were enough.

**A promotion rule for market themes, rejected on principle.** The first design let an observed theme become one of ours after appearing three times. The maintainer's objection: the theme watches are close to the company's actual strategy, so counting appearances would let the market edit our self-knowledge. It became two blocks that never merge, with adoption as a human decision.

**The impact sweep, written as a sixth skill and deleted the same day.** The judgement it needed fitted in a scheduler prompt. The maintainer's challenge was direct: if a scheduler can hold it, what justifies a skill. The honest answer was only one step, and once that step was out of scope the skill was ceremony. `skills-index.md` records that it was considered and rejected so nobody rebuilds it.

**A people-to-segment table for analytics, rejected for the right reason.** It was proposed in the same breath as saying the system must be forkable. Those contradict: thirty rows of one company's names would be the first thing a fork deletes.

**A flat two-path absence bar, scaled instead.** Two was a number chosen arbitrarily and it was wrong in both directions. It became bounded versus unbounded: one authoritative path for a named artifact in its own place, two named paths for a claim about everywhere.

**The window anchored to the run date, re-anchored.** As written it produced a silent overlap whenever a run slipped. Anchored to the previous window's end instead, contiguity holds by construction.

**A parallel friction score, collapsed into one.** §2.9 first said a friction-solving move is scored against the friction rather than the theme watch. That produced two numbers, and the digest's candidate sheet orders mechanically on one. A friction now raises the single threat score.

**Tier 1 by rule for a company named once, resolved by amending the rule.** A company surfaced in one deal and §1 as written made it Tier 1. The maintainer's judgement was that once is not enough. Rather than record an exception, §1 was amended to define what counts as an active evaluation, deliberately as an evidence test rather than a count.

---

## Errors made, and the one cause

*Recorded because they share a single cause and a future session will make them again otherwise.*

**A skill was edited from a stale local copy.** the maintainer had rewritten the weekly digest and pasted it into the conversation. The edit was applied to an earlier version held locally, and presented as ready to upload. Uploading it would have deleted the whole rewrite. Caught only because the maintainer asked what the starting point had been.

**A shell command failed silently and the work was reported as done.** A copy step failed, the chained command never ran, and an unmodified file was presented as a new version. Caught by grepping for the change rather than trusting the success message.

**A finding was claimed that a deeper pass had already made the same morning.** A free supplier network was written up as a major discovery. The profile already carried it, in more depth, from a pass run hours earlier. Caught by fetching the profile before writing to it.

**Missing project files were raised as a finding when the mount was stale.** Three core files appeared absent from the container. They were present in the interface. The container's view was a snapshot.

**One cause, four times: trusting a local view instead of verifying against the authoritative one.** Every one was caught, and every one was caught the same way, by checking rather than asserting. The standing correction is to re-read from the authoritative source before editing anything that may have changed outside the session.

---

## What the system looks like now

**Five rules hold the layers together**, all in `README.md`, and all learned rather than designed. Every piece of content has exactly one home. Skill files are reconciled last, never first. A document change naming a database field is not done until the database has the field. A rule carried inline in a skill is a rule in the wrong place. One version stamp per file, in the footer.

**Four rules hold the skills together**, propagated across all five. A gate closes only on a restatement the human agrees to, and partial agreement, modification, silence and ambiguity all resolve to still-at-the-gate. The writing layer is re-read before drafting and its versions stated. The confirmed selection is restated before any artifact exists. And no skill carries method inline.

**The measurement layer is documented for the first time.** Five databases rather than four, the full tracker shape, and two scheduled tasks collapsed into one that asks on a real condition rather than on a schedule.

---

## What is still open

**Parked by decision until the week of September 15:** the mission run and everything downstream, including the Capterra pass, the historical positioning sweep and three untracked analyst-benchmarked competitors.

**Waiting on evidence:** investment-side archetypes, and a contradiction on whether one competitor offers supplier self-registration, where two sources disagree.

**Unblocked and mechanical:** per-company registry fetching across two source types, plus review-site category everywhere and the relevant national public registers.

⚠️ **The honest caveat**
Every skill was rewritten twice across two days and **none has been executed**. The first real run is the first real test, and some of what was written will turn out wrong in practice. Treat it as supervised.

---

*[Your name] x Claude — September 9, 2026 — v1*
