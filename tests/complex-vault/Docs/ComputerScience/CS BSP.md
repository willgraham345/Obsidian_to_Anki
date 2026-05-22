---
summary: A board support package, which is the layer of low-level software that bridges specific piece of hardwRE with the OS or app code running on top of it. Think of this as the "glue" that makes generic sofware aware of your specific hardware's quirks, peripherals, and memory layout.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
aliases:
  - CS Board Support Package
concept_of:
  - "[[CS Embedded Computing]]"
date created: Monday, February 23rd 2026, 8:47:18 am
date modified: Monday, February 23rd 2026, 9:02:43 am
tags:
  - cs/firmware
  - cs/firmware/bsp
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[CS Clock Configuration]]"
  - "[[CS Hardware Abstraction Layer]]"
  - "[[CS Interrupt Vector Table]]"
  - "[[CS Memory Map and Linker Script]]"
  - "[[CS OS Porting]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎 BSP ;; A board support package, which is the layer of low-level software that bridges specific piece of hardwRE with the OS or app code running on top of it. Think of this as the "glue" that makes generic sofware aware of your specific hardware's quirks, peripherals, and memory layout.

## Concepts of Note
Typically contains:
- Startup & init code
- [[Hardware abstraction layer]]