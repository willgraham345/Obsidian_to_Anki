---
type: note/component
component_of: ["[[Linux Kernel]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, November 25th 2024, 5:08:24 pm
---
# Background
The linux kernel config and build system. Been around since the Linux kernel code migrated to Git. 

## Targets
A target is an optional interface for the build system, defined within their appropriate makefiles. 

|   |   |
|---|---|
|`menuconfig`|Update current config utilizing a menu-based program. The most popular option. |
|config|Update current config utilizing a line-oriented program|
|nconfig|Update current config utilizing a ncurses menu-based program|
|xconfig|Update current config utilizing a Qt-based frontend|
|gconfig|Update current config utilizing a GTK+ based frontend|
|oldconfig|Update current config utilizing a provided .config as base|
|localmodconfig|Update current config disabling modules not loaded|
|localyesconfig|Update current config converting local mods to core|
|defconfig|New config with default from Arch-supplied defconfig|
|savedefconfig|Save current config as ./defconfig (minimal config)|
|allnoconfig|New config where all options are answered with 'no'|
|allyesconfig|New config where all options are accepted with 'yes'|
|allmodconfig|New config selecting modules when possible|
|alldefconfig|New config with all symbols set to default|
|randconfig|New config with a random answer to all options|
|listnewconfig|List new options|
|olddefconfig|Same as oldconfig but sets new symbols to their default value without prompting|
|kvmconfig|Enable additional options for KVM guest kernel support|
|xenconfig|Enable additional options for xen dom0 and guest kernel support|
|tinyconfig|Configure the tiniest possible kernel|

`menuconfig` is the most popular of the targets
- A configuration mechanism provided by the Linux kernel build system that provides menu-based access to the different kernel options. 


Targgets are processed by different host programs which are provided by the kernel and built during kernel building.
- Some targets have a GUI, while most don't 
- Housed under the `scripts/kconfig/` in the kernel source

# Kconfig's Infrastructure
Has parts to implement a new language to define configuration items
Parses Kconfig language and deals with configuration actions