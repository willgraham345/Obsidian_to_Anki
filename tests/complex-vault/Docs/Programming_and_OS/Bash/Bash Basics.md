---
summary: Basics for bash scripting
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
concepts:
  - "[[Bash Builtin Commands]]"
  - "[[Bash Redirections]]"
  - "[[Bash Streams]]"
concept_of:
  - "[[Bash]]"
date created: Monday, December 8th 2025, 3:41:46 pm
date modified: Thursday, April 9th 2026, 10:03:47 am
tags: [lang/control_flow, lang/syntax]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary


# Additional Background
[BashSheet - Greg's Wiki](https://mywiki.wooledge.org/BashSheet)

## Concepts of Note
󰙎 Synchronous command ;; A command where the next command will wait on it before executing. 
󰙎 asynchronous command ;; It mans bash will run the command in the background and run the next command immediately after, without waiting for the former to end. 
󰠗 How do I disable all syntactical meaning of characters in bash? ;; Add a single quote string `'`
󰠗 How do I disable all syntactical meaning of characters in bash *except* for expansions? ;; Add a double quoted string `"`

## Usage

 `;` ;;; Signify end of a synchronous command
 `&` ;;; Signify the end of an asynchronous command
 `|` ;;; Signify that output of one command should be connected to input of the next.
 `$$` ;;; A variable for the current shell's PID

 `$?` ;;; Exit status of last task
 `$!` ;;; Bash PID of last background task
 `$$` ;;; Bash PID of shell
 `$0` ;;; Bash filename of the shell script
 `$_` ;;; Bash last argument of the previous command
 `${PIPESTATUS[n]}` ;;; Bash return value of piped commands (array)

 `#!/usr/bin/env bash` ;;; Starts a bash program

 `name="John"` ;;; Create a bash variable `name` that holds `John`.

 `if [[ -z "$VAR" ]]; then :; fi` ;;; True if STRING is empty (e.g. unset env var)
 `if [[ -n "$VAR" ]]; then :; fi` ;;; True if STRING is not empty
 `if [[ -e FILE ]]; then :; fi` ;;; True if FILE exists
 `if [[ -r FILE ]]; then :; fi` ;;; True if FILE is readable
 `if [[ -h FILE ]]; then :; fi` ;;; True if FILE is a symlink
 `if [[ -d FILE ]]; then :; fi` ;;; True if FILE is a directory
 `if [[ -w FILE ]]; then :; fi` ;;; True if FILE is writable
 `if [[ -s FILE ]]; then :; fi` ;;; True if FILE size > 0 bytes
 `if [[ -f FILE ]]; then :; fi` ;;; True if FILE is a regular file
 `if [[ -x FILE ]]; then :; fi` ;;; True if FILE is executable
 `if [[ $a -eq 1 ]]; then :; fi` ;;; True if integer `a` equals 1



󰠗 Should you quote your variables in bash? When should you break precedent? ;; Yes, generally quote them unless they contain wildcards or expand to contain fragments.

󰠗 What is `[[` in bash? What does it return? ;; It is a command/program, which returns either `0` (true) or `1` (false).

### Parameter Expansion

```bash
name="John"
echo "${name}"
echo "${name/J/j}"    #=> "john" (substitution)
echo "${name:0:2}"    #=> "Jo" (slicing)
echo "${name::2}"     #=> "Jo" (slicing)
echo "${name::-1}"    #=> "Joh" (slicing)
echo "${name:(-1)}"   #=> "n" (slicing from right)
echo "${name:(-2):1}" #=> "h" (slicing from right)
echo "${food:-Cake}"  #=> $food or "Cake"
```

