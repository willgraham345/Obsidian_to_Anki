---
summary: Open source kernel written mostly in C. Modular design and monolithic in architecture.
type: note/system
headings:
  - "[[#Concepts of Note]]"
implements:
  - "[[CS Kernel]]"
concepts:
  - "[[Linux Cybersecurity]]"
  - "[[Linux groups]]"
  - "[[Linux Kernel Architecture]]"
  - "[[Linux Kernel cgroups]]"
  - "[[Linux kernel memory]]"
  - "[[Linux kernel module]]"
  - "[[Linux Kernel Namespaces]]"
  - "[[Linux Kernel Subsystems]]"
  - "[[Linux serial console]]"
  - "[[Linux signals]]"
similar:
  - "[[Linux microkernel]]"
date created: Friday, November 15th 2024, 2:59:47 pm
date modified: Tuesday, April 7th 2026, 5:47:13 pm
item_of:
  - "[[Linux]]"
items:
  - "[[Linux device drivers]]"
  - "[[Linux Devicetree Source (DTS) Files]]"
  - "[[Linux Kconfig and kbuild]]"
  - "[[Linux Kernel Core API]]"
  - "[[Linux Kernel Driver API]]"
  - "[[Linux kernel module]]"
  - "[[Linux Kernel TTY Layer]]"
  - "[[Linux proc]]"
  - "[[Linux seccomp]]"
tags: [cs/linux/kernel, cs/linux/kernel/syscall, cs/linux/process/interaction-with-kernel, cs/linux/process/IPC]
template:
template-version:
tools:
  - "[[Linux Kernel Core API]]"
uses:
  - "[[Linux syscall]]"
  - "[[Time and Time Servers]]"
---

---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Linux kernel - Wikipedia](https://en.wikipedia.org/wiki/Linux_kernel)

## Concepts of Note
[[CS Embedded Computing#Concepts of Note]]


[[UNIX Domain Sockets]]

### Tasks performed by the kernel:
- Process scheduling
- Memory management
- Provision of a file system
- Creation/termination of processes
- Access to devices
- Networking
- Provision of a system call API
