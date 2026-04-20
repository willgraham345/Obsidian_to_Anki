---
summary: For loops in Cpp
headings: ["[[#Examples]]", "[[#Usage]]"]
type: note/concept
associations: ["[[Cpp while loops]]"]
concept_of: ["[[Cpp Control Flow]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, September 2nd 2025, 11:03:59 am
tags: [lang/control_flow/forLoop]
uses: ["[[Cpp auto]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
  `for (int i=0; i< data.size() ; i++ )` ;;;  Range based for loop (Note, you can use std size_t, but that gave me weird formatting) = #lang/control_flow/forLoop 
ID: 1751997629762



  `for (const auto &x: data )` ;;; Automatic iterator, better practice than typical for loop = #lang/control_flow/forLoop  
ID: 1751997629766

## Examples


### For Loop
```cpp
for (int i = 1; i <= 5; i++) {  
  std::cout << i;  
}
```

### For Each Loop
Useful when iterating through list-like structures like arrays or `std::vector`
```cpp
int fibonacci[5] = {0, 1, 1, 2, 3};  
for (int number : fibonacci) {  
  std::cout << number;  
}
```

#### Auto Keyword
When iterating through an with for each loop, the counter variable may be declared using the auto keyword. This lets C++ deduce the type of variable based on the type of the list it belongs to
```cpp
int fibonacci[5] = {0, 1, 1, 2, 3};  
for (auto number : fibonacci) {  
  std::cout << number;  
}
```
