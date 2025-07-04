---
type: note
tags: note/git
---
# Background
## Types of merge conflicts
Git fails to start the merge
- When Git sees there are changes in the working directory or staging area of the current project. 
- These changes could be overwritten by commits that are being merged in. 
Git fails during the merge
- A failure during a merge indicates a conflict between the current local branch and the branch being merged.
- Git will do its best to merge the files, but will leave things to you to manually resolve in conflicted files. 

## Identifying Merge Conflicts
```shell
git log --merge
```
- Produces a log with a list of commits that conflict between the merging branches