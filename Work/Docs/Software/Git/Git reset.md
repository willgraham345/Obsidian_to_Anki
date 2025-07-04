---
summary: Great for removing tracked changes.
type: note/function
up: ["[[Git]]"]
associations: ["[[Git.clean]]"]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, April 16th 2025, 11:18:14 am
function_of: ["[[Git]]"]
tags: [command/git/clean_reset, note/git]
---
# Background
- 3 ways to use `git reset`
	- `--soft`
	- `--mixed`
	- `--hard`'

- Git has "3 trees" which are node and pointer-based data structures used to track timeline of edits.
	- [[Git.Working Directory]]
	- [[Git.Staging Index]]
	- [[Git.Commit History]]

- `git reset` behaves similarly to `git checkout`, but `git checkout` only operates on the `HEAD` reference pointer. 
- `git reset` will move the `HEAD` reference pointer and the current branch of the reference pointer. 

## Usage
- [p] `git reset --hard origin/branch` = Reset local copy to branch you want your local to be = #command/git/clean_reset 
<!--ID: 1751434089827-->

- [p] `git reset` = Revert tracked changes (hard->reset HEAD+working tree)(soft->reset only HEAD) = #command/git/clean_reset
<!--ID: 1751434089833-->


## Unstage a file back to the currrent commit
```shell
git reset HEAD <file>
```