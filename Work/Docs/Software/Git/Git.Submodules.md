---
type: note
tags: note/git
---
# Background
Git submodules allow you to keep a Git repository as a subdirectory of another git repository.
- A reference to another repository at a particular snapshot in time. 
- Git submodules let your code depend on other external code, with the external code being copied and pasted into the main repository. This method has the downside of losing any upstream changes to the external repository. 
[Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
## When to use a submodule
- When you need strict version management over your external dependencies. 
	- External component or subproject is changing too quickly, and changes will break the API. 
	- When you have a component that isn't updated very often
	- Delegating a piece of the project to a third party. 

## Forgot to pass in `--recurse-submodules` to your existing repo?
`git submodule update --init --recursive`

# Usage
## Adding a submodule
```shell
$ mkdir git-submodule-demo 
$ cd git-submodule-demo/ 
$ git init 
Initialized empty Git repository in /Users/atlassian/git-submodule-demo/.
$ git submodule add https://bitbucket.org/jaredw/awesomelibrary
```


https://www.atlassian.com/git/tutorials/git-submodule

## Removing a Submodule
### Gitkraken
Use this, it's way easier
### CLI version
1. Deinitialize the submodule
2. Remove submodule entry from configuratino
3. Delete submodule's directory
4. Commit changes
5. Update .gitmodules file (optional)
```bash
git submodule deinit path/to/submodule
git rm --cached path/to/submodule
rm -rf path/to/submodule
git commit -m "Remove submodule: path/to/submodule"

```

## Working on a Project with Submodules
Fetching updates on your submodules: `git submodule update --remote`