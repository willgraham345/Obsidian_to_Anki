---
type: note
tags: note/git
---
Imagine a nice A->B->C linear programming owned by Ashton
- Cody is a remote, and he's on the main branch
- Will is on a branch called main too

Think of a branch, as a branch pointer
- It points to a commit

Main usually represents the canonical, or the currently deployed version on a server. You DON'T want to break main. 

Merge is integrating two different commits

Reset means it resets the branch pointer to do something else
- If nothing points to a git, then it doesn't exist

A branch is a mutable object, it can change over time

A tag is immutable that cannot change
- Kind of like highlighting something when you read. 