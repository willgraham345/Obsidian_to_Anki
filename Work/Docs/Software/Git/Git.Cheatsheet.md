---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, April 16th 2025, 11:15:29 am
tags: [command/git, command/git/clean_reset, command/git/config]
---
[good site with guides](https://graphite.dev/guides/topic/git)

| Modify Commits                      |                                                                                                                                                                                            |                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `git commit --amend`                | Change old commit message                                                                                                                                                                  |                                                                |
| `git commit --amend --no-edit`      | Change files that are in the commit, but keep the message.                                                                                                                                 |                                                                |
| `git rebase -i <after-this-commit>` | Squash multiple commits into one commit (NOTE: will only work from the top-down, meaning you have to squash the newest commit into the oldest commit see [[Git.Rebase#Squashing Commits]]) | [guide](https://www.freecodecamp.org/news/git-squash-commits/) |
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



- [p] `git commit --amend` = Change old commit message = #command/git
<!--ID: 1751434089755-->

- [p] `git commit --amend --no-edit` = Change files that are in the commit, but keep the message. = #command/git
<!--ID: 1751434089759-->

- [p] `git checkout .` = Revert changes in working copy = #command/git = `<commit-id>` Change to that commit id
<!--ID: 1751434089763-->

- [p] `git checkout -- <file_name>` = Discard changes in a file = #command/git
<!--ID: 1751434089767-->

- [p] `git clean` = Remove all untracked files = #command/git = `-f` is force
<!--ID: 1751434382606-->

      `-d` for directories 
- [p] `git remote set-url <remote_name> <remote_url>` = Set the remote origin = #command/git
<!--ID: 1751434089772-->

- [p] `git branch <branch_name>` = Create a new branch. = #command/git = `-c` Creates the new branch
<!--ID: 1751434089776-->

      `-d` Deletes the branch (safe if merged)
- [p] `git switch <branch_name>` or `git checkout <branch_name>` = Switch to a new branch (safer than checkout) = [Guide](https://graphite.dev/guides/git-checkout-vs-switch) #command/git = 
<!--ID: 1751434089780-->

- [p] `git config branch.main.remote` = View the remote origin = #command/git/config
<!--ID: 1751434089785-->

- [p] `git config ` = Shows current config = #command/git/config = `-l` List current config
<!--ID: 1751434089790-->

      `--system` view/edit system (machine) level
      `--global` view/edit global (user) git config
      `--local` view/edit local (repository) level
      `user.signingkey <MY_KEY_ID>` Configure git to use your gpg key
      `--list --show-origin` Also shows the origin of each config item
- [p] `git checkout <branch_name>` = Switch to a branch. = #command/git
<!--ID: 1751434089795-->

- [p] `git cherry -v <base> <dev>` = Will compare the commits which are contained within `dev`, but not in `develop`.
- [p] `git log <main>..<feature>` = Shows the commits between the main and the feature branch.
- [p] `git difftool <main>..<feature>` = Will show the differences between two branches with your configured difftool (meld recommended) = #command/git = `--dir-diff` Launches directory differences, rather than serial differences.
<!--ID: 1751434089799-->

- [p] `git pull` = Updates local repo with changes from remote = #command/git = `-v` is verbose
<!--ID: 1751434089803-->

      `-ff-only` Only update to new history if there is no divergent local history.
      `-r` Rebase the current branch on top of the upstream after fetching. If there is a remote-tracking branch corresponding to the upstream branch.
      `-all` Fetch all remotes
- [p] `git submodule update` = Basically does a git pull with each submodule = #command/git = `--init` initializes submodule recorded in the index.
<!--ID: 1751434089808-->

      `--recursive` Will recurse into nested submodules and update them as well.
- [p] `git diff` = Show changes between the working tree and the index or a tree (or tree/tree, merge/tree, blob/blob, file/file) = #command/git = `<paths>` Two paths for limiting a diff to multiple paths. 
<!--ID: 1751434089812-->

- [p] `git cherry-pick` = Grabs arbitrary commits and append them to working tree = #command/git = [Git Cherry Pick | Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/cherry-pick)
<!--ID: 1751434089816-->


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




