---
summary: A process is the active management of a program, consisting of just about anything. There are different types of processes and Linux has functions/methods for interacting with ongoing processes.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
functions:
  - "[[Linux df]]"
  - "[[Linux free]]"
  - "[[Linux kill]]"
  - "[[Linux pidof]]"
  - "[[Linux ps]]"
  - "[[Linux ptrace]]"
concept_of:
  - "[[Linux]]"
  - "[[UNIX]]"
date created: Monday, December 16th 2024, 12:59:50 pm
date modified: Tuesday, December 30th 2025, 3:06:32 pm
items:
  - "[[Linux poll]]"
  - "[[Linux process limits]]"
  - "[[Linux Standard streams]]"
  - "[[UNIX File Descriptor]]"
tags:
  - cs/linux/kernel/syscall
  - cs/linux/process/environment
template:
template-version:
uses:
  - "[[Linux syscall exec]]"
  - "[[Linux syscall fork]]"
  - "[[Linux syscall setenv]]"
  - "[[Linux syscall setrlimit]]"
  - "[[Networking socket]]"
  - "[[Linux kernel memory]]"
concepts:
  - "[[Linux process capabilities]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  Environment list ;;; A set of environment variables that are maintained within the user-space memory of the process. Each element consists of a name and an associated value, created via `fork()`. When a process replaces the program it is using with `exec()` the new program either inherits the environment used by the old program or receives a new environment. 

![[Linux process limits#^30b9fe]]

## Concepts of Note
- Process happens in isolation, and can't directly communicate with another process. 
- Process can't itself create a new process or even end its own existence without the kernel.
- Processes call and assign memory as directed by the CPU. Modern CPUs have an MMU 