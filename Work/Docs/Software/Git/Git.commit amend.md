---
type: note
tags: note/git
---
# Background
Convenient way to modify the most recent commit.

- Lets you combine staged changes with the most previous commit instead of creating an entirely new commit. 
- Can be used to edit commit message without changing its snapshot. 

# Usage
## Change the Last Commit Message
```shell
git commit --amend -m "updated commit message"
```

## Changing Committed Files Without Changing Commit Message
```shell
git commit --amend --no-edit
```
- Needs to have changes staged to work, so run `git add` before running this