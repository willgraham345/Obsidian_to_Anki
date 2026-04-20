---
type: note/library
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:01:56 am
library_of: "[[Linux CLI]]"
---
![[Linux.Vim and Vim Keybindings - 1.svg|875]]

# Useful Shortcuts
| Shortcut   | Mode   | Description                                                                                                                                           |
| ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Ctrl + O` | Insert | Will switch to normal mode for one command, then go back to insert.                                                                                   |
| `Ctrl + O` | Normal | Paired with `Ctrl + i`, these jump the user through a "jump list", a list of places where your cursor has been. Can be used with the quickfix feature |

# Sorta useful Shortcuts
| Control Shortcuts       | Mode        | Description                                                                             |
| ----------------------- | ----------- | --------------------------------------------------------------------------------------- |
| `^`                     | Normal Mode | Move to the first non-whitespace char of the line.                                      |
| `gg`                    | Normal Mode | Move to the beginning of the document.                                                  |
| `{line number}G`        | Normal Mode | Move to a specific line number.                                                         |
| `Ctrl + u`              | Normal Mode | Scroll up half a page.                                                                  |
| `Ctrl + d`              | Normal Mode | Scroll down half a page.                                                                |
| `Ctrl + b`              | Normal Mode | Scroll up a full page.                                                                  |
| `Ctrl + f`              | Normal Mode | Scroll down a full page.                                                                |
| `m{letter}`             | Normal Mode | Set a mark at the current position.                                                     |
| `{letter}`              | Normal Mode | Jump to the mark previously set with `m{letter}`.                                       |
| `Ctrl + b` / `Ctrl + h` | Insert Mode | Move left one character.                                                                |
| `Ctrl + f` / `Ctrl + l` | Insert Mode | Move right one character.                                                               |
| `Ctrl + a`              | Insert Mode | Move to beginning of line.                                                              |
| `Ctrl + e`              | Insert Mode | Move to end of line.                                                                    |
| `Ctrl + left arrow`     | Insert Mode | Move one word to the left.                                                              |
| `Ctrl + right arrow`    | Insert Mode | Move one word to the right.                                                             |
| `Ctrl + p`              | Insert Mode | Move to previous line.                                                                  |
| `Ctrl + n`              | Insert Mode | Move to next line.                                                                      |
| `Ctrl + u`              | Insert Mode | Delete text to beginning of line.                                                       |
| `Ctrl + w`              | Insert Mode | Delete word before cursor.                                                              |
| `Ctrl-r *`              | Insert Mode | Will paste the value of the clipboard while in insert mode                              |
| `Ctrl-r "`              | Insert Mode | Will paste the value of the unnamed register (last delete or yank) while in insert mode |

# Text Manipulation Hacks
Start with a `v`, and then do a command (similar to y-yank)
- Can also be done with `d` and `y` as the starting variable

| Shortcut | Description |  |
| ---- | ---- | ---- |
| `v` | Start visual mode, mark lines, then do a command (like y-yank) |  |
| `V` | Start linewise visual mode |  |
| `o` | Move to the other end of the marked area |  |
| `Ctrl + v` | Start visual block mode |  |
| `O` | Move to the other corner of the block |  |
| `aw` | Mark a word |  |
| `ab` | A block with `()` |  |
| `aB` | A block with `{}` |  |
| `at` | A block with `<>` tags |  |
| `ib` | Inner block with `()` |  |
| `iB` | Inner block with `{}` |  |
| `it` | Inner block with `<>` tags |  |
| `Esc` or `Ctrl + c` | Exit visual mode |  |
Tip: Instead of `b` or `B`, one can also use `(` or `{` respectively.

## Deleting Word Hacks
| Shortcut | Description |
| ---- | ---- |
| `x` | Delete current character |
| `dw` | Delete the curent word |
| `db` | Deletes to beginning of the word |
| `dd` | Delete the current line |
| `d$` | Delete to the end of the line |
| `d0` | Delete to the beginning of line |
Tip: You can put an integer in front of any of these to repeat it multiple times (i.e. `5db` deletes the last 5 words)

# Marks
| Shortcut      | Description                          |
| ------------- | ------------------------------------ |
| `m + any_key` | Sets that location equal to that key |
| `' + any key` | Goes to that location                |


Great page: [here](https://vim.rtorr.com/)

# Registers
Access a register with `"<key><command>`
- Registers can be any key... I think
Copy to register
`"<reg>y`
Paste from register:
`"<reg>p`

Example:
`"ayy`
- Copies the current line into `a` register
``
