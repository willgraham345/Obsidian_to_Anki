---
type: note
---
# Background
[cmake-init](https://github.com/friendlyanon/cmake-init.git)
- REALLY good library for starting a new CMake library. Can be installed with python, and also can be invoked from the command line. 

# Usage
## Start a new library
```shell
cmake-init [--c] <path>
```
### Options
`-s`: Shared library
`-e`: Executable
`-h`: Header only library
`-c`: Set generated project's type to C instead of C++
`-p`: Select a package manager from the project
#### Package Managers
Options
- none
- `conan`
- `vcpkg`
When using a package manager, the following packages are used in the generated project
- fmt for C++, json-c and hedley for C projects
- Catch2 as as dev dependency for C++ and C projects. 
There is a generated HACKING document to see what needs to be done to fetch dependencies