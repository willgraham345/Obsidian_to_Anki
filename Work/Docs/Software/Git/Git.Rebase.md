---
type: note
tags: [command/git, note/git]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Friday, October 4th 2024, 12:59:09 pm
---
[summary:: Tool for maintaining cleaner merge conflicts, and squashing multiple commits into one commit. ]

# Background
- Used when you want to maintain a cleaner, linear commit history and ensure that your change appear as if they were made sequentially. 
- When you rebase a branch onto another, git takes the commits of a branch and appends them to the commits of a different branch. The commits to rebase are previously saved into a temporary area, and then reapplied to the new branch, one by one, in order. 

## Example
In the case of two different branches below:
![[Pasted image 20230913094608.png | 500]]
where `other_branch` is based on `master`, we want to copy the commits of `other_branch` and add them after the last commit of `master` in order to achieve this result:
![[Pasted image 20240508115342.png|500]]

`other_branch` now includes all the commits of `master`. In order to achieve this we have to use the following Git command:

## Pros and Cons
| Pros                                                  | Cons                                                                                              |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Cleaner linear commit history                         | Rewriting history can be disruptive if other team members are working on the same branch          |
| Helps isolate and identify issues or bugs more easily | Use rebase primarily for local or feature branches; avoid rebasing shared or long-lived branches. |
| Can make it easier to integrate changes from the destination branch |                                                                                                   |

# Usage
- [p] `git rebase <base>` or `git rebase <main> <feature>` = Enables the user to rebase (integrate main commits while squashing feature commits) the current feature into main. It also can also be performed interactively with the `-i` option. This is done easiest through VSCode and searching for changes. NOTE: Make sure you have your local develop updated. = #command/git = `-i` interactive mode (highly recommended),[Guide here](https://www.freecodecamp.org/news/git-squash-commits/). It will also require `git rebase --continue` to step through each commit.
<!--ID: 1751434089737-->


## Squashing Commits
You can only squash backwards in the commit history. Later commits will need to be squashed into earlier commits. 
```
git rebase -i <branch_name>
```
- `branch_name` is optional, and will only be done when trying to combine a feature back into main.

An editor will pop up, squash the messages you'd like to squash, save, and go back. 
Make sure to double check your git log.
From there you can push