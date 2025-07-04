---
type: note
tags: note/git
---
## Check version to see if it's installed on system
```shell
meld --version
```
## Installation on ubuntu
```shell
sudo apt-get install meld
```
## Edit global `.gitconfig` file
```shell
git config --global --edit
```
- Add these lines to tell git to use Meld as the difftool
```
   [diff]
       tool = meld
   [difftool]
       prompt = false
   [difftool "meld"]
       cmd = meld "$LOCAL" "$REMOTE"
```
