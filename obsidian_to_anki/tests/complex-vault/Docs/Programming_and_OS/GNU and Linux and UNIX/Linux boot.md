---
summary: The process by which Linux boots and loads into a new environment
type: note/process
headings:
  - "[[#Concepts of Note]]"
  - "[[#Workflows]]"
processes:
  - "[[Linux boot#Boot process]]"
date created: Wednesday, January 21st 2026, 11:08:13 am
date modified: Wednesday, January 21st 2026, 11:16:07 am
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[Linux initrd]]"
  - "[[Linux systemd]]"
process_of:
  - "[[Linux]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
### Processes
##### Boot process
 start:
1. BIOS initializing hardware, running power on self test
2. Load bootloader ([[GNU GRUB]]) from MBR/EFI partition
3. Load kernel into memory and transfer control to it
	1. Starts [[Linux systemd]]
4. 

? Not sure where this happens...
1. Linux uses an initial ram disk ([[Linux initrd]]) containing essential drivers & tools required to mount the actual root filesystem.
 end:


