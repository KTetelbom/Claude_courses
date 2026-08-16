---
name: status-report-generator
description: Generate a concise weekly status report (done, in-progress, blockers, next steps) from a list of raw project updates or task notes. Use when the user asks for a status report, weekly update, or project summary.
---

# Status Report Generator

Turn a messy list of task updates into a clean, structured status report.

## Instructions

1. Read the raw notes provided by the user (bullet points, Slack messages, task
   titles, whatever format they come in).
2. Group them into four sections, in this order:
   - **Done** — completed since the last report
   - **In progress** — actively being worked on
   - **Blockers** — anything stuck, and what's needed to unblock it
   - **Next steps** — what's planned next
3. Keep each bullet to one line. Drop filler words, keep the concrete outcome
   or number if there is one (e.g. "Migrated 3/5 services" not "Made progress
   on the migration").
4. If a section has nothing to report, omit it entirely rather than writing
   "None".
5. Output plain Markdown with `##` headers for each section, ready to paste
   into an email or a doc.
