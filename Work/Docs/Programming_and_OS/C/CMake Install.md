---
summary: Generates installation rules for a project. Installing puts the executable as a program within the computer, rather than an executable script.
source: ["[[CMake]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, November 13th 2024, 9:50:38 am
type: note/function
---
[Installing Files — Mastering CMake](https://cmake.org/cmake/help/book/mastering-cmake/chapter/Install.html#:~:text=CMake%20provides%20the%20install%20command,the%20actual%20installation%20of%20files.)
[install — CMake 3.31.0-rc2 Documentation](https://cmake.org/cmake/help/latest/command/install.html#command:install)

# Background
- As a developer, you don't see a lot of benefit from making install rules in your own projects, but users of your project will.
	- CMake installation works by generating a `cmake_install.cmake` script at configure/generate time. If you look inside of this, script, it executes [[CMake.file]] for all of your files. 
- Projects can install files other than those created with [[CMake.add_executable]] and [[CMake.add_library]].
	- See [[#General-purpose file installation]]
	- Projects can also install helper programs that are not compiled as targets. 
	- The install process is different than the build/source libraries. It can go wherever the user wants it to go. Specified by [[CMake.CMAKE_INSTALL_PREFIX]].

- You would use the install interface of project B if your project depends on B and you know that its going to be installed on windows/linux platforms. 

## Difference between executable, and installed executable
- Often, it isn't enough to only build an executable, but it should also be installable. 
	- A typical `.exe` (or Linux equivalent) will contain a program that is standalone. It will directly execute without need for installation. Great for portable applications.
	- Installed `.exe` applications, create necessary files, links, shortcuts, and potentially register entries. Might contain multiple files, libraries, config files, and more. 
		- When you run an installed `.exe` application, it launches the program through the main `.exe` file, but it may also access other files.

# Usage
## Common Use Cases 
### Binary files corresponding to targets
```cmake
install(TARGETS ...)
```

### General-purpose file installation
```cmake
install(FILES...)
```
- Typically used for headers, documentation, and data files required by software

### Executables not built by project
```cmake
install(PROGRAMS...)
```
- Shell scripts

### Entire directory tree
```cmake
install(DIRECTORY …)
```
- Great for icons/images

### CMake Script file
```cmake
install(SCRIPT …)
```
- Specifies a user-provided CMake script file to be executed during installation. This is typically used to define pre-install or post-install actions for other rules.

### CMake code during execution
```cmake
install(CODE …)
```
- Specifies user-provided CMake code to be executed during the installation. This is similar to `install (SCRIPT)` but the code is provided inline in the call as a string.

### Code to Import Targets
```cmake
install(EXPORT …)
```
- Generates and installs a CMake file containing code to import targets from the installation tree into another project.

## Signatures
- Meant to create install rules for files. Additional details can be specified using keyword arguments followed by corresponding values. 

### DESTINATION
- This argument specifies the location where the installation rule will place files, and must be followed by a directory path indicating the location. If the directory is specified as a full path, it will be evaluated at install time as an absolute path. If the directory is specified as a relative path, it will be evaluated at install time relative to the installation prefix. The prefix may be set by the user through the cache variable CMAKE_INSTALL_PREFIX. A platform-specific default is provided by CMake: `/usr/local` on UNIX, and `“<SystemDrive>/Program Files/<ProjectName>”` on Windows, where SystemDrive is along the lines of C: and ProjectName is the name given to the top-most project command.

### PERMISSIONS
- This argument specifies file permissions to be set on the installed files. This option is needed only to override the default permissions selected by a particular install command signature. Valid permissions are `OWNER_READ`, `OWNER_WRITE`, `OWNER_EXECUTE`, `GROUP_READ`, `GROUP_WRITE`, `GROUP_EXECUTE`, `WORLD_READ`, `WORLD_WRITE`, `WORLD_EXECUTE`, `SETUID`, and `SETGID`. Some platforms do not support all of these permissions; on such platforms those permission names are ignored.

### CONFIGURATIONS
- This argument specifies a list of build configurations for which an installation rule applies (Debug, Release, etc.). For Makefile generators, the build configuration is specified by the CMAKE_BUILD_TYPE cache variable. For Visual Studio and Xcode generators, the configuration is selected when the install target is built. An installation rule will be evaluated only if the current install configuration matches an entry in the list provided to this argument. Configuration name comparison is case-insensitive.

### COMPONENT
- This argument specifies the installation component for which the installation rule applies. Some projects divide their installations into multiple components for separate packaging. For example, a project may define a Runtime component that contains the files needed to run a tool; a Development component containing the files needed to build extensions to the tool; and a Documentation component containing the manual pages and other help files. The project may then package each component separately for distribution by installing only one component at a time. By default, all components are installed. Component-specific installation is an advanced feature intended for use by package maintainers. It requires manual invocation of the installation scripts with an argument defining the COMPONENT variable to name the desired component. Note that component names are not defined by CMake. Each project may define its own set of components.

### OPTIONAL
- This argument specifies that it is not an error if the input file to be installed does not exist. If the input file exists, it will be installed as requested. If it does not exist, it will be silently not installed.