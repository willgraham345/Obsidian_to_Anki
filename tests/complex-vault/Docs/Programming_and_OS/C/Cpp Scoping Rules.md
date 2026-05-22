---
summary: "How C++ deals with naming conflicts. "
type: note/keyword
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
up: ["[[Cpp Basics]]"]
similar: ["[[Python Scoping Rules]]"]
associations: ["[[Cpp Lifetimes]]", "[[Cpp Variables Scope]]"]
concept_of: ["[[Cpp Class]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 29th 2026, 5:15:07 pm
items: ["[[Cpp Scope Operator]]", "[[Cpp this]]", "[[Cpp using]]"]
keyword_of: ["[[Cpp Design Patterns]]"]
tags: [lang/scope/namespace]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

󰙎  Anonymous namespace ;;; Trick you can do in a source file to define a function that's only used locally. A hacky way to get around creating an additional source file. 
- A namespace provides scope to identifiers like function names, variable names defined within it. 

The keyword `using` is all over this. You can use the `using` keyword

## Usage


### Namespace declaration in depth
[Stack overflow](https://stackoverflow.com/questions/25006127/difference-between-using-and-using-namespace)
`using namespace` makes all the names of the namespace visible, rather than just on a specific object of the namespace
```cpp
#include <iostream>

void print(){
using std::cout; 
using std::endl;
cout<<"test1"<<endl;
}
int main(){
 using namespace std;
cout<<"hello"<<endl;
print();
return 0;
}
```
- `using namespace std` all elements under `std` are made available
- `using std::cout` we explicitly mention what element under the std is required for the function. 
