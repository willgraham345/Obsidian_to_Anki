---
summary: Keyword that declares it is possible to evaluate the value of a variable/function at compile time. Can lead to improvements by avoiding runtime calculations.
type: note/concept
headings:
  - "[[#Examples]]"
date created: Monday, March 17th 2025, 10:18:49 am
date modified: Monday, March 17th 2025, 10:20:00 am
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