---
type: note
---
# Background
- If a global variable is non-`const`, its linkage is `extern` by default
- `static` defines that this variable cannot be accessed outside of the file in which it has been initialized. It must be forwarded if it is in another file. 
- A global variable initialized with a legal value where it is declared in order to be used elsewhere
	- Can be accessed between two different files which are part of a large program.
- Tells us that the variable is defined elsewhere and not within the same block where it is used
- The value assigned to it in a different block, and can be overwritten/changed in a different block as well. 

# Usage
## Global Variables
```cpp
//main2.cpp
 //static global variable, cannot be in another file
 static int global_var3 = 23;                              
//Can be accessed outside this file
 extern double global_var4 = 71;
 int main() { return 0; }
```
```cpp
//main3.cpp
#include <iostream>

int main()
{
//This variable refers to the global_var4 defined in main2.cpp file
   extern int gloabl_var4; 
// Prints 71
  std::cout << global_var4 << "\n"; 
  return 0;
}
```
