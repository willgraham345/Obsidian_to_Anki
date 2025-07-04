---
type: note
tags: note/VSCode
---
# Background
Can be done with either
- [[VSCode CMake Presets]]
- [[VSCode CMake Kits]]
Designed to work well, even if you run CMake from the command line, or another IDE/tool. 
## Configure Step
The *configure step* refers to:
- Detecting requirements
- Generating build files that will produce the final compiled artifacts
### Concepts
- [[CMake.Cache]] is a list of key-value pairs. Contains a lot of stuff. 
- Cache initializer arguments are arguments passed to CMake that set values in the cache before any CMake scripts are run (see [[CMake.Cache#Cache Initializer Arguments]])
- CMake doesn't do the build itself, it relies on the build tools installed on your system. The result of a configure depends on the CMake generator. [[CMake.cmake-generators]]
### Configure Step in Detail
CMake tools drives CMake via the cmake-file-api. 
The following are taken into consideration
1. The active kit
	1. These provide info about the toolchains available on your system
		1. Toolchain, [[CMake.CMAKE_TOOLCHAIN_FILE]]
		2. Compilers, sets the `CMAKE_<LANG>_COMPILER` cache variable for each `<LANG>` in the kit
		3. For Visual Studio, it has other stuff. See [docs](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/configure.md#the-cmake-tools-configure-step)
2. Which generator to use
	1. config setting `cmake.generator`
	2. config setting `cmake.preferredGenerators`
	3. Kit's `preferredGenerator` attribute
3. Config options 
	1. See [[VSCode CMake Tools Configure Settings]] for a full list
	2. Big ones include:
		- The `cmake.configureSettings` option from `settings.json`.
		- The `settings` value from the active [variant options](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/variants.md#variants-options).
		- `BUILD_SHARED_LIBS` is set based on [variant options](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/variants.md#variants-options).
		- `CMAKE_BUILD_TYPE` is set based on [variant options](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/variants.md#variants-options).
		- `CMAKE_INSTALL_PREFIX` is set based on [cmake.installPrefix](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/cmake-settings.md#cmake-settings).
		- `CMAKE_TOOLCHAIN_FILE` is set for [toolchain](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/kits.md#specify-a-toolchain).
		- The [cmakeSettings](https://github.com/microsoft/vscode-cmake-tools/blob/main/docs/kits.md#generic-options) attribute on the active kit.
4. Configuration environment
	1. Sets environment variables for the child process it runs for CMake. 

# Usage
## CMake Presets
see [[VSCode CMake Presets]]