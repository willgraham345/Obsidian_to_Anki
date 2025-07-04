---
company: Varex
tags: archive_deprecated/Varex
---
# Background
Same basic idea as [[VD.Git.Gerrit.Intro]], but you don't necessarily need to have someone review your commit/push. It can be just for Jenkins to trigger the build. 

[Making DevBranches](https://fpbugs/projects/gerrit/wiki/Tips)
[See here](https://fpbugs/projects/gerrit/wiki/Using_Gerrit) for a good guide on how to go through it. 

Basic workflow
1. Make changes
2. Add changes
3. Commit changes `git commit`
	1. Involves a substep of modifying the commit to link it to Gerrit.
4. Pushing (`git push origin HEAD:refs/for/branch_name`)
	1. Will generate an error, with an appropriate changeID. Add that changeID 
5. Add that change id back to the commit `git commit --amend`
6. Push again `git push origin HEAD:refs/for/branch_name`

# Usage
## Commit Message
```
A change with an issue number; refs #1234

// in between stuff

Change-Id: Iaeb85f51cfa5669fdb8388f30ef8cfd7dfc68f0c
```
refs matches up with the number generated by Redmine. 