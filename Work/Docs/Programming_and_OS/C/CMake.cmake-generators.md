---
summary: 
type: note/component
component_of: ["[[CMake]]"]
concept_of: ["[[CMake Workflow 2 Generation]]", "[[Doxygen TOC]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 3:39:37 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
A CMake generator is responsible for writing input files for a native build system. Exactly one of the CMake Generators must be selected for a build tree to determine what native build system is to be used. 

CMake generators are platform-specific so each may be available only on certain platforms. [[CMake CLI commands]] will output list of available generators on the current platform. 

## CMake Generators
### Command Line Build Tool Generators
#### Makefile generators
- [Borland Makefiles](https://cmake.org/cmake/help/latest/generator/Borland%20Makefiles.html)
- [MSYS Makefiles](https://cmake.org/cmake/help/latest/generator/MSYS%20Makefiles.html)
- [MinGW Makefiles](https://cmake.org/cmake/help/latest/generator/MinGW%20Makefiles.html)
- [NMake Makefiles](https://cmake.org/cmake/help/latest/generator/NMake%20Makefiles.html)
- [NMake Makefiles JOM](https://cmake.org/cmake/help/latest/generator/NMake%20Makefiles%20JOM.html)
- [Unix Makefiles](https://cmake.org/cmake/help/latest/generator/Unix%20Makefiles.html)
- [Watcom WMake](https://cmake.org/cmake/help/latest/generator/Watcom%20WMake.html)

#### Ninja Generators
- [Ninja](https://cmake.org/cmake/help/latest/generator/Ninja.html)
- [Ninja Multi-Config](https://cmake.org/cmake/help/latest/generator/Ninja%20Multi-Config.html)

### IDE Build Tool Generators
#### Visual Studio
- [Visual Studio 6](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%206.html)
- [Visual Studio 7](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%207.html)
- [Visual Studio 7 .NET 2003](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%207%20.NET%202003.html)
- [Visual Studio 8 2005](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%208%202005.html)
- [Visual Studio 9 2008](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%209%202008.html)
- [Visual Studio 10 2010](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2010%202010.html)
- [Visual Studio 11 2012](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2011%202012.html)
- [Visual Studio 12 2013](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2012%202013.html)
- [Visual Studio 14 2015](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2014%202015.html)
- [Visual Studio 15 2017](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2015%202017.html)
- [Visual Studio 16 2019](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2016%202019.html)
- [Visual Studio 17 2022](https://cmake.org/cmake/help/latest/generator/Visual%20Studio%2017%202022.html)

### Extra Generators

# Usage