# Contributing

This repo is a method, not a workspace. It is built to be forked and run by any
company, so everything in it stays generic and nothing in it identifies whoever
is running it.

## The one hard rule

**Never commit anything that identifies a real organisation.** This applies to
every file, every commit and every pull request, whatever the change is about.
It is not a checklist item on a ticket; it outranks the ticket.

Never in this repo:

- the name of the company running the system, or any of its people
- any real customer, prospect, account or deal name
- any real competitor name, including inside an example
- real figures: deal values, revenue, customer or deal counts, OKRs
- internal addresses: Slack channels, CRM field names, document IDs or URLs
- any insight that reveals who runs the system, or what its competitive
  position is

Examples use **Groundline**, the invented demo company. If an example needs a
second company, invent one. Every company shown in this repo is fictional, and
that has to stay true.

If you are unsure whether something identifies a real organisation, treat it as
if it does.

## Before you open a pull request

Run the release check:

```
cp .release-denylist.example .release-denylist   # first time only
scripts/check-release.sh
```

It fails if any term in your denylist appears in a tracked file. Fill the
denylist with your own real names: your company, your people, your customers
and deals, and the competitors you actually track.

`.release-denylist` is gitignored on purpose. Committing it would publish
exactly the list it is there to protect.

A clean run exits 0. Do not open a pull request on a failing check.

## Why this is strict

Real names reach a public repo through examples, not through data files. The
workspace files are obviously yours, so they get handled carefully. A "good
versus bad" writing example, a gate-modification example, or a one-line skill
description is where a real name slips through unnoticed and then sits there
for months.

A later scrub does not undo it. Removing a name in a new commit leaves it
readable in history, in the diff of the commit that removed it, and in any
fork taken before the fix.
