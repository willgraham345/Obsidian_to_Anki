---
type: note
tags: note/git
---
# Background
- When you merge one branch into another, Git creates a new commit known as the "merge" commit that ties together the histories of both branches. This commit has two parent commits, one from each branch. 
- This preserves commit history for both branches, showing clearly when and where the branches were merged.
- Typically better choice for collaboration when you have a team or shared branch. 

## Fast Forward Merge
- A fast forward merge can occur when there is a linear path from the current branch tip to the target branch. Instead of "actually" merging the branches, all Git has to do is integrate the histories between the two. This effectively combines the histories. 
![[05-06 Fast forward merge.svg|534]]
- Execution in code below:
```shell
# Start a new feature git checkout -b new-feature main # Edit some files git add <file> git commit -m "Start a feature" # Edit some files git add <file> git commit -m "Finish a feature" # Merge in the new-feature branch git checkout main git merge new-feature git branch -d new-feature
```

# Usage
## `git merge`
- Takes two commit pointers, usually the branch tips
- Will find a common base commit between them. Once Git finds a common base commit, it will create a new "merge commit" that combines the changes of each queued merge commit sequence. 

## Merging a Feature into the Main through fast forward
Usually `git merge feature main`

## Merge Strategies