# Bug template

Use this when a ticket turns out to be our bug. Save the write-up in bugs/ as BUG-<short-name>.md. It's a draft: nothing gets filed until the PM says so.

```
# <What's broken, for whom, in one line>

**Release:** <version and the change it came from, or "not release-related">
**Severity:** <high / medium / low, and why in one clause>
**Impact:** <how many walks or owners since launch, from analytics/>

## What the customer saw
<one or two sentences, in their words>

## What actually happened
<timeline from the GPS session and logs, oldest first>

## Evidence
- walk_gid: <id>
- trace_id: <id>
- GPS session: <session_id>
- Log lines: <quote each one>

## Cause
<file, the line, and what it does>

## Suggested fix
<the smallest change that fixes it>

## How to check the fix
<what to look for in logs or analytics after it ships>

## Linked support ticket
<ticket number and customer_id>
```
