---
summary: One of the ways to define a string, with the other being a C string. This style has dynamic memory, member functions which are better than C strings.
type: note/concept
down:
  - "[[Cpp strcpy]]"
  - "[[Cpp.string.substring]]"
  - "[[Cpp.string.tokenizing]]"
  - "[[Cpp.string.user.input]]"
functions:
  - "[[Cpp string methods]]"
  - "[[Cpp to_string]]"
component_of:
  - "[[Cpp std]]"
  - "[[Cpp string]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 2nd 2025, 11:31:09 am
library_used_in:
  - "[[Cpp std]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
Sequences of characters, stored in a char array

Can be defined in a variety of ways

# Usage
## std::string Class
Defined inside `<string>.h`
- Dynamic size, member functions
```cpp
std::string str("StringValues")
```

## C Style
These strings are stored as the plain old array of characters terminated by a null character `\0`. They are the type of strings that C++ inherited from C language.
```cpp
char str[] = "stringStuff";
```

## Pointers
- Array of string literals is created by an array of pointers in which each pointer points to a particular string
- The `4` can be omitted. The compiler will be able to calculate the correct block of memory. 
- We must specify `const` here to prevent unwanted accesses that may crash the program. d

### 
```cpp
// C++ program to demonstrate 
// array of strings using
// pointers character array
#include <iostream>

// Driver code
int main()
{
// Initialize array of pointer
const char* colour[4]
	= { "Blue", "Red", "Orange", "Yellow" };

// Printing Strings stored in 2D array
for (int i = 0; i < 4; i++)
	std::cout << colour[i] << "\n";

return 0;
}

```

## 2D Array
- Simplest form of multidimensional array
- Useful when the length of all strings is known and a particular memory footprint is desired
```cpp
// C++ program to demonstrate 
// array of strings using
// 2D character array
#include <iostream>

// Driver code
int main()
{
// Initialize 2D array
char colour[4][10]
	= { "Blue", "Red", "Orange", "Yellow" };

// Printing Strings stored in 2D array
for (int i = 0; i < 4; i++)
	std::cout << colour[i] << "\n";

return 0;
}

```

## Vector Class
- Dynamic array that doubles its size whenever a new character is added that exceeds the limit.
- 
```cpp
// C++ program to demonstrate 
// array of strings using 
// vector class
#include <iostream>
#include <string>
#include <vector>

// Driver code
int main()
{
// Declaring Vector of String type
// Values can be added here using 
// initializer-list
// syntax
std::vector<std::string> colour{"Blue", "Red",
								"Orange"};

// Strings can be added at any time 
// with push_back
colour.push_back("Yellow");

// Print Strings stored in Vector
for (int i = 0; i < colour.size(); i++)
	std::cout << colour[i] << "\n";
}

```

## Array Class
```cpp
// C++ program to demonstrate 
// array of string using STL array
#include <array>
#include <iostream>
#include <string>

// Driver code
int main()
{
// Initialize array
std::array<std::string, 4> colour{"Blue", "Red",
									"Orange", "Yellow"};

// Printing Strings stored in array
for (int i = 0; i < 4; i++)
	std::cout << colour[i] << "\n";

return 0;
}
```