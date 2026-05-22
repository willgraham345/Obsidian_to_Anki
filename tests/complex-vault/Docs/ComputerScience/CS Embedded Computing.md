---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
concepts:
  - "[[CS ACPI]]"
  - "[[CS BSP]]"
  - "[[CS Embedded Bus Types]]"
  - "[[CS Events]]"
  - "[[CS Interrupts]]"
  - "[[CS Kernel]]"
  - "[[CS Virtual memory]]"
  - "[[Linux kernel module]]"
same:
  - "[[Readings embedded]]"
associations:
  - "[[CS Architecture]]"
concept_of:
  - "[[CS|Computer Science]]"
date created: Thursday, December 11th 2025, 9:46:09 am
date modified: Monday, April 6th 2026, 4:05:29 pm
implementations:
  - "[[Python Memory]]"
items:
  - "[[ECE Embedded Processors]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
tools:
  - "[[Buildroot]]"
  - "[[CS Compiler]]"
  - "[[Networking Protocols]]"
uses:
  - "[[ECE Bootloader and Bootmanager]]"
  - "[[ECE Hardware connectors]]"
---

# Summary
󰙎 Embedded computing ;;; The type of code that computers *actually* run on. This is the processor's ISA, and is typically built from programming languages.

# Additional Background
[Introduction — The Linux Kernel documentation](https://linux-kernel-labs.github.io/refs/heads/master/lectures/intro.html)

## Concepts of Note
󰙎 REPL ;; Read eval print loop, something that is often used for debugging.

󰙎  Kernel ;;; The central software that manages and allocates computer resources (i.e. CPU, RAM, and devices).

󰙎  System call ;;; An entry point into the kernel for a given process

󰙎  Pipes ;;; "FIFO" which can be used to transfer data between processes

![[Linux signals#^3ca4bd]]

󰙎  Signal handler ;;; A programmer-defined function automatically invoked when the signal is delivered to the process. ^a05265

󰙎 Address space ;;; Can refer to: physical address space in RAM, virtual address space (how the CPU sees memory).

󰙎 Process space ;;; Part of the virtual address space associated with a process. The "memory view" of processes. Continuous area that starts at zero.

󰙎 SFP ;;; Small form factor pluggable, a compact hot-pluggable transceivers used in network switches and routers to convert electrical signals to optical/electriclal signals. Data rates from 100 Mbps to 10 Gbps. Commonly use LC connectors for fiber, and RJ45 for copper.

󰙎 LKM ;;; Linux kernel module, a way to combat a monolithic kernel which is a loadable module that can extend kernel functionality at runtime (loaded as it is needed). Most device drivers operate as kernel modules.