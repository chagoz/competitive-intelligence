# Analysis Rules

*The canonical rulebook for how the competitive intelligence system researches, scores, and classifies signals. Read before every digest, every reality check, and every competitive mission.*

*This file owns method. It does not own any content about the company itself: the theme watch list, the regulation coverage status and the reader groups all live in `about-us.md` and are referenced here, never restated. See the ownership rule in `README.md`.*

---

## 1. Tier criteria

**Gate-keeper rule:** Tier 1 is determined by one criterion only: we have lost a qualifying deal to them, or they are named by prospects in active evaluations. Everything else is secondary.

**What counts as a qualifying loss.** Two conditions, both required. Recent: the deal closed lost within the recency window, counted back from the day the tier is reviewed. The window defaults to 12 months and is set in the user's settings, which offer other windows. On the product area: the deal was for the product area the user defines in their settings. A loss that fails either condition stays on the profile with its date and counts in the deals-lost line, but it does not set the tier.

**Losing the qualification.** A Tier 1 company whose most recent qualifying loss passes the recency window, and that is not named in an active evaluation, is proposed for a move down at the next monthly reality check. Proposed, never moved automatically: tier changes belong to the human.

**What counts as named in an active evaluation.** A company the prospect is demonstrably weighing against us: named on a shortlist, quoted alongside us, named in a comparison the buyer is running, or recorded in a deal as an alternative under consideration. A single mention in passing is not that.

A company named once is a profile, not a tier. It triggers a profile setup under the prospect-named unknowns rule below, and it lands in the market lens, and it stops there. A second independent mention, by a different buyer or in a different deal, is sufficient evidence of active evaluation, though not the only way to establish it.

**Why the two limbs are asymmetric.** One lost deal is enough on the first limb because a loss is already evidence that a buyer made a decision. A mention is not a decision. Without this distinction, one sentence in one transcript places a company at Tier 1 alongside our most-cited competitor, and the tier stops carrying meaning.

**This is deliberately not a counting rule.** Section 2.6 states that a market theme does not become one of ours by appearing often enough, because counting appearances would let the market edit our self-knowledge. The same logic applies here: the test is evidence of active evaluation, and a second independent mention is one way to satisfy it rather than the definition of it.

**Tier 1, direct competitors.** Always include in every digest, even if nothing happened.
**Tier 2, adjacent.** Related problem, similar buyer, or expanding toward our territory. Include only if genuinely eventful.
**Tier 3, partnership or ecosystem lens.** Not a threat. Influences buyers from outside, or a potential data/integration partner.
**Tier 4, niche or emerging.** Specialist in one dimension. Watch for escalation.

**Tier 5, the platforms the category sits on.** Systems buyers already run that our category either sits on top of or gets absorbed into. Not a dedicated tool, and not necessarily a competitor. The question per entry is where their offer intersects ours, and whether the intersection is growing. Recorded as a market signal and read into the market lens (§2.6), never scored on the threat axis, because a platform is not making a move against us.

**Genuinely eventful, the Tier 2 to 4 inclusion bar.** Tier 1 is always included, eventful or not. A Tier 2 to 4 competitor enters an output for the window only on a dated, observable change that clears the eventfulness bar. A restated claim, a rebrand of existing positioning, or mere presence in search with no observable change behind it never clears it, at any setting. The bar is one operator setting, the eventfulness bar in `configuration.md`, default material:
- **any:** any dated, observable change. Highest volume, most noise.
- **material (default):** a dated, sourced instance of any corporate event in §2.5 (funding, acquisition, partnership, integration, senior hire, ownership change, positioning change), a shipped or announced product feature, a pricing or packaging change, a named customer win or loss, or a regulatory action.
- **threat:** a strict subset of material, a material event that also moves the competitor's threat score or directly targets our buyers. Lowest volume. The levels nest: any contains material contains threat.

This one bar governs competitor-attributed inclusion and movement: the weekly scan, Competitor pulse and Three things, the monthly review, the profile changelog, and a flash edition. It does not gate the topic passes (This week in AI, Regulation watch) or the Follow-up tracker, which keep their own noise floors, so a cross-cutting topic finding or a tracked move is never silently dropped by the bar. A skill reads the level from `configuration.md` and names the level it used.

**AI-native flag (cross-cutting).** A company can be AI-native and any tier. Criteria: AI is the primary differentiator (not a feature), targets buyers wanting to reduce human involvement, no established methodology credibility comparable to Tier 1.

**Escalation rule:** Any Tier 2/4/AI-native company named in a prospect conversation triggers a human gate review before tier change.

**Prospect-named unknowns trigger a profile.** Any company named in a prospect conversation that we do not already track gets a profile setup run, before and regardless of the tier review. Previously a negative tier review made the signal vanish. The profile is the record that it was named at all, and the name also lands in the market lens.

---

## 2. Research schema, two layers

**Layer 1, What they say.** LinkedIn company page, press releases, product pages, website. Scanned weekly, feeds the digest.
**Layer 2, What they actually do.** G2, Capterra, TrustRadius, help center, job postings, employee LinkedIn posts, public company registers. Scanned monthly, feeds the reality check. Source types and their cadences live in `evidence-registry.md`; the addresses themselves live in the Evidence Registry database named in `configuration.md`.

### 2.1 Recency filter, mandatory

**Only review/comment evidence dated within the current reality-check window counts as a new signal.**

- A G2, Capterra, or employee post must carry a visible date. If the date falls inside the current cycle (the period since the last reality check), it is a new finding.
- If a review or post is undated, or dated outside the current window, it does not get presented as new. It either (a) already belongs in the standing profile as established baseline evidence, or (b) is discarded as too old to be a signal.
- Never present old evidence with fresh-sounding language ("users report...") without the date attached. Every Layer 2 citation includes its date.

