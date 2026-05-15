---
type: note/concept
concept_of: ["[[Cpp Input Output]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 10:35:27 am
---
# Background
- How command line arguments are passed into `main()` with C and C++
```
int main();
```
- Doesn't take any arguments
```
int main(int argc, char* argv[]);
```
- Can run your program with anything attached.  

## What is `argc`?
- Argument count
- `argc` is the number of strings pointed to by `argv`. 
	- In practice, this is 1 plus the number of arguments as virtually all implementations will prepend the name of the program to the array. 

## What is `argv`?
- Argument vector

## What is `envp`?
- A parameter that contains environment variables.
	- Each entry follows the format:
```
VARIABLENAME=VariableValue
```

# Usage
- They can be omitted entirely, but also renamed into something like `int main(int num_args, char** arg_strings)`

## WARNING
DO not use any `argv` or `envp` values directly in calls to `system()` this is a big security hole that could set environment environment variables to command-line commands and cause big damage. In general, avoid `system()` as there's typically a better solution in C libraries. 

## Example Usage of Command Line Arguments
```cpp
#include <iostream>

int main(int argc, char** argv) {
    std::cout << "Have " << argc << " arguments:\n";
    for (int i = 0; i < argc; ++i) {
        std::cout << argv[i] << "\n";
    }
}
```

Using the following execution:
```shell
./ a1 b2 c3
```

```output
Have 4 arguments:
./test
a1
b2
c3
```
