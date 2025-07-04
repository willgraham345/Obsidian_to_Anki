---
summary: An object/class that defines the operator() and "looks like" a function. Can be thought of as an alternative to an object, with the added advantage of having data. Can contain different data each time it is instantiated.
type: note/function
similar:
  - "[[Cpp Lambda Capture]]"
concept_of:
  - "[[Cpp Functions]]"
date created: Thursday, November 21st 2024, 2:49:51 pm
date modified: Thursday, February 6th 2025, 10:58:11 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
```cpp
// this is a functor
struct add_x {
  add_x(int val) : x(val) {}  // Constructor
  int operator()(int y) const { return x + y; }

private:
  int x;
};

// Now you can use it like this:
add_x add42(42); // create an instance of the functor class
int i = add42(8); // and "call" it
assert(i == 50); // and it added 42 to its argument

std::vector<int> in; // assume this contains a bunch of values)
std::vector<int> out(in.size());
// Pass a functor to std::transform, which calls the functor on every element 
// in the input sequence, and stores the result to the output sequence
std::transform(in.begin(), in.end(), out.begin(), add_x(1)); 
assert(out[i] == in[i] + 1); // for all i
```
