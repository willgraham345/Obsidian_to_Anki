---
type: note/item
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Tuesday, August 12th 2025, 9:07:23 am
item_of: ["[[Git]]"]
tags: [ ]
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
