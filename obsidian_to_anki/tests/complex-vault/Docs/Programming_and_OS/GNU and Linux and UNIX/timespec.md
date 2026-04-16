---
type: note/class
headings:
  - "[[#Properties]]"
members:
  - "[[timespec#tv_nsec: `long`]]"
  - "[[timespec#tv_sec: `time_t`]]"
class_of:
  - "[[Cpp time]]"
  - "[[Linux time]]"
  - "[[POSIX.1b]]"
date created: Monday, March 2nd 2026, 2:55:22 pm
date modified: Tuesday, March 3rd 2026, 2:15:22 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 timespec ;;; Defined in `<time.h>`, and represents precise time value with second and nanosecond precision. Used almost everywhere to pass time between kernel and userspace.

# Additional Background
[timespec - cppreference.com](https://cppreference.com/w/c/chrono/timespec.html)

## Properties
##### tv_sec: `time_t`
󰫧 :
- description: Whole seconds
󰫧 end:

##### tv_nsec: `long`
󰫧 :
- description: Nanoseconds, valid between nanoseconds (valid values are [​0​, 999999999]). On some systems, `tv_nsec` may be of type `long` `long`.
󰫧 end:



