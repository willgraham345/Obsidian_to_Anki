---
type: note
---
## Include Statements
Include statements occur in the following order:
1. C system headers
2. C++ standard library headers
3. User-defined libraries headers

## Naming Conventions
### Class Names Function Names
User-defined class names and function names use pascal case, which starts with a capital letter (camelcase)
- `LinkedList`
- `BubbleSort()`
### Variable Names
Variable names are all lowercase, with underscores between words
- `student_id`
- `result`


## Punctuation Marks
### Brackets
Open bracket is on the same line as the statement. The closing bracket should be placed under the last line of code in the scope

### Parentheses
There should be no space between the parentheses and the code inside. When used in a statement, there should be a space before, and after.

### Commas
There should always be a blank space after each comma



## Formatting
### Spacing
Types, variables, operators, and literal values should be separated by one space horizontally
```cpp
string message = "Hello World!";
```
Classes, functions, global variable declarations, and preprocessor directives should be separated by one space vertically
```cpp
#include <iostream> // preprocessor directive  
  
float pi = 3.1415;  // global variable  
  
class MyClass {     // class  
  public:  
    myClass() {  
  }  
};  
  
int main() {        // function  
  return 0;  
}
```

## Line Length
Each line of text should be at most 80 characters long. You do not need to follow this as strictly as the others