---
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Configuration]]"
date created: Tuesday, March 3rd 2026, 3:30:34 pm
date modified: Tuesday, March 3rd 2026, 3:38:28 pm
implementations:
  - "[[Linux mount]]"
  - "[[Linux network]]"
  - "[[Linux PID]]"
  - "[[Linux time_namespaces]]"
  - "[[Linux user_namespaces]]"
  - "[[Linux uts_namespaces]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Linux namespaces ;;; Wraps a global system resource in an abstraction that makes it appear to the process within the namespace, so everything is isolated. 

# Additional Background
## Concepts of Note

### Namespace types

| Namespace | Flag              | Page | Isolates                             |
| --------- | ----------------- | ---- | ------------------------------------ |
| cgroup    | `CLONE_NEWCGROUP` |      | cgroup root directory                |
| IPC       | `CLONE_NEWIPC`    |      | System V IPC & POSIX message queues  |
| Network   | `CLONE_NEWNET`    |      | Network devices, stacks, ports, etc. |
| Mount     | `CLONE_NEWNS`     |      | Mount points                         |
| PID       | `CLONE_NEWPID`    |      | Process IDs                          |
| Time      |                   |      | Boot and monotonic clocks            |
| User      |                   |      | User and group IDs                   |
| UTS       |                   |      | Hostname and NIS domain name         |

## Configuration
[[Linux Filesystem Hierarchy#proc/pid/ns]]