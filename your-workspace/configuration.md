# Configuration

*Workspace-specific values every skill reads before running. Confirmed once per Notion connection, then read, never re-searched. No page IDs recorded here on purpose, titles only, so the system stays portable across Notion workspaces.*

*Nothing here gets written by a skill. Project knowledge is read-only at runtime, so a skill that finds a mismatch reports the delta and asks you to update this file by hand, and a skill that searches for a title here and finds no exact match stops and names the field to set and the value it searched for, rather than running thin on a missing resource. That's deliberate: a configuration change is always visible to a person, never silent.*

---

## Setup Progress

| Step | Status | Notes |
|---|---|---|
| 1. Read existing files | Not started | |
| 2. Build Notion structure | Not started | |
| 3. Content (About Us, Competitor List, Watch List) | Not started | |
| 4. First competitor evidence batch | Not started | |
| 5. Suggest cadence, walk through scheduling | Not started | |

---

## Notion

*Fill each title below with the exact name of the page or database you created in Phase 2. The skills find each one by searching this title, so it must match what is in Notion, character for character. An example value follows each field.*

**Competitive Intelligence home page (title to search):** *e.g., Competitive Intelligence*
**Type:** Markdown page
**Status:** unconfirmed

**Competitor Profiles database (title to search):** *e.g., Competitor Profiles*
**Type:** Database
**Status:** unconfirmed

**Competitor Employee List database (title to search):** *e.g., Competitor Employee List*
**Type:** Database
**Status:** unconfirmed

**Digest Impact Tracker database (title to search):** *e.g., Digest Impact Tracker*
**Type:** Database
**Status:** unconfirmed
*If you want to track what a digest caused, not just whether it was read, you'll also want a Digest Actions database, a relation between the two. See the setup skill for the full shape of both, it's worth building even though it's more schema than the minimum.*

**Digest Actions database (title to search, optional but recommended):** *e.g., Digest Actions*
**Type:** Database
**Status:** unconfirmed

**Evidence Registry database (title to search):** *e.g., Evidence Registry*
**Type:** Database
**Status:** unconfirmed
*Live-maintained by the skills, not a static file. `templates/evidence-registry.md` defines the source types, this database holds the actual addresses.*

**Flash Report Template page (if mirroring it into Notion):**
*If you keep a Notion copy of any template alongside the Project knowledge one, both must be updated together, or they will drift. This has happened in real use, worth taking seriously rather than as a theoretical risk.*

**Monthly page:** one page per month, titled `Monthly Competitor Review, [month] [year]`

---

## Slack

**Default channel for digest posts:**
**Status:** not configured
*Channel choice can be editorial and vary by edition if you want that flexibility, in which case track which channel each post actually went to rather than assuming the default every time.*

---

## Your CRM (lost-deal data)

**Status:** not configured

**Lost-deal reason field (structured):**
**Lost-deal reason field (free text):**
**Activity objects to query:**
**Activity type values that count:**

*If activity-type data is inconsistently entered in your CRM, expect a large "unassigned" bucket. Report it as a floor, not a count, and decide whether the section is worth including until data discipline improves, rather than presenting an unreliable number as precise.*

*If not configured, or if a field mismatch is found, the reality check skill runs without the lost-deal pull and says so explicitly, rather than failing the whole run.*

---

## External sources

*Anything your category needs watched that isn't a competitor-by-competitor scan, a regulatory tracker, an industry index, a standards body's own feed. One saved search or feed per tracked item beats relying on a person to notice manually.*

---

## Settings

*Method knobs with sensible defaults. Change a value here, never in a skill. The eventfulness bar is defined in `analysis-rules.md` §1.*

**Eventfulness bar (Tier 2 to 4 inclusion):** material
*What pulls a non-Tier-1 competitor into an output, and what counts as a reportable movement for one. One of:*
- *any: any dated, observable change. Highest volume, most noise.*
- *material (default): a dated, sourced corporate event per §2.5 (funding, acquisition, partnership, integration, senior hire, ownership change, positioning change), a shipped or announced product feature, a pricing or packaging change, a named customer win or loss, or a regulatory action.*
- *threat: a strict subset of material that also moves the threat score or targets our buyers. Lowest volume.*
*A claim with no observable change behind it never qualifies, at any setting. Tier 1 is never gated, always included. The bar gates competitor-attributed sections (Competitor pulse, Three things, profile changelog); the topic passes (This week in AI, Regulation watch) and the Follow-up tracker are not gated by it.*

---

## Scheduled tasks

| Task | Cadence | Notes |
|---|---|---|
| | | |

*If you split a cadence skill into a research pass and a separate write pass in the same conversation thread (recommended once you're running this regularly, since a writing rule read hours before it's applied tends to get dropped), record both halves here, not just one, and note which day each runs.*

*Cron schedules are typically evaluated in UTC. If your local timezone observes daylight saving, note here when the actual local time will shift, so a "same time every week" assumption doesn't quietly become an hour off.*

---

*Confirmed by: [pending first run]*
*Last confirmed: [pending]*
