---
summary: User-defined datatype, which holds its own data members and member functions. Data members are the data variables and member functions are the functions used to manipulate these variables together, these data members and member functions define the properties and behavior of the objects in a Class.A C++ class is like a blueprint for an object. Constructors are called whenever the class is created [[Cpp.Class.Constructors]]
type: note/system
examples:
  - "[[Cpp Casting]]"
concepts:
  - "[[Cpp Access Modifiers]]"
  - "[[Cpp Class Inheritance]]"
  - "[[Cpp Class static members and methods]]"
  - "[[Cpp Class Virtual_Function_Members]]"
  - "[[Cpp const Member Functions]]"
  - "[[Cpp Scope and Namespace]]"
  - "[[Cpp templates]]"
  - "[[Cpp this]]"
functions:
  - "[[Cpp Class Constructors]]"
  - "[[Cpp override specifier]]"
concept_of:
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 10:49:15 am
associations:
  - "[[Cpp interfaces]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Background

# Usage
## Syntax
```cpp
class classname { 
	public: 
		classname(parms); // constructor 
		~classname(); // destructor 
		member1; member2;
	protected:
		member3;
		...
	private:
		member4; } objectname;
```
- `private` members of a class are accessible only from within other members of the same class (or from their _"friends"_).
- `protected` members are accessible from other members of the same class (or from their _"friends"_), but also from members of their derived classes.
- `public` members are accessible from anywhere where the object is visible.

## Example Class Usage
```cpp
class CSquare { // class declaration
	public:
		void Init(float h, float w);
		float GetArea(); // functions
	private: // available only to CSquare
		float h,w;
} // implementations of functions
void CSquare::Init(float hi, float wi){
	 h = hi; w = wi;
}
float CSquare::GetArea() {
	 return (h*w);
}
// example declaration and usage
CSquare theSquare;
theSquare.Init(8,5);
area = theSquare.GetArea();
// or using a pointer to the class
CSquare *theSquare;
theSquare->Init(8,5);
area = theSquare->GetArea();
```
- Scope operator used to define a class function outside of the class declaration

### Instantiation
```cpp
# C++ Class Instantiation Cheatsheet

## Creating a Class

```cpp
class MyClass {
public:
    // Member variables
    int myVariable;
    
    // Constructor
    MyClass() {
        // Constructor code
    }
    
    // Member functions
    void myFunction() {
        // Function code
    }
    
    // Destructor
    ~MyClass() {
        // Destructor code
    }
};

```

### Accessing Member Variables
```cpp
MyClass obj;
obj.myVariable = 10;
obj.myFunction();



```

### Accessing Member Pointers
```cpp
#include <iostream>

class MyClass {
private:
    int* ptr; // Pointer variable
    
public:t
    // Constructor to initialize pointer
    MyClass() {
        ptr = new int(0); // Dynamically allocate memory for the pointer
    }
    
    // Destructor to deallocate memory
    ~MyClass() {
        delete ptr; // Release memory allocated for the po
        My nuinter
    }
    
    // Pointer function to set value through pointer
    void setValue(int value) {
        *ptr = value;
    }
    
    // Pointer function to get value through pointer
    int getValue() {
        return *ptr;
    }
};

int main() {
    // Create an object of MyClass
    MyClass obj;
    
    // Access pointer variable directly
    int* pointer = obj.ptr;
    
    // Access pointer function to set value
    obj.setValue(42);
    
    // Access pointer function to get value
    int value = obj.getValue();
    
    // Print the value
    std::cout << "Value: " << value << std::endl;
    
    return 0;
}

```