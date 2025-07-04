---
type: note/function
summary: Allocates memory on the free store (usually the heap). If sufficient memory is available it will return the newly allocated + initialized memory to the pointer variable. Increases dynamic runtime until it's companion function `delete` is called.
associations:
  - "[[Cpp delete]]"
function_of:
  - "[[Cpp Runtime Allocation]]"
---
# Background
## New operator
`new` allocates memory for the object on the free store (frequently the same thing as the heap)
- If sufficient memory is available, `new` operator initializes the memory and returns the address of newly allocated and initialized memory to the pointer variable. 
`new` memory will increase until you `delete` it
- You could `return` an object that you created using `new`

When you create an object of class using `new`
- The memory for the object is allocated using `new` from heap
- The constructor of the class is invoked to properly initialize this memory.

## Operator new
Operator new is a function of a class

# Usage
## New Operator
```cpp
// CPP program to illustrate 
// use of new keyword 
#include<iostream> 
using namespace std; 
class car 
{ 
	string name; 
	int num; 

	public: 
		car(string a, int n) 
		{ 
			cout << "Constructor called" << endl; 
			this ->name = a; 
			this ->num = n; 
		} 

		void enter() 
		{ 
			cin>>name; 
			cin>>num; 
		} 

		void display() 
		{ 
			cout << "Name: " << name << endl; 
			cout << "Num: " << num << endl; 
		} 
}; 

int main() 
{ 
	// Using new keyword 
	car *p = new car("Honda", 2017); 
	p->display(); 
} 

```

## Operator New
```cpp
// CPP program to illustrate 
// use of operator new 
#include<iostream> 
#include<stdlib.h> 

using namespace std; 

class car 
{ 
	string name; 
	int num; 

	public: 

		car(string a, int n) 
		{ 
			cout << "Constructor called" << endl; 
			this->name = a; 
			this->num = n; 
		} 

		void display() 
		{ 
			cout << "Name: " << name << endl; 
			cout << "Num: " << num << endl; 
		} 

		void *operator new(size_t size) 
		{ 
			cout << "new operator overloaded" << endl; 
			void *p = malloc(size); 
			return p; 
		} 

		void operator delete(void *ptr) 
		{ 
			cout << "delete operator overloaded" << endl; 
			free(ptr); 
		} 
}; 

int main() 
{ 
	car *p = new car("HYUNDAI", 2012); 
	p->display(); 
	delete p; 
} 
 ```