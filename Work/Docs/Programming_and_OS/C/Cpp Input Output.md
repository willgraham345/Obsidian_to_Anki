---
type: note/concept
classes:
  - "[[Cpp buffer]]"
  - "[[Cpp.iomanip]]"
  - "[[Cpp.iostream]]"
  - "[[Cpp std stringstream (class)]]"
  - "[[Cpp CLI App]]"
concepts:
  - "[[Cpp parsing arguments]]"
functions:
  - "[[Cpp cin]]"
  - "[[Cpp getline]]"
  - "[[Cpp scanf]]"
  - "[[Cpp.Input Streams]]"
  - "[[Cpp.ios]]"
similar:
  - "[[Cpp Class Constructors]]"
concept_of:
  - "[[Cpp]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, January 7th 2025, 10:35:51 am
libraries:
  - "[[Cpp fstream]]"
---
# Background
`stdin` = standard input stream
`stdout` = standard output stream
`stderr` = standard error stream

## Common Flags
| Flag   | Format | Description       |
| ------ | ------ | ----------------- |
| Int    | `%d`   | 32 Bit integer    |
| Int    | `%i`   | Other integer?    |
| Long   | `%ld`  | 64 bit integer    |
| Char   | `%c`   | Character type    |
| Float  | `%f`   | 32 bit real value |
| Double | `%lf`  | 64 bit real value |

## Control Characters
|Control Character|Description|
|---|---|
|`\b`|Backspace - Moves the cursor back one position.|
|`\f`|Form Feed - Advances the paper to the next page or form.|
|`\r`|Carriage Return - Moves the cursor to the beginning of the line.|
|`\'`|Apostrophe (Single Quote) - Inserts a single quote character.|
|`\"`|Quote (Double Quote) - Inserts a double quote character.|
|`\n`|Newline - Inserts a newline character.|
|`\t`|Tab - Inserts a tab character.|
|`\nnn`|Character Specified by Octal Value - Inserts the character specified by the octal number.|
|`\NN`|Character Specified by Hexadecimal Value - Inserts the character specified by the hexadecimal number.|
