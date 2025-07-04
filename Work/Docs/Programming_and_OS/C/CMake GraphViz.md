---
summary: CMake outputs the dependency graphs as a graphviz dot file. This can be VERY useful for debugging pu
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, November 13th 2024, 9:52:40 am
tags:
  - command/cmake
type: note/workflow
component_of:
  - "[[CMake]]"
---
# Background
A way to show dependencies in a project, as well as external libraries

[Variable Specific to Graphviz](https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions)

# Usage

## Generating CMake Target Dependency Graph
- [p] `cmake -S "path_to/src/CMake" --graphviz<equalSign>foo.dot` = Generate a graph of the dependencies for the entire CMake project. Generates a `foo.dot` file showing *all* dependencies within the project. = #command/cmake  
<!--ID: 1751434091815-->

```shell
cmake --graphviz=foo.dot
# or
cmake -S "path_to/src/CMake" --graphviz=foo.dot
```
Produces:
- `foo.dot` showing dependencies
- `foo.dot.<target>` for each target
- `foo.dot.<target>dependers>` file for each target

## Generate Header Dependency Graph C++
## Convert dot file to an image
- [p] `dot -Tpng -o foo.png foo.dot` = Convert a `.dot` file into an image (typically done with `cmake --graphviz`) #command/cmake = See [Graphviz variables here](https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions)
<!--ID: 1751434091819-->


```shell
dot -Tpng -o foo.png foo.dot
# or
dot graph -Tsvg -o graph.svg
```

## Variables Specific to Graphviz
<iframe src="https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions" style="width: 100%; height: 800px;"></iframe>