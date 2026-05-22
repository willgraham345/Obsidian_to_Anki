---
summary: Keyword that declares it is possible to evaluate the value of a variable/function at compile time. Can lead to improvements by avoiding runtime calculations.
headings: ["[[#Examples]]"]
type: note/item
similar: ["[[Cpp const]]"]
date created: Monday, March 17th 2025, 10:18:49 am
date modified: Tuesday, September 2nd 2025, 11:08:36 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Examples
```cpp
// C++ program to demonstrate constexpr function for product
// of two numbers. By specifying constexpr, we suggest
// compiler to evaluate value at compile time
#include <iostream>

constexpr int product(int x, int y) { return (x * y); }

int main()
{
    constexpr int x = product(10, 20);
    std::cout << x;
    return 0;
}

```