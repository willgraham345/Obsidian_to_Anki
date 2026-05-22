---
summary: The process of synchronizing system time across hardware and software components.
type: note/concept
headings:
concept_of:
  - "[[CS]]"
  - "[[Linux]]"
  - "[[Networking]]"
  - "[[Space]]"
date created: Monday, February 9th 2026, 9:20:53 am
date modified: Wednesday, March 18th 2026, 1:14:28 pm
items:
  - "[[clock_gettime]]"
  - "[[hwclock]]"
  - "[[NTP server]]"
  - "[[PTP Server]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1 - "[[Networking]]" - "[[Linux]]"
used_by:
  - "[[Linux Kernel]]"
  - "[[Linux time]]"
uses:
  - "[[hwclock]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

This is not necessarily *just* Linux time, but it happens to be surrounded by a bunch of Linux time stuff.

# Additional Background
󰙎 Monotonic clock ;; Varies in such a way that it only decreases/increases. Typically resets after each boot, and will go back to zero once it hits end. Used to be a bigger concern with 32 bit architectures, as the nanoseconds would run out every ~49 days.
󰙎 Syntonization ;;; Adjust frequency  of a local oscillator to match a master clock. "How long is time?"
󰙎 Synchronization ;;; Correct absolute time (phase) of the local clock to match master clock. "When is time?"