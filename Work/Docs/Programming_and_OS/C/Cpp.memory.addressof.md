---
summary: Returns the address of the object or function referenced by `ref`
headings: ["[[#Usage]]"]
type: note/function
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, June 19th 2025, 1:38:43 pm
function_of: ["[[Cpp std memory]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Usage

```
# std::addressof
template <class T> T* addressof (T& ref) noexcept;
```

```cpp
// addressof example
#include <iostream>
#include <memory>

struct unreferenceable {
  int x;
  unreferenceable* operator&() { return nullptr; }
};

void print (unreferenceable* m) {
  if (m) std::cout << m->x << '\n';
  else std::cout << "[null pointer]\n";
}

int main () {
  void(*pfn)(unreferenceable*) = std::addressof(print);

  unreferenceable val {10};
  unreferenceable* foo = &val;
  unreferenceable* bar = std::addressof(val);

  (*pfn)(foo);   // prints [null pointer]
  (*pfn)(bar);   // prints 10

  return 0;
}
```