Why this matters: without a recency filter, an old review can read as if it happened this week, inflating the sense of new activity and eroding trust in the reality check over time.

*One exemption, corporate events, see §2.5.*

**Defining the window.** The recency filter needs a window, and the window is defined here rather than in whichever skill happens to need it.

**Every watch-list item carries its own time window.** The window applies to any item on the watch list, not only regulation dates. It is written as timestamps with a time zone, and an item outside its window is not scored, however it is worded. Regulation dates need the official source, or two independent ones; a single secondary source is recorded as 🟠 Reported.

**The window runs from where the previous window ended to the moment this research run starts.** Anchoring it to the previous end rather than to the run date is deliberate: contiguity then holds by construction, and it survives a run that slips by a day or two. In the normal weekly rhythm this produces a Tuesday to Monday window, but that is the usual result, not the rule.

**The first run has no previous window to anchor to.** It uses the recency window, an operator setting defaulting to 12 months. Every run after anchors to the previous window's end as above, so the steady-state window is simply the run's own cadence: a weekly digest reads the last week, a monthly check the last month.

**An explicit window in the run's prompt overrides the computed one.** If the operator asks for a different reach for a given run, that request wins, and the output states the window it actually used.

- No gap and no overlap with the previous window, ever. If a run slips, the window stretches; it does not shift.
- The window applies to the **event date**, never to when someone wrote about it, covered it or promoted it. Third-party coverage, analyst commentary and vendor promotion of an earlier event are all out of window if the event is.
- **One carve-out, first public disclosure.** Where a source reveals something that was not previously public, the disclosure is the event. An analyst report published this week that benchmarks work done months ago is in window for what it discloses, and out of window for the work it describes. The August 2026 Green Quadrant is the worked example: the benchmarking was old, the fact that our company was absent from sixteen vendors was new on the day it appeared.
- **Undated is out of window.** It cannot be a candidate for a headline finding. It becomes standing evidence on the profile, or it is discarded.
- Corporate events keep their §2.5 exemption as standing evidence, but an out-of-window corporate event cannot be a headline candidate.
- Where a run covers more than one window's worth of time, the output says so in its opening line.

**Any process that splits research from publication carries a blind spot** between the two, and should say so rather than let a reader assume the window runs to the publication date.

### 2.2 Source honesty, mandatory

**Every claim is tagged with who said it, not just how certain we are.**

Two tags, always both present:

**Origin tag:**
`[Self-declared]`, the competitor's own words: press release, website, product page, sponsored/incentivized review
`[Independent, verified]`, a third party with no incentive to make the competitor look good: organic G2/Capterra review, analyst report, journalist coverage, named customer quote outside the competitor's own site, public company register

**Link:** whenever the source is public and linkable, the citation includes the URL. If no link is available, say so explicitly rather than omitting it silently.

**Format:**
`[Independent, verified], source name, dated (URL). Claim/finding text.`
`[Self-declared], source name (dated if known). Claim/finding text.`

Why this matters: an old certainty-only scale answered "how sure are we this is true" but silently conflated a press release with a G2 review, both could land as high-confidence. Origin and certainty are different questions. A self-declared claim can still be well-sourced; an independent claim can still be thin. Both dimensions need to be visible, not merged into one number.

**Check the incentivized flag before citing any review count.** A vendor-solicited review base is Self-declared, not Independent, regardless of how many reviews it holds.

**Certainty grades still apply, as a second, separate signal:**
Confirmed, high confidence this is accurate, regardless of origin
Reported, credible but not fully verified
Inferred, our own read, explicitly stated as opinion

### 2.2.1 The absence bar

**Absence is a finding, and it has to meet a standard before it is written as confirmed.** A single failed retrieval is evidence of a failed retrieval, not of absence.

**A guessed URL returning 404 proves the guess was wrong.** It proves nothing about the company. This has produced false absences more than once and it is the most common way the bar gets missed.

**The standard scales to what is being claimed**, because a flat number is wrong in both directions.

**Bounded absence**, a named artifact in a place that is authoritative for it. No G2 listing, checked on G2. No filing, checked at the register. **One authoritative path is sufficient**, and the path is named in the finding. A second path adds cost and no confidence.

**Unbounded absence**, a claim about everywhere. No documentation anywhere, no AI claim on their site, no pressroom. **Two independent access paths minimum**, both named, and the claim is written with its scope attached: *not found on their site or in search*, never *does not exist*.

**Where only one path was tried on an unbounded claim**, record it as `🟠 Reported` and name the path. Do not upgrade it to `✅ Confirmed` later without trying the second.

**Category-level absence beats company-level absence.** Where a source type turns out not to cover the category at all, record that once with its evidence rather than as an absence row per company. The alternative generates work forever and implies a listing we have no reason to expect.

### 2.2.2 Name collisions, the wrong company

**A perfectly sourced finding about the wrong company is still wrong.** Source honesty asks who said it. This asks who it is about, and nothing downstream catches the mistake: the citation is real, the quote is real, the company is not ours.

**Some tracked names collide with a louder namesake**, a near-identical spelling belonging to a larger company in another market, or a common word that returns unrelated businesses. An unqualified search returns the namesake, and the finding arrives clean, cited and about the wrong entity.

**The identifier goes in the query, not only in the record.** Where a name is ambiguous, every query for that company carries its unique identifier, a domain or a registration number, per the Search condition in §10. `competitor-list.md` owns which names collide and what each one's identifier is. This rule owns what the run does about it.

**Verify before scoring, not after.** A finding on a colliding name is tied to the identifier before it reaches a sheet: the domain on the page, or the registration number on the record. A result that cannot be tied to the identifier is recorded as `🟠 Reported` with the ambiguity named, never `✅ Confirmed`.

