---
summary: A tool used for recompilation various pieces of a large program and issues commands to recompile them. Needs makefiles to work.
up:
  - "[[Cpp.build.tools.overview]]"
down:
  - "[[GNU make.makefile cleaning the directory]]"
  - "[[GNU make.makefile how make processes a makefile]]"
  - "[[GNU make.makefile implicit rules]]"
  - "[[GNU make.makefile rules]]"
  - "[[GNU make.makefile simple makefile]]"
  - "[[GNU make.makefile styles]]"
  - "[[GNU make.makefile variables]]"
  - "[[GNU make.makefile]]"
concepts:
  - "[[GNU make.makefile rules]]"
components:
  - "[[GNU make.makefile variables]]"
  - "[[GNU make.makefile]]"
similar:
  - "[[CMake Workflow]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, November 1st 2024, 4:26:54 pm
tags:
  - command/make
type: note
---

[GNU make](https://www.gnu.org/software/make/manual/make.html)

```breadcrumbs
title: Breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

# Background

- A tool that controls the generation of executables and other non-source files of a program from the program's source files.
- Gets its knowledge of how to build your program from a _Makefile_
- Applies to any process that involves executing arbitrary commands to transform a source file to a target result. Not tied to any particular programming language.
  - Automatically determines which source files have been changed and performs minimal build process to get final output
- You _can_ use it to compile C++, but that doesn't mean you _should_ use it to compile C++

Capabilities

- Enables end user to build and install package without knowing details of how its done
- Figure out automatically what it needs to update.
  - Automatically determines proper order for updating files, in case on non-source file depends on another non-source file.
- Not limited to any one language. The makefile specifies the shell commands for each non-source file. These shell commands can run a compiler to produce an object file, the linker to produce an executable, `ar` to update a library, or TeX or Makeinfo to format documentation.
- Make is not limited to building a package. It can be used to control installing or deinstalling a package, generate tags tables for it.

# Make Rules and Targets

_Rule_

- Tells Make how to execute a series of commands in order to build a _target_ file from source files. Specifies a list of _dependencies_ of the target file. Should include all files which are used as inputs to the commands in the rule.

Rule Example

```
target:   dependencies ...
          commands
          ...
```

- The commands required for a target comprise a recipe.

# Usage

[GNU make](https://www.gnu.org/software/make/manual/make.html#Running)

- [p] `make <target>` = Run make on a target = #command/make = `-f` Specify the file option
<!--ID: 1751434091125-->

  `all` Make all the top-level targets the makefile knows about
  `clean` Delete all files that are normally created by running make.
  `install` Copy the executable files into a directory that users typically search for commands.
  `tar` Create a tar file of the source files.
- [p] `make <target> install` = Automated way to install built software to a system. Defaults to `/usr/local/bin`

## See all targets

Type make into the command line and double tab
