---
type: note
---
# Background
[[CMake]] automates the configuration of build systems. 

You can use CMake from [[Qt.Creator]].

# Usage
## Build a GUI executable (Qt 5.15)
```cmake
cmake_minimum_required(VERSION 3.1.0)

project(helloworld VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

if(CMAKE_VERSION VERSION_LESS "3.7.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()

find_package(Qt5 COMPONENTS Widgets REQUIRED)

add_executable(helloworld
    mainwindow.ui
    mainwindow.cpp
    main.cpp
    resources.qrc
)

target_link_libraries(helloworld Qt5::Widgets)
```
For `find_package` to be successful, CMake must find the Qt installation in one of two ways
1. (recommended) Set `CMAKE_PREFIX_PATH` environment variable to wherever Qt 5 lives 
2. Set `Qt5_DIR` in the CMake cache to the location of the `Qt5Config.cmake` file