**A name variant is the same company.** Where a company appears under more than one spelling, the variants resolve to the existing profile rather than opening a second one. The competitor list records the variant so a later run does not re-open it.

### 2.3 Talk vs implement verdict

Talk, positioning, visibility, advisory, announcement with nothing shipped
Implement, a real product or process change, evidenced

### 2.4 The reality check gap format

[Their claim], origin tag, source (linked), certainty
[What evidence shows], origin tag, source (linked), certainty
Verdict: Talk or Implement

**The five founding rules:**
1. Separate the claim from the evidence, never blend into one sentence
2. Tag origin and certainty for each side independently
3. Apply the talk-vs-implement verdict once both sides are gathered
4. Find the gap, that divergence is the actual insight
5. State what the gap means for us specifically, not just that it's unverified

### 2.5 Corporate events

A corporate event is a change to the company itself rather than to its product or its claims: **funding, acquisition, partnership, integration, senior hire, ownership change.**

**Why they are captured separately.** These are the hardest evidence of where a company is actually committed, because each one costs money or people. A press release states an intention; an acquisition is an intention already paid for. Captured as prose in a changelog they become unreadable within a cycle, which is why they carry a type.

**Where they live.** The Signal history table on the competitor profile, all tiers, typed in the Type column. Same table as every other signal, so there is one shape per section. Full format: `competitor-profile-template.md`.

**Recency filter.** §2.1 applies to the reporting of an event, not to the event itself. A funding round from eleven months ago is not a new signal, but it is legitimate standing evidence and belongs in the table with its own date. This is the one place the system looks back further than a cycle, and it does so because commitment compounds where a claim does not.

**Source honesty.** §2.2 applies unchanged. A company announcing its own acquisition is Self-declared. A company register or a filing is Independent.

**No talk-versus-implement verdict.** A corporate event has no such state. The Grade cell is left empty, and an empty Grade on a corporate row is correct, not an unfinished verdict. `language-guidelines.md` Part 1 carries the matching exemption.

**Positioning is the seventh type.** A change to how the company categorises itself, sourced from the press descriptor or the standing boilerplate, is typed Positioning and also carries no Grade. Full method: `competitor-profile-template.md`.

**Who captures them.** The monthly reality check, on every profile, per the all-tier rule in §7. §9 still applies: any skill that discovers one writes it to the profile in the same session.

### 2.6 The market lens

Every research object in this system is company-indexed. That makes category-level questions unanswerable: what is converging on us, what is becoming commoditised, what buyers are starting to want. The market lens is the reading pass that answers them.

**It is a reading pass, not a scan.** It runs monthly, over evidence the reality check has already collected. It never triggers its own research.

**Four inputs, all already collected.**

*Tier 5, per §1.* The platforms the category sits on top of or gets absorbed into. The question per entry is where their offer intersects ours.

*Regulatory movement itself*, not competitor moves on it. Adopted, delayed, amended, consultation opened or closed, enforcement date reached. Sourcing and scope: `watch-list.md` Topic 2.

*Unattributed losses, read as buyer behaviour.* A loss that names no vendor still names a want. The CRM is already the permanent store; what was missing was the reading.

*Prospect-named companies we do not track.* Per §1 these now trigger a profile, and they also stand as a market observation regardless of the tier outcome.

**Two blocks, never merged.** Our theme watches, owned by `about-us.md`, are the company's strategy anchors. Anything observed that does not fit one of them goes in a separate block labelled *observed in the market, not ours*.

**No promotion rule.** A market theme does not become one of ours by appearing often enough. Counting appearances would let the market edit our self-knowledge. A recurring market theme becomes a Product conversation. Adoption is a strategy decision, made by a human, recorded in `about-us.md`.

**Trajectory without storage.** Each cycle's matrix carries a since-last-cycle column, read off the previous edition. Heating, cooling or unchanged. Nothing new is stored.

**Where it is written.** The market lens section of the monthly page, drawn from the Theme Watch activity matrix in the working record. Both defined in `monthly-review-template.md`.

### 2.8 The bets pillar

**A bet is where a competitor is going, inferred from what they have already paid for.** The two scoring axes answer whether a move is real and whether it matters. Neither answers direction, which is the question a product strategy needs.

**Three tags, all mandatory.**

*Evidence class*, what the bet is inferred from, ranked by how hard it is to reverse:

1. Acquisition or capital allocation, an intention already paid for
2. Shipped product, verifiable and in general availability
3. Hiring pattern, a standing function rather than one role
4. Partnership or integration, a commitment with someone else's name on it
5. Positioning change on the standing boilerplate, which moves only on a decision
6. Announcement with none of the above

*Conviction*, what they have actually spent to make it true. Money, headcount, an acquisition, a descriptor they now have to maintain everywhere. This is the tag that stops a press release counting as a bet.

*Distance from us*, measured against the directions and non-goals in `about-us.md`. Three values only:

- **On our path**, they are betting on something we are also betting on
- **Adjacent**, neither our direction nor a stated non-goal
- **Divergent**, they are betting on something we have explicitly chosen not to chase

Name the stretch in one clause. "Divergent" on its own tells a reader nothing.

**The exclusion rule.** A bet missing any of the three tags is excluded, not shown partial. A bet we cannot evidence, cannot show conviction for, and cannot place against our own direction is a guess, and publishing it as a finding launders the guess into a fact.

**Where distance cannot be answered because our own direction is silent, the silence is the output.** Log it as a gap for Product rather than inventing a position. The model never guesses our own strategy.

