---
type: note
tags: note/git
---
# Background
- A remote in git, is a repository on the internet that is tied to a folder on your computer. The remote tells Git where to push or pull from
- The command that lets you interact with remote repositories, hosted on servers. 
- This lets us collaborate with others

# Important Git Remotes
## Origin
- The origin is the alias for a particular remote repository. 
- When you clone a repo with `git clone`, it automatically creates a remote connection called `origin` pointing back to the cloned repo. 
- Most repositories call their central repository `origin`
### Viewing the Origin
```bash
git remote -v
# or
git remote show origin
```
### Setting the correct remote origin
```bash
git remote set-url <remote_name> <remote_url>
```
#### Example
```shell
git remote add origin https://github.com/OWNER/REPOSITORY.git
```
# Usage
### View Remotes
```shell
git remote -v
```

```shell
git remote
```
### Adding Remotes
```shell
git remote add <remote_name> <repository_url>
```

### Renaming Remotes
```shell
git remote rename origin upstream 
```

### Fetching changes from a remote
```shell
git fetch <remote_name>
```

### Get a URL
```shell
git remote get-url <remote_name>
```