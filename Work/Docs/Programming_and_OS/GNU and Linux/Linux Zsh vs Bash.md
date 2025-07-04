---
type: note/concept
concept_of: ["[[Linux CLI]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:02:46 am
---
A shell is the environment in which commands can be executed and is the interface between the user and the UNIX system. 

## BASH (Bourne-Again Shell)
- The most popularly used shell and comes as default. Also available on windows

## Zsh (Z shell)
- Built on top of bash, with additional features
	- More flexibility with plug-in support, customization, theme, spell correction
- Default shell for macOS and Kali Linux


|Bash|Zsh|
|---|---|
|Bash is the default shell for Linux and it is released in the replacement of Bourne Shell.|Z shell is built on top of the bash shell and is an extended version of the bash with plenty of new features.|
|Bash reads the .bashrc file in non-login interactive shell and .bash_profile in login shells.|Zsh reads .zshrc in an interactive shell and .zprofile in a login shell.|
|Bash uses backslash escapes.|Zsh uses percentage escapes.|
|Bash doesn’t have an inline wildcard expansion.|Zsh has a built-in wildcard expansion.|
|Doesn’t have customization options.|Zsh has many frameworks that provide customization.|
|It doesn’t have many themes and plug-in support.|Has plenty of plug-in’s and themes.|
|Bash lacks syntax highlighting and auto-correction features.|Zsh has syntax highlighting and auto-correction features.|
|In bash keybinding is done using ‘.inputrc’ and ‘bind builtin’.|In zsh binding is done using ‘bindkey builtin’.|

Zsh's syntax is not completely compatible with bash, but it's close. A lot of code will keep working (aliases and functions). The main differences are in interactive configuration features. 

Really good [article](https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh) detailing the differences