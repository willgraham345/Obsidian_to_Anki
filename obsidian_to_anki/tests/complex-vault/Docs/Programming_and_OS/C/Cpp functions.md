---
summary: Set of statements that takes input, does something, and produces output. Has various rules regarding parameter passing and variable usage.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
examples:
  - "[[Cpp Function Examples]]"
concepts:
  - "[[Cpp const member functions]]"
  - "[[Cpp functors]]"
  - "[[Cpp Lambda Capture]]"
  - "[[Cpp Variadic Functions]]"
similar:
  - "[[Python Functions]]"
associations:
  - "[[Cpp explicit]]"
  - "[[Cpp std optional (class)]]"
  - "[[Cpp templates]]"
concept_of:
  - "[[Cpp]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 1:11:56 pm
implementations:
  - "[[Cpp pointers]]"
  - "[[Cpp references]]"
processes:
  - "[[Cpp function array arguments]]"
tags: [lang/data/const/pointers, lang/functions]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- You can have functions which take another function as an argument (i.e. [[DP Functional Programming]])
󰙎  Function prototype ;;; Declaration of function's name, return type, and params without the function body (blueprint for compiler before definition) 
󰙎  Function implementation ;;; Definition of a function and what it does

### Pointers and References in Functions
Functions use pass by reference, pointers, and pass by value. 
- Note: There is *no* pass by address

| Code                        | Method                     | Description                                                                       |
| --------------------------- | -------------------------- | --------------------------------------------------------------------------------- |
| `function(int var);`        | Pass by value              | Variable passed into function and can be changed, but changes are not passed back |
| `function(const int var);`  | Pass by constant value     | Variable passed into function but cannot be changed                               |
| `function(int &var);`       | Pass by reference          | Variable is passed into function and can be changed, changes passed back          |
| `function(const int &var);` | Pass by constant reference | Variable cannot be changed in function                                            |

### Const Member Functions
[Const member functions in C++ - GeeksforGeeks](https://www.geeksforgeeks.org/const-member-functions-c/)
󰙎 Const member functions ;;; Functions which are guaranteed not to change `this` when called. This type of member is great for "getter" functions, and is the opposite of a "setter". They cannot call non-const functions.
Example: [[#^41bc73]] for usage

### Const return
When the return value can't be modified

## Usage

 `int* swap(int* i)` ;;; Declares a function `swap` with an int pointer called `i` variable that returns an an int pointer.

 `char* call(char b)` ;;; Declares a function `call` with a char param `b`, and returns a pointer to a char variable

 `int add(int a, int b=2) {}` ;;; Declares a function `add` with default parameter values for `a`to be 0, and `b` to be 2. `add` should also return an integer.

 `int getTacos() const` ;;; Declares a function `getTacos()` (no args) which is guaranteed to not change `this`. `getTacos` should return an `int`. ^41bc73

## Syntax
```cpp
//declaration
return_type functionName(param_type paramName);

//definition
functionName(param_type paramName);
{
	//Implementation
}
```

See [[Cpp function pointers and references]] for more examples/usage cases
