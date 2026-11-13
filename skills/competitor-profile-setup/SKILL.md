---
name: competitor-profile-setup
description: "Sets up a full initial competitor profile for a new competitor: scans both research layers, fetches the help centre, populates the Evidence Registry database, proposes tier placement, and proposes employee list candidates for the operator's validation. Trigger phrase: 'set up competitor profile for [name]'. Also triggered automatically by any company a prospect names that we do not already track. Ad hoc only, once per new competitor, never scheduled."
---

# Competitor Profile Setup

## Route first

- A confirmed tier and employee list in this conversation: this is the write step. Go to Output, items 1 to 4.
- An unconfirmed or partly confirmed set: gate resume. Do not re-research.
- Anything else, including any case not clearly one of the above: still at the gate, and ask. Ambiguity never resolves toward writing.
- Neither state exists: research run.

If the earlier conversation is gone, run a fresh research pass and say so in the first line.

## Status and cadence

**Mode:** ad hoc only. Runs once per new competitor. Not a candidate for scheduling, there is nothing recurring here.
**Also triggered by:** any company named in a prospect conversation that we do not already track, per `analysis-rules.md` §1. This runs **before and regardless of the tier review**. Previously a negative tier review made the signal vanish; the profile is the record that the company was named at all.
**Human gate:** required. The operator confirms tier placement and validates the proposed employee list before either is saved.

## Before anything else

Read from Project knowledge:

- `about-us.md`, the lens every competitor gets judged through: the theme watch list, the Product direction the bets pillar measures against, and the buyer archetypes whose documented frictions are standing research questions
- `analysis-rules.md`: §1 tier criteria and the gate-keeper rule, §2 research schema, §2.1 the recency filter, §2.2.1 the absence bar, §2.2.2 name collisions, §2.5 corporate events, §2.8 the bets pillar, §2.9 archetype frictions, §5 employee list rules
- `competitor-profile-template.md`, the shape the profile takes
- `evidence-registry.md` for the source types to look for and their priorities
- `configuration.md` for the Competitor Profiles database, the Evidence Registry database and the Competitor Employee List database

**If a configuration value is missing, unconfirmed, or does not match the workspace:** search Notion by the name given in the file, show what you found, and ask the operator to confirm before writing. If the search returns nothing, stop and name the field in `configuration.md` and the exact title you searched for, rather than running thin on a missing resource.

**Do not attempt to write to `configuration.md`.** Project knowledge is read-only at runtime. Report the delta and ask the operator to update it. **No skill configures itself.**

## Research, both layers

**Layer 1, what they say.** LinkedIn company page, press releases, product pages, website.

**Layer 2, what they actually do.** Help centre (mandatory: if it is documented there, it shipped), G2, Capterra, TrustRadius, job postings, public company register.

**Positioning descriptor, both fields.** The one-line self-category in the lede of a press release, and the standing boilerplate at the foot of it. Capture both verbatim, never paraphrased, since the comparison between them is the finding. The descriptor moves first; the boilerplate moves late and only on a decision.

**Corporate events.** Funding, acquisition, partnership, integration, senior hire, ownership change. These are exempt from the recency filter on the event date, so capture the last twelve months at setup and write them to the Signal history table, typed, with an empty Grade.

**Absence is a finding, and it meets the bar in §2.2.1 before it is written as Confirmed.** Check whether the claim is bounded or unbounded first. One authoritative path is enough for a bounded claim, no G2 listing checked on G2. An unbounded claim needs two independent paths, both named, with the scope written in: not found on their site or in search, never does not exist. A guessed URL returning 404 proves the guess was wrong, not that the thing is absent.

A company with no help centre, no reviews and no pressroom is telling you something. Record each absent source type with its search trail rather than leaving it blank.

**Public user voice has a low ceiling in this category**, tested and confirmed absent. Do not treat an empty review base as a research failure; it is the norm here and the Evidence Registry carries it as a category-level finding.

**Which archetype do they design for.** Answer it at setup from what the scan already surfaced: does onboarding present defaults or settings, is there a supplier-facing surface and is it free, does the pricing page address a decider or a champion, and who appears in reviews where reviews exist. This separates competitors better than tier does, and it is cheapest to answer while the sources are open.

Apply source honesty tags and the recency filter to everything. Check the incentivized flag before citing any review count.

## Tier placement

