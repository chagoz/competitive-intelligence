# Setup Guide, Installing the Competitive Intelligence System

*A simple checklist to get everything running on a new Claude account. Follow the steps in order, don't skip ahead, some steps depend on the one before.*

*[Your name] x Claude · August 17, 2026*

---

## Before you start

You'll need:
- [ ] Access to the Claude account you're setting this up on
- [ ] Notion connected to that account, with access to your workspace
- [ ] Slack connected, if you want digest posts distributed there (optional)
- [ ] Your CRM connected, if you want lost-deal data in the monthly reality check (optional, the system works without it)
- [ ] The knowledge files and skill zips from this system, downloaded somewhere you can find them

If any connector (Notion, Slack, your CRM) isn't available yet, that's usually an admin setting on Team or Enterprise plans. Ask whoever manages your workspace to turn it on before you continue, steps 2 onward won't fully work without it.

---

## Step 1: Create the Project

- [ ] Create a new Project in Claude
- [ ] Name it something clear, for example "[Your Company] Competitive Intelligence"

**Why a Project and not just a regular chat:** a Project holds files (Project knowledge) that every conversation inside it can read automatically, without you re-uploading them each time. That's what makes the skills work without repeating yourself.

---

## Step 2: Upload the knowledge files

- [ ] Open the Project, find "Project knowledge" (sometimes called "Add content" or similar)
- [ ] Upload all thirteen files below. Claude's Project knowledge is flat, it doesn't preserve folders, so grab each file from wherever it lives in the repo and upload it directly, the repo's folder structure (`your-workspace/`, `rules/`, `templates/`, `docs/`) is just for keeping the GitHub repo itself organized, it doesn't need to be recreated inside the Claude Project:
  - From `your-workspace/`: `configuration.md`, `about-us.md`, `competitor-list.md`, `watch-list.md`
  - From `rules/`: `analysis-rules.md`, `language-guidelines.md`
  - From `templates/`: `digest-template-structure.md`, `slack-message-template.md`, `competitor-profile-template.md`, `flash-report-template.md`, `evidence-registry.md`
  - From `docs/`: `skills-index.md`
  - The root `README.md`

**Why all of them at once:** the skills reference each other, for example the digest skill reads `analysis-rules.md` and `language-guidelines.md` together. If some files are missing, the skill will still run but may make mistakes or ask you questions it shouldn't need to ask.

**Before you upload `about-us.md`, `competitor-list.md`, and `watch-list.md`:** these three are templates, not filled-in content. You'll answer the questions inside them either by hand, or by letting the setup skill in step 5 ask you and write the answers for you. Either way, they need real content before the rest of the system will produce anything useful, this is the one part of setup that's actually about your business, not just configuration.

**Not uploaded to the Project:** `LICENSE`, `CHANGELOG.md`, `starter-prompt.md`, and this file itself, `setup-guide.md`. These are for the GitHub repo and for humans reading it, not reference material Claude needs mid-task.

---

## Step 3: Add the skills

- [ ] Go to Settings, find "Skills" (sometimes called "Customize" or "Capabilities")
- [ ] Upload each zip file one at a time: `weekly-digest.zip`, `monthly-reality-check.zip`, `competitor-profile-setup.zip`, `competitive-mission.zip`, `ci-system-setup.zip`
- [ ] Make sure "Code execution and file creation" is turned on too, some skills need it to write files

**Why zips and not the plain files:** Claude Skills are uploaded as a zip containing one `SKILL.md` file each. That's just the required format, nothing to configure inside it.

**If skills can be added at the Project level instead of the account level:** do that instead, it keeps this system separate from anything else on the account. If that option doesn't exist yet, account-level is fine.

---

## Step 4: Add the Project instructions

- [ ] In the Project, find "Custom instructions" (sometimes called "Project instructions")
- [ ] Paste this in:

```
This project holds the source-of-truth documents for our competitive 
intelligence system. Before any competitive intelligence task, read 
about-us.md and analysis-rules.md. For writing output, also read 
language-guidelines.md (the relevant part: 1 for all documents, 
2 for Weekly Digest, 3 for Quarterly Review) and the matching template 
file. Always read configuration.md before touching Notion, Slack, or 
your CRM, never use a page ID or field name from memory. Treat the 
uploaded documents as current and authoritative, they are a deliberate 
snapshot, not a live Notion mirror.
```

