---
summary: Function template that generates a forwarding call wrapper for `f`. This lets you create function objects that are different in order and/or argument than the original definition.<br><br>Calling this wrapper is equivalent to invoking `f` with some of its arguments bound to `args`.<br><br>Alternatives include lambda functions.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/function
similar: ["[[Cpp Lambda Capture]]"]
date created: Tuesday, June 24th 2025, 3:39:22 pm
date modified: Tuesday, June 24th 2025, 4:10:59 pm
uses: ["[[Cpp std placeholders]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

- [p] `std::bind(function, object/value, args...)` = Binds a function/value to a specific object/value. Creates a new function object by allowing it to be called with a different number of arguments or with a different order of arguments.

## Examples

```cpp
#include <iostream>
#include <functional>

int add(int a, int b) {
    return a + b;
}

int main() {
    // Using std::bind to create a new function that always adds 5
    auto add_five = std::bind(add, std::placeholders::_1, 5);
    std::cout << "3 + 5 = " << add_five(3) << '\n'; // Output: 3 + 5 = 8

    return 0;
}
```