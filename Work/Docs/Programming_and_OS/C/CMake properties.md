---
summary: A property is a key value pair attached to an object.
functions: ["[[CMake set_property]]"]
date created: Thursday, October 17th 2024, 1:03:18 pm
date modified: Thursday, October 17th 2024, 1:13:57 pm
type: note/concept
---
`VIEW[**{summary}**][text(renderMarkdown)]`


[cmake-properties(7) — CMake 3.31.0-rc2 Documentation](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html)
- Global Scope
- Directory scope
- Target Scope
- 

# Background
## Property Scope
- **GLOBAL**: Applies to the entire CMake project and is accessible anywhere in the project.
- **DIRECTORY**: Applies to a specific directory (and optionally its subdirectories) and affects targets, tests, and other entities in that directory.
- **TARGET**: Applies to individual targets like executables or libraries, affecting how they are built and linked.
- **SOURCE**: Applies to individual source files, influencing their specific compilation options or behaviors.
- **INSTALL**: Applies to installation rules, controlling how targets or files are installed.
- **TEST**: Applies to individual tests, defining how tests are executed or reported.
- **CACHE**: Applies to cache variables, modifying their behavior within the CMake cache (persisted settings between runs).
