---
summary: How we store and read anything. Huge stuff here.
type: note/system
headings:
concepts:
  - "[[ECE NVMe]]"
  - "[[ECE Volatile]]"
  - "[[Memory Nonvolatile]]"
date created: Tuesday, January 7th 2025, 4:29:36 pm
date modified: Wednesday, April 8th 2026, 9:10:07 am
tags: []
template:
template-version:
item_of:
  - "[[CS Memory Types]]"
---

# Summary

# Additional Background

󰙎 MMU ;; memory management unit, a thing in modern cpus which grants virtual memory. To each process, it appears that it has an entire machine to itself. It does this by intercepting memory calls from the process. When the process accesses some of its memory, the page table (MMU implementation) translates the memory location to the process point of view. 
󰙎 Page table ;; An implementation of an MMU. Translates 