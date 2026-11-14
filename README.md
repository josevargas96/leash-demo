# Leash demo (ProductTank Denver, Nov 18)

A fake dog-walking company, built so you can show how a real investigation turns into a skill. Every name, ID and number here is made up.

## The story

On Monday Nov 2, Leash launched **Walk Done alerts**. When the walker brings your dog home, you get a ping with a photo and how long the walk was, so you stop texting your walker "is she back yet?" And you only pay for real walks: a walk has to last at least 20 minutes to count.

It's Wednesday. Support is sending the PM tickets, and every one asks the same thing: is this the new release?

## What's in here

| Folder | Pretends to be |
| --- | --- |
| tickets/ | Support tickets. They only have a CRM link, never the customer's name in a usable form. |
| services/ | Our microservices: customers, bookings, walks, walkers. Each is a JSON file. |
| sessions/ | A GPS session-replay tool, keyed by walk_gid. |
| logs/ | Service logs with trace IDs, like an observability tool. |
| src/ | The code behind the 20-minute rule and the Walk Done alert. |
| docs/ | Product notes (how things are supposed to work) and release notes (what shipped Monday). |
| backup/ | A finished copy of the skill, in case the live build stalls. |

## The ID chain (the part people don't know)

CRM link -> customer_id -> account_gid -> booking_gid -> walk_gid -> GPS session and log trace_id.
You can't jump straight to the session by name. That's the knowledge you teach the agent.

## The three tickets

| Ticket | The customer says | Actually | The release? |
| --- | --- | --- | --- |
| 1 | "I never got the walk done alert, so I thought the walker didn't come. But I was charged." | The walk happened. The alert tried once, the alert service was busy, and retries are off. Our bug. | Yes: the new alert |
| 2 | "I was charged for a walk the walker cut short because of a storm." | Lightning auto-cancel. The refund was issued on the spot and takes 3 to 5 days. Working as intended. | No: that's been live since October |
| 3 | "The app said my walk didn't count, but my dog was walked. I even got a photo." | The walker's phone lost GPS for 26 of the 41 minutes, so the app only saw 15 minutes. Under 20, so no charge and no pay for the walker. Edge case: what do we want to do? | Yes: the new 20-minute rule never planned for lost signal |

## Demo flow

1. Open Claude Code in this folder. Make sure there is no .claude/skills folder yet.
2. **Ticket 1, by hand.** Walk it one step at a time:
    - "Here's a support ticket. Pull the customer ID out of the CRM link."
    - "Look them up in services/customers.json and grab the account_gid. Heads up, everything after this is keyed by account_gid, not the name."
    - "Find their bookings in services/bookings.json. The ticket says today, so pick the one that matches the sent date."
    - "Get the walk_gid for that booking from services/walks.json."
    - "Replay that walk in sessions/gps-sessions.json. What actually happened?"
    - "Search logs/service-logs.jsonl for that walk_gid and follow the trace_id across services."
    - "Something failed. Open the code in src/ and tell me what it expects."
    - "Give me a verdict: bad data, user behavior, our bug, working as intended, or edge case. Then check docs/release-notes.md: is this from Monday's release? Quote the evidence."
3. **Ticket 2, on its own.** "Now do ticket 2 the same way, by yourself."
4. **Make the skill.** "Turn what we just did into a skill called leash-ticket-triage: the steps, the verdicts, the release check, the output format, and an empty case library."
5. **Ticket 3, fresh session.** Run /clear, then "triage ticket 3." It should land on the edge case and ask what we want to do.
6. **Add a guardrail** if it slips anywhere (for example, blaming the 20-minute rule for ticket 2): "Add a rule: check docs/product-notes.md and the release notes before calling anything a bug. Add this ticket to the case library."

## If something goes wrong

Copy the backup skill into place and keep going:

```
mkdir -p .claude/skills && cp -r backup/leash-ticket-triage .claude/skills/
```

To reset before a rehearsal or the real thing:

```
rm -rf .claude/skills
```
