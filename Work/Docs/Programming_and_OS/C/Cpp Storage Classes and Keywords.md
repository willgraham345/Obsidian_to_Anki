---
summary: Different keywords used to store variables.
type: note/concept
classes:
  - "[[Cpp Class static members and methods]]"
  - "[[Cpp Class static members and methods]]"
  - "[[Cpp const]]"
  - "[[Cpp mutable]]"
  - "[[Cpp.Storage Classes.register]]"
  - "[[Cpp.Storage.Classes.auto]]"
  - "[[Cpp.Storage.Classes.extern]]"
  - "[[Cpp.Storage.Classes.thread_local]]"
similar:
  - "[[Cpp Class Constructors]]"
  - "[[Cpp Class Inheritance]]"
concept_of:
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, February 7th 2025, 10:42:39 am
---
# Background
- Used to describe the characteristics of a variable/function.  

![[Cpp-Storage-Class.webp | 500]]

| File                                 | Keyword        | Lifetime         | Visbility       | Initial Value |
| ------------------------------------ | -------------- | ---------------- | --------------- | ------------- |
| [[Cpp.Storage.Classes.auto]]         | `auto`         | Function block   | Local           | Garbage       |
| [[Cpp.Storage.Classes.extern]]       | `extern`       | Whole program    | Global          | Zero          |
| [[Cpp.Storage.Classes.static]]       | `static`       | Whole program    | Local           | Zero          |
| [[Cpp.Storage Classes.register]]     | `register`     | Function Block   | Local           | Garbage       |
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