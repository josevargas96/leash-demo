---
name: leash-ticket-triage
description: Triage a Leash support ticket that links to a customer in the CRM, say whether it comes from the latest release, draft a bug write-up when it's our bug, report how the release is going, and point out one user-behavior pattern worth knowing. Use when given a Leash ticket or a crm.leash.example customer link and asked what happened.
---

# Leash ticket triage

Follow these steps in order. Do not skip a step, and do not guess an ID.

1. **Get the customer ID** from the CRM link in the ticket (the part after /customers/, like CUS-48213).
2. **Find the account** in services/customers.json. Note the account_gid. Everything after this is keyed by account_gid, never by name.
3. **Pick the booking** in services/bookings.json. A customer can have several; use the ticket's sent date and wording ("today", "yesterday afternoon") to choose the one that matches. Say which one you picked and why.
4. **Get the walk** from services/walks.json using the booking_gid. Note the walk_gid and the walk status.
5. **Replay the GPS session** in sessions/gps-sessions.json for that walk_gid. Describe what actually happened, in order.
6. **Follow the logs** in logs/service-logs.jsonl: find lines for that walk_gid, then follow the trace_id across every service.
7. **Check the code** in src/ for anything that failed or made a decision, and say what it expects.
8. **Check the product notes** in docs/product-notes.md before calling anything a bug.
9. **Check the release** in docs/release-notes.md: is this tied to a change in the latest release? Name the change, or say it isn't related.
10. **Size it** in analytics/walks-since-launch.csv: how many other walks look like this one since launch?
11. **If it's our bug,** write it up for the developers with docs/bug-template.md and save it in bugs/. It's a draft. Never file it anywhere.
12. **Release health:** from analytics/, compared with analytics/week-before-launch.json, give three numbers on how the release is going: alerts delivered, walks that didn't count (and why), and owner texts to walkers per walk.
13. **One pattern worth knowing:** look through analytics/ for one thing users are doing that isn't a bug but the PM should know about. Give the numbers and what it might mean. Don't say what to build; the PM decides.

## Verdict (pick exactly one)

- **Bad data**: the records themselves are wrong or missing.
- **User behavior**: the customer or walker did something unexpected.
- **Our bug**: our system failed to do what it is designed to do.
- **Working as intended**: the app did what the product notes say.
- **Edge case**: the system did what the code says, but the code never planned for this. Ask what we want to do.

## Output

1. One-line verdict, plus whether it's from the latest release (and which change).
2. A short table: step, what you found, evidence (quote the record or log line).
3. What to tell support, in two sentences they can paste.
4. For a bug: the path to the bug write-up in bugs/. For an edge case: the product question, with how many walks it touches.
5. Release health: three lines, numbers only, compared with the week before launch.
6. One pattern worth knowing: two sentences, with numbers. An observation, not a recommendation.

## Rules (added after mistakes)

- Check the product notes before calling anything a bug. If the app did what it is designed to do, it is working as intended.
- Quote the evidence for every claim. No evidence, no claim.
- Never file a bug or message anyone. Draft only; the PM decides.
- Count with a script, never by eye.

## Case library

- Charged after a storm cut the walk short: lightning auto-cancel, refund already issued, 3 to 5 business days. Working as intended, and not from 4.12 (shipped in 4.11).
