---
summary: Specifies that a virtual function cannot be overridden in a derived class, or that a class cannot be derived from.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/keyword
similar: ["[[Cpp override specifier]]"]
date created: Tuesday, September 16th 2025, 5:10:46 pm
date modified: Tuesday, September 16th 2025, 5:15:00 pm
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
virt-specifier-seq? #questions/cpp
- What is this?

pure-specifier? #questions/cpp 
- What's this?

## Concepts of Note


## Examples
``` cpp
struct Base
{
    virtual void foo();
};
 
struct A : Base
{
    void foo() final; // Base::foo is overridden and A::foo is the final override
    void bar() final; // Error: bar cannot be final as it is non-virtual
};
 
struct B final : A // struct B is final
{
    void foo() override; // Error: foo cannot be overridden as it is final in A
};
 
struct C : B {}; // Error: B is final
```