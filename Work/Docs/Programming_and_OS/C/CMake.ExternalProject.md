---
type: note
---
# Background
`ExternalProject_Add()` creates a custom target to drive download, update/patch, configure, build, install and test steps of an external project. 
- Individual steps within the process can be driven independently if required.
- Directory structure used for the management of the external project can also be customized. The function supports a large number of options which can be used to tailor the external project behavior. 

[Docs](https://cmake.org/cmake/help/latest/module/ExternalProject.html#module:ExternalProject)
## Similar Modules
- [[CMake.FetchContent]]

# Usage