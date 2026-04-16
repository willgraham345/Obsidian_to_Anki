---
summary: How to manage input and output within Bash.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
concept_of:
  - "[[Bash Basics]]"
  - "[[Bash Streams]]"
date created: Thursday, January 8th 2026, 11:48:39 am
date modified: Thursday, April 9th 2026, 9:25:43 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
3 standard redirections:
󰙎 0 (redirection) ;; Standard input
󰙎 1 (redirection) ;; Standard output
󰙎 2 (redirection) ;; Standard err

## Usage

 `>` ;;; bash redirect output operator
 `>>` ;;; bash append output operator
 `<` ;;; Bash input redirection output operator
 `&>` ;;; Bash redirect *all* output operator
 `|` ;;; bash connect stdout of one command to the stdin of another command
 `echo $?` ;;; bash prints the exit value for the previous command.

## Examples
```bash
python hello.py > output.txt            # stdout to (file)
python hello.py >> output.txt           # stdout to (file), append
python hello.py 2> error.log            # stderr to (file)
python hello.py 2>&1                    # stderr to stdout
python hello.py 2>/dev/null             # stderr to (null)
python hello.py >output.txt 2>&1        # stdout and stderr to (file), equivalent to &>
python hello.py &>/dev/null             # stdout and stderr to (null)
```
