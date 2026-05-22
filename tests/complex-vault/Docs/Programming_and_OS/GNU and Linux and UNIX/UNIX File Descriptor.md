---
summary: Part of the POSIX API. Each Unix process (except potentailly daemons) should have 3 standard POSIX file descriptors, corresponding to three standard streams.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
type: note/item
similar:
  - "[[Windows File Handles]]"
date created: Tuesday, August 12th 2025, 11:37:04 am
date modified: Tuesday, August 12th 2025, 12:11:31 pm
item_of:
  - "[[Linux Processes]]"
  - "[[POSIX]]"
  - "[[UNIX]]"
items:
  - "[[Linux Standard streams]]"
used_by:
  - "[[Linux poll]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Here is all you need to know about File Descriptors in linux \| by Ishan Dhar \| Medium](https://medium.com/@dhar.ishan04/here-is-all-you-need-to-know-about-file-descriptors-in-linux-d93f05166026) 

## Concepts of Note
󰙎  File descriptor ;;; Serve as the channel between user-space apps and kernel-space system calls using I/O operations which use standard streams. To perform input/output, the process passes the file descriptor through a system call and the kernel will access the file on behalf of the process. = #cs/linux/process/file_descriptor #cs/linux/stream/process_stdio_stdout 
<!--ID: 1758253289197-->

󰙎  File table ;;; Traditional implementation of UNIX for File descriptors, where they would be indexed into per-process descriptor tables. Tabled recording the mode with which the file has been opened (reading/writing/appending/other modes). 
- Traditional UNIX had file descriptors index into per-process descriptor table that the kernel would manage. 
󰠗  Where are the set of file descriptors open in a process available in Linux? ;; `proc/PID/fd/`, `PID` is the process identifier. = #cs/linux/process/file_descriptor  
<!--ID: 1758253289185-->

󰠗  What are the 3 standard streams for file descriptors? What is their integer value? What C-standard library are they respectively defined? ;; 0 -> standard input (`STDIN_FILENO`, `stdin`), 1 -> standard output (`STDOUT_FILENO`, `stdout`), 2 -> standard error (`STDERR_FILENO`, `stderr`) = #cs/linux/stream/process_stdio_stdout #cs/linux/stream/stdout #cs/linux/stream/stdin #cs/linux/stream/stderr 
<!--ID: 1758253289191-->

- File descriptors serve as the communication channel between user-space apps and the kernel-space system calls for I/O operations.

## Diagrams

[unix - What are file descriptors, explained in simple terms? - Stack Overflow](https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms)
- ![[UNIX File Descriptor.png | 700]]
- ![[UNIX File Descriptor.jpg | 700]]
