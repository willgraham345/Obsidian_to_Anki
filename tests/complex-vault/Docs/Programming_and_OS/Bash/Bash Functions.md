---
summary: Defining and using functions in Bash — arguments, return values, and local scope
type: note/concept
ai_generated: true
concept_of:
  - "[[Bash Basics]]"
tags:
  - lang/syntax
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

- [I] function ;;; Named block of reusable commands; must be defined before first call
- [I] argument ;;; Positional input accessed via `$1`, `$2`, etc. inside the function
- [I] return code ;;; Integer exit status (0–255) set by `return N`; 0 = success
- [I] local variable ;;; Variable scoped to the function; declared with `local`

## Usage

- [p] `$1`, `$2` ;;; Positional function arguments (first, second, …)
- [p] `$@` ;;; All arguments as separate quoted words
- [p] `$*` ;;; All arguments as a single word
- [p] `$#` ;;; Number of arguments passed to the function
- [p] `local varname=value` ;;; Declare a variable local to the function scope
- [p] `return N` ;;; Exit function with status code N (0 = success)
- [p] `result=$(myfunc arg)` ;;; Capture function stdout as a value

## Examples

```bash
# Two equivalent definition styles
function greet { echo "Hello, $1"; }
greet() { echo "Hello, $1"; }

# Arguments + echo return value
add() {
  echo $(( $1 + $2 ))
}
result=$(add 3 4)   # result=7

# Local variable
counter() {
  local count=0
  ((count++))
  echo "$count"
}

# Error handling via return code
validate() {
  [[ -n "$1" ]] || return 1
  echo "Valid: $1"
  return 0
}
validate "" || echo "empty input"
```
