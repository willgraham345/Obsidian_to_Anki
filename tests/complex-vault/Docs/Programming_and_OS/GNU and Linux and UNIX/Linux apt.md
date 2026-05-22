---
summary: Interactive cl tool for managing debian-based system packages, doing everything that is needed to get your system to successfully execute the new installed software. A tool that combines various commands from apt-get and apt-cache with improved usability.
type: note/system
headings:
  - "[[#Commands]]"
  - "[[#Usage]]"
  - "[[#Workflow]]"
prev:
  - "[[Linux apt-cache]]"
  - "[[Linux apt-get]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, February 2nd 2026, 10:35:38 am
item_of:
  - "[[Linux Package Management]]"
tags: [tools/package_management]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
  `apt install <package_to_install_1> <package_to_install_2>` ;;; Installs a package using apt, will likely need sudo access
  `apt remove <package>` ;;; Removes a package using apt, will likely need sudo access
  `apt purge <package>` ;;; Removes a package and its configuration files using apt, will likely need sudo access
  `apt update <package>` ;;; Updates a package, needs update first.
  `apt upgrade <package>` ;;; Upgrades a package, needs update first.
  `add-apt-repository ppa:<repository_name>` ;;; Adds a new repository source to apt (`/etc/apt/sources.list.d/`)
  `add-apt-repository -- remove ppa:<repository_name>` ;;; Remove a repository source to apt.
  `apt search <keyword>` ;;; Searches for a package by name or description
  `apt show <package_name>` ;;; Searches for a package by name or description, and prints its information

## Workflow
![[Pasted image 20240515154142.png | 500]]

 1. Checks for dependencies based on the `etc/apt/sources.list` file
 2. Downloads the package, verifies it, and then tells [[Linux dpkg]] to install it
	 1. [[Linux apt# apt-get]] installs needed ones into a temporary directory (`/var/cache/apt/archives/`)
 3. See [[Linux dpkg# How it works]] for more information

[Common Ubuntu Packages](https://packages.ubuntu.com/search?suite=default&section=all&arch=any&searchon=names&keywords=emacs)

