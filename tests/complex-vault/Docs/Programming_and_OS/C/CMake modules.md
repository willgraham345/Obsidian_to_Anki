---
summary: Cmake modules are a file (or group of CMake files) containing cmake commands that can be reused across different projects. Commonly, this refers to a set of commands that is used to import an external library/package. When you type find_package(OpenSSL) you're asking cmake to look for a module that knows how to locate this on your system.
type: note/concept
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
date created: Monday, January 5th 2026, 12:12:34 pm
date modified: Monday, January 5th 2026, 12:44:04 pm
template: "[[base_note_template]]"
template-version: 1.0.1
uses: ["[[CMake find_package]]", "[[CMake FindPkgConfig]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[cmake-modules(7) — CMake 4.2.1 Documentation](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html)

## Concepts of Note


󰙎 CMake modules ;; Cmake modules are a file (or group of CMake files) containing cmake commands that can be reused across different projects. Commonly, this refers to a set of commands that is used to import an external library/package. When you type find_package(OpenSSL) you're asking cmake to look for a module that knows how to locate this on your system.
󰙎 Find modules ;; Usually written by the CMake team or 3rd party users
󰙎 Config files ;; Written by library authors themselves, these are preferred over find modules. They install the library into a specific place that tells CMake exactly where everything is.

CMake looks in the system folder for modules.

### Old way vs new way
```cmake
include_directories(${CURL_INCLUDE_DIRS})
target_link_libraries(MyApp ${CURL_LIBRARIES})
```
vs
```cmake
target_link_libraries(MyApp PRIVATE CURL::libcurl)
```

## Usage