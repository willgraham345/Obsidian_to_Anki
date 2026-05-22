---
type: cheatsheet
date created: Thursday, August 29th 2024, 4:41:00 pm
date modified: Thursday, February 6th 2025, 10:02:18 am
library_of: "[[Linux CLI]]"
---

|Expression|Example|Description|
|---|---|---|
|`!!`|`sudo !!`|Last command (`sudo !!`)|
|`!*`|`vim !*`|Last command’s parameters (`vim !*`)|
|`!^`||Last command’s first parameter|
|`!$`||Last command’s last parameter|
|`!?ls` `<tab>`|`sudo !?mv` `<tab>`|Command and params of last `ls` command|
|`!?ls?:*` `<tab>`||Params of last `ls` command|
|`*(m0)`|`rm *(m0)`|Last modified today|
|`*(m-4)`||Last modified <4 days ago|

![[Linux tmux keybindings.png| 1200]]
Changing shell
```bash
chsh -s `which zsh`
```

[Bash cheatsheet](https://devhints.io/bash)