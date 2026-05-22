---
type: note/tool
tags:
  - programming/shell
date created: Monday, March 30th 2026, 12:00:00 pm
date modified: Monday, March 30th 2026, 12:00:00 pm
ai_generated: true
item_of:
  - "[[POSIX]]"
similar:
  - "[[cd]]"
  - "[[Linux export]]"
---

# Summary
- [I] pushd / popd ;;; Shell builtins for managing a directory stack, enabling save/restore of working directory locations

# Additional Background
`pushd` and `popd` are POSIX shell builtins (bash, zsh) that maintain a **directory stack** — a LIFO list of paths. Unlike `cd`, they let you return to a prior location without remembering the path. `dirs` displays the current stack.

## Concepts of Note

### Directory Stack
- [I] directory stack ;;; An ordered list of directory paths maintained per-shell session; index 0 is always the current directory
- [I] dirs ;;; Builtin that prints the directory stack; `dirs -v` shows indices, `dirs -c` clears the stack

### pushd
- [I] pushd ;;; Pushes `$PWD` onto the stack and `cd`s to the given path; with no args, swaps the top two stack entries
- [p] `pushd /some/path` ;;; Save current dir, move to `/some/path`
- [p] `pushd +N` ;;; Rotate stack so the Nth entry (0-indexed) becomes current

### popd
- [I] popd ;;; Removes the top entry from the stack and `cd`s to the new top; fails if stack is empty
- [p] `popd` ;;; Return to the most recently pushed directory
- [p] `popd +N` ;;; Remove the Nth stack entry without changing directory (N > 0)

## Usage

### Save / Restore Pattern
The most common pattern — bracket a temporary `cd` with push/pop:
- [p] `pushd /tmp && do_work && popd` ;;; Temporarily visit a dir, return on completion

Prefer a subshell when you don't need the stack:
- [p] `(cd /tmp && do_work)` ;;; Isolated cd with automatic restore; no stack side effects

### Iterate Over Directories
- [p] `for d in a b c; do pushd "$d"; make; popd; done` ;;; Build in multiple dirs, returning home after each

### Guard Against Empty Stack
`popd` errors when the stack is empty. Protect scripts with:
- [p] `[[ $(dirs -v | wc -l) -gt 1 ]] && popd` ;;; Only pop if stack has entries beyond the current dir

### Debugging Mismatched pushd/popd
- [p] `dirs -v` ;;; Print indexed stack — if empty before a `popd`, the push was skipped
- [p] `set -x` ;;; Trace execution to see which pushd/popd calls fire

## Flashcards
- [t] What does `pushd` do with no arguments? ;; Swaps the top two entries of the directory stack (toggles between current and previous)
- [t] How do you print the directory stack with indices? ;; `dirs -v`
- [t] Why prefer a subshell over pushd/popd for temporary directory changes? ;; Subshell scope is automatically restored on exit, no risk of unbalanced stack
- [t] What causes "directory stack empty" error? ;; `popd` called more times than `pushd`, often due to an early return or error skipping the matching `pushd`