**One exemption, the open questions.** `about-us.md` records the questions Product has not settled. A competitor bet landing on one of those is **flagged, not scored**. Scoring it would grade a competitor against a position we do not hold. Raise it as evidence bearing on an open decision and stop there.

**Corporate events feed this pillar rather than being scored by it.** §2.5 captures them because each one costs money or people, which is exactly what the conviction tag reads.

### 2.9 Persona schema

**Schema only. The roles themselves are self-knowledge and live in `about-us.md`.** A fork inherits these seven fields with no company content inside them.

A persona is defined by seven fields:

1. **Role name**, the job title as spoken by customers, not a category we invent
2. **Side of the exchange**, demand or supply
3. **Product surface touched**, which parts of the product they actually open
4. **Job to be done**, what they are trying to accomplish, in their words
5. **What they are measured on**, how success is judged for them internally
6. **Chose or received**, did this person select the tool, or was it handed to them? This separates a buyer from a user and predicts whether ease of use or coverage wins an argument
7. **Where their voice appears publicly**, review sites, professional networks, forums, or nowhere at all

Field 7 is the hinge. It turns a definition into a collection instruction, which is why the persona layer must exist before any evidence is collected against it.

**Three evidence states, not two.** A field is *evidenced*, with a speaker count where it is thin; *empty by design*, where filling it would mean inventing it; or **tested and confirmed absent**, where the search was run and the thing genuinely is not there. The third is a finding, not a gap, and it must be distinguishable from the first two. A field marked absent carries what was searched.

**Evidence rules.** A role seen once is a hypothesis, not a persona. Contradictions between customers describing the same title are reported, not averaged. Any evidence base drawn from our own conversations carries a stated bias: it only contains people we already talk to.

**Archetype frictions are research questions.** Each archetype in `about-us.md` carries a key friction, evidenced from real users. For every documented friction, the standing question about a competitor is **has that competitor solved it**, and the answer is looked for in the Layer 2 sources that would show it: onboarding articles in a help centre, a supplier-facing surface, a permission model, an invitation flow.

**A friction raises the threat score. It does not create a second one.** The theme watches score a move against our strategy. A friction scores it against evidence that a real person is blocked. Both feed **the same Axis 2 number**, and a move that removes a documented friction scores 4-5 whether or not it touches a theme watch.

This matters for a practical reason. Any output that ranks candidates mechanically by threat needs exactly one number to sort on. A parallel friction score would leave two numbers and no defined order, and the ranking would quietly become editorial. State the friction as the reason for the score, in the same line that carries the score.

A competitor removing a documented blocker is a threat whether or not it touches one of our anchors, and that is usually the sharper read of the two.

**This creates no new research layer and no new source type.** The frictions change what is asked of Layer 2, not where Layer 2 lives. When a friction changes in `about-us.md`, nothing here needs editing, which is the point of holding the rule here and the frictions there.

**Frictions do not become theme watches.** A friction is evidence about behaviour; a theme watch is a statement of strategy. Promoting one to the other would let audience research edit our strategic anchors, which is the same error §2.6 has a no-promotion rule to prevent. Adoption is a human decision, recorded in `about-us.md`.

**Until archetypes are defined in `about-us.md` for a given side of the product, no competitor evidence is collected against them for that side.**

---

## 3. Scoring system, two independent axes

**A single relevance score conflates two different questions. They are separate and both must be visible.**

### Axis 1, Talk vs Implement (is it real?)

Talk, announced or claimed, nothing verified as shipped
Implement, verified as actually running, shipped, or live

### Axis 2, Threat level (does it matter to us?)

Independent of Axis 1. Scored against the theme watches. **The list is owned by `about-us.md` and is not restated here.** Read it there. A copy in two files is how the previous version came to hold nine themes while the scoring matrix used eleven.

High (4-5), Strikes at a core differentiator or theme watch, active deal, or ICP. Act now.
Moderate (3), Worth monitoring.
Low (1-2), Note and move on.

**The critical rule: a pure announcement (Talk) can still score 4-5 on threat level if it strikes at a core theme watch.**

Example: a competitor announcing free-for-suppliers pricing is a high threat the moment it's said, waiting to see if they actually ship it before treating it seriously would mean reacting too late. Conversely, a fully shipped (Implement) feature can stay moderate or low if it's tangential to our segment.

**Display both axes together, always:** e.g. "Talk · High 4/5" or "Implement · Moderate 3/5", never collapse into a single score.

**Scoring triggers for Axis 2 (threat level):**
- Competitor moves on a theme watch (especially transparency, network effect, lowest customer effort, visibility at scale) → 4-5, regardless of talk/implement status
- Competitor ships something that removes a friction documented in the buyer archetypes → 4-5, per §2.9. Name the friction as the reason for the score
- Competitor publishes on a regulation we cover → 4-5
- Competitor publishes on a regulation we do not cover → 2-3 (gap signal, flag to product)
- Competitor AI move touching transparency or auditability → 4-5
- Generic AI automation claims with no evidence → 2-3
- Competitor gets analyst coverage shaping enterprise shortlists → 4-5
- General thought leadership, culture, hiring content → 1-2
- Topic-specific triggers live with their topic in `watch-list.md`

**Visibility line:** [Company] was [very active / active / quiet] this [period]. They mainly talked about [theme].

**Signal classification:**

| Threat score | Classification | Flag | "So what for us" | Editorial gate | Follow-up tracker |
|---|---|---|---|---|---|
| 5 | Existential | Yes | Always (callout) | Always | Yes |
| 4 | Strategic | Yes | Always (callout) | Proposed | Yes |
| 3 | Watch | No | Never | If escalating | Yes |
| 2 | Context | No | Never | No | No |
| 1 | Noise | No | Never | No | No |

