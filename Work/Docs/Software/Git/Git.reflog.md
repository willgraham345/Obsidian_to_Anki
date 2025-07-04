---
type: note
tags: note/git
---
# Background
Safety net Git uses to record updates applied to tips of branches and other commit references. 

Every time your branch tip is updated for any reason, a new entry will be added to the reflog. 

# Usage
Show Reflog for Local Repo
```shell
git reflog --relative-date
```
- Can be used with [[Git reset]] (with a `--hard` flag) to move back to a previous commit. 