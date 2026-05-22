---
summary: CLI tool and executable used for interaction with the CMake buildsystem. Can be used in script, as well as from command line. Helps you run, build, and install any cmake projects.
type: note/process
headings:
similar:
  - "[[CMake gui]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 11:47:56 am
tags: [tools/cmake]
template:
template-version:
tool_of:
  - "[[CMake]]"
---

# Usage
## Basic Usage
1. Create and change directory to where you want the binaries to be placed. 
2. Run `cmake` specifying the path to the source tree and pass in options with the `-D` flag. 
3. The configure and generate steps are combined into one when using the `cmake` executable. 

## Syntax


 - [p] `cmake [options>] -B path-to-build> [-S path-to-source>]` = Generate a Project Buildsystem = 
 - [p] `cmake --build dir> [options] [-- build-tool-options]` = Build a project = 
 - [p] `cmake --install dir [options]` = Install a project = 
 - [p] `cmake --open dir` = Open a project = 
 - [p] `cmake [-D var=value]... -P cmake-script-file` = Run a script = 
 - [p] `cmake -E command [options]` = Run a command line tool = 
 - [p] `cmake --find-package [options]` = Run the find-package tool = 
 - [p] `cmake --workflow [options]` = Run the workflow preset = 
 - [p] `cmake --help[-topic]` = view help = 
