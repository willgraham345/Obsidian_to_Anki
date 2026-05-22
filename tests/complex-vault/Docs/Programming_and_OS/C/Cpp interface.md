---
summary: Cpp has no concept of interfaces, and these are instead accomplished through abstract classes (classes which contain virtual functions).
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
up:
  - "[[Cpp]]"
implements:
  - "[[Abstract Factory]]"
similar:
  - "[[Python Protocols]]"
  - "[[Rust trait]]"
  - "[[Rust traitocols]]"
aliases: [Cpp abstract classes]
concept_of:
  - "[[Cpp Class]]"
  - "[[Cpp Design Patterns]]"
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, March 3rd 2026, 1:49:31 pm
tags: [lang/oop/interface_trait, lang/oop/interface_trait/virtual]
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Abstract Factory]]"
  - "[[Cpp Variables and Containers]]"
uses:
  - "[[Cpp Class Inheritance]]"
  - "[[Cpp Class virtual functions]]"
  - "[[Cpp virtual]]"
  - "[[Cpp.Class.Overloading_Operators]]"
---

# Summary
󰙎 Cpp interface ;;; Cpp doesn't have "interfaces", and are instead accomplished with abstract classes. Each abstract class describes behavior/capabilities of a class without committing to an implementation. Each abstract class has at least one pure virtual function.

# Additional Background
## Concepts of Note
󰙎  Interface (abstract class) ;;; Class which only contains declaration of pure virtual functions, which requires implemented classes to implement all methods. You can't create an instance of an interface.

󰙎  Pure virtual function ;;; A function that *must* be implemented in a class implementing it's interface class. 

## Usage
  `virtual void fn()` ;;; Implement a pure virtual function within a template (class *must* implement this).

  `virtual void fn()` ;;; Implement a virtual function, useful for defining default behavior while allowing classes to specialize it. 

## Examples
```cpp
#include <bits/stdc++.h>
using namespace std;

// Interface equivalent pure abstract class
class I {
  public:
    virtual string getName() = 0;
};

// Class B which inherits I
class B : public I {
  public:
    string getName() {
        return "GFG";
    }
};

// Class C which inherits I
class C : public I {
  public:
    string getName() {
        return "GeeksforGeeks";
    }
};i

int main() {
    B obj1;
    C obj2;
    I *ptr;

    // Assigning the address of obj1 to ptr
    ptr = &obj1;
    cout << ptr->getName() << endl;

    // Assigning the address of obj2 to ptr
    ptr = &obj2;
    cout << ptr->getName();
  
    return 0;
}i
```


```cpp
class Interface
{
public:
	Interface(){}
	virtual ~Interface(){}
	virtual void method1() = 0; //"=0" makes this method pure virtual, and
	virtual void method2() = 0; // also makes this class abstract
};
class Concrete : public Interface
{
private:
	int myMember;
public:
	Concrete(){}
	~Concrete(){}
	void method1();
	void method2();
}
void Concrete::method1()
{
	// stuff goes here
}
void Concrete::method2()
{
	//other stuff here
}
int main(void)
{
	Interface *f = new Concrete();
	f->method1();
	f->method2();
	delete f;
	return 0;
}
```