Classification is driven by Axis 2 (threat) alone. Axis 1 (talk/implement) is always displayed alongside but never determines whether something gets flagged.

**Corporate events are not scored on either axis.** They are evidence of commitment, not a move against us. Their weight is read in the market lens and in the profile changelog. They do not count toward the candidate total, but they can be selected into the final three.

**Follow-up tracker status:**
Escalating, threat score rose since last cycle, or a Talk item became Implement
Still open, no change
Resolved, signal played out

---

## 4. OKR signal tags

Max 3 per document. Only when: (1) connects to an active OKR, (2) implies a concrete action this week/month. Signal relevance only, never assign team ownership. OKRs live in `about-us.md`.

---

## 5. Employee list rules

**Tier 1:** top 10 scored on seniority (1-3) + LinkedIn activity (1-3), minimum combined 4. Tie-breaker: product/GTM over culture/HR.
**Tier 2 and below:** C-level only.
**Storage:** Competitor Employee List database, related to Competitor Profiles.
**Review cadence:** full rescoring every 6 months.
**Monthly use:** scan tracked employees' recent posts, dated within the current cycle only, for reality-check-relevant signals (early product hints, hiring focus, team stability, sentiment, conference/analyst engagement, credibility checks, internal tooling reveals, tone shifts). Lightweight, no rescoring, just signal scanning feeding into the profile's evidence tables. Same recency filter applies (§2.1).

---

## 6. Editorial gate, human vs AI role

**Claude owns:** all research (both layers), Axis 1 and Axis 2 scoring, signal classification, flag proposals, "So what for us" drafts, key learning/3-things candidates with reasoning, monthly reality check execution, lost deal table pull, market lens drafting, Slack post draft, contextual closing line options.

**The human owns:** final selection of top 3 (digest) or top 3 key learnings (monthly review), full editorial authority, no constraint. Adjusting scores when internal context changes the picture. Escalation decisions between tiers. Employee list revalidation. Adoption of any market theme into the theme watch list. Any claim requiring first-hand sales/CS/product knowledge. Picking or rewriting the Slack closing line.

**The principle:** Claude scores on market signals. The human corrects based on internal reality. The gate is a context injection step, not a validation step.

**The gate is a stop, not a checkpoint.** Claude does not write the digest page, the monthly page, or any Slack post until the human has confirmed the selection. This holds in every permission mode, including auto, and holds even if the request says to just run it. If a run ends with nothing written, that is a correct outcome. The order is fixed: research and scoring, stop for the human, Notion write, then Slack options.

**One exemption, §9 profile updates.** Competitor Profiles entries are written through the §9 write plan at the end of the research pass, independently of the gate. Those are a record of what was found, not an editorial choice. Everything else waits.

**No skill configures itself.** A skill may search for a workspace value and ask for confirmation, but it never writes its own configuration. Project knowledge is read-only at runtime, so any attempted write silently does nothing. Report the delta and ask the human to update `configuration.md`.

---

## 7. Workflow architecture, five skills

**Weekly digest**, Layer 1 only, enriched by the latest reality check's findings as context (not restated in full, referenced and acted on). Reads: latest monthly page + previous digest's follow-up tracker. Every finding shown with both Axis 1 (talk/implement) and Axis 2 (threat) visible. Outputs: digest page, 3 Slack options, tracker entry.

**Monthly reality check**, a job with two outputs, not a single document. It is Layer 2 research run monthly. It reads the previous cycle's competitor profiles and the CRM lost deal data. It applies the recency filter (§2.1) and source honesty tags (§2.2) to everything it finds. It feeds two separate consumers:

1. **Competitor Profiles database**, every profile's evidence tables, positioning block, signal history and changelog get updated through the §9 write plan at the end of the research pass (per §9, the always-true rule). This is the detailed, permanent record.

   **All-tier refresh.** The monthly reality check refreshes the Layer 2 section on every competitor profile, all tiers, not just Tier 1. Tier 1 keeps its full treatment on top. Lower tiers get, at minimum, a re-scan of their Layer 2 section against the source types in `evidence-registry.md` with the recency filter, and a light glance at their orientation section.

2. **The monthly page**, one page per month holding the review, the market lens and the working record in a toggle. Summarises rather than repeats: what each competitor says vs what we can verify, what moved in the category, and where the opportunity sits. Audience: Product, Sales, C-level. Structure: `monthly-review-template.md`. Voice: `language-guidelines.md` Part 3.

   *This replaces the previous pair of sibling pages, a review and a working record, which carried the same month and date and were indistinguishable from outside. The review is distributed to Slack like the digest, because a monthly document with no distribution does not get read.*

**Competitor profile setup**, once per new competitor. Scans both layers, fetches help center, records source addresses in the Evidence Registry database, proposes employee list candidates. Also triggered by any prospect-named company we do not track, per §1.

**Competitive mission**, open-scope ad hoc research. If the request is vague, ask for scope clarification before researching. If comparative analysis against us is requested without our own side available, flag the gap and ask whether to proceed without it or wait, never guess.

**Dependency chain:**
```
Profile setup → Reality check (job) → Competitor Profiles database (updated via the §9 write plan at end of pass)
                                    → Monthly page (review + market lens + working record)
                                         ↓
                                    Weekly digest (reads the monthly page as enrichment)
```

---

## 8. Lost deal data

**Field names and connection status are workspace-specific, read them from `configuration.md`, never hardcode them here.** This section defines the method, not the exact endpoint names.

**Approach:** pull from the structured lost-reason field first, competitor-relevant values look like "Chose competitor (solution fit)" or "Chose competitor (relationship or brand)". Cross-check against the free-text reason field for competitor name extraction the structured field misses.

