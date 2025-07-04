---
summary: GNU project debugger. Enables you to poke around your C/C++ programs while they are executing. Operates on binary files produced by a compilation process. Open-source and portable tool.
type: note
concepts: ["[[GDB Debugging Symbols]]"]
components: ["[[VSCode Cpp Debugging]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, June 11th 2025, 12:07:28 pm
tags: [command/gdb]
---
# Usage
## Commands
- [p] `print <variable>` = Displays the value of a variable = #command/gdb
<!--ID: 1751434091357-->

- [p] `p <variable>` = Displays the value of a variable = #command/gdb = `@ <n>` Append this to print `n` values starting at name
<!--ID: 1751434091360-->

- [p] `inf r` = shows you the hex values of all things inside the code
- [p] `-exec -enable-pretty-printing` = Enables pretty printing for gdb within VSCode = #command/gdb 
<!--ID: 1751434091364-->

- [p] `-exec set print pretty on` = Enables pretty printing for gdb within VSCode, specifically when calling `display <var>` or `p <var>` from VSCode console = #command/gdb 
<!--ID: 1751434091368-->

- [p] `run or r`  = Executes the program from start to end. *Should* reload the binary if it has changed = #command/gdb
<!--ID: 1751434091372-->

- [p] `break or b` = Sets a breakpoint on a particular line = #command/gdb
<!--ID: 1751434091376-->

- [p] `disable` = Disables a breakpoint = #command/gdb
<!--ID: 1751434091379-->

- [p] `enable` = Enables a disabled breakpoint = #command/gdb
<!--ID: 1751434091383-->

- [p] `next or n` = Executes the next line of code without diving into functions = #command/gdb
<!--ID: 1751434091387-->

- [p] `step` = Goes to the next instruction, diving into the function = #command/gdb
<!--ID: 1751434091391-->

- [p] `list or l` = Displays the code = #command/gdb
<!--ID: 1751434091395-->

- [p] `quit or q` = Exits out of GDB = #command/gdb
<!--ID: 1751434091399-->

- [p] `clear` = Clears all breakpoints = #command/gdb
<!--ID: 1751434091406-->

- [p] `continue`   = Continues normal execution = #command/gdb
<!--ID: 1751434091413-->


## Working in VSCode
[[VSCode Debugging]]