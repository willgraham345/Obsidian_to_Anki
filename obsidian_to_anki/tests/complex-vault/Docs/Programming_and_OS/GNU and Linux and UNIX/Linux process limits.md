---
summary: 
type: note/item
headings: 
date created: Tuesday, August 12th 2025, 11:59:12 am
date modified: Sunday, December 28th 2025, 1:44:07 pm
item_of: ["[[Linux Processes]]"]
tags: [cs/linux/kernel/syscall, cs/linux/process/limits]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰠗  Where are system-level limits (applying to all users/processes) stored in Linux? ;; `/etc/sysctl.conf` and `/etc/security/limits.conf` = 

󰠗  Where are user-level limits stored in Linux? ;; `/etc/sysctl.conf` and `/etc/security/limits.conf`, specified by username/group = 

󰙎  Resource limits ;;; Limits set on a process through a `setrlimit()` system call. There are soft limits (limits amount of the resource a process may consume), and hard limits which is a ceiling. 
^30b9fe 

