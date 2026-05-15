---
type: note/concept
headings:
  - "[[#Concepts of Note]]"
date created: Thursday, April 2nd 2026, 11:54:07 am
date modified: Thursday, April 2nd 2026, 11:58:54 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[CS Data Structures Page Table]]"
---

# Summary
󰙎 CS Virtual memory ;;; OS technique that creates abstraction of large, contiguous memory space for applications, using combo of RAM and disk storage to extend available memory.

# Additional Background
## Concepts of Note
### Page tables

### Demand paging 
󰙎 Demand paging ;;; Pages enter main memory only when requested or needed by the CPU
![[CS Virtual memory.png]]
1. Program Execution: Upon launching a program, the operating system allocates a certain amount of memory to the program and establishes a process for it.
2. Creating Page Tables: To keep track of which program pages are currently in memory and which are on disk, the operating system makes page tables for each process.
3. Handling Page Fault: When a program tries to access a page that isn't in memory at the moment, a page fault happens. In order to determine whether the necessary page is on disk, the operating system pauses the application and consults the page tables.
4. Page Fetch: The operating system loads the necessary page into memory by retrieving it from the disk if it is there.
5. The page's new location in memory is then reflected in the page table.
6. Resuming The Program: The operating system picks up where it left off when the necessary pages are loaded into memory.
7. Page Replacement: If there is not enough free memory to hold all the pages a program needs, the operating system may need to replace one or more pages currently in memory with pages currently in memory. on the disk. The page replacement algorithm used by the operating system determines which pages are selected for replacement.
8. Page Cleanup: When a process terminates, the operating system frees the memory allocated to the process and cleans up the corresponding entries in the page tables.