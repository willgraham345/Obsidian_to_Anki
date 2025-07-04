---
summary: This keyword is used to mark constructors to not implicitly convert types in C++. It is optional for constructors that take exactly one argument and work on constructors (with a single argument) since those are the only constructors that can be used in typecasting. The compiler is allowed to make one implicit conversion to resolve the parameters to a function.
type: note/concept
associations:
  - "[[Cpp Functions]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, February 7th 2025, 10:45:08 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background


## Usage
### Example converting constructors
Suppose you have a class `String`
```cpp
class String {
public:
    String(int n); // allocate n bytes to the String object
    String(const char *p); // initializes object with char *p
};
```
If you try
```cpp
String mystring = 'x';
```
The character `x` will be implicitly converted to `int` and then the `String(int)` constructor will be called. That MIGHT not be what we intend. To prevent such conditions, we define the constructor as `explicit` as shown below:
```cpp
class String {
public:
    explicit String (int n); //allocate n bytes
    String(const char *p); // initialize sobject with string p
};
```