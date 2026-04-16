---
type:
headings:
  - "[[#Properties]]"
date created: Tuesday, March 3rd 2026, 3:27:54 pm
date modified: Tuesday, March 3rd 2026, 3:28:58 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[clock_gettime]]"
  - "[[timer_settime]]"
uses:
  - "[[clock_id]]"
implements:
  - "[[Linux namespaces]]"
---

# Summary
󰙎 Linux time_namespaces ;;; Linux timespaces virtualize the value of two system clocks: `CLOCK_MONOTONIC` `CLOCK_BOOTTIME`. There are a few APIs which measure against these clocks.

# Additional Background
## Properties

