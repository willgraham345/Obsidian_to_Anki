---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:08:48 am
function_of:
  - "[[Linux CLI]]"
  - "[[Linux Filesystem Hierarchy]]"
tool_of: "[[Linux]]"
---
# Background
- Finds a string in a given file or input
	- Can be used on a given file, or files on a system
- Accepts input (usually via a pipe) from another command or series of commands

# Usage
```shell
grep [options] [regexp] [filename]
```

## Basic Usage

| Command | Usage                                                           | Really useful |
| ------- | --------------------------------------------------------------- | ------------- |
| `-i`    | Ignore case                                                     | $X$           |
| `-v`    | Return lines which *don't* match the pattern                    |               |
| `-c`    | Print a count of matching lines                                 |               |
| `-l`    | Print the name of each file which contains a match              |               |
| `-n`    | Print line number before each line that matches                 |               |
| `-r`    | Recursive, read all files in a given directory and subdirectory | $X$           |

## Regular Expressions
.

| Expression | Meaning                                       |
| ---------- | --------------------------------------------- |
| `[abc]`    | Range (any of these characters)               |
| `[^abc]`   | Not range (opposite of range)                 |
| `(abc)`    | Group these characters and remember for later |
| `\n`       | Replace `n` with a number.                    |
| `\|`       | Logical 'or' operation `\|`                   |

## Examples
[See here](https://ryanstutorials.net/linuxtutorial/cheatsheetgrep.php)