---
summary: Common log sink for systemd. Kernel, network devices, services, and even other system sources that might not be immediately relevant are put into the journal. Similar to the Windows event logs. Accessed with jounralctl.
type: note/tool
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
similar: ["[[Linux systemctl]]"]
date created: Tuesday, December 3rd 2024, 10:05:58 am
date modified: Wednesday, January 21st 2026, 11:32:37 am
template: "[[base_note_template]]"
template-version: 1.0.1
uses: ["[[Linux dmesg]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
The `journald` daemon handles all the messages produced by the kernel, initrd, servcies, etc.

## Usage


 `journalctl <path_to_executable>` ;;; Show all messages by a specific executable captured by systemd-journald
 `journalctl _PID=<pid>` ;;; Show all messages from a specific process captured by sytemd-journald
 `journalctl -b` ;;; Show all messages from the current boot session.
 `journalctl -u <service>.service` ;;; Show all messages filtered by a given service
 `journalctl -x` ;;; Show all messages in system, augmented with explanation texts from the message catalog.
 `journalctl -e` ;;; Show all messages in system, jumping to the end of the pager.
