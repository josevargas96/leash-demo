---
name: leash-ticket-triage
description: Triage a Leash support ticket that links to a customer in the CRM. Use when given a Leash ticket or a crm.leash.example customer link and asked what happened.
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

## Verdict (pick exactly one)

- **Bad data**: the records themselves are wrong or missing.
- **User behavior**: the customer or walker did something unexpected.
- **Our bug**: our system failed to do what it is designed to do.
- **Working as intended**: the app did what the product notes say.
- **Edge case**: the system did what the code says, but the code never planned for this. Ask what we want to do.

## Output

1. One-line verdict.
2. A short table: step, what you found, evidence (quote the record or log line).
3. What to tell support, in two sentences they can paste.
4. For a bug or edge case: what you would bring to engineering.

## Rules (added after mistakes)

- Check the product notes before calling anything a bug. If the app did what it is designed to do, it is working as intended.
- Quote the evidence for every claim. No evidence, no claim.

## Case library

- Charged after a lightning cancel: working as intended. The refund is issued at cancel time and takes 3 to 5 business days.
