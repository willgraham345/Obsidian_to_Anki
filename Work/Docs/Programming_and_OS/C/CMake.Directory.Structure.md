---
type: note
---
# Background
Two main directories: `src/` and `bin/`
- `src/` is where source code for project is located
	- also where `CMakeLists` files are found
- `bin/`
	- Sometimes referred to as `build/`





## More complex example
The idea is to avoid patterns that cause conflicts, easily read, and keep complicating the build. 
Project name = `project`
Library name = `lib`
Executable application = `app`
```
- project
  - .gitignore
  - README.md
  - LICENSE.md
  - CMakeLists.txt
  - cmake/
    - FindSomeLib.cmake
    - something_else.cmake
  - include/
    - project
      - lib.hpp
  - src/
    - CMakeLists.txt
    - lib.cpp
  - apps/
    - CMakeLists.txt
    - app.cpp
  - tests/
    - CMakeLists.txt
    - testlib.cpp
  - docs/
    - CMakeLists.txt
  - extern/
    - googletest
  - scripts/
    - helper.py
```
### dotfiles
- `.gitignore` should have something like `/build*`, so you can build directories in the source directory. 
### apps/
- Where you might store executables
### cmake/
- `cmake/` holds CMake helper files (i.e. `Find<library>.cmake`)
- Use `add_subdirectory()` to add a subdirectory containing a `CMakeLists.txt`
### extern/
### include
### scripts/
### test/
- `tests/` can also be `test/`
- You may see a `python` folder for python bindings

### `CMakeLists.txt`
- The central configuration for the entire project. The entry point for CMake and where you define configuration for your project. 
# Usage
## [[CMake.Adding.CMake.Helper.Functions#Adding a cmake folder to your CMake path]]