---
type: note
---
# Background
- 

# Usage
## See changes on what you haven't `git add` yet
```shell
git diff myfile.txt
```

## See already added changes
```shell
git diff --cached myfile.txt
```

## Show changes you added to your worktree from the last commit
```shell
git diff HEAD file
```