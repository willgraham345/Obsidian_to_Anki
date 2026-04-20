---
summary:
type: note/configuration
headings:
  - "[[#Concepts of Note]]"
configurations:
  - "[[CMake Build Configurations]]"
processes:
  - "[[CMake toolchain variables and properties]]"
concept_of:
  - "[[CMake Workflow 1 Configuration]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 30th 2026, 11:50:39 am
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[Clang]]"
  - "[[gcc and gpp]]"
  - "[[QNX QCC]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- CMake uses a toolchain (collection of software development tools used for building, compiling, and debugging) for compiling, linking, creating archives, and other tasks to *drive* the build. 
- Must be defined before CMake starts processing the `CMakeLists.txt` file, unless you provide this with the command-line argument
	- CMake will validate the compiler and linker by building and discarding a simple test application. A toolchain configuration must define all compiler and linker options necessary to perform a successful test build. 
- 

### Cross Compiling
- If compiling for a platform different than the one you're on (i.e. compile for Linux while on Windows), then the recommended way to handle this is by overriding the default toolchain with a file.
	- We will specify the location and command names of the compiler, linker, and other build tools (toolchain). 
- Add a command line to [[CMake CLI commands]] to tell it to read toolchain information from a file. 

### Toolchain Definition Files
A toolchain definition file should define variables for the target system name and version. Namely:
- [[CMake CMAKE_SYSTEM_NAME]]
- [[CMake CMAKE_SYSTEM_VERSION]]
- [[CMake CMAKE_C_COMPILER]]
- [[CMake CMAKE_CXX_COMPILER]]
A downside of specifying pathnames for tools rather than the command name is that the path will need to be updated as the build tool is moved. 

### Languages
- Enabled by the [[CMake project]] command. 
	- Language-specific built-in variables are also enabled by the same command.

### Variables and Properties
- See [[CMake toolchain variables and properties]]

### Toolchain Features
[[CMake try_compile]] can be used to test capability and availability of various toolchain features. These APIs test the toolchain in some way and cache the result so that the test does not have to be performed again the next time CMake runs. 

Some toolchain features have built-in handling in CMake, and do not require compile-tests. 

### Linux
### Clang
Variables relating to the language components of a toolchain

## Properties
### Variables
`CMAKE_<LANG>_COMPILER`
- Full path to the compiler used for `<LANG>`

`CMAKE_<LANG>_COMPILER_ID`
- Compiler identifier used by CMake

`CMAKE_<LANG>_COMPILER_VERSION`
- Version of the compiler

`CMAKE_<LANG>_FLAGS`
- Variables and configuration-specific equivalents contain flags that will be added to the compile command when compiling a file of a particular language

### Configurations
`CMAKE_TOOLCHAIN_FILE`