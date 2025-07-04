---
type: note
tags:
  - note/git
---
# Background
Used to fetch + download content from a remote repo and update the local repo to match that content. 

Combination of [[Git fetch]] and [[Git.merge]]

# Usage

## Typical Use
```
git pull <remote>
```
Download all the changes from the point where the local and main diverged. This will then create a new local merge commit contain the content of the new diverged remote commits
![[01 bubble diagram-01.svg|435]]
![[02 bubble diagram-02.svg|508]]

## Rebasing
```
git pull --rebase <remote>
```
Fetches remote content but does not create a new merge commit.

Ensures a linear history by preventing unnecessary merge commits. Similar to saying "I want to put my changes on top of what everybody else has done"
![[Git.pull.png|500]]