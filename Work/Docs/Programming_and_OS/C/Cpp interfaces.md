---
summary: Describes the behavior/capabilities of a class without committing to a particular implementation of that class. C++ interfaces are implemented with abstract classes which have at least one *pure virtual* function.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
associations: ["[[Cpp Class]]"]
concept_of: ["[[Cpp Variables and Containers]]"]
date created: Thursday, May 1st 2025, 11:41:26 am
date modified: Thursday, June 26th 2025, 8:24:11 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- [I] Interface (abstract class) = Class which only contains declaration of pure virtual functions, which requires implemented classes to implement all methods. You can't create an instance of an interface. = #term/cpp/interface
- [I] Pure virtual function = A function that *must* be implemented in a class implementing it's interface class. `virtual void fn() = 0`
- [p] `virtual void fn()=0` = Implement a pure virtual function (class *must* implement this) = #code/cpp/interface/virtual
<!--ID: 1751434091640-->

- [p] `virtual void fn()` = Implement a virtual function, useful for defining default behavior while allowing classes to specialize it = #code/cpp/interface/virtual
<!--ID: 1751434091644-->


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