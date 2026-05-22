---
summary: Different keywords used to store variables.
type: note/concept
similar:
  - "[[Cpp Class Inheritance]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, September 2nd 2025, 11:02:55 am
implementations:
  - "[[Cpp Class static members and methods]]"
items:
  - "[[Cpp union]]"
keywords:
  - "[[Cpp const]]"
  - "[[Cpp mutable]]"
  - "[[Cpp register]]"
  - "[[Cpp union]]"
  - "[[Cpp auto]]"
  - "[[Cpp extern]]"
  - "[[Cpp.Storage.Classes.thread_local]]"
used_by:
  - "[[Cpp Variables and Containers]]"
---

# Background
- Used to describe the characteristics of a variable/function.  

![[Cpp-Storage-Class.webp | 500]]

| File                                 | Keyword        | Lifetime         | Visbility       | Initial Value |
| ------------------------------------ | -------------- | ---------------- | --------------- | ------------- |
| [[Cpp auto]]         | `auto`         | Function block   | Local           | Garbage       |
| [[Cpp extern]]       | `extern`       | Whole program    | Global          | Zero          |
| [[Cpp static]]       | `static`       | Whole program    | Local           | Zero          |
| [[Cpp register]]     | `register`     | Function Block   | Local           | Garbage       |
| [[Cpp mutable]]      | `mutable`      | Class            | Local           | Garbage       |
| [[Cpp.Storage.Classes.thread_local]] | `thread_local` | Whole thread<br> | Local or Global | Garbage       |

```cpp
storage_class var_data_type var_name;
```

```cpp
// defining uninitialized vairbles
int globalVar1; //  uninitialized global variable with external linkage 
static int globalVar2; // uninitialized global variable with internal linkage
const int globalVar3; // error, since const variables must be initialized upon declaration
const int globalVar4 = 23; //correct, but with static linkage (cannot be accessed outside the file where it has been declared*/
extern const double globalVar5 = 1.57; //this const variable ca be accessed outside the file where it has been declared
```