---
summary: Collection of items stored in a *continuous* memory location. Used to store multiple values of similar data types. Represents many instances in one variable.<br><br> Closely related to pointers, as the array name is treated as a pointer that stores the memory address of the first element of the array.
headings:
  - "[[#Media]]"
  - "[[#Usage]]"
type: note/library
processes:
  - "[[Cpp function array arguments]]"
associations:
  - "[[Cpp pointers]]"
concept_of:
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, October 31st 2025, 12:31:05 pm
items:
  - "[[Cpp pointers]]"
library_of:
  - "[[Cpp std]]"
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Arrays and pointers are closely related to each other. The array name is treated as a pointer that stored the memory address of the first element of the array. 

## Concepts of Note
󰙎  C-style array ;;; A ”naked” array, which is not wrapped in a class like `std::array`. It is in a contiguous location, and is primarily worked with the use of pointers. = #lang/data/array  
<!--ID: 1758253289792-->

󰙎  Cpp array ;;; An array which uses another class (I.e. `std::array`, `std::vector`) = #lang/data/array 
<!--ID: 1758253289799-->

## Usage
  `type varName[arraySize] ``=`` {vals}` ;;; Statically initialize a c-style array with values and size. = #lang/data/array  
<!--ID: 1751998538001-->


  `type a[]` ;;; Declare a c-style array `a` with undeclared size. = #lang/data/array  
<!--ID: 1758253289782-->

  `type varName[5] ``=`` {1, 2}` ;;; Statically initialize a size 5 c-style array with 1 and 2 with the rest of the elements set to 0. = #lang/data/array  
<!--ID: 1751998538007-->



  `std::array<dataType, size> varName ``=`` {}` ;;; Initialize a std array in cpp. = #lang/data/array  
<!--ID: 1751998538012-->



  `arrayName.fill(5)` ;;; Fill an std::array in cpp with 5's. = #lang/data/array  
<!--ID: 1751998538016-->



  `std::array<int, 3> a2 ``=`` a1` ;;; Copy initialize a standard library array `a2` from already-initialized `a1`. = #lang/data/array  
<!--ID: 1751998538021-->



- [p] `std::array<int, 3> a ``=`` {1, 2, 3}`
      `int* c_style_ptr = a.data()` = Get pointer from `std::array` to the underlying c-style array. = #lang/data/array 


  `std::array<std::array<int, 4>, 3> a` ;;; Set a multi-dimensional standard library int array that has 3 arrays of 4 ints using the standard library. = #lang/data/array  


  `std::tuple_size<a> a` ;;; Obtains the number of elements in an array `a` in c++ = #lang/data/array
  `std::tuple_element<a>` ;;; Gets compile-time indexed access to the type of the elements in an array using a tuple-like interface. = #lang/data/array 

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
