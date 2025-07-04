---
summary: User-defined datatype, with members of different types and data similar to structures. Can allocate memory separately for each variable. Memory space can only be used one member variable at a time. Has better memory efficiency. Can hold member functions.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/concept
similar: 
component_of: ["[[Cpp Storage Classes and Keywords]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, July 3rd 2025, 2:14:26 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[C++ Unions - GeeksforGeeks](https://www.geeksforgeeks.org/cpp/cpp-unions/)

## Concepts of Note
- [p] `union union_Name {`<br>  `type1 member1;`<br>  `type2 member2;`  <br>`}` = How to declare a union in cpp, which points multiple = #code/cpp/memory/pointers #code/cpp/variables
- [p] `union union_Name {`<br>  `type1 member1;`<br>  `type2 member2;`  <br>`}var_name` = How to declare a union in cpp with an initialized member, which points multiple = #code/cpp/memory/pointers #code/cpp/variables
- [t] What in cpp lets us define a new datatype with multiple types of data in the same memory location? = Unions
- [t] Can unions have their own methods? How about virtual functions? = Yes, and no to virtual methods.
- [t] Can unions be used as base classes? = No
- [t] What is the size of a union in cpp? = The size of a union is equal to the size of the largest memory element.

## Examples
```cpp
// C++ program to illustrate the use of union in C++ 
#include <iostream> 
using namespace std; 

// Creating a union 
union geek { 
	// Defining data members 
	int age; 
	char grade; 
	float GPA; 
}; 

int main() 
{ 

	// Defining a union variable 
	union geek student1; 

	// Assigning values to data member of union geek and 
	// printing the values of data members 
	student1.age = 25; 
	cout << "Age : " << student1.age << endl; 

	student1.grade = 'B'; 
	cout << "Grade : " << student1.grade << endl; 

	student1.GPA = 4.5; 
	cout << "GPA : " << student1.GPA << endl; 

	return 0; 
}

```