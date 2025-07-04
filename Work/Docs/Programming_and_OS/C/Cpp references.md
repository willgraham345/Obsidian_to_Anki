---
summary: References are an alias for an already existing variable. Implemented by storing the address of an object. Can be thought of as a constant pointer (not necessarily pointing to a constant value) with automatic indirection. The automatic indirection means the compiler will apply the * for you.
type: note/concept
associations:
  - "[[Cpp Pointers]]"
concept_of:
  - "[[Cpp Memory]]"
  - "[[Cpp Variables and Containers]]"
date created: Thursday, January 16th 2025, 4:34:38 pm
date modified: Thursday, June 19th 2025, 1:42:39 pm
keywords:
  - "[[Cpp &]]"
implements:
  - "[[Cpp Functions]]"
similar:
  - "[[Cpp pointers]]"
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
component_of:
  - "[[Cpp Memory]]"
workflows:
  - "[[Cpp function pointers and references]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
### How are they different from pointers?
- Cannot be reassigned.
- Typically cleaner, since the compiler will do the dereferencing for you
- You can use the dot operator with references, rather than the pointer m

## Usage
References are initialized when:
1. Naming an [[Cpp value categories]] declared with an initializer
2. When a named [[Cpp rvalue]] variable is declared with an initializer
3. In a function call expression, when the function parameter has reference type
4. In the return statement, when the function returns a reference type.

### LValue
**Correct**:
```cpp
int a = 10;
int &p = a; // Correct
```

**Incorrect**: 
```cpp
int &p;
p = a; // Incorrect, since we should declare AND initialize in the same step
```

### Parameter in Function (Pass by reference)

```cpp
void modifyStr(string &str) {  
  str += " World!";  
}  
  
int main() {  
  string greeting = "Hello";  
  modifyStr(greeting);  
  cout << greeting;  
  return 0;  
}
```

### Reference Return
It's okay to do this if the lifetime of the object won't end after the call.



A reference *T* can be initialized with an object of type *T*, a function of type *T*, or an object implicitly convertible to *T*. Once initialized, a reference cannot be changed to refer to another object.

# Additional Background
## Good answer I liked
### `*` and `&` as _type modifiers_

- `int i` declares an int.
- `int* p` declares a [pointer](http://en.wikipedia.org/wiki/Pointer_(computer_programming)#C_and_C.2B.2B) to an int.
- `int& r = i` declares a [reference](http://en.wikipedia.org/wiki/Reference_(C%2B%2B)) to an int, and initializes it to refer to `i`.  
    C++ only. Note that references must be assigned at initialization, therefore `int& r;` is not possible.

Similarly:

- `void foo(int i)` declares a function taking an int (by value, i.e. as a copy).
- `void foo(int* p)` declares a function taking a pointer to an int.
- `void foo(int& r)` declares a function taking an int by reference. (C++ only)

### `*` and `&` as _operators_

- `foo(i)` calls `foo(int)`. The parameter is passed as a copy.
- `foo(*p)` dereferences the int pointer `p` and calls `foo(int)` with the int pointed to by `p`.
- `foo(&i)` takes the address of the int `i` and calls `foo(int*)` with that address.