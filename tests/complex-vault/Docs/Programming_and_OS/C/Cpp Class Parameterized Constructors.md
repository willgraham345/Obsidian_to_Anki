---
summary: 
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
next:
  - "[[Cpp Class Initialization List Constructors]]"
date created: Tuesday, June 10th 2025, 12:18:32 pm
date modified: Tuesday, February 24th 2026, 5:09:57 pm
item_of:
  - "[[Cpp Class Constructors]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary

# Summary
󰙎 Cpp Class Parameterized Constructors ;; Use one or more parameters to initialize an object with specific values. This is also used to instantiate a base as the first object, ensuring it is initialized properly.

# Additional Background
[Constructors and member initializer lists - cppreference.com](https://en.cppreference.com/w/cpp/language/constructor)

## Concepts of Note
󰙎 Constructor initialization list ;; A procedure used to initialize member variables directly.

## Syntax

```cpp
className (parameters...) {
      // body
}
 // Rewritten as...

MyClass::MyClass(int val) : memberVar(val) {};

// or

MyClass::MyClass(int val)
	: memberVar1(),
	memberVar2,
	...
	lastVar()
	
```

### Base and Derived Class
```cpp
class Base {
public:
    int id;
    Base(int id_val) : id(id_val) { /* ... */ } // Parameterized constructor
    // If you define another constructor, the default Base() is not automatically generated
};

class Derived : public Base {
public:
    double cost;
    // Explicitly call the Base parameterized constructor
    Derived(int id_val, double cost_val) : Base(id_val), cost(cost_val) { 
        // Derived class construction code runs after Base is fully constructed
    }
};

```

## Usage