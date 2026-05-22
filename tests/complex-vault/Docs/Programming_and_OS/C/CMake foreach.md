---
type: note
---
# Background
Lets you execute a group of CMake commands repeatedly on the members of a list. 
[Docs](https://cmake.org/cmake/help/latest/command/foreach.html#command:foreach)


# Usage
## Syntax
```cmake
foreach(<loop_var> <items>)
  <commands>
endforeach()
```
- Scope of `<loop_var>` is restricted to the loop scope. 
- `<items>` are a list of items separated by semicolon or whitespace. 
## Examples
```cmake
foreach(tfile
        TestAnisotropicDiffusion2D
        TestButterworthLowPass
        TestButterworthHighPass
        TestCityBlockDistance
        TestConvolve
        )
  add_test(${tfile}-image ${VTK_EXECUTABLE}
    ${VTK_SOURCE_DIR}/Tests/rtImageTest.tcl
    ${VTK_SOURCE_DIR}/Tests/${tfile}.tcl
    -D ${VTK_DATA_ROOT}
    -V Baseline/Imaging/${tfile}.png
    -A ${VTK_SOURCE_DIR}/Wrapping/Tcl
    )
endforeach()
```
- This iteratively repeats the `add_test()` command