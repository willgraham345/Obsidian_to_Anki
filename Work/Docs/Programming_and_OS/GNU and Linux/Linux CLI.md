---
type: note
down:
  - "[[Linux CLI Cheatsheet]]"
  - "[[Linux Vim and Vim Keybindings]]"
  - "[[Linux ZSH Cheatsheet]]"
  - "[[Linux Zsh vs Bash]]"
  - "[[Linux ZSH]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, November 26th 2024, 1:47:05 pm
---
## Changing Directory
- `cd $(dir_name $(command))
	- You can also  have cd evaluate statements with `cd $(...)`
	- Often `cd $(dirname $(...))`

## Copying/Pasting
-   `Ctrl+Shift+C` = Copy terminal
-   `Ctrl+Shift+V` = Paste into terminal

## History
- `Ctrl+r` = Search command history
- `!!` = last command

## Open/Close the terminal 
-  ` Ctrl + Alt + T `= Open terminal from desktop
- `Ctrl+d` = Exit the current shell or end input (EOF)

## Navigation
### Backspace
- `Ctrl+u` = Delete from cursor to beginning of the line
- `Ctrl+k` = Delete from cursor to end of the line
- `Ctrl+w` = Delete the word before the cursor
- `Ctrl+y` = Undo deletions

### Move Cursor
- `Ctrl+a` = Move cursor to beginning of the line
- `Ctrl+e` = Move cursor to end of the line

## Undo

## Viewing
-   `Ctrl+L` = Clear/redraw the screen (clean blank screen)
-   `Ctrl++` = Make text bigger in terminal emulator
-   `Ctrl+-` = Make text smaller in terminal emulator



https://www.redhat.com/sysadmin/shortcuts-command-line-navigation#:~:text=Alt%2BF%20moves%20one%20word,B%20moves%20one%20word%20back.