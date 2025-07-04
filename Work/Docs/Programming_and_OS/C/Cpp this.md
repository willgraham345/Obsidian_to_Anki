---
summary: Access operator, pointing to the memory location of the current object
headings:
  - "[[#Concepts of Note]]"
type: note/component
component_of:
  - "[[Cpp Member Access Operators]]"
  - "[[Cpp Scope and Namespace]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, April 15th 2025, 9:59:38 am
concept_of:
  - "[[Cpp Class]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- Each object gets its own copy of the data member
- All access the same function definition in the code segment
	- All data objects share the same single copy of member functions. 
- `this` pointer is passed as a hidden argument to all nonstatic member function calls and is available as a local variable within nonstatic functions.

# Usage
## Return reference to the calling object
```cpp
/* Reference to the calling object can be returned */
Test& Test::func () 
{ 
// Some processing 
return *this; 
} 

```

## When local variable's name is same as members name
```cpp
#include<iostream> 
using namespace std; 

/* local variable is same as a member's name */
class Test 
{ 
private: 
int x; 
public: 
void setX (int x) 
{ 
	// The 'this' pointer is used to retrieve the object's x 
	// hidden by the local variable 'x' 
	this->x = x; 
} 
void print() { cout << "x = " << x << endl; } 
}; 

int main() 
{ 
Test obj; 
int x = 20; 
obj.setX(x); 
obj.print(); 
return 0; 
} 

```

## Chain function calls on a single object
```cpp
#include<iostream> 
using namespace std; 

class Test 
{ 
private: 
int x; 
int y; 
public: 
Test(int x = 0, int y = 0) { this->x = x; this->y = y; } 
Test &setX(int a) { x = a; return *this; } 
Test &setY(int b) { y = b; return *this; } 
void print() { cout << "x = " << x << " y = " << y << endl; } 
}; 

int main() 
{ 
Test obj1(5, 5); 

// Chained function calls. All calls modify the same object 
// as the same object is returned by reference 
obj1.setX(10).setY(20); 

obj1.print(); 
return 0; 
} 

```