**Unattributed losses are not discarded.** A loss that names no vendor still names a want. Those records are read as buyer behaviour and feed the market lens (§2.6) rather than the lost-deal table.

**Meetings/calls cross-check:** query both meetings and calls objects, filtered by creation date within the period. Sum both objects, activity-type data is often sparse on meetings alone. Dedup any scheduling-tool pairs by datetime and title so the same booking doesn't count twice.

**Period:** always the previous calendar month (or quarter, if cadence moves to quarterly) relative to when the reality check runs.

**Table format:** one row, competitor names as columns with counts, zero entries excluded, Unknown column always present.

**The deals-lost line is conditional.** It appears on a profile only when a lost-deal source is connected. Without one, the line is omitted and the rest of the profile is unchanged.

**If no lost-deal source is connected, or the fields in `configuration.md` aren't set:** run the reality check without this section and say so explicitly in the output. Never fail the whole reality check over a missing lost-deal pull.

---

## 9. The always-true rule

**Every discovery reaches the Competitor Profiles database in the same session it is found, through a write plan, not at the next scheduled reality check.**

This applies regardless of which skill surfaced the finding: weekly digest, monthly reality check, a competitive mission, or an ad hoc lost-deal pull. If something new is learned about a competitor, the profile page is the single source of truth and must reflect it the same session it was found.

**The write plan.** Each finding becomes one line in a plan: the profile, the section, the new text, its origin and certainty tags, and its event date. The plan runs at the end of the research pass, without a gate. Each line is verified before it runs. A line that fails verification leaves the plan, and the profile stays as it was. A line that cannot run, for a blocked permission or a lost connection, is reported with what landed and what did not, and every other line still runs. One blocked write never holds the rest.

In practice, each line covers:
- Update the Changelog block at the top with what changed and when
- Update the relevant evidence table row rather than only adding a new signal history line
- Update the positioning block if the descriptor or boilerplate moved
- Update Strategic Relevance (both axes) if the new evidence changes the picture
- Update Last Updated
- Apply recency filter and source honesty tags to any new evidence added

Why this matters: dated findings that live only in a digest or a mission page go stale and get lost. The profile is the only place guaranteed to be read every time, by the next digest, by sales, by the next reality check. If it isn't updated there, it effectively didn't happen.

---

## 10. Sufficiency

*What a run needs before its output can reach the human gate, and how the system checks it. Read at the end of setup, and again before every gate. Applies to ci-system-setup, weekly-digest, monthly-reality-check and competitor-profile-setup. Competitive mission keeps its own three-findings rule in its skill.*

*This section owns the conditions, their pass tests, the diagnosis order, and the input map that ranks every setup input by criticality. It does not own scoring, which stays in §3, the recency window, which stays in §2.1, or cadence, which lives in `configuration.md`. The setup inputs themselves are collected by ci-system-setup.*

### 10.1 The conditions

*A condition is something the system can check by itself. Whether a judgment is right is never checked here. That stays with the human at the gate.*

**1. Search.** The run knows what to scan and where.
- At setup, the digest passes when: at least 3 watch topics each state why, what to scan for, and a noise floor, the activity level below which the topic's movement is not treated as a signal; at least 3 Tier 1 companies have a name plus a unique identifier, such as a domain, wherever the name could be mistaken for another; the tracked set holds at least 8 companies across at least 3 tiers, not counting Tier 5 defaults that are not companies; and every Tier 1 company has at least one source in the Evidence Registry.
- At setup, the profile passes when: the company has a name plus a unique identifier.
- Before the gate, the run also passes search execution: every Tier 1 company and every topic returned at least one result about it, of any date; every query used the identifier; and every Tier 1 company has a live path, meaning a **fetchable** registry source with at least one dated item in the last 90 days. A source that cannot be retrieved, because it is robots-blocked or repeatedly errors, does not carry a live path on its own, and a row that records an absence carries none at all.

**2. Fill the gate.** The human has a real choice.
- Digest passes when: at least 4 candidates survive the recency gate (§2.1).
- Profile passes when: both research layers (§2) were searched, so a claim can be compared with what shipped.

**3. Weight.** Candidates can be ordered by importance.
- Both pass when: every threat score (§3) names its anchor. An anchor is a theme watch, a value driver, a documented buyer friction, a row of the regulation coverage table, or a scoring trigger in `watch-list.md`. A score with no named anchor counts as unweighted.
- Profile also needs: a tier placed on an evidence limb (§1), or marked provisional on a stand-in.
- An anchor proposed by Claude and adopted without evidence still counts, but the candidate says so.

**4. Trend, monthly reality check only.** A time comparison rests on enough history.
- Passes when enough reality-check cycles exist to show direction honestly. When they do not, present current state rather than direction of travel, and state how many cycles exist. If a baseline is needed, run a dedicated fresh search against the `watch-list.md` topics, topic by topic, flagged as a separate step, never compressed into the same session.
- This condition is checked only by the monthly reality check. It does not apply at setup, in the digest, or in a profile setup.

### 10.2 Diagnosing a failure

A failed condition is traced to its cause before it is reported, in this order:

1. **Setup.** An input feeding the condition is missing or fails its test in the map below. Reported as a finding about the setup, naming the input.
2. **Search execution.** Inputs pass, but the execution test fails: a company or topic returned nothing about it, a query skipped the identifier, or a Tier 1 company has no live path. Reported as a finding about the run, naming the company or topic.
3. **Market.** Inputs and execution both pass, and Fill the gate still fails. Only then is the window reported as quiet.

**A repeated quiet market is a cadence question.** When Fill the gate fails on market grounds for two consecutive windows, the run proposes a cadence or scope change, which the operator sets in `configuration.md`, instead of reporting a quiet market a third time. The human decides.

### 10.3 Input map

