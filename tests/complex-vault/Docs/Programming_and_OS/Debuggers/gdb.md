---
summary: Debugger widely used, typically with an executable that's been built with debugging symbols.
type: note/system
headings:
  - "[[#Usage]]"
concepts:
  - "[[GDB Debugging Symbols]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 2:00:21 pm
items:
  - "[[VSCode Cpp Debugging]]"
tags: [tools/gdb]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage


### Commands
  `print <variable>` ;;; Displays the value of a variable = 
  `p <variable>` ;;; Displays the value of a variable = = `@ <n>` Append this to print `n` values starting at name 
  `inf r` ;;; shows you the hex values of all things inside the code
  `-exec -enable-pretty-printing` ;;; Enables pretty printing for gdb within VSCode =  
  `-exec set print pretty on` ;;; Enables pretty printing for gdb within VSCode, specifically when calling `display <var>` or `p <var>` from VSCode console =  
  `run or r`  ;;; Executes the program from start to end. *Should* reload the binary if it has changed = 

  `break or b` ;;; Sets a breakpoint on a particular line = 
  `disable` ;;; Disables a breakpoint = 
  `enable` ;;; Enables a disabled breakpoint = 
  `next or n` ;;; Executes the next line of code without diving into functions = 
  `step` ;;; Goes to the next instruction, diving into the function = 
  `list or l` ;;; Displays the code = 
  `quit or q` ;;; Exits out of GDB = 
  `clear` ;;; Clears all breakpoints = 
  `continue`   ;;; Continues normal execution = 

## Working in VSCode
[[VSCode Debugging]]
