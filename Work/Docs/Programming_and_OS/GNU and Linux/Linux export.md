---
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, November 26th 2024, 1:50:58 pm
function_of: ["[[Linux environment variables]]"]
---
# Background
- Export is a built-in command of the Bash shell. It is used to mark variables and functions to be passed to child processes. Basically, a variable will be included in child process environments without affecting other environments.

# Usage
## Options

|Option|Description|
|---|---|
|**`-f`**|Exports **`[name]`**s as functions.|
|`-n` | Allows users to remove `[name]`s from the list of exported variables.|
|`-p`|Displays a list of all exported variables and functions in the current shell.|

## Examples


### Assign a Value Before Exporting

Assign a value to a variable before exporting it using the **`export`** command. For example:

```
x = 15
```


Print the value of the variable using the [echo command](https://phoenixnap.com/kb/echo-command-linux) or **`printenv`**:

```
printenv x
```

### Set a Default Value

Use the **`export`** command to assign the default value of an environment variable. For example, choose one of the [22 Best Linux text editors](https://phoenixnap.com/kb/best-linux-text-editors-for-coding) and change the default text editor to your preferred one.

Run the following command to set [vim](https://phoenixnap.com/kb/vim-commands-cheat-sheet) as the default text editor via the **`EDITOR`** variable:

```
export EDITOR= /usr/bin/vim
```

Check the value of the **`EDITOR`** variable by piping the **`export`** command output to **`grep`** and searching for the _EDITOR_ string:

```
export | grep EDITOR
```

### Change Command Line Appearance

Change and export the value of the primary prompt **`PS1`** variable, which defines the Bash prompt's default structure, displaying it every time the user logs in using the terminal. The default values of **`PS1`** are set in the _/etc/bashrc_ file.

For example, change the prompt color by running:

```
export PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '
```