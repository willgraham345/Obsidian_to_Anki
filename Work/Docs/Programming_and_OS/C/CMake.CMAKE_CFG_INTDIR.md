---
type: note
---
# Background
- [CMAKE_CFG_INTDIR](https://cmake.org/cmake/help/latest/variable/CMAKE_CFG_INTDIR.html#variable:CMAKE_CFG_INTDIR)
- Deprecated since version 3.21: This variable has poor support on [`Ninja Multi-Config`](https://cmake.org/cmake/help/latest/generator/Ninja%20Multi-Config.html#generator:Ninja%20Multi-Config "Ninja Multi-Config"), and predates the existence of the [`$<CONFIG>`](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#genex:CONFIG "CONFIG") generator expression. Use `$<CONFIG>` instead.
- Build-time reference to per-config output subdirectory. 
	- This variable is read-only

For native build systems supporting multiple configurations in the build tree (Visual Studio Generators and Xcode), the value is a reference to a build-time variable specifying the name of the per-configuration output subdirectory. 

# Usage
## Example values
```cmake
$(ConfigurationName) = Visual Studio 9
$(Configuration)     = Visual Studio 12 and above
$(CONFIGURATION)     = Xcode
.                    = Make-based tools
.                    = Ninja
${CONFIGURATION}     = Ninja Multi-Config
```
- These value are evaluated by the native build system, this variable is suitable only for use in command lines that will be evaluated at build time. 
Intended usage
```cmake
add_executable(mytool mytool.c)
add_custom_command(
  OUTPUT out.txt
  COMMAND ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool
          ${CMAKE_CURRENT_SOURCE_DIR}/in.txt out.txt
  DEPENDS mytool in.txt
  )
add_custom_target(drive ALL DEPENDS out.txt)
```
- `CMAKE_CFG_INTDIR` is no longer interested for this purpose but has been left for compatibility with existing projects. 
	- 