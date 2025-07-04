---
type: note
tags:
  - note/git
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Monday, August 26th 2024, 12:41:18 pm
---
# Usage
## Writing a value
```shell
git config --<level> <parent>.<child> "<string>"
```

### Email
```shell
git config user.email
%% for example %%
git config --global user.email "your@email.com"
```

### Username
```shell
git config --global user.name "Your name"
```

### Editor
#### Vim
```shell
~ git config --global core.editor "vim"~
```

### Merge tools

### Color Outputs
`color.ui`
- Master variable for git colors. Setting this to false will disable this. 
- [Changing color outputs on git](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)

## Show Current Configuration
```shell
git config --global --list --show-origin
```

# Background
- The git config is a function that lets you set both global and local git configuration files. 
- Configuration names are dot delimited strings, composed of a section and a key based on their hierarchy
	- `user.email` Email is a child property of the user configuration block. 

## Git Config levels and files
- Can accept arguments to specify configuration levels to operate on
`--local`
- Writes to a local level if no configuration option is passed. Applied to the context repository `git config` is invoked in. Files will be stored in `.git/config`
`--global`
- User-specific, meaning it is applied to an OS system user. Configuration files are stored in a file located in a user's home directory (`~/.gitconfig`  or `C:\Users\\.gitconfig`)
`--system`
- Applied across an entire machine. Covers all operating systems and repos. Config file lives off the system root path `$(prefix)/etc/gitconfig` for unix systems
