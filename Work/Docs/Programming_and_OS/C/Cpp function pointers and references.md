---
summary: How to implement cpp pointers and references within functions
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/workflow
date created: Thursday, June 19th 2025, 1:48:57 pm
date modified: Thursday, June 19th 2025, 2:25:59 pm
workflow_of: ["[[Cpp Functions]]", "[[Cpp pointers]]", "[[Cpp references]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
Functions use pass by reference, pointers, and pass by value. 
- Note: There is *no* pass by address

| Code                        | Method                     | Description                                                                       |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------------- |
| `function(int var);`        | Pass by value              | Variable passed into function and can be changed, but changes are not passed back |
| `function(const int var);`  | Pass by constant value     | Variable passed into function but cannot be changed                               |
| `function(int &var);`       | Pass by reference          | Variable is passed into function and can be changed, changes passed back          |
| `function(const int &var);` | Pass by constant reference | Variable cannot be changed in function                                            |

## Usage
- [p] `int* swap(int*, int)` = Declares a function with an int pointer variable that returns an an int pointer. = #code/cpp/functions #code/cpp/variables/const/pointers 
<!--ID: 1751434091661-->

- [p] `char* call(char b)` = Declares a function with a char param, and returns a pointer to a char variable = #code/cpp/functions #code/cpp/variables/const/pointers 
<!--ID: 1751434091665-->

- [p] `int add(int a, int b=2) {}` = Declares a function with default parameter values = #code/cpp/functions 
<!--ID: 1751434091669-->
