---
summary: 
headings: ["[[#Diagrams]]"]
type: note/item
similar: 
date created: Thursday, August 14th 2025, 12:25:34 pm
date modified: Thursday, August 14th 2025, 12:38:12 pm
diagrams: ["[[poll.puml]]"]
item_of: ["[[Linux Processes]]"]
uses: ["[[UNIX File Descriptor]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  poll ;;; Function that waits for one of a set of file descriptors to become ready to perform I/O. = #cs/linux/process/poll  
<!--ID: 1758253289431-->

󰙎  epoll ;;; Linux-specific version of Poll which: monitors multiple file descriptors to see if I/O is possible on any of them. = #cs/linux/process/poll 
<!--ID: 1758253289438-->

󰙎  epoll instance ;;; In-kernel data structure. From a user-space perspective, it can be considered  as a container for two lists.
󰙎  interest list ;;; (a.k.a. epoll set), the set of files descriptors that the process has registered in interest of monitoring. = #cs/linux/process/poll  
<!--ID: 1758253289444-->

󰙎  ready list ;;; Set of file descriptors that are "ready" for I/O. This is really a subset of the earlier "interest list", which is dynamically populated as I/O activity on fd's ensues. = #cs/linux/process/poll  
<!--ID: 1758253289451-->


## Diagrams
![[poll.puml]]
