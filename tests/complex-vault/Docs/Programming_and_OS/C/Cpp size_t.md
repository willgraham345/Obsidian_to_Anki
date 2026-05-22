---
summary: An int we use for sizing things, so we don't have integer overflow when using cpp code.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/keyword
similar: ["[[Rust usize]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, October 31st 2025, 12:36:41 pm
keyword:
template: "[[base_note_template]]"
template-version: 1.0.0
used_by: ["[[Cpp std array]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


An unsigned integer that is *guaranteed* to be large enough to store the size of any object on the system

| Characteristic | size_t                                                                      | unsigned int                                                                    |     |
| -------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --- |
| Size           | Guaranteed to be large enough to store the size of any object on the system | Not guaranteed to be large enough to store the size of any object on the system |     |
| Type           | Unsigned integer                                                            | Unsigned integer                                                                |     |
| Use cases      | Used when working with object sizes                                         | Used for general-purpose integer operations                                     |     |

## Usage


### Basics
```cpp
// Declaring a variable of type size_t
size_t my_size = sizeof
(my_object);
// Declaring a variable of type unsigned int
unsigned int my_count = 10;
// Using size_t to store the size of an object
size_t object_size = sizeof(my_object);
// Using unsigned int for a general-purpose integer operation
unsigned int sum = my_count + 1;
```

### Iterating over a string
```cpp
#include <iostream>
#include <string>

int main() {
    // Define a string array
    std::string strings[] = {"Hello", "World", "This", "Is", "An", "Example"};

    // Get the size of the array
    size_t arraySize = sizeof(strings) / sizeof(strings[0]);

    // Iterate over the array using size_t
    for (size_t i = 0; i < arraySize; ++i) {
        std::cout << "String at index " << i << ": " << strings[i] << std::endl;
    }

    return 0;
}

```