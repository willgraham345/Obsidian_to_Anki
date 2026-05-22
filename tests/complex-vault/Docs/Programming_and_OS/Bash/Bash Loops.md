---
summary: Loop constructs in Bash — for, while, C-style, range, and infinite loops
type: note/concept
ai_generated: true
concept_of:
  - "[[Bash Basics]]"
tags:
  - lang/control_flow
date created: Wednesday, April 9th 2026, 12:00:00 pm
date modified: Wednesday, April 9th 2026, 12:00:00 pm
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

- [I] for loop ;;; Iterates over a list of words or file globs
- [I] while loop ;;; Repeats while a condition is true
- [I] C-style loop ;;; Numeric loop using `for ((init; cond; step))` syntax
- [I] range loop ;;; Iterates over a brace-expanded integer sequence `{start..end}`
- [I] infinite loop ;;; Loop with no natural exit condition; use `break` or signal to stop

## Usage

- [p] `for f in /path/*; do` ;;; for loop over file glob matches
- [p] `for i in {1..5}; do` ;;; range loop from 1 to 5
- [p] `for i in {5..50..5}; do` ;;; range loop with step size 5
- [p] `for ((i=0; i<5; i++)); do` ;;; C-style numeric for loop
- [p] `while [[ condition ]]; do` ;;; while loop with test condition
- [p] `while IFS='' read -r line; do ... done < file.txt` ;;; iterate over file lines
- [p] `while true; do` ;;; infinite loop — use `break` to exit
- [p] `break` ;;; exit innermost loop immediately
- [p] `continue` ;;; skip to next iteration of innermost loop

## Examples

```bash
# For loop — file glob
for f in /etc/rc.*; do
  echo "$f"
done

# C-style loop
for ((i=0; i<5; i++)); do
  echo "$i"
done

# Range loop
for i in {1..5}; do
  echo "$i"
done

# Range with step
for i in {5..50..5}; do
  echo "$i"
done

# While loop with counter
count=0
while [[ $count -lt 5 ]]; do
  echo "$count"
  ((count++))
done

# Read file line by line
while IFS='' read -r line; do
  echo "$line"
done < file.txt

# Infinite loop with break
while true; do
  read -r input
  [[ "$input" == "quit" ]] && break
done
```
