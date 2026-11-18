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
| logs/ | Service logs with trace IDs, like an observability tool. Only the walks support asked about. |
| analytics/ | Product analytics for every walk since launch, plus the week before, to see if the release is working. |
| src/ | The code behind the 20-minute rule and the Walk Done alert. |
| docs/ | Product notes, release notes, and the bug template. |
| backup/ | A finished copy of the skill and an example bug write-up, in case the live build stalls. |

## How the tickets get to Claude

For the demo, each ticket is a file in tickets/ and you hand it over in the chat. In real life the same skill can read a support channel every morning and triage whatever came in overnight.

## The ID chain (the part people don't know)

CRM link -> customer_id -> account_gid -> booking_gid -> walk_gid -> GPS session and log trace_id.
You can't jump straight to the session by name. That's the knowledge you teach the agent.

## The three tickets

| Ticket | The customer says | Actually | The release? |
| --- | --- | --- | --- |
| 1 | "I never got the walk done alert, so I thought the walker didn't come. But I was charged." | The walk happened. The alert tried once, the alert service was busy, and retries are off. Our bug. | Yes: the new alert |
| 2 | "I was charged for a walk the walker cut short because of a storm." | Lightning auto-cancel. The refund was issued on the spot and takes 3 to 5 days. Working as intended. | No: that's been live since October |
| 3 | "The app said my walk didn't count, but my dog was walked. I even got a photo." | The walker's phone lost GPS for 26 of the 41 minutes, so the app only saw 15 minutes. Under 20, so no charge and no pay for the walker. Edge case: what do we want to do? | Yes: the new 20-minute rule never planned for lost signal |

## The short run (three prompts, for a timed talk)

Each prompt takes Claude a minute or two, so the talk uses three:

1. **Ticket 1, in one prompt.** "Here's a ticket from support: tickets/ticket-1.md. Triage it end to end. Heads up: you can't find the walk by name. Go from the customer in services/customers.json (use the CRM link) to their booking in services/bookings.json to the walk in services/walks.json. Replay the walk in sessions/gps-sessions.json, follow its trace_id through logs/service-logs.jsonl, then read the code in src/. Give me a verdict: bad data, user behavior, our bug, working as intended, or edge case, and say whether it's from Monday's release (docs/release-notes.md). Quote the evidence. If it's our bug, write it up with docs/bug-template.md and save it in bugs/. End with three release-health numbers from analytics/ against the week before launch."
2. **Make the skill.** "Turn what you just did into a skill called leash-ticket-triage: the ID chain, the verdicts, the release check, a bug write-up when it's our bug, three release-health numbers every time, one user-behavior pattern worth knowing, and an empty case library."
3. **Ticket 3, fresh session.** Run /clear, then "Triage tickets/ticket-3.md."

If a step runs long, skip ahead with the finished skill:

```
mkdir -p .claude/skills && cp -r backup/leash-ticket-triage .claude/skills/
```

Then open backup/leash-ticket-triage/SKILL.md to show it, or run /clear and go straight to ticket 3.

## What you say to Claude

Talk to it like you're training a new hire: one step at a time, say the part only you know, and say what a good answer looks like.

1. **Ticket 1, by hand.** One step at a time:
    - "Here's a ticket from support: tickets/ticket-1.md. Pull the customer ID from the CRM link and look them up in services/customers.json. Heads up: everything after this is keyed by account_gid, not the name."
    - "Find their booking for today in services/bookings.json, then its walk_gid in services/walks.json."
    - "Replay that walk in sessions/gps-sessions.json, then follow its trace_id through logs/service-logs.jsonl. What actually happened?"
    - "Open the code in src/ for whatever failed. Give me a verdict: bad data, user behavior, our bug, working as intended, or edge case. And is it from Monday's release? Check docs/release-notes.md. Quote the evidence."
    - "It's our bug, so write it up for the developers with docs/bug-template.md and save it in bugs/. Use analytics/ to say how many other walks this hit. Then tell me how the release is going overall: check analytics/ against the week before launch and give me three numbers."
2. **Ticket 2, on its own.** "Now do tickets/ticket-2.md the same way, by yourself."
3. **Make the skill.** "That's twice. Turn what we just did into a skill called leash-ticket-triage: the ID chain, the verdicts, the release check, a bug write-up when it's our bug, three release-health numbers every time, one user-behavior pattern worth knowing, and an empty case library."
4. **Ticket 3, fresh session.** Run /clear, then "Triage tickets/ticket-3.md." It should land on the edge case, size it, ask what we want to do, and point out a pattern in how owners use the app mid-walk. You make the call out loud.
5. **Add a rule when it slips** (for example, blaming the 20-minute rule for ticket 2): "That was a lightning cancel, not the new rule. Add a rule: check the product notes and release notes before blaming the release. Add this ticket to the case library."

Before the demo, open Claude Code in this folder and make sure there is no .claude/skills folder or bugs/ folder yet.

## If something goes wrong

Copy the backup skill into place and keep going:

```
mkdir -p .claude/skills && cp -r backup/leash-ticket-triage .claude/skills/
```

To reset before a rehearsal or the real thing (this throws away every local change and new file in this folder):

```
git fetch origin && git reset --hard origin/main && git clean -fdx
```

If the bug write-up stalls, show backup/BUG-walk-done-alert-no-retry.md instead.