| Input | Owned by | Profile | Digest | Condition fed | Rank | Passes when |
|---|---|---|---|---|---|---|
| Tier 1 names with unique identifiers | competitor-list, Competitor Profiles | | ✓ | Search | Critical | At least 3, each with a domain or qualifier where the name is ambiguous |
| Evidence Registry sources | Evidence Registry | | ✓ | Search | Critical | At least one source per Tier 1 company, with an address, and at least one of them fetchable and carrying a dated item in the last 90 days |
| Watch topics, with what to scan for | watch-list | | ✓ | Search, Fill | Critical | At least 3, each with why, what to scan for and a noise floor |
| Theme watches | about-us | ✓ | ✓ | Weight | Critical | At least 5, each a dimension a competitor move can strike |
| Competitor name and identifier | profile request | ✓ | | Search | Critical | Name plus domain or qualifier |
| Regulation coverage | about-us | ✓ | ✓ | Weight | Critical when a scoring trigger depends on our own coverage, otherwise Important | Each tracked regulation marked covered, partial, not covered or monitor |
| Category, and what we are not | about-us | ✓ | ✓ | Weight | Important | Category named, and at least one thing the company is not |
| Value drivers | about-us | ✓ | ✓ | Weight | Important | Each names a buyer outcome, not a feature |
| Buyer frictions | about-us | ✓ | ✓ | Weight | Important | Each role has at least one evidenced friction |
| How the company came up, deal evidence | profile intake | ✓ | | Weight (tier limb) | Important | The occasion is named with a date or a deal |
| Tiers 2 to 5 | competitor-list | | ✓ | Fill | Important | Each name has a one-line tier rationale |
| Product direction and non-goals | about-us | ✓ | | Weight (bets distance) | Important | At least one direction and one non-goal |
| ICP archetypes | about-us | ✓ | ✓ | Weight | Important | Each segment has a stated need |
| Priorities or OKRs | about-us | | ✓ | none, sharpens tagging | Refinement | Current cycle, tied to competitive positioning |
| Loss patterns | about-us | ✓ | ✓ | none, sharpens scoring | Refinement | Drawn from deal data, not assumption |
| Material already held on a competitor | profile intake | ✓ | | none, speeds research | Refinement | At least one source dropped, with its usage limit |
| Tone, positioning vocabulary, reader groups | about-us | | ✓ | none, write phase only | Refinement | Register stated, with one sentence that sounds right and one that sounds wrong |

**Critical:** without it, a condition fails.
**Important:** conditions pass, but scoring flattens or a section is excluded.
**Refinement:** conditions pass and scoring holds. It only sharpens.

**Rich documents do not make a run searchable.** About Us, the watch list and the tiers make candidates weighable. Search depends on knowing where each company publishes, which is the Evidence Registry's job, and the registry matures run by run. A first run on a new setup should expect Search to be its weakest condition. At a profile setup the registry is written, not required: a new competitor has no registry rows yet, so the registry gates the digest, not the first profile.

### 10.4 Rules

**When the check runs.** At the end of setup, against the inputs only: the Search setup tests and the input map. Fill the gate, Weight, Trend and search execution only exist once a run has searched, so they are checked before every gate.

**A skip carries its cost.** Every skipped input is stated with the condition it weakens and the run it affects, from this map. A skip is never shown without that line.

**No padding.** A condition is never met by lowering quality. Candidates that failed recency do not count toward Fill the gate, and a score with no named anchor does not count toward Weight. An Evidence Registry row that records an absence is a finding, not a source, and never counts toward a live path. A source that cannot be fetched does not count toward one either.

### 10.5 Low-communication competitors

*Some competitors publish almost nothing dated. A registry built only from their own site and a static register record carries no live path at all, and the run cannot tell silence from blindness. These rules apply at setup, so a silent competitor is never mistaken for a quiet one.*

1. **Off-site-first.** Where a Tier 1 has no dated first-party surface, at least one off-site dated surface is registered before Search is declared set: the national job board, a register-announcement feed, a register-data aggregator, or third-party coverage.
2. **Fetchability.** A dated source that is robots-blocked or repeatedly errors does not satisfy the live path alone. Every blocked or repeatedly erroring official source is paired with a fetchable mirror, and the mirror is recorded in the registry as the retrieval route.
3. **The job board is a standing source.** Each Tier 1 carries its national job-board or careers employer page. Hiring is dated when it exists, and the kind of hiring, sales against engineering, is evidence for the AI topic rather than only a vacancy feed.
4. **Provisional detection date.** Where the only in-window dated item is an aggregator refresh rather than a self-published event, the live path is tagged provisional. Weight reads it as lower-confidence standing evidence, never as a dated move.
5. **Fallback tagging.** Where no fetchable dated surface is reachable at all, the competitor's result is tagged `🟠 Reported` under the absence bar in §2.2.1, naming the paths tried, and surfaced as a named finding. Silence is reported, never inferred as quiet.

**An undated index is not an undated company.** Where a newsroom or blog lists items without dates, open each item for its own dateline before deciding in or out of window. The dateline on the item is an event date and is preferred over any detection date. This is not confined to small vendors, the largest names do it too.

*Name collisions are a related but separate problem, owned by the competitor list and its identifiers, not by this section.*

### 10.6 Hypotheses under review

*Every threshold and rank here is a starting design. Each run's test log records which conditions passed or failed, and which cause a failure traced to. Review after five runs.*

