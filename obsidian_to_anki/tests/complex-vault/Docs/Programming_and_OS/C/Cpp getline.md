---
summary: 
type: note/function
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## `getline()`
- `std::getline()`
- Reads a line of input from a stream.
	- Typically read with `cin`
- Takes a pointer to the string, and a reference to an integer (length of the line input)
- Reads until it encounters a newline character `'\n'`
```cpp
#include <iostream>
#include <string>
int main() {
    std::string input;
    std::cout << "Enter a line of text: ";
    std::getline(std::cin, input);
    std::cout << "You entered: " << input << std::endl;
    return 0;
}
```
```cpp
getline(cin, mystr)
```
