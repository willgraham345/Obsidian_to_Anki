---
type: note/concept
components: ["[[Cpp Variables Datatype Modifiers]]"]
concept_of: ["[[Cpp Variables and Containers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, February 7th 2025, 1:03:51 pm
---
- **Integer**: The keyword used for integer data types is **int**. Integers typically require 4 bytes of memory space and range from -2147483648 to 2147483647.  
- **Character**: Character data type is used for storing characters. The keyword used for the character data type is **char**. Characters typically require 1 byte of memory space and range from -128 to 127 or 0 to 255.  
- **Boolean**: Boolean data type is used for storing Boolean or logical values. A Boolean variable can store either __true__ or __false__. The keyword used for the Boolean data type is **bool**. 
- **Floating Point**: Floating Point data type is used for storing single-precision floating-point values or decimal values. The keyword used for the floating-point data type is **float**. Float variables typically require 4 bytes of memory space. 
- **Double Floating Point**: Double Floating Point data type is used for storing double-precision floating-point values or decimal values. The keyword used for the double floating-point data type is **double**. Double variables typically require 8 bytes of memory space. 
- **void**: Void means without any value. void data type represents a valueless entity. A void data type is used for those function which does not return a value. 
- **Wide Character**: [Wide character](https://www.geeksforgeeks.org/wide-char-and-library-functions-in-c/) data type is also a character data type but this data type has a size greater than the normal 8-bit data type. Represented by **wchar_t**. It is generally 2 or 4 bytes long.
- **sizeof() operator:** [sizeof() operator](https://www.geeksforgeeks.org/sizeof-operator-c) is used to find the number of bytes occupied by a variable/data type in computer memory.

## Examples with `sizeof()`
```cpp
// C++ Program to Demonstrate the correct size
// of various data types on your computer.
#include <iostream>
using namespace std;

int main()
{
	cout << "Size of char : " << sizeof(char) << endl;
	cout << "Size of int : " << sizeof(int) << endl;

	cout << "Size of long : " << sizeof(long) << endl;
	cout << "Size of float : " << sizeof(float) << endl;

	cout << "Size of double : " << sizeof(double) << endl;

	return 0;
}

```

```
Size of char : 1
Size of int : 4
Size of long : 8
Size of float : 4
Size of double : 8
```