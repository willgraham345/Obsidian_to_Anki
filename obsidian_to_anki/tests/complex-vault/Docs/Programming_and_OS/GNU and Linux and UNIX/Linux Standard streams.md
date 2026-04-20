---
headings: ["[[#Usage]]"]
type: note/item
inspiration: ["[[UNIX standard streams]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, August 18th 2025, 1:01:29 pm
item_of: ["[[Linux Processes]]", "[[Linux]]", "[[UNIX File Descriptor]]"]
---

# Additional Background
󰙎  Standard streams ;;; Preconnected input/output communication channels between a computer program and its environment. = #cs/linux/stream #cs/unix/stream 
<!--ID: 1758253289380-->


Originally, I/O happened via a physically connected system console (input via keyboard, output via monitor), and standard streams are a way to abstract this (see [[Unix abstract devices]])
- When a command is executed via an interactive shell, the streams are typically connected to the text terminal on which the shell is running, but can be changed with a redirection or a pipeline. 
- A child process inherits the standard streams of its parent process.

## Usage


- Unix wanted everything to be a file ([[Unix Tools Philosophy]]), so you can read the streams using the same library functions and interfaces without worrying about whether the I/O stream is connected to a keyboard, a disk file, a socket, a pipe, or some other I/O abstraction. 
