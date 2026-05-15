---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, January 2nd 2025, 11:30:57 am
function_of:
  - "[[Cpp std string]]"
---
# Background
[More info](https://www.geeksforgeeks.org/cpp-string-functions/)

# Usage
## General String Manipulation
| Method     | Return Type   | Example                                      | Description                                                                                            |
| ---------- | ------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `length()` | `size_t`      | `size_t len = str.length();`                 | Returns the number of characters in the string.                                                        |
| `size()`   | `size_t`      | `size_t size = str.size();`                  | Same as `length()`, returns the number of characters in the string.                                    |
| `append()` | `void`        | `str.append(" World");`                      | Appends the given string at the end of the current string.                                             |
| `substr()` | `std::string` | `std::string sub = str.substr(6, 5);`        | Returns a substring of the current string starting from the specified position and length.             |
| `erase()`  | `iterator`    | `str.erase(5, 5);`                           | Erases a portion of the string starting from the specified position for the given length.              |
| `strcpy()` | `char*`       | `char dest[20];`<br>`strcpy(dest, "Hello")`; | Copies a string from source to destination (Warning: C-style function). Will include the null pointer. |

## Searching and Comparing
| Method      | Return Type | Example                            | Description                                                                                                           |
| ----------- | ----------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `find()`    | `size_t`    | `size_t pos = str.find("World");`  | Finds the first occurrence of the specified substring within the string.                                              |
| `replace()` | `void`      | `str.replace(6, 5, "Universe");`   | Replaces a portion of the string with the given string starting from the specified position.                          |
| `compare()` | `int`       | `int result = str1.compare(str2);` | Compares two strings lexicographically. Returns 0 if equal, a negative value if less, or a positive value if greater. |
|             |             |                                    |                                                                                                                       |

## Information Retrieval
|Method|Return Type|Example|Description|
|---|---|---|---|
|`empty()`|`bool`|`bool isEmpty = str.empty();`|Checks if the string is empty.|
|`at()`|`char&`|`char& c = str.at(1);`|Accesses the character at the specified position in the string.|

## Iterators
|Functions|Description|
|---|---|
|begin()|This function returns an iterator pointing to the beginning of the string.|
|end()|This function returns an iterator that points to the end of the string.|
|[rfind()](https://www.geeksforgeeks.org/stdstringrfind-in-c-with-examples/)|This function is used to find the string’s last occurrence.|
|rbegin()|This function returns a reverse iterator pointing to the end of the string.|
|rend()|This function returns a reverse iterator pointing to the beginning of the string.|
|cbegin()|This function returns a const_iterator pointing to the beginning of the string.|
|cend()|This function returns a const_iterator pointing to the end of the string.|
|crbegin()|This function returns a const_reverse_iterator pointing to the end of the string.|
|crend()|This function returns a const_reverse_iterator pointing to the beginning of the string.|

## String Functions
| Function                                                                               | Description                                                                                                                               |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| length()                                                                               | This function returns the length of the string.                                                                                           |
| [swap()](https://www.geeksforgeeks.org/swap-in-cpp/)                                   | This function is used to swap the values of 2 strings.                                                                                    |
| size()                                                                                 | Used to find the size of string                                                                                                           |
| [resize()](https://www.geeksforgeeks.org/stdstringresize-in-c/)                        | This function is used to resize the length of the string up to the given number of characters.                                            |
| [find()](https://www.geeksforgeeks.org/string-find-in-cpp/)                            | Used to find the string which is passed in parameters                                                                                     |
| [push_back()](https://www.geeksforgeeks.org/stdstringpush_back-in-cpp/)                | This function is used to push the passed character at the end of the string                                                               |
| pop_back()                                                                             | This function is used to pop the last character from the string                                                                           |
| clear()                                                                                | This function is used to remove all the elements of the string.                                                                           |
| [strncmp()](https://www.geeksforgeeks.org/stdstrncmp-in-c/)                            | This function compares at most the first num bytes of both passed strings.                                                                |
| [strncpy()](https://www.geeksforgeeks.org/why-strcpy-and-strncpy-are-not-safe-to-use/) | This function is similar to strcpy() function, except that at most n bytes of src are copied                                              |
| [strrchr()](https://www.geeksforgeeks.org/strrchr-function-in-c-c/)                    | This function locates the last occurrence of a character in the string.                                                                   |
| [strcat()](https://www.geeksforgeeks.org/strcat-vs-strncat-c/)                         | This function appends a copy of the source string to the end of the destination string                                                    |
| find()                                                                                 | This function is used to search for a certain substring inside a string and returns the position of the first character of the substring. |
| [replace()](https://www.geeksforgeeks.org/stdstringreplace-stdstringreplace_if-c)      | This function is used to replace each element in the range [first, last) that is equal to old value with new value.                       |
| substr()                                                                               | This function is used to create a substring from a given string.                                                                          |
| compare()                                                                              | This function is used to compare two strings and returns the result in the form of an integer.                                            |
| erase()                                                                                | This function is used to remove a certain part of a string.                                                                               |

## Concatenation
https://www.geeksforgeeks.org/cpp-string-functions/