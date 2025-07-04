---
summary: Interactive cl tool for managing debian-based system packages, doing everything that is needed to get your system to successfully execute the new installed software. A tool that combines various commands from apt-get and apt-cache with improved usability.
type: note/system
headings:
  - "[[#Commands]]"
  - "[[#Workflow]]"
prev:
  - "[[Linux apt-cache]]"
  - "[[Linux apt-get]]"
component_of:
  - "[[Linux Package Management]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, March 13th 2025, 10:19:38 am
tags:
  - command/linux/package_management
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Workflow
![[Pasted image 20240515154142.png | 500]]

 1. Checks for dependencies based on the `etc/apt/sources.list` file
 2. Downloads the package, verifies it, and then tells [[Linux dpkg]] to install it
	 1. [[Linux apt# apt-get]] installs needed ones into a temporary directory (`/var/cache/apt/archives/`)
 3. See [[Linux dpkg# How it works]] for more information

[Common Ubuntu Packages](https://packages.ubuntu.com/search?suite=default&section=all&arch=any&searchon=names&keywords=emacs)

# Commands
- [p] `apt install <package_to_install_1> <package_to_install_2>` = Installs a package using apt, will likely need sudo access = #command/linux/package_management
<!--ID: 1751434091094-->

- [p] `apt remove <package>` = Removes a package using apt, will likely need sudo access = #command/linux/package_management 
<!--ID: 1751434091098-->

- [p] `apt purge <package>` = Removes a package and its configuration files using apt, will likely need sudo access = #command/linux/package_management 
<!--ID: 1751434091101-->

- [p] `apt update <package>` = Updates a package, needs update first. = #command/linux/package_management 
<!--ID: 1751434091105-->

- [p] `apt upgrade <package>` = Upgrades a package, needs update first. = #command/linux/package_management 
<!--ID: 1751434091109-->

- [p] `add-apt-repository ppa:<repository_name>` = Adds a new repository source to apt (`/etc/apt/sources.list.d/`) = #command/linux/package_management  = `--remove` changes this to a remove command.
<!--ID: 1751434091113-->

- [p] `apt search <keyword>` = Searches for a package by name or description =  #command/linux/package_management 
<!--ID: 1751434091117-->

- [p] `apt show <package_name>` = Searches for a package by name or description, and prints its information =  #command/linux/package_management 
<!--ID: 1751434091121-->
