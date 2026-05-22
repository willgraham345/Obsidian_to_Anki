---
summary: Displays the kernel ring buffer (log buffer), which has messages from device drivers and kernel related issues. Works for most Unix-like devices. Think of this as printing kernel logs.
type: note/tool
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
similar: ["[[Linux journald]]", "[[Linux syslog]]"]
date created: Thursday, December 4th 2025, 2:45:19 pm
date modified: Thursday, December 11th 2025, 4:26:49 pm
tags: [cs/linux/kernel, cs/linux/networking/serial, TODO/learn, todo/refactor]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background  

## Concepts of Note
󰙎 Kernel ring buffer ;; Basically a log buffer where all the kernel boot messages are written. dmesg controls outputting these messages. 
- Hardware messages, boot up logs 

## Usage

 `dmesg | grep tty` ;;; Search your system for what serial ports are started