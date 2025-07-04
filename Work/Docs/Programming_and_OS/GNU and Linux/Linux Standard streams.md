---
type: note/component
component_of:
  - "[[Linux Processes]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 9:59:54 am
---
# Background
Standard streams are preconnected input/output communication channels between a computer program and its environment.

Originally, I/O happened via a physically connected system console (input via keyboard, output via monitor), and standard streams are a way to abstract this (see [[Unix abstract devices]])
- When a command is executed via an interactive shell, the streams are typically connected to the text terminal on which the shell is running, but can be changed with a redirection or a pipeline. 
- A child process inherits the standard streams of its parent process.

# Usage
- Unix wanted everything to be a file ([[Unix Tools Philosophy]]), so you can read the streams using the same library functions and interfaces without worrying about whether the I/O stream is connected to a keyboard, a disk file, a socket, a pipe, or some other I/O abstraction. 