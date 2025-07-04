---
type: note
tags: note/git
---
# Background
Switch branches or restore working tree files


## Create a New Branch
_git checkout_ -b|-B <new-branch> [<start-point>]

Specifying `-b` causes a new branch to be created as if [git-branch[1]](https://git-scm.com/docs/git-branch) were called and then checked out. In this case you can use the `--track` or `--no-track` options, which will be passed to _git branch_. As a convenience, `--track` without `-b` implies branch creation; see the description of `--track` below.

If `-B` is given, `<new-branch>` is created if it doesn’t exist; otherwise, it is reset. This is the transactional equivalent of

$ git branch -f <branch> [<start-point>]
$ git checkout <branch>

that is to say, the branch is not reset/created unless "git checkout" is successful.