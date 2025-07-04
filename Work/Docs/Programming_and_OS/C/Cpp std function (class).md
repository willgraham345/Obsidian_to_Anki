---
summary: A general-purpose polymorphic function wrapper. Instances can store, copy, and invoke any target. The target is the stored callable object of the std::function. If a std::function contains no target, it is considered empty.
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Syntax]]"
  - "[[#Members]]"
class_of:
  - "[[Cpp std functional]]"
date created: Friday, October 11th 2024, 2:17:19 pm
date modified: Friday, February 21st 2025, 11:56:29 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background


## Syntax
```cpp
std::function <returnType (argType1, argType2)> name();
name = [](arg1, arg2){
 return ...;
};
```

## Concepts of Note
### Lambda Captures

## Members
| Function              | Description                                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **swap()**            | Swaps the wrapped callable of two std::function objects.                                                                                                                |
| **operator bool**     | Checks if the `std::function` contains a callable.                                                                                                                      |
| **operator ()**       | Invoke the callable with the given arguments.                                                                                                                           |
| **target()**          | Returns a pointer to the stored callable. If there is no callable stored, returns nullptr.                                                                              |
| **target_type()**<br> | Returns the [`**typeid**`](https://www.geeksforgeeks.org/typeid-operator-in-c-with-examples/) of the callable. If no callable is stored, it returns `**typeid(void)**`. |

## Media
[std function - cppreference.com](https://en.cppreference.com/w/cpp/utility/functional/function)