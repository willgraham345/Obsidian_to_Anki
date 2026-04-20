---
summary: Linux stream editor, useful for search/replace, text transformation, and stream editing.
type: note/tool
headings:
  - "[[#Usage]]"
date created: Monday, June 30th 2025, 4:01:31 pm
date modified: Tuesday, March 10th 2026, 10:32:34 am
tags:
  - cs/linux/files
  - cs/linux/stream
template:
template-version:
tool_of: "[[Linux]]"
aliases: []
id: Linux sed
---

# Summary
󰙎 sed ;;; Stream editor for non‑interactive text transformations in Unix‑like systems.  

# Additional Background
[Sed Command in Linux/Unix With Examples - GeeksforGeeks](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)

## Concept Overview  
 `sed 's/foo/bar/g' file.txt` ;;; Runs **sed** in substitution mode, replacing every occurrence of the string “foo” with “bar” in each line of *file.txt* and writing the result to **stdout** (original file unchanged). 

### Use cases:
- Substitution: `s/regex/replacement/flags`  
- Deletion: `d`  
- In‑place editing: `-i[.bak]`  
- Addressing lines: `1,5`, `/pattern/`, `$`  


## Usage
`sed 's/foo/bar/g' file.txt` ;;; 
  `sed [OPTIONS] 'COMMAND' [INPUTFILE...]` ;;; Modify a stream, useful for text processing in Linux/Unix systems. You can manipulate texxt files without opening them in an editor, making it ideal for automating edits in batch files, log files, and performing fast conversions on large databases. Commands can also be read from a file and performed with this tool.


## Flashcards  
󰠗 What does the `-i` flag do in `sed`? ;; It edits the file in place, optionally creating a backup.  
󰠗 How would you delete empty lines with `sed`? ;; `sed '/^$/d'`  


