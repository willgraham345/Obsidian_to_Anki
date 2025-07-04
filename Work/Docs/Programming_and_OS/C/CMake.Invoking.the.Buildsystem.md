---
type: note
---
# Background
Software can be built by invoking particular build tool.
- With IDE generators, this can involve loading the generated project file into the IDE to invoke the build. 

# Usage


## Specifying a Build Program

|Generator|Default make program|Alternatives|
|---|---|---|
|XCode|`xcodebuild`||
|Unix Makefiles|`make`||
|NMake Makefiles|`nmake`|`jom`|
|NMake Makefiles JOM|`jom`|`nmake`|
|MinGW Makefiles|`mingw32-make`||
|MSYS Makefiles|`make`||
|Ninja|`ninja`||
|Visual Studio|`msbuild`||
|Watcom WMake|`wmake`|
## Software Installation 
[Software Installation](https://cmake.org/cmake/help/latest/guide/user-interaction/index.html#id20)

## Running Tests
[Running tests](https://cmake.org/cmake/help/latest/guide/user-interaction/index.html#id21)


## Other considerations
### If using a newer version of CMake
```shell
~/package $ cmake -S . -B build
~/package $ cmake --build build
```

#### Any of these commands will install
```shell
# From the build directory (pick one)
~/package/build $ make install
~/package/build $ cmake --build . --target install
~/package/build $ cmake --install . # CMake 3.15+ only
# From the source directory (pick one)
~/package $ make -C build install
~/package $ cmake --build build --target install
~/package $ cmake --install build # CMake 3.15+ only
```

### Picking a compiler
Selecting a compiler must be done on the first run in an empty directory. 
#### To pick Clang
```shell
~/package/build $ CC=clang CXX=clang++ cmake ..
```
- Sets environment variables in bash for `CC` and `CXX`. CMake will respect those variables. Sets it for one line, but that's the only time you'll need those. 

# If above commands didnt work, see [[CMake.Command.Line.Environment]]