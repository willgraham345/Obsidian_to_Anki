---
type: note
---
# Examples
## Adding a library with our own implementation of computing the square root of a number
- We will put the library into a subdirectory called `MathFunctions`
	- Has header files `MathFunctions.h` and `mysqrt.h`
		- `MathFunctions.cxx` and `mysqrt.cxx`

#### ~/MathFunctions/CMakeLists.txt
```CMakeLists.txt
# Add library called MathFunctions with two source files
add_library(MathFunctions MathFunctions.cxx mysqrt.cxx)
```
#### ~/CMakeLists.txt
```CMakeLists
add_subdirectory(MathFunctions)

target_link_libraries(Tutorial PUBLIC MathFunctions) # Links executable to library
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           "${PROJECT_SOURCE_DIR}/MathFunctions"
						   )
```

#### Execution Script
```shell
mkdir Step2_build
cd Step2_build
cmake ../Step2
cmake --build .
```

## Adding an Option
Option will be seen with the GUI and `ccmake` with a default value of `ON`

```cpp
# TODO 7: MathFunctions/CMakeLists.txt
option(USE_MYMATH "Use tutorial provided math implementation" ON)


# TODO 8: MathFunctions/CMakeLists.txt

if (USE_MYMATH)
  target_compile_definitions(MathFunctions PRIVATE "USE_MYMATH")
endif()

TODO 9: MathFunctions/MathFunctions.cxx

#ifdef USE_MYMATH
  return detail::mysqrt(x);
#else
  return std::sqrt(x);
#endif

TODO 10: MathFunctions/MathFunctions.cxx

#ifdef USE_MYMATH
#  include "mysqrt.h"
#endif

TODO 11 : MathFunctions/MathFunctions.cxx

#include <cmath>


TODO 12 : MathFunctions/CMakeLists.txt

  add_library(SqrtLibrary STATIC
              mysqrt.cxx
              )

  # TODO 6: Link SqrtLibrary to tutorial_compiler_flags

  target_link_libraries(MathFunctions PRIVATE SqrtLibrary)
endif()

TODO 13 : MathFunctions/CMakeLists.txt

  target_link_libraries(MathFunctions PRIVATE SqrtLibrary)

TODO 14 : MathFunctions/CMakeLists.txt

add_library(MathFunctions MathFunctions.cxx)
```