**Why this matters:** without this, Claude won't automatically know to check these files first. This one paragraph is what ties the knowledge files and the skills together.

---

## Step 5: First run, the five-step setup flow

- [ ] Start a new conversation inside the Project
- [ ] Type: `set up competitive intelligence system`
- [ ] This triggers `ci-system-setup`, which runs five steps in order. Each one is tracked in `configuration.md`, so if you stop partway through, typing `continue setup` later picks up where you left off rather than starting over.

**Step 1, read existing files.** Claude checks what already exists, in Project knowledge and in Notion, and reports back plainly. Nothing gets created yet.

**Step 2, build the Notion structure.** For anything step 1 found missing (a database, a page), Claude shows you the proposed shape, fields and all, and waits for you to confirm before creating it, one item at a time. Confirm each carefully, if Notion turns up something with a similar name that isn't quite right, an old page instead of a database, a stray duplicate, don't assume it's the one, check before pointing the system at it.

**Step 3, content.** If About Us, Competitor List, or Watch List don't already have real content (see the note in step 2 above), Claude asks four questions and writes them for you: who your company is, who your competitors are by tier, what topics you want to watch, and what your voice or brand guidelines look like. If these documents already have real answers filled in, this step is skipped automatically, you won't be asked to re-answer anything already on file.

**Step 4, first competitor evidence batch.** Claude shows your Tier 1 competitor list and asks whether to run research on all of them now or a smaller batch first. **Say yes to something here.** Skipping this step is the single most common way this setup goes wrong, the Notion structure gets built but stays empty, because nothing ever actually asked for real data. Don't skip past it.

**Step 5, cadence and scheduling.** Claude suggests when the Weekly Digest and Monthly Reality Check should run, then walks you through setting each one up as a Cowork scheduled task yourself, it won't create the schedule for you, just tell you exactly where to click.

- [ ] Once step 2 is confirmed, ask Claude to save it: "please save these confirmed values to configuration.md"
- [ ] Download the updated `configuration.md` and re-upload it to Project knowledge, replacing the old version, do this again after any step that changes it

**Why you do this manually:** Claude can edit files in a conversation, but Project knowledge files need to be re-uploaded by you to actually update what every future conversation reads. This is the one manual step that repeats through the setup.

---

## Step 6: Test that it actually works

Run through these three checks before trusting the system day to day:

- [ ] **Weekly digest test.** Let it finish a full run, check the Notion page it creates looks right, and that it stopped and asked you to confirm the top 3 before writing anything (it should never skip this).
- [ ] **Slack test, if connected.** Check the Slack post options it drafts, and that it asks where to post rather than posting automatically.
- [ ] **CRM test, if connected.** Run the monthly reality check and confirm the lost-deal table has real numbers in it, not an empty table or an error.

If any of these don't work, don't try to fix it mid-run, stop and check `configuration.md` first, most first-time issues come from a value that got confirmed against the wrong Notion page.

---

## Quick reference, if something breaks later

| Problem | Most likely cause |
|---|---|
| Claude can't find a Notion page | The title in `configuration.md` doesn't match the actual page title, or Claude doesn't have Notion access turned on |
| Claude writes to the wrong database | `configuration.md` was confirmed against a duplicate or old page, check for a stray page with a similar name |
| Slack post doesn't send | Claude should never send it automatically anyway, check it's asking you where to post, not trying to post itself |
| CRM data comes back empty | your CRM isn't connected, or the field names in `configuration.md` don't match your workspace, check `analysis-rules.md` §8 for what it's expecting |
| A skill seems to ignore the rules | Check all the knowledge files actually uploaded, a missing `analysis-rules.md` is the most common cause |
| Notion structure exists but everything is empty | Step 4 of setup (first competitor evidence batch) never ran or was skipped, run `continue setup` and say yes when it offers to process your Tier 1 list |

---

*This system was built for and by a real company's competitive intelligence practice, then generalised for anyone to fork. The three files that need your own answers, not generic ones, are `about-us.md`, `competitor-list.md`, and `watch-list.md`, everything else is reusable methodology as-is.*
