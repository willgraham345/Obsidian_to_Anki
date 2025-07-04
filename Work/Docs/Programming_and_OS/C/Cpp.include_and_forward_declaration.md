---
type: note
---
# Background
- Directive to include different libraries, header files, and other declarations. 
- `#include` inserts a copy of the header file directly into the `.cpp` file prior to compilation

## Concepts
### Types of Files
#### Declaration file (`.h`, `.hpp`, `.hxx`)
- Where you say what you have, and include documentation 
- Included and not compiled
	- Standard header files (like `string.h`), let us access underlying functionality in a C library. 
	- If you have a module called `rational.c` for rational number calculations, every file that uses the implementation should include the `.h` file as its public interface. 
#### Source file (`.cpp`, `.cxx`, `.cc`)
- Where stuff is told what it is
- DO NOT include source files (done very rarely)
#### Include guard
- Statements that help you avoid redefining certain includes
### Two types of Dependencies
Imagine we have two classes:
```
class A
class B
```
- Class `A` uses class `B`, so `B` is a dependency on `A`
#### Forward Declared
Default to this to avoid circular dependencies.  (A and B both depend on each other, and neither can be referenced)
##### Examples
Forward declare `B` : 
- `A` contains a `B` pointer or reference 
  `B* myb`
- One or more functions has a `B` object/pointer/reference as a parameter or return type
  `B MyFunction(B myb)`
#### Including
##### Examples
- `B` is a parent class of `A`
- `A` contains `B` object:
  `B myb`
### Dealing with Inline Functions
- Inline functions need to exist in the header, but they do not need to exist in the class definition themself. 
- [Read this](https://cplusplus.com/articles/Gw6AC542/)
# Usage
## Best Practice
```cpp
#ifndef MYFILENAME_H
#define MYFILENAME_H
// put code here
#endif
```
- Means you cannot fall over on redefining the headers in your compilation (also known as an include guard)
### Pragma
```cpp
#pragma once
```
## Include a file
- Warning, make sure you are following best practice, and use forward declarations if possible. 
### Search System Include Path
```cpp
#include <stdio.h>
```
### Search User Include Path, Then The System Include Path
```cpp
#include "myfile.h"
```

## Forward declare dependencies
Within the header:
`myclass.h`
```cpp
class Foo;
class Bar
```
- Always default to this if possible. 
- 