- **Thresholds:** 3 watch topics, 3 Tier 1 companies, 8 tracked companies across 3 tiers, 4 candidates at the gate, a 90-day live path.
- **Ranks:** whether each Critical input is truly needed, and whether anything Important should be Critical. Open question: what a 5-minute setup can afford to lose.
- **Hypothesis anchors:** whether an adopted, unevidenced anchor should count toward Weight.
- **Fetchability:** whether an unfetchable dated source should fail the live path outright, as it does now, or count at a discount. Also whether an aggregator refresh is a strong enough dated item to carry a live path on its own, given it is a detection date and not an event date, and whether a source dated only to the month satisfies a 90-day window at its boundary.

---

*v1.19*
*v1.19 changes: re-anchor material to the §2.5 corporate-event taxonomy so partnerships, positioning changes and announced features count; make threat a strict subset of material so the levels nest; scope the bar to competitor-attributed sections, leaving the topic passes and the Follow-up tracker on their own noise floors.*
*v1.18 changes: define genuinely eventful as the Tier 2 to 4 inclusion bar, a three-level operator setting in `configuration.md` (any / material / threat, default material), governing inclusion and movement everywhere a non-Tier-1 change is reported.*
*v1.17 changes: §2.2.2 added, name collisions. A tracked name that collides with a louder namesake returns a clean, cited finding about the wrong company, so the identifier now belongs in the query and every finding on an ambiguous name is tied to a domain or registration number before it is scored. Which names collide stays with `competitor-list.md`; this section owns what the run does about it.*
*v1.16 changes: the live path now requires a fetchable source, and a row recording an absence never counts toward one. §10.5 added, the low-communication competitor rules: off-site-first sourcing, a recorded fetchable mirror where the official source is blocked, the job board as a standing source, a provisional detection date where the only dated item is an aggregator refresh, and fallback Reported tagging under §2.2.1 where nothing dated is reachable, plus the undated-index dateline rule. The Evidence Registry row of the input map gains the fetchable-and-dated test, No padding gains the absence and fetchability clauses, and fetchability joins the hypotheses. The per-run evidence paragraphs are removed from §10.6: the method carries rules and open questions, and run evidence lives with the run, not in the rulebook.*
*v1.15 changes: §10 added, the sufficiency conditions (Search, Fill the gate, Weight, and a monthly-only Trend), the diagnosis order, the input map, and the skip-cost and no-padding rules. The former data-sufficiency gate name is retired and folded into §10 as the Trend condition. The Evidence Registry is a critical Search input for the digest; at a profile setup it is produced, not required.*
*v1.13 changes: §1 gate-keeper gains the qualifying-loss definition, with a user-set recency window defaulting to 12 months. §2.1 gains a time window for every watch-list item, and the regulation source rule. §3 lets unscored items be selected into the final three. §6, §7 and §9 move profile updates to a write plan at the end of the research pass, without a gate. §8 makes the deals-lost line conditional on a lost-deal source.*
*v1.12 changes: the friction rule in §2.9 corrected. A friction raises the single Axis 2 threat score rather than producing a parallel one, because any output that ranks candidates mechanically needs one number to sort on and two would make the ranking editorial by accident. Matching scoring trigger added to §3. Header version stamp removed, per the single-stamp rule now in README.*
*v1.11 changes: §2.9 gains a third evidence state, tested and confirmed absent, which is a finding rather than a gap and must be distinguishable from empty. And it gains the friction rule: archetype frictions in about-us.md are standing research questions about competitors, scored against the friction rather than against a theme watch, with an explicit bar on frictions being promoted into theme watches. No new research layer and no new source type, so a friction changing in About Us needs no edit here.*
*v1.10 changes: two rules migrated in from the weekly digest skill, where they were carried inline against the ownership rule. §2.1 gains the window definition, re-anchored to the previous window's end rather than to the run date so contiguity holds when a run slips, plus a carve-out for first public disclosure. §2.2.1 added, the absence bar, scaled to bounded versus unbounded claims rather than a flat path count, with the guessed-404 rule and the category-level precedence written in. Both now live with the method rather than with one skill.*
*v1.9 changes: §2.8 added, the bets pillar. Three mandatory tags, evidence class ranked by reversibility, conviction as what has actually been spent, and distance measured against the directions and non-goals now held in about-us.md. Bets missing a tag are excluded rather than shown partial, silence about our own direction is logged for Product rather than guessed, and a bet landing on one of Product's open questions is flagged rather than scored. The persona schema moves from §2.7 to §2.9.*
*v1.8 changes: section 1 gate-keeper rule amended to define what counts as named in an active evaluation, and to state that a single mention is a profile rather than a tier. Recorded after a company surfaced once in one deal and the rule as written would have placed it at Tier 1 on arrival. Written as an evidence test rather than a count, for consistency with the no-promotion rule in 2.6.*
*v1.14 changes: the first-run window default and the inline-prompt override named in §2.1.*
*v1.7 changes: §1 Tier 5 redefined as the platforms the category sits on, and prospect-named unknowns now trigger a profile rather than vanishing on a negative tier review. §2.5 added, corporate events, seven types carrying no talk-implement verdict and exempt from the recency filter on the event date. §2.6 added, the market lens, four already-collected inputs read at category level with two blocks that never merge and no promotion rule. §2.7 added, the persona schema, seven generic fields with instances living in About Us. §3 stops restating the theme watch list, which About Us owns, the drift that produced nine themes against eleven. §7 monthly outputs consolidated into one page. §8 unattributed losses routed to the market lens instead of being discarded.*
*v1.6 changes: §6 gate strengthened from a statement of ownership into an explicit stop, and the §9 profile-update exemption named.*
*v1.5 changes: §7 monthly reality check specified as an all-tier job.*
*v1.4 changes: §8 CRM lost-deal field names moved out to configuration.md.*
*v1.3 changes: Monthly review template shipped, data-sufficiency gate named as a rule.*
*v1.2 changes: two-axis scoring model, recency filter, source honesty tags.*
