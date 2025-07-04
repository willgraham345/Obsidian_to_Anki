---
summary: Collection of items stored in a *continuous* memory location. Used to store multiple values of similar data types. Represents many instances in one variable.<br><br> Closely related to pointers, as the array name is treated as a pointer that stores the memory address of the first element of the array.
headings: ["[[#Media]]", "[[#Usage]]"]
type: note/library
components: ["[[Cpp pointers]]"]
workflows: ["[[Cpp function array arguments]]"]
associations: ["[[Cpp pointers]]"]
concept_of: ["[[Cpp Variables and Containers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, July 3rd 2025, 5:02:39 pm
library_used_in: ["[[Cpp std]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Arrays and pointers are closely related to each other. The array name is treated as a pointer that stored the memory address of the first element of the array. 

## Usage
- [p] `type varName[arraySize] = {vals}` = Statically initialize a c-style array with values and size. = #code/cpp/variables/array 
- [p] `type varName[5] = {1, 2}` = Statically initialize a size 5 c-style array with 1 and 2 with the rest of the elements set to 0. = #code/cpp/variables/array 
- [p] `std::array<dataType, size> varName = {}` = Initialize a std array in cpp. = #code/cpp/variables/array 
- [p] `arrayName.fill(5)` = Fill an std::array in cpp with 5's. = #code/cpp/variables/array 
- [p] `std::array<int, 3> a2 = a1` = Copy initialize an array `a2` from already-initialized `a1`. = #code/cpp/variables/array 

### Access Array Elements 
#### For Loop
```cpp
// C++ Program to Illustrate How to Traverse an Array 
#include <iostream> 
using namespace std; 

int main() 
{ 

	// Initialize the array 
	int table_of_two[10] 
		= { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 }; 

	// Traverse the array using for loop 
	for (int i = 0; i < 10; i++) { 
		// Print the array elements using indexing 
		cout << table_of_two[i] << " "; 
	} 

	return 0; 
}

```

### Find Size of an Array
```cpp
data_type size = sizeof(Array_name) / sizeof(Array_name[index])
```

### Multidimensional Arrays
```cpp
Data_Type Array_Name[Size1][Size2]...[SizeN];
```
- Data_Type: Type of data to be stored in the array.
- Array_Name: Name of the array.
- Size1, Size2,…, SizeN: Size of each dimension.

#### 2D array
```cpp
data_type array_name[n][m];
```

#### 3D array
```cpp
data_type array_name[n][m][o]
```

### Arrays and Pointers
[[Cpp pointers]]

## Media
[Standard library header \<array\> (C++11) - cppreference.com](https://en.cppreference.com/w/cpp/header/array)