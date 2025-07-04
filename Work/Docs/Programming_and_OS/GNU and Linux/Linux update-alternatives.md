---
summary: A tool that juggles multiple versions of something on the same machine through symbolic links located in the /usr/bin directory.
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Workflow]]"
date created: Tuesday, September 3rd 2024, 11:44:42 am
date modified: Thursday, March 13th 2025, 1:34:20 pm
function_of:
  - "[[Linux Package Management]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of note
- History
	- Creates, removes, maintains, and displays information about the symbolic links comprising the alternatives system. 
		- The alternatives system was written to remove the dependency on perl, and is intended to be a drop in replacement for Debian's update-dependencies script.
- Two different modes
	1. Auto mode
		1. The command will select the generic name of the highest program automatically based on the Priority value of the alternates. (Highest priority gets set as the generic)
	2. Manual mode
		2. Sets the generic name as the user selected alternative irrespective of the Priority value of the alternatives
- ! IMPORTANT GOTCHA
	- Make sure to have the version for `update-alternatives` in the `/usr/bin`
		- If you have the version located in `/usr/local/bin`, it will not work correctly and will not have the `--config` option. **Remove this version**

# Workflow
Switch between manual/auto mode for a given thing
```
sudo update-alternatives --auto editor
```

Basic Install
```
sudo update-alternatives --install <path_to_have_different_versions> <program> <path_to_install_location>
```

Change between different usage of C++ instances
[More info here](https://linuxconfig.org/how-to-switch-between-multiple-gcc-and-g-compiler-versions-on-ubuntu-22-04-lts-jammy-jellyfish)
Before running this, it's assumed you installed gcc and g++ versions 8, 9 and 10
```shell
sudo apt -y install gcc-8 g++-8 gcc-9 g++-9 gcc-10 g++-10
```

then...
```shell
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 9
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 9
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 10
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 10
```
switching between versions
```shell
$ sudo update-alternatives --config gcc
There are 3 choices for the alternative gcc (providing /usr/bin/gcc).

  Selection    Path            Priority   Status
------------------------------------------------------------
  0            /usr/bin/gcc-9   9         auto mode
  1            /usr/bin/gcc-10  10         manual mode
* 2            /usr/bin/gcc-8   8         manual mode
  3            /usr/bin/gcc-9   9         manual mode
```

Example for switching between all tools
```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10 --slave /usr/bin/gcov-tool gcov-tool /usr/bin/gcov-tool-10 --slave /usr/bin/gcov-dump gcov-dump /usr/bin/gcov-dump-10
```