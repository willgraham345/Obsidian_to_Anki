---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Tuesday, August 12th 2025, 9:08:10 am
tags: [tools/git, tools/git/clean_reset, tools/git/config]
---

[good site with guides](https://graphite.dev/guides/topic/git)

| Modify Commits                      |                                                                                                                                                                                            |                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `git commit --amend`                | Change old commit message                                                                                                                                                                  |                                                                |
| `git commit --amend --no-edit`      | Change files that are in the commit, but keep the message.                                                                                                                                 |                                                                |
| `git rebase -i <after-this-commit>` | Squash multiple commits into one commit (NOTE: will only work from the top-down, meaning you have to squash the newest commit into the oldest commit see [[Git Rebase#Squashing Commits]]) | [guide](https://www.freecodecamp.org/news/git-squash-commits/) |
| `git rebase -i HEAD~<numCommits>`   | Squash multiple commits into one commit from last `numCommits`                                                                                                                             |                                                                |
|                                     |                                                                                                                                                                                            |                                                                |

| Go back                            |                                                                       |
| ---------------------------------- | --------------------------------------------------------------------- |
| `git reset`                        | Revert changes made to index (reset all unpushed commits)             |
| `git reset --hard origin/<branch>` | Revert local copy to the point/branch you want it to be               |
| `git checkout .`                   | Revert changes in working copy                                        |
| `git checkout <commit-id> .`       | Checkout a previous branch (make sure to add and stage it to go back) |
| `git checkout -- <file_name>`      | Discard changes in a file                                             |
| `git clean -f`                     | Remove all untracked files (Add `-d` for directories)                 |

| Branching/origin                                                             |                                                 |                                                             |
| ---------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------- |
| `git remote set-url <remote_name> <remote_url>`                              | Set the remote origin                           |                                                             |
| `git branch <branch_name>`                                                   | Create a new branch.                            |                                                             |
| `git switch <branch_name>`<br>or (less safe)<br>`git checkout <branch_name>` | Switch to a new branch (safer than checkout)    | [Guide](https://graphite.dev/guides/git-checkout-vs-switch) |
| `git switch -c <new_branch_name>`                                            | Create and switch to a branch                   |                                                             |
| `git branch -d <branch_name>`                                                | Delete a branch (safe if merged).               |                                                             |
| `git branch -v`                                                              | Shows the tracking status of the current branch |                                                             |
| `git config branch.main.remote`                                              | View the remote origin                          |                                                             |


| Configuration   |                      |
| --------------- | -------------------- |
| `git config -l` | Shows current config |
|                 |                      |

| Collaboration Commands       | Description          | Flags                                                                            |
| ---------------------------- | -------------------- | -------------------------------------------------------------------------------- |
| `git branch <branch_name>`   | Create a new branch. | `-d` = delete a branch<br>`-v` = shows the tracking status of the current branch |
| `git checkout <branch_name>` | Switch to a branch.  |                                                                                  |



  `git commit --amend` ;;; Change old commit message = #tools/git/commits 
ID: 1751997630109



  `git commit --amend --no-edit` ;;; Change files that are in the last commit, but keep the message. = #tools/git/commits 
ID: 1751997630114



  `git checkout .` ;;; Revert changes in working copy = #tools/git = `<commit-id>` Change to that commit id 
ID: 1751997630118



  `git checkout -- <file_name>` ;;; Discard changes in a file = #tools/git 
ID: 1751997630122



  `git clean` ;;; Remove all untracked files = #tools/git = `-f` is force 
ID: 1751997630126



      `-d` for directories 
  `git remote set-url <remote_name> <remote_url>` ;;; Set the remote origin = #tools/git 
ID: 1751997630130



  `git branch <branch_name>` ;;; Create a new branch. = #tools/git = `-c` Creates the new branch 
ID: 1751997630134



      `-d` Deletes the branch (safe if merged)
  `git switch <branch_name>` or `git checkout <branch_name>` ;;; Switch to a new branch (safer than checkout) = [Guide](https://graphite.dev/guides/git-checkout-vs-switch) #tools/git =  
ID: 1751997630138



  `git config branch.main.remote` ;;; View the remote origin = #tools/git/config 
ID: 1751997630143



  `git config ` ;;; Shows current config = #tools/git/config = `-l` List current config 
ID: 1751997630147



      `--system` view/edit system (machine) level
      `--global` view/edit global (user) git config
      `--local` view/edit local (repository) level
      `user.signingkey <MY_KEY_ID>` Configure git to use your gpg key
      `--list --show-origin` Also shows the origin of each config item
  `git checkout <branch_name>` ;;; Switch to a branch. = #tools/git 
ID: 1751997630153



  `git cherry -v <base> <dev>` ;;; Will compare the commits which are contained within `dev`, but not in `develop`.
  `git log <main>..<feature>` ;;; Shows the commits between the main and the feature branch.
  `git difftool <main>..<feature>` ;;; Will show the differences between two branches with your configured difftool (meld recommended) = #tools/git = `--dir-diff` Launches directory differences, rather than serial differences. 
ID: 1751997630157



  `git pull` ;;; Updates local repo with changes from remote = #tools/git = `-v` is verbose 
ID: 1751997630162



      `-ff-only` Only update to new history if there is no divergent local history.
      `-r` Rebase the current branch on top of the upstream after fetching. If there is a remote-tracking branch corresponding to the upstream branch.
      `-all` Fetch all remotes
  `git submodule update` ;;; Basically does a git pull with each submodule = #tools/git = `--init` initializes submodule recorded in the index. 
ID: 1751997630166



      `--recursive` Will recurse into nested submodules and update them as well.
  `git diff` ;;; Show changes between the working tree and the index or a tree (or tree/tree, merge/tree, blob/blob, file/file) = #tools/git = `<paths>` Two paths for limiting a diff to multiple paths.  
ID: 1751997630171



  `git cherry-pick` ;;; Grabs arbitrary commits and append them to working tree = #tools/git = [Git Cherry Pick | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/cherry-pick) 
ID: 1751997630175

# Common Q&A

## Merge Request vs Pull Request
There's no real distinction, it's semantics. A merge request is assigned to someone to review your code.

## What is a Github submodule?
A way to include one Git repository within another.

### Steps on how to Initialize a new Submodule
1. Have a working repository
2. Add a submodule using 
  ```bash
   git submodule add <URL>
   ```
3. Initialize Submodule, must be done after adding. 
```bash
git submodule init
```
4. Update submodule, which will fetch the contents of the submodule
```bash
git submodule update
# The --recursive flag can be used to automatically update all submodules. 
```




