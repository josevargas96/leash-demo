# Walk Done alerts that fail once are never retried, so owners think the walker didn't come

**Release:** 4.12 (Mon Nov 2), Walk Done alerts
**Severity:** High. The owner is charged but hears nothing, and it reads like a no-show.
**Impact:** 43 of 1,241 Walk Done alerts since launch failed (3.5%). Those owners texted their walker about 8 times as often as owners who got the alert.

## What the customer saw
"I never got the walk done alert, so I thought the walker didn't come. But I was charged $25."

## What actually happened
1. 1:58 PM: walker arrived at the owner's address.
2. 2:02 PM: walk started.
3. 2:18 PM: photo uploaded.
4. 2:33 PM: walk ended. 31 tracked minutes, so it counted and the owner was charged.
5. 2:33 PM: the Walk Done alert failed with a 503. It was not retried.
6. 2:34 PM: email receipt sent.

## Evidence
- walk_gid: wlk_7f9e44
- trace_id: tr_7f9e44d
- GPS session: gps_7f9e44
- Log line: "walk done alert failed: alert service busy (503); retries off (MAX_RETRIES=0), not retried"

## Cause
src/notifications/walk_done_alert.py sets MAX_RETRIES = 0 for launch week, so one busy response from the alert service means the alert is never sent.

## Suggested fix
Turn retries on (for example MAX_RETRIES = 3 with a short backoff). Resend the alert for the 43 walks that missed it, or at least tell those owners the walk happened.

## How to check the fix
alert_status = failed in analytics/walks-since-launch.csv should drop close to zero, with no "not retried" lines in the logs.

## Linked support ticket
Ticket 1, CUS-48213
