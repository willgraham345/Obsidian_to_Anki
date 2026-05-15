---
summary: Miscellaneous Bash features — arithmetic expansion, heredoc, process substitution, trap, printf, and history expansion
type: note/concept
ai_generated: true
concept_of:
  - "[[Bash Basics]]"
  - "[[Bash]]"
tags:
  - lang/syntax
date created: Wednesday, April 9th 2026, 12:00:00 pm
date modified: Wednesday, April 9th 2026, 12:00:00 pm
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage

### Arithmetic

- [p] `$((a + b))` ;;; Arithmetic expansion — integer math only
- [p] `$(( (a + b) * c ))` ;;; Compound arithmetic expression
- [p] `((i++))` ;;; Increment variable in-place (no `$` needed inside `((...))`)

### Here-Documents & Herestrings

- [p] `cmd <<EOF ... EOF` ;;; Heredoc — multiline string fed to stdin; variables expanded
- [p] `cmd <<'EOF' ... EOF` ;;; Heredoc with single-quoted delimiter — no expansion
- [p] `cmd <<< "$var"` ;;; Herestring — single string fed to stdin

### Process Substitution & Subshells

- [p] `<(command)` ;;; Process substitution — command output as a readable file descriptor
- [p] `>(command)` ;;; Process substitution — write to command's stdin as a file descriptor
- [p] `(cd /tmp; ls)` ;;; Subshell — changes inside do not affect the parent shell

### Error Handling

- [p] `trap 'handler' ERR` ;;; Execute handler when any command returns non-zero
- [p] `trap cleanup EXIT` ;;; Execute cleanup function on shell exit (normal or error)

### Output Formatting

- [p] `printf "%s\n" "$var"` ;;; Formatted output (more portable than `echo`)
- [p] `printf "%-10s %5d\n" "$name" $num` ;;; Left-padded string, right-aligned integer

### History Expansion

- [p] `!!` ;;; Repeat the last command
- [p] `!$` ;;; Last argument of the previous command
- [p] `!*` ;;; All arguments of the previous command

## Examples

```bash
# Arithmetic
i=5
echo $(( i * 3 ))    # 15
((i++)); echo $i      # 6

# Heredoc (variables expanded)
cat <<EOF
Hello $USER
Today is $(date)
EOF

# Heredoc (literal)
cat <<'EOF'
No $expansion here
EOF

# Herestring
grep "pattern" <<< "$multiline_var"

# Process substitution
diff <(ls dir1) <(ls dir2)

# Trap cleanup on exit
cleanup() { rm -f /tmp/tmpfile; }
trap cleanup EXIT

# Printf formatting
printf "%-10s %5d\n" "apples" 42
# apples         42
```
