# Evidence Registry, Method

*What a source type is, what it reveals, its priority and how often it gets checked. **No URLs.** Every address lives in the Evidence Registry database, named in `configuration.md`, which is the only authoritative source for where to look.*

*This file previously carried per-company URL tables. They were removed on September 4, 2026 because they had gone stale against the live database, and a stale address read as current is the exact failure the source-honesty rules exist to prevent. We do not keep two copies of the same thing, and if the system ever moves, the database moves with it.*

---

## Why this exists

The reality check compares what a competitor claims (Layer 1) against what they actually do (Layer 2). Layer 2 evidence lives in a small set of source types. Finding the addresses takes real effort the first time, which is why they are recorded once, in the database, and revisited by priority order every cycle rather than rediscovered.

This file defines the types. The database holds the instances.

---

## Source type reference

| Source type | What it reveals | Priority | Check frequency | Effort |
|---|---|---|---|---|
| Help centre / documentation | What actually shipped. If it is documented, it exists | Critical | Monthly | Low |
| G2 profile | User evidence, feature reality, pricing signals. Check the incentivized flag before citing any count | Critical | Monthly | Medium |
| Capterra profile | SMB user reviews, ease of use, support quality | High | Monthly | Low |
| Gartner Peer Insights | Enterprise and procurement-side reviews. Often the only independent review base for companies absent from G2 and Capterra. Reviewers are validated but frequently vendor-solicited, so treat as weak independent | High | Monthly | Low |
| Careers / job board | What they are building next, where they invest, and whether they sell as infrastructure or as a self-serve product | Medium | Monthly | Low |
| Press / newsroom | Announcements, partnerships, corporate events | Critical | Weekly | Low |
| LinkedIn company page | Weekly content signals, positioning shifts | Critical | Weekly | Low |
| Product pages | Currently claimed capabilities | High | Monthly | Low |
| Pricing page | Cost signals, packaging changes, and which function the offer addresses | Medium | Monthly | Low |
| Positioning descriptor | The one-line self-category in press ledes, plus the standing boilerplate. The two fields that move when positioning moves | High | Quarterly | Low |
| Review-site category | Which categories a vendor chose to be listed and compared under. Present state only, no retrievable history | Medium | Quarterly | Low |
| Public company register | Ownership, filings, headcount, accounts. Often the only independent window on a private company with no pressroom and no reviews | High | Quarterly | Medium |
| Analyst coverage | Framing that shapes enterprise shortlists. Already a scoring trigger, so it needs a source behind it | High | Quarterly | Medium |
| Supplier-facing surface | Whether a supplier help centre exists, whether it is free, what a supplier gets back, what cascading costs. The supply side of the exchange | High | Quarterly | Medium |

**On TrustRadius, checked and dropped September 4, 2026.** TrustRadius does not cover supplier sustainability due diligence. Both relevant category pages were read: ESG lists general reporting and finance tooling, and Vendor Risk Management lists information-security products. None of the tracked companies appears in either. Recorded once in the database as a category-level finding rather than as an absence row per company, and replaced in this table by Gartner Peer Insights, which does carry our companies. Recheck quarterly in case the category shifts, but do not re-search company by company.

**Priority legend.** Critical, check every cycle without exception. High, check unless time-constrained. Medium, check on a full pass.

**Cadence note on the quarterly types.** A positioning descriptor changes on the order of years, and a company register updates on a filing schedule. Checking them monthly spends the whole tracked set of fetches to confirm nothing.

---

## Rules that travel with the sources

**Dates.** Every Layer 2 citation carries its date. Full rule: `analysis-rules.md` §2.1. Corporate events are the one exemption, per §2.5.

**Origin before certainty.** Who said it is a different question from how sure we are. Both are recorded. Full rule: `analysis-rules.md` §2.2.

**Absence is a finding.** A source type that does not exist for a company gets recorded as absent, with the search trail, rather than left blank. A company with no help centre, no reviews and no pressroom is telling you something.

**Incentivized reviews are Self-declared.** A vendor-solicited review base is the company's own words with extra steps, regardless of how many reviews it holds. Check the flag before citing any count or average.

### Date traps, carried forward

Several sites serve dates that are not publication dates. A session that trusts them will report false signals.

- **Read the body dateline, not the page header.** Header dates are often content-migration artifacts and can be more than a year out.
- **A "last updated" line on a review site is a page refresh**, not a new review. It has produced false signals on companies whose reviews were all years old.
- **A review-site modified date is a content-management artifact**, and sort order is not reliably chronological, so a single "most recent" pull is not proof that nothing newer exists.
- **An image upload path is not a publication date.**
- **A vendor listing that renders without any dates** means absence of a visible date, not absence of an event. Treat as baseline and say so.

---

## The registry as a byproduct

Source addresses are recorded by the profile setup skill as part of the first deep scan, not filled in by hand as a separate task. The monthly reality check revisits them by priority order and updates the last-checked date. A broken address gets fixed on the row, with the date of the correction.

---

## For a fork

Replace nothing here. This file is method and travels as is. Build your own rows in your own database, and add a source type only if it reveals something none of the above does.

---

*v2.1*
*v2.1 changes: TrustRadius checked at category level, found not to cover this category at all, and replaced by Gartner Peer Insights which does. The absence is recorded once as a category finding rather than as 25 rows. Also recorded: a document change that names a database field is not done until the database has the field, after the v2.0 source types were declared here and never added to the live select.*
*v2.0 changes: all per-company URL tables removed. This file is now method only, and the live database is the sole authoritative source for addresses. Four source types added: positioning descriptor, review-site category, public company register and supplier-facing surface. The date traps found during the August reality check written in as standing rules rather than left in a working record. Careers and pricing rows extended to name the infrastructure-versus-experience read they support.*
