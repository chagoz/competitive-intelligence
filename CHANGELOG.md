# Changelog

*What changed, when, across the whole system. Individual files also carry their own version footer, this page is the aggregate view for anyone landing on the repo cold. The reasoning behind the biggest decisions, including what was tried and reversed, lives in `docs/rework-method-sept-2026.md`, this page doesn't restate it.*

---

## September 2026, the big rework

Triggered by an external Product Vision brief asking questions the system's rulebook didn't yet have language for. Used as an audit rather than answered directly: what does the system already cover, how well, and what has to change. The audit found 23 problems. Fixing them reworked 14 reference documents, 6 skill files, every competitor profile, and 2 Notion databases plus a schema fix on a third.

**The headline isn't the 23 findings, it's that giving existing evidence a shape produced 12 findings the system couldn't previously state, from research already done.** Almost none of it came from new searching.

### New capabilities

- **Corporate events** (`analysis-rules.md` §2.5): funding, acquisition, partnership, integration, senior hire, ownership change, plus positioning as a seventh type. Exempt from the recency filter, since old commitments are still legitimate standing evidence.
- **The market lens** (§2.6): a monthly reading pass over already-collected evidence, not a new scan. Two blocks that never merge, our theme watches versus observed-in-the-market, with an explicit no-promotion rule.
- **The positioning block**: tracks the press-release lede descriptor against the standing boilerplate as two fields that move at different speeds. The gap between them is the finding.
- **Buyer archetypes, sourcing side** (`about-us.md`): five archetypes drawn from customer transcripts, deal records and support conversations, with a stated evidence bias and public user voice tested and confirmed absent as a category fact, not a research gap.
- **The bets pillar** (§2.8): three mandatory tags per competitor bet, evidence class, conviction, distance from our own stated direction. A bet missing any tag is excluded, not shown partial.
- **The absence bar** (§2.2.1): bounded claims need one authoritative path, unbounded claims need two independent ones. A guessed URL returning 404 proves the guess was wrong, not that the thing is absent.
- **The friction rule** (§2.9): a competitor move that removes a documented buyer friction raises the same single threat score a theme watch would, rather than creating a second, parallel number.
- **Product direction** (`about-us.md`): three directions, five explicit non-goals, and three open questions Product hasn't settled, which is what the bets pillar's distance tag measures against.
- **Two runs, one conversation**: the weekly digest and monthly reality check both split into a research-and-gate pass and a later write pass in the same thread, with explicit routing logic and a re-read-and-restate-version step before drafting.
- **The gate protocol**: partial agreement, modification, silence and ambiguity all explicitly resolve to still-at-the-gate, never to writing. Propagated across all five skills.
- **Two checks after every write, both reported**: does it render, and does it comply. A page can pass the first and fail the second, which happened once and is why both are now checked separately.
- **A fifth database, Digest Actions**: records what a digest caused, not just whether it was read. Status and Outcome are human-entry only, by design.

### Corrections

- The theme watch list had drifted to nine items in one file against eleven in another. `about-us.md` now owns the list outright; nothing else restates it.
- Loss patterns corrected: the dominant loss mode is buyer-internal, not competitive, at roughly twice the value of product-fit losses. Being too capable is a documented loss condition in its own right.
- Four errors caught in the estate during the profile rework, all traced to one cause, trusting a local view instead of re-reading the authoritative source: an independence claim that was actually vendor-solicited, a digest citing a competitor product that doesn't exist, a review-count claim where only 2 of 25 reviews were relevant, and an analyst credential cited for the wrong category.
- **A status-restated-outside-its-owner bug hit three files independently**: `skills-index.md` (cadence), a separate running-status file (cadence and database list), and this repo's own `README.md` (both). Fixed in all three, and named as a standing rule in `README.md` so the next occurrence is recognised rather than treated as new.
- `slack-message-template.md` had gone untouched since August 13, missed every convention change since, and contradicted its own no-em-dash rule in its own example two sections down. Fixed.
- `digest-template-structure.md` had no section for two watch list topics added after it was last touched. Fixed with a routing note rather than new mandatory sections, since both topics' findings are inherently company-attributable.

### Decisions made and reversed, worth knowing before proposing them again

A dedicated database for corporate events, a fixed-date archive snapshot for positioning history, keyword-mapping over press bodies, a promotion rule letting a market theme become one of ours after three mentions, a sixth skill for the impact sweep, and a people-to-segment analytics table. All considered, all rejected, reasoning for each in `docs/rework-method-sept-2026.md`.

### Worth knowing before your first real run

⚠️ **In the source system, every skill was rewritten twice across two days and none had been executed since.** If you're forking mid-rework the same way, treat the first real run as a test, not a rollout, some of what reads correctly on paper will turn out wrong in practice.

---

## Earlier

- **Two-axis scoring model, recency filter, source honesty tags.**
- **Monthly review template shipped**, replacing a pair of sibling pages that were indistinguishable from outside.
- **Five-skill architecture established**: Weekly Digest, Monthly Reality Check, Competitor Profile Setup, Competitive Mission, CI System Setup.
- **Initial system**: single weekly digest workflow, one skill, tier-based competitor tracking, manual research.

---

*For the reasoning behind any specific change, the individual file's own version footer usually has more detail than this summary does.*
