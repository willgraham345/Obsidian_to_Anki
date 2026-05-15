---
summary:
type: note/concept
headings:
ai_generated: true
concept_of:
  - "[[Bash Basics]]"
date created: Thursday, April 9th 2026, 9:44:45 am
date modified: Thursday, April 9th 2026, 9:56:18 am
tags:
  - lang/control_flow
  - lang/syntax
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary


# Additional Background

## Concepts of Note

󰠗 What operator tests string equality with glob support? ;; `[[ STRING == PATTERN ]]`
󰠗 What is the difference between `&&` inside `[[ ]]` vs outside? ;; Inside: logical AND within a test expression; outside: short-circuit AND between two commands

## Usage

### String Tests

 `[[ STRING == PATTERN ]]` ;;; String equality or glob match (pattern must be unquoted)
 `[[ STRING != PATTERN ]]` ;;; String inequality
 `[[ STRING =~ REGEX ]]` ;;; ERE regex match; captures stored in `${BASH_REMATCH[@]}`

### Numeric Comparisons

 `[[ NUM -eq NUM ]]` ;;; Equal
 `[[ NUM -ne NUM ]]` ;;; Not equal
 `[[ NUM -lt NUM ]]` ;;; Less than
 `[[ NUM -le NUM ]]` ;;; Less than or equal
 `[[ NUM -gt NUM ]]` ;;; Greater than
 `[[ NUM -ge NUM ]]` ;;; Greater than or equal

### Logical Operators

 `[[ EXPR && EXPR ]]` ;;; Logical AND inside a test
 `[[ EXPR || EXPR ]]` ;;; Logical OR inside a test
 `[[ ! EXPR ]]` ;;; Logical NOT
 `cmd1 && cmd2` ;;; Run cmd2 only if cmd1 succeeds (exit 0)
 `cmd1 || cmd2` ;;; Run cmd2 only if cmd1 fails (non-zero exit)

## Examples

```bash
# String comparison with glob
name="Alice"
if [[ "$name" == A* ]]; then
  echo "starts with A"
fi

# Numeric comparison
age=25
if [[ $age -ge 18 ]]; then
  echo "adult"
fi

# Regex match with capture
str="abc123"
if [[ "$str" =~ ^[a-z]+([0-9]+)$ ]]; then
  echo "digits: ${BASH_REMATCH[1]}"  # 123
fi

# case/switch
case "$1" in
  start)  echo "starting"  ;;
  stop)   echo "stopping"  ;;
  *)      echo "unknown: $1" ;;
esac
```
