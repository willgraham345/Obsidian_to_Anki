---
summary: Determines which variables and functions can be modified by what. `public` Members are accessible from outside the class. `private` Members are only accessible from within the class. `protected` Similar to private, but accessible in derived classes (a.k.a. subclasses).
type: note/concept
source:
  - "[[Cpp Class]]"
concepts:
  - "[[Cpp.Friend.Class]]"
  - "[[Cpp protected]]"
  - "[[Cpp private]]"
  - "[[Cpp public]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 22nd 2024, 3:51:59 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
```cpp
class MyClass {
public:
    int publicVariable;
    
private:
    int privateVariable;
    
protected:
    int protectedVariable;
};

```