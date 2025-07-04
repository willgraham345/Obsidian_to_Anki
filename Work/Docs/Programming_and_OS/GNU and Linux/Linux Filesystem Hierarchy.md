---
summary: How files are typically organized within Linux
type: note/concept
concepts: ["[[Linux File Permissions]]", "[[Linux File System Types]]", "[[Linux sysfs]]", "[[Linux VFS Overview]]"]
components: ["[[Linux archive types]]", "[[Linux disk partitioning]]", "[[Linux symlinks]]"]
functions: ["[[Linux ag]]", "[[Linux df]]", "[[Linux du]]", "[[Linux fdfind]]", "[[Linux fdisk]]", "[[Linux free]]", "[[Linux grep]]", "[[Linux locate]]", "[[Linux systemd-cgls]]", "[[Linux.fzf]]"]
workflows: ["[[Linux disk partitioning]]", "[[Linux Mounting another Filesystem]]"]
concept_of: ["[[Linux]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, March 13th 2025, 1:31:21 pm
tags: [include]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage 
See hierarchy stuff with:
```shell
man hier
```

```
 +---------+-----------------+-------------+
 |         | shareable       | unshareable |
 +---------+-----------------+-------------+
 |static   | /usr            | /etc        |
 |         | /opt            | /boot       |
 +---------+-----------------+-------------+
 |variable | /var/mail       | /var/run    |
 |         | /var/spool/news | /var/lock   |
 +---------+-----------------+-------------+

 "Shareable" files are defined as those that can be stored on one host and
 used on others. "Unshareable" files are those that are not shareable. For
 example, the files in user home directories are shareable whereas device
 lock files are not. "Static" files include binaries, libraries,
 documentation files and other files that do not change without system
 administrator intervention. "Variable" files are defined as files that
 are not static.
 
```

## Rules of Thumb
- `/sbin` and `/bin` are typically related because sbin programs are needed before the other stuff is loaded
- `/, /usr`: The OS itself; things that use the native packaging system.
- `/usr/local`: things I've developed myself, or that I've compiled from source.
- `/opt`: third party products.

# Usage

## /
- Root directory, where EVERYTHING is under

## \~  a.k.a /home
- Home directory of user

### ~/.local
- Stores user-specific data in fixed directories. Followed by GNU.
- Made because Unix programs were free to spread data all over the $HOME directory. The idea is to make this behavior more predictable.
- Users put info such as emails, calendar events.
	- This data can be removed, but program will lose its state. 

### ~/.cache
- A slightly less important version of [[#~/.local]], as it can typically recall everything. 
- Single directory holding non-essential data files, defaults to ~/.cache

### ~/.config
- Same as [[#~/.local]], but for configuration 

## /bin
- Important binaries for the entire system, stuff like /bin/sh
	- Originally there for programs that needed to be on a small partition before larger /usr

## /boot
- Stuff for booting the system. Boot loader's configuration files are in the /etc with other configuration files. - /cdrom
- Temporary location for CD-ROM's inserted into system. Standard location for inserted media is in the /media folder

## /dev
- Device files (not really files, but they appear that way). See [[Linux Devices]]
	- /dev/sda represents the first SATA (interface of hard drive) drive in the system.
	- Also has pseudo-devices. /dev/random produces random numbers, /dev/null is a device that produces no output and discards all input. When you pipe an output of a command to /dev/null you're discarding it.

## /etc
- Common place to put configuration files
- User specific configuration found in each user's home directory

### /etc/apt/
#### /etc/apt/sources.list.d
- List of repositories apt will check

### /etc/systemd
#### /etc/systemd/system
- ![[#/lib/systemd/system]]

### /etc/resolv.conf
File that configures the network DNS. Read more [here](https://www.baeldung.com/linux/etc-resolv-conf-file)
- Note, this is no longer used for Raspberry PI, instead, everything is run through [[Linux NetworkManager]]

### /etc/udev/
#### /etc/udev/rules.d
- Where custom rules are made for device files. Files are conventionally named with a number as prefix (`50-udev-default.rules`) and processed in lexical order independently of file directory. Files installed in this directory override those with the same name as installed in the default system path.
- See [[Linux udev rules workflow and syntax]] for more info on how to write these files...

## /home
- Personal directories for users.

## /lib
- Libraries needed by essential binaries in /bin and /sbin folder
- Libraries needed by binaries in the /usr/bin are located within

### /lib/systemd
#### /lib/systemd/system
- Files that define how [[Linux systemd|systemd]] will handle a unit. Default location for these files
	- Read more at [[Linux systemd units#Types of Units/Best Practice]]
	- Administrator-configured units should go in [[#/etc/systemd/system]]. 
	- Non-persistent runtime modifications go in [[#/run/systemd/system]]

## /media
- Contains subdirectories where removable media devices inserted into computer are mounted. A CD will be read here.

## /mnt
- Temporary mount points. You can mount other file systems

## /opt
- Subdirectories for optional software packages.
	- Commonly used by proprietary software that doesn't obey the standard file system hierarchy.
		- These programs may dump files in /opt/application when you install it

## /proc
- Kernel and process files. Special files that represent system and process info.

## /root
- Root home directory of the root user. Distinct from "/", which is the system root directory place to store transient files.

## /root
- The root user's home directory (see also [[#/home]])

## /run
### /run/systemd/system
- See [[#/lib/systemd/system]]

## /srv
- Data for services provided by system. If you were using Apache HTTP server to serve a website, you'd want to store website files in a directory inside the /srv.

## /sbin
System management programs needed before /usr is mounted

## /tmp
- Storage for temporary files

## /usr
- Where locally complied applications install to by default.
	- Usually the package manger will install binaries, shared files, etc from all programs here. Everything other than config files (which go to etc)

### /usr/bin
- Distribution managed normal user programs
- User binaries, usually where executables are stored from package managers. 
- Where [[Linux update-alternatives]] should have its files

### /usr/sbin
Same relationship here as /sbin to bin (you need some things before the /usr/bin is installed)

### /usr/include
Includes headers for C compilers (stuff like stdio.h and stdlib.h)
- When you #include <stdio.h> this is where the compiler looks first by default. 

### /usr/lib
#### /usr/lib/udev
- Where `rules.d` file for system-installed rules is located [[#/etc/udev/rules.d]] is reserved for custom rules.

### /usr/local
- Some programs from (usually) proprietary software go here. 

#### /usr/local/bin
Small user programs *not* managed by the distribution package manager.

### /usr/share
- Shared files (media)

#### /usr/share/doc
- Documentation on shared media
- Contains applications and files used by users.
	- Non-essential applications are located in the /usr/sbin directory instead of /sbin directory. Also contains other directories, like graphics.
	- If you add a folder in your home directory titled "bin", that is where Ubuntu will look first for executable programs (\$PATH stuff). Installations in other places will be not be paid attention to because it will see this first. Additionally, other users and root users will be unable to access this program.
		- Occasionally this will not work, and you can fix this by making sure the /home/bin is added to path in your .bashrc (or equivalent) file
	- To make something usable to everyone at the local level, move programs to "/usr/local/bin" (you will need root permission)

## /var
- Location for variable things like:
	- logs
	- running process ID pointer files
	- spool directories
	- other things important for running services

### /var/log
- Usually where logs would go

### /var/lib
- Usually where libs would go. You'll see these in subdirectories (i.e. /var/lib/mysql)
