---
summary:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/tool
down:
  - "[[Linux CLI Cheatsheet]]"
  - "[[Linux Vim and Vim Keybindings]]"
  - "[[Linux ZSH Cheatsheet]]"
  - "[[Linux Zsh vs Bash]]"
  - "[[Linux ZSH]]"
concepts:
  - "[[Linux Zsh vs Bash]]"
concept_of:
  - "[[Linux]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, November 19th 2025, 1:52:12 pm
items:
  - "[[Linux ZSH]]"
libraries:
  - "[[Linux Vim and Vim Keybindings]]"
  - "[[Linux ZSH Cheatsheet]]"
template:
template-version:
tools:
  - "[[Linux fzf]]"
  - "[[Linux grep]]"
  - "[[Linux grep]]"
  - "[[Linux less]]"
  - "[[Linux pidof]]"
  - "[[Linux ps]]"
  - "[[Linux ptrace]]"
  - "[[Linux stdout and stderr to a file]]"
  - "[[Linux sysinfo]]"
  - "[[Linux wget]]"
  - "[[sops]]"
  - "[[the norms and standards protecting satellites and satellite transmissions are developed and enforced by those nation-state actors that are committed to system operability and overall mission sustainability for those satellites launched under their aegis and responsibility. However]]"
  - "[[Linux man]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
[[Docs/Programming_and_OS/C/C]] programs can access command line arguments via the `main()` function with:
```
int main(int argc, char *argv[])
```
- `argc` = Total number of command line arguments
- `argv` = Individual args available as strings
- `argv[0]` = Name of the program itself.

󰠗  How do you access cli arguments within a C/Cpp program? What are the associated variables and what they do? ;; Within the main function, `int main(int argc, char *argv[])`. `argc` is the total number of command line arguments, `argv` is the individual args available as strings, and `argv[0]` is the name of the program itself. = #cs/linux/process/cli #lang/IO/cli  
<!--ID: 1758253289501-->

## Usage
### Changing Directory
- `cd $(dir_name $(command))
	- You can also  have cd evaluate statements with `cd $(...)`
	- Often `cd $(dirname $(...))`

### Copying/Pasting
-   `Ctrl+Shift+C` = Copy terminal
-   `Ctrl+Shift+V` = Paste into terminal

### History
- `Ctrl+r` = Search command history
- `!!` = last command

### Open/Close the terminal 
-  ` Ctrl + Alt + T `= Open terminal from desktop
- `Ctrl+d` = Exit the current shell or end input (EOF)

### Navigation
#### Backspace
- `Ctrl+u` = Delete from cursor to beginning of the line
- `Ctrl+k` = Delete from cursor to end of the line
- `Ctrl+w` = Delete the word before the cursor
- `Ctrl+y` = Undo deletions

#### Move Cursor
- `Ctrl+a` = Move cursor to beginning of the line
- `Ctrl+e` = Move cursor to end of the line

### Undo

### Viewing
-   `Ctrl+L` = Clear/redraw the screen (clean blank screen)
-   `Ctrl++` = Make text bigger in terminal emulator
-   `Ctrl+-` = Make text smaller in terminal emulator



https://www.redhat.com/sysadmin/shortcuts-command-line-navigation#:~:text=Alt%2BF%20moves%20one%20word,B%20moves%20one%20word%20back.
