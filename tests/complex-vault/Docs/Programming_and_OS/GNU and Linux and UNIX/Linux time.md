---
type: note/item
headings:
  - "[[#Concepts of Note]]"
classes:
  - "[[timespec]]"
concepts:
  - "[[Linux time_namespaces]]"
date created: Tuesday, March 3rd 2026, 3:42:24 pm
date modified: Tuesday, March 3rd 2026, 3:45:39 pm
item_of:
  - "[[Linux]]"
items:
  - "[[Linux hardware clock]]"
  - "[[Linux system clock]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[Time and Time Servers]]"
  - "[[Unix Epoch]]"
---

# Summary
󰙎 Linux time ;;; How linux uses time and timers to make things happen.

# Additional Background
## Concepts of Note
󰙎 Hardware clock ;;; A clock most computers have that is battery-powered, and runs even when powered off. Hardware clock read by the kernel at boot time.
󰙎 System clock ;;; The kernel supports a range of clocks, which are accessed by [[clock_gettime]]