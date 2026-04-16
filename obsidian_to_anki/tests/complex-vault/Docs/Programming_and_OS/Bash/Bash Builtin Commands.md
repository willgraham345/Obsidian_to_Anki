---
summary: Commands the bash shell ships with. Some of these commands are stored as binaries, others are read by the interpreter.
headings:
  - "[[#Usage]]"
type: note/item
date created: Wednesday, October 22nd 2025, 2:18:00 pm
date modified: Monday, December 8th 2025, 3:28:30 pm
tags:
  - tools/bash_cli/arithmetic
  - tools/bash_cli/command_execution
  - tools/bash_cli/file
  - tools/bash_cli/history
  - tools/bash_cli/input_output
  - tools/bash_cli/job_control
  - tools/bash_cli/misc
  - tools/bash_cli/shell
  - tools/bash_cli/shell_control
  - tools/bash_cli/variable
template: "[[base_note_template]]"
template-version: 1.0.0
item_of:
  - "[[Bash]]"
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage

 `.` ;;; Execute commands from a file in the current shell  
 `:` ;;; Do nothing; a no-op  
 `[` ;;; Equivalent to `test`  
 `alias` ;;; Define or display aliases  
 `bg` ;;; Continue a job in the background  
 `bind` ;;; Bind key sequences to readline commands or functions  
 `break` ;;; Break out of the innermost loop or shell function  
 `builtin` ;;; Execute a builtin command, bypassing function lookup  
 `caller` ;;; Display the function or script name and line number of a caller  
 `cd` ;;; Change the current working directory  
 `command` ;;; Execute a command bypassing function lookup  
 `compgen` ;;; Generate possible completion matches for a word  
 `complete` ;;; Define completion behavior for a command  
 `continue` ;;; Continue to the next iteration of the innermost loop  
 `declare` ;;; Declare variables and give attributes such as types or read‑only status  
 `dirs` ;;; List the directory stack maintained by pushd/popd  
 `disown` ;;; Remove jobs from the job table so they are no longer associated with the shell  
 `echo` ;;; Write arguments to standard output  
 `enable` ;;; Enable or disable builtin commands  
 `eval` ;;; Evaluate arguments as shell commands  
 `exec` ;;; Execute a command in place of the current shell process  
 `exit` ;;; Exit the shell with an optional exit status  
 `export` ;;; Mark variables to be exported to child processes  
 `fc` ;;; Fix, list, or re‑execute commands from the history list  
 `fg` ;;; Bring a job to the foreground  
 `getopts` ;;; Parse positional parameters according to a specified format string  
 `hash` ;;; Remember or display the full path of executable commands for speed  
 `help` ;;; Display help for builtins  
 `history` ;;; Display or manipulate the command history list  
 `jobs` ;;; List active jobs with status  
 `kill` ;;; Send a signal to a job or process  
 `let` ;;; Evaluate arithmetic expressions  
 `local` ;;; Create a local variable within a function  
 `logout` ;;; Exit a login shell  
 `mapfile` ;;; Read lines from standard input into an array variable  
 `popd` ;;; Remove the top directory from the stack and change to it  
 `popd > /dev/null` ;;; Remove the top directory from the stack and change to it, and discard the normal output (usually prints the new directory stack)  
 `printf` ;;; Format and print data to standard output  
 `pushd` ;;; Add a directory to the stack and change to it. Note, this will normally print the new directory stack as well.  
 `pwd` ;;; Print the current working directory  
 `read` ;;; Read a line from standard input into a variable  
 `readonly` ;;; Mark a variable as read‑only  
 `return` ;;; Return from a shell function with an optional status  
 `set` ;;; Set or unset shell options or positional parameters  
 `shift` ;;; Shift positional parameters to the left  
 `source` ;;; Read and execute commands from a file in the current shell  
 `suspend` ;;; Suspend the shell (for job control)  
 `test` ;;; Evaluate conditional expressions  
 `time` ;;; Measure execution time of a command or pipeline  
 `times` ;;; Display user and system times for the shell and its children  
 `trap` ;;; Execute a command when a signal is received  
 `true` ;;; Do nothing successfully (exit status 0)  
 `type` ;;; Indicate how a name would be interpreted if used as a command  
 `typeset` ;;; Alias for `declare`, set attributes on a variable  
 `ulimit` ;;; Set or display user limits for the shell  
 `umask` ;;; Set file mode creation mask  
 `unalias` ;;; Remove an alias definition  
 `unset` ;;; Remove a variable or function  
 `wait` ;;; Wait for job completion and return its exit status  
 `shopt` ;;; Set or unset shell options for the current shell  
 `compopt` ;;; Set options for the current completion command  
 `false` ;;; Do nothing but return a non‑zero exit status
