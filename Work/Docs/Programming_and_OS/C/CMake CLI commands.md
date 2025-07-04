---
summary: CLI tool and executable used for interaction with the CMake buildsystem. Can be used in script, as well as from command line. Helps you run, build, and install any cmake projects.
type: note
similar: ["[[CMake.gui]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 12:05:22 pm
tags: [command/cmake, Generate]
---
# Usage
## Basic Usage
1. Create and change directory to where you want the binaries to be placed. 
2. Run `cmake` specifying the path to the source tree and pass in options with the `-D` flag. 
3. The configure and generate steps are combined into one when using the `cmake` executable. 

## Syntax


 - [p] `cmake [options>] -B path-to-build> [-S path-to-source>]` = Generate a Project Buildsystem = #command/cmake 
 - [p] `cmake --build dir> [options] [-- build-tool-options]` = Build a project = #command/cmake 
 - [p] `cmake --install dir [options]` = Install a project = #command/cmake 
 - [p] `cmake --open dir` = Open a project = #command/cmake 
 - [p] `cmake [-D var=value]... -P cmake-script-file` = Run a script = #command/cmake 
 - [p] `cmake -E command [options]` = Run a command line tool = #command/cmake 
 - [p] `cmake --find-package [options]` = Run the find-package tool = #command/cmake 
 - [p] `cmake --workflow [options]` = Run the workflow preset = #command/cmake 
 - [p] `cmake --help[-topic]` = view help = #command/cmake 
