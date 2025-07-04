---
type: note
---
# Background
See [[VSCode CMake Presets]]
Sharing settings in CMake is a mess. There are reasons to have settings configured (CI builds, other users) and other stuff.

## `CMakePresets.json` and `CMakeUserPresets.json`
- CMake makes use of two files in the projects root directory. 
- These files allow common configuration options to be shared with others, and supports files included with the `include` field. 
- Exactly the same format, and both are optional (if `--preset` is specified, you need at least one. )
- Do *not* track `CMakeUserPresets.json` in your git repo. 


# Usage
[See overview](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)