Apply the gate-keeper rule in `analysis-rules.md` §1: Tier 1 only on a qualifying loss, which is recent within the user's recency window (default 12 months, set in settings) and on the product area the user defines, or on a named appearance in an active evaluation. A loss that fails either condition is recorded on the profile and does not set the tier.

**What counts as named in an active evaluation, per the amended section 1.** A company the prospect is demonstrably weighing against us: on a shortlist, quoted alongside us, named in a comparison the buyer is running, or recorded in a deal as an alternative. **A single mention in passing is not that.** A company named once is a profile, not a tier. It lands in the market lens and it stops there until a second independent mention or a loss. Otherwise place by the Tier 2 to 5 criteria in §1. Tier 5 is the platforms the category sits on or gets absorbed into, recorded as a market signal and never scored on the threat axis.

Check the AI-native flag independently; it is cross-cutting, not a tier.

**Propose the tier and the reasoning, then wait for the operator to confirm before saving.**

### Sufficiency check before the gate

Apply the profile conditions in `analysis-rules.md` §10 before the gate: Search (name plus a unique identifier), Fill the gate (both research layers searched), and Weight (a tier placed on an evidence limb, or marked provisional on a stand-in). State any failed condition with its cost. A thin profile is disclosed, never padded into a confident tier.

### The gate protocol

**The gate closes on one condition only: the skill has restated the proposed tier and the employee list, and the operator has agreed to that restatement.** Nothing else counts as confirmation. A wrong tier persists in a database with a rationale attached, which is worse than a wrong document.

- **Partial agreement** ("tier is fine, not sure about the employees"): still at the gate on the open half. Restate both with the settled one fixed, then ask the single question that resolves the other.
- **Modification** ("make it Tier 4 instead"): apply it, restate the result, and treat a plain yes as confirmation. Do not return to research.
- **Silence or an unrelated reply**: still at the gate.
- **Anything unclear**: still at the gate. Ask. Never read ambiguity as confirmation, and never resolve it in the direction that lets the run continue.

**Ask at most one question per turn, the one that actually blocks progress.**

### Before writing, restate

Open the write step by restating the confirmed tier and the confirmed employee list in one line each, exactly as agreed. This is the mis-route check, and it happens before a database row exists rather than after.

## Output

1. **New row in the Competitor Profiles database**, with a full initial scan across both layers, following `competitor-profile-template.md`. Tier 1 gets the full shape; Tier 2 to 4 get the medium form. Every tier gets the Signal history table as a standing section.
2. **New rows in the Evidence Registry database**, one per source type located, with the address, priority and check frequency. Absent source types recorded as absent. This is a database, not a page.
3. **A bets reading**, per section 2.8, where the evidence supports one. Evidence class, conviction, and distance from us against the directions and non-goals in `about-us.md`. All three tags or the bet is excluded and recorded as excluded.
4. **Proposed employee list candidates** for the Competitor Employee List database, scored per §5. Tier 1: top 10 on seniority plus LinkedIn activity, minimum combined 4. Tier 2 and below: C-level only. **Flag anything that cannot be verified without manually browsing a profile as pending manual validation rather than guessing.**
5. **Stop. Wait for the operator to validate the tier and the employee list before adding them.**

**After any write that includes a toggle, callout, table or chip, fetch the page back and inspect the returned markdown before calling it done.** Notion markdown fails silently. After a write that coincided with a connection warning or a timeout, read the page back before retrying.

## Gotchas

- A single mention in passing makes a company a profile, not a tier. Do not tier it on that alone.
- A wrong tier persists with its rationale attached, so restate the tier at the gate before anything is written.
- An employee who cannot be verified without a manual browse is pending manual validation, never guessed.
- A bet missing one of its three tags is excluded, and recorded as excluded.
- A louder namesake can own the search results for a tracked name. Carry the identifier in the query, and tie each finding to the domain or registration number before it is used (§2.2.2).

---

*v5*
*v5 changes: title-lookup recovery, a configured title that finds nothing stops and names the field and the searched value, matching configuration.md.*
*v4 changes: §10 sufficiency check added before the tier gate, with the profile conditions Search, Fill the gate and Weight.*
*v3 changes: route-first added. The gate-keeper rule now names the qualifying-loss definition in analysis-rules.md §1, with the recency window as a user setting, default 12 months. The do-not list is replaced by gotchas.*
