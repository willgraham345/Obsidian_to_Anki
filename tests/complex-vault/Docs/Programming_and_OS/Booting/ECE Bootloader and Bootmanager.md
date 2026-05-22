---
type: note
headings:
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, April 6th 2026, 4:07:14 pm
tags: []
template:
template-version:
used_by:
  - "[[CS Embedded Computing]]"
uses:
  - "[[CS ACPI]]"
---

# Background
- A bootloader starts first, and loads the kernel into memory and executes it
- A boot manager program allows you to choose between operating systems if there is more than one system. 

The most popular boot manager for Linux is [[GNU GRUB]]. 
- Alternatives include the systemd-boot manager, and the rEFInd boot manager (very customizable)

# Usage