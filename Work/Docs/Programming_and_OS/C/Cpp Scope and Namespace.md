---
type: note/concept
up:
  - "[[Cpp Basics]]"
components:
  - "[[Cpp Scope Operator]]"
  - "[[Cpp this]]"
  - "[[Cpp using]]"
associations:
  - "[[Cpp Variables Scope]]"
  - "[[Cpp Lifetimes]]"
concept_of:
  - "[[Cpp Class]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 16th 2025, 12:15:26 pm
---
# Background
- A namespace provides scope to identifiers like function names, variable names defined within it. 
- Not present in C++

# Concept
The keyword `using` is all over this. You can use the `using` keyword

# Usage
## Namespace declaration in depth
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