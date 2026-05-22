---
summary:
headings:
type: note/process
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Tuesday, October 21st 2025, 10:42:37 am
tags: []
template:
template-version:
process_of:
  - "[[Git]]"
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

  `<<<<<<< HEAD` ;;; Designates what your local changes (your current branch) are showing. = #tools/git/merge_conflicts
- [p] `=======`
      `other lines`
      `hashNum:filename.txt` = The changes the "other" branch introduces into your code. = #tools/git/merge_conflicts
