---
type: note
---
# Background
By default, `make` starts with the first target (Not targets whose names start with `.` unless they contain one or more `/`)

Goals: Targets that `make` strives ultimately to update.

```shell
make
```
- This command
1. Reads the makefile in the current directory
2. Begins processing the first rule
	1. Before `make` can fully process this rule, it must process the rules for the files that the default goal depends on. Each of these files is processed according to its own rule. 
3. Other rules are processed because their targets appear as prerequisites of the goal. If a rule is not depended on by the goal it is not processed.
4. 