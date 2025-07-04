---
type: note
---
To compile an executable from one source file, CMakeLists file contains three lines
```cmake
cmake_minimum_required(VERSION 3.20)
project(Hello)
add_executable(Hello Hello.c)
```
- 1st line should always be `cmake_minimum_required`