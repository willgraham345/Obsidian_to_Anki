---
summary:
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Flashcards]]"
date created: Friday, December 12th 2025, 9:20:30 am
date modified: Monday, April 6th 2026, 3:55:22 pm
items:
  - "[[CS Scheduler]]"
tags: [cs/linux/kernel]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
󰙎 Kernel ;;; Core suprvisory software that provides minimal logic, scheduling, and resource management algorithms. Can be a combination of modules (file system, network protocols, device drivers, device IO, other components).

# Additional Background
## Concepts of Note
󰙎 Monolithic kernel ;; Runs all system services in kernel space
󰙎 Micro kernel ;; Runs only basic process comms and IO.
󰙎 Hybrid kernel ;; Combo of monolithic kernel and microkernel.

## Flashcards
󰠗 What is in the kernel space in a monolithic kernel? ;; The system call interface, the kernel, kernel functions, and device drivers.
󰠗 What is the distinction between a monolithic kernel and a microkernel? ;; No access protection between various kernel subsystems in monolithic kernel, and public function calls called between subsystems. Micro-kernel has large parts of the kernel protected from each other, usually running services in userspace (hence, the kernel is much smaller).



󰙎 Kernel objects ;; Tasks, task scheduler, interrupt service routines, semaphores, mutexes, mailboxes, message queues, pipes, timers


