---
type: note
tags: note/git
---
# Background
- Git subtree lets you nest one repository inside another as a sub-directory. 
- Useful for:
	- Integrating third-party libraries or components into your project.
	- Managing shared codebases across multiple projects.
	- Including another Git repository within your project without the need for submodules.

# Usage
## No Remote Tracking
```shell
git subtree add --prefix .vim/bundle/tpope-vim-surround https://bitbucket.org/vim-plugins-mirror/vim-surround.git main --squash
```
- Squash flag will omit all history of the other repository. 
## Steps to using
### 1. Add a subtree
```shell
git subtree add --prefix <subdirectory> <repository-url> <branch>
```
### 2. Pull changes from the subtree repo
```shell
git subtree pull --prefix <subdirectory> <repository-url> <branch>
```
### 3. Push changes to the subtree repo
```shell
git subtree push --prefix <subdirectory> <repository-url> <branch>
```
### 4. Split changes back into a separate repository (optional)
```shell
git subtree split --prefix=<subdirectory> -b <new-branch>
```
### 5. Update the subtree reference in your project
```shell
git push <repository-url> <new-branch>:<original-branch>
```