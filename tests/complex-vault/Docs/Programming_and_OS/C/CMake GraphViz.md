---
summary: CMake outputs the dependency graphs as a graphviz dot file. This can be VERY useful for debugging pu
type: note/process
headings:
  - "[[#Usage]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 11:50:53 am
item_of:
  - "[[CMake]]"
tags:
  - tools/cmake
template:
template-version:
process_of:
  - "[[Graphviz]]"
---

# Summary
A way to show dependencies in a project, as well as external libraries

# Additional Background
[Variable Specific to Graphviz](https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions)

## Usage
### Generating CMake Target Dependency Graph
  `cmake -S "path_to/src/CMake" --graphviz<equalSign>foo.dot` ;;; Generate a graph of the dependencies for the entire CMake project. Generates a `foo.dot` file showing *all* dependencies within the project. =   
ID: 1751997629887



```shell
cmake --graphviz=foo.dot
# or
cmake -S "path_to/src/CMake" --graphviz=foo.dot
```
Produces:
- `foo.dot` showing dependencies
- `foo.dot.<target>` for each target
- `foo.dot.<target>dependers>` file for each target

### Generate Header Dependency Graph C++
### Convert dot file to an image
  `dot -Tpng -o foo.png foo.dot` ;;; Convert a `.dot` file into an image (typically done with `cmake --graphviz`) = See [Graphviz variables here](https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions) 
ID: 1751997629892




```shell
dot -Tpng -o foo.png foo.dot
# or
dot graph -Tsvg -o graph.svg
```

### Variables Specific to Graphviz
<iframe src="https://cmake.org/cmake/help/latest/module/CMakeGraphVizOptions.html#module:CMakeGraphVizOptions" style="width: 100%; height: 800px;"></iframe>
