---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:09:17 am
function_of:
  - "[[Linux CLI]]"
tool_of: "[[Linux]]"
---
# Background
- A tool that lets you read large text files without cluttering your screen. Some people like vim, but less is much faster as it doesn't read the entire file before starting. 

# Basics
`less filename`

# Options
| Option | Description                              |
| ------ | ---------------------------------------- |
| `-N`   | Show line numbers                        |
| `-X`   | File contents will be left on the screen |
| `+F`   | Tells less to watch for file changes (useful for log files)                                         |

# Commands 
|Command|Action|
|---|---|
|`Down arrow`, `Enter`, `e`, or `j`|Move forward one line.|
|`Up arrow`,`y` or `k`|Move backward one line.|
|`Space bar` or `f`|Move Forward one page.|
|`b`|Move Backward one page.|
|`/pattern`|Search forward for matching patterns.|
|`?pattern`|Search backward for matching patterns.|
|`n`|Repeat previous search.|
|`N`|Repeat previous search in reverse direction.|
|`g`|Go to the first line in the file.|
|`Ng`|Go to the N-th line in the file.|
|`G`|Go to the last line in the file.|
|`p`|Go to the beginning of fthe ile.|
|`Np`|Go to N percent into file.|
|`h`|Display help.|
|`q`|Exit `less`.|


