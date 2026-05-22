---
summary: Friend classes can access private/protected members of other classes declared to be their friends. Friendship is not mutual. Friend functions can access private/protected members of a class in C++. Friend classes are either global, or a member function of another class.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/keyword
concept_of: ["[[Cpp Access Modifiers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, September 16th 2025, 1:08:54 pm
used_by: ["[[Cpp Class]]", "[[Cpp Variables and Containers]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Friend is placed only in the function declaration of the friend function and not in the function definition or call.

### Use cases:
- A `LinkedList` class may be allowed to access private members of a `Node`
- A friend class can access private and protected members of other classes in which it is declared as a friend


[More info here](https://www.geeksforgeeks.org/friend-class-function-cpp/)

## Examples
### Friend function %% fold %% 
```cpp
#include <iostream>
using namespace std;

class base {
private:
    int private_variable;

protected:
    int protected_variable;

public:
    base() {
        private_variable = 10;
        protected_variable = 99;
    }
    
    // Friend function declaration
    friend void friendFunction(base& obj);
};


// friend function definition
void friendFunction(base& obj) {
    cout << "Private Variable: " 
         << obj.private_variable << endl;
    cout << "Protected Variable: " 
         << obj.protected_variable;
}

int main() {
    base object1;
    friendFunction(object1);
    return 0;
}
```
