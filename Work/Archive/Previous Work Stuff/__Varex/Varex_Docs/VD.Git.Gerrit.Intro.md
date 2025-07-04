---
company: Varex
tags: archive_deprecated/Varex
---
# Gerrit Overview
See [[VD.Jenkins.and.Gerrit.Pipeline]] for a more Cheatsheet-oriented way of this.

They do things a bit differently than Git, because they need one place where all the code and build system goes. 
- Gerrit is Android open-source
	- Redmine has a [Wiki](https://fpbugs/projects/gerrit/wiki) that covers different stuff about Gerrit. 

![[gerrit.workflow.excalidraw]]
There is a project in Redmine called Gerrit (`https://fpgit/#/dashboard/self`)
- Some version control systems would version each version differently
![[Pasted image 20240507151754.png|300]]

- 1st 2 changes are the same for Gerrit as GitHub
	- We'll push to a special branch to Git. 
	- Gerrit keeps track of all of these projects after you push. 

project = another name for repo in Gerrit

In commit message
- 128-bit change-ID
	- Thing Gerrit uses to tie all commits to a specific feature or change. 
- Change set
- Each and every change can be thought of as a `feature-branch`
	- Changes may or may not be consecutive on a branch. 
- 

`gitblit` links
- Online repository editor. It's a history editor where you can look at anything previous to it. 
- You can find tags, older builds, entire set of code, and code tree at a given time. 

# Code Review
## Code Review Process
### Main change screen
Gives you highlights of the changeset and current state of the change. Shows related changes, list of the changeset, and history.
- ![[Pasted image 20240508092858.png| 750]]
	- From here you can add reviewers
### Being a Reviewer
1. Start by checking commit message, and make sure the bug is the correct bug in the change. 
	1. If you find an error here, then click on the commit message and attach a comment to the line with the comment stuff. Click return arrow in image to return to change page. 
![[Pasted image 20240508093033.png | 750]]
![[Pasted image 20240508093616.png|750]]
2. Reviewing Code Changes
	1. Click on other file names, and you'll see a diff where you can add comments. After adding comments, click the up arrow to go back to the change page or go to the next file with the right arrow.
3. Check that reviewed files have a checkmark next to them
![[Pasted image 20240508093752.png|750]]
4. Finish Review
	1. When you're done, click reply and type any additional comments you'd like to add to the change
	2. Click post when you're finished. 
![[Pasted image 20240508093841.png|750]]
![[Pasted image 20240508093904.png|750]]

## Code Review Scoring
### Scores
- -2 is a veto
- +2 is a "good job"
- We need at least one person to give it a +2, and no one can give it a -2. 
### refs and number
A Link back to Redmine
Every change we have **must** have a link back to Redmine. 
- Gerrit won't allow it to be merged if it doesn't have a link back. 

Any time we push, Jenkins is kicked off. 
- There are ways to initiate builds without using Gerrit, but they're a pain in the butt. If we're ready to push into Gerrit, that means we have something that we have that we need to test. 
	- We can cancel a build within Jenkins. 
- Drafts are not visible to anyone but you. Clicking reply is how we respond. 


`gitk`
- Local graphical browser
	- Smartgit, and tortoisegit are alternatives
- Great for simple `diff`s
- `gitk --all &`


## Pushing
Git commit and git add are the same, but push is differently. 
![[Pasted image 20240507155022.png|500]]

Fixing Commits is done with:
```shell
git commit --amend
```
- Look wayyyy more into this
- You can also add a `--no-edit` if you'd like to amend it to reflect other changes. 

```shell
git log
```


## ChangeIDs
You MUST have a blank line before Change-ID, looking something like this:
```
Added my_file.txt for testing upload to git server

Change-Id: I7e93e695bcba20ebeb39e342c1a5367893cf19c7

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Tue May 7 15:57:22 2024 -0600
#
# On branch master
# Your branch is ahead of 'origin/master' by 1 commit.
#   (use "git push" to publish your local commits)
#
# Changes to be committed:
#       new file:   my_file.txt
#
~

```


# Gerrit Workflow
We don't commit over and over again, but instead amend the same commit over and over again. 
- That way you don't have 120 different changesets. 
`git push origin HEAD:refs/for/master`
Squashing commits together is done through `git rebase`

We don't do `merge` in the git definition. We rebase.
- Easier to see what happens, especially with long-running code. 
- By default, rebase takes the change, and puts it on the end of the repo. 

The most recent commit is the `HEAD`

## Varex Software Repos
SDK
- History for client sdk
- Dan 

Templates and MACROS drive Keith nuts