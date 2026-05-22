---
type: note/keyword
headings:
ai_generated: true
date created: Friday, March 27th 2026, 12:00:00 pm
date modified: Friday, March 27th 2026, 1:11:14 pm
item_of:
  - "[[Bash Builtin Commands]]"
keyword_of:
  - "[[Bash]]"
tags: [tools/bash_cli/shell, tools/bash_cli/shell_control]
template:
template-version:
---

# Summary
󰙎 `set` ;;; Bash builtin that enables (`-`) or disables (`+`) shell options and sets positional parameters

# Additional Background

## Concepts of Note

### Flag Reference

| Flag | Long form (`-o`) | Effect |
|------|------------------|--------|
| `-e` | `errexit` | Exit immediately on non-zero exit status |
| `-u` | `nounset` | Error on unset variable reference |
| `-x` | `xtrace` | Print each command before execution |
| `-a` | `allexport` | Auto-export all set/modified variables |
| — | `pipefail` | Pipeline exit = exit of first failed stage |

### Toggle Convention

`-` enables an option; `+` disables it — applies to all flags.

 `set -a` ;;; enable allexport
 `set +a` ;;; disable allexport
 `set -o` ;;; list all options with current state
 `set +o` ;;; print `set` commands to restore current options

### Subshell Behavior

Options are inherited by subshells. Changes inside a subshell do not propagate back to the parent.

## Usage

 `set -euo pipefail` ;;; strict mode — exit on error, unset vars, or pipeline failure; place at top of every script
 `set -e` ;;; errexit — abort on any command failure
 `set -u` ;;; nounset — treat unset variable as error
 `set -x` ;;; xtrace — debug: echo each command before running
 `set -a` ;;; allexport — auto-export all subsequent variable assignments
 `set -o pipefail` ;;; fail if any command in a pipeline fails (not just last)
 `set -o` ;;; inspect all current shell option states
