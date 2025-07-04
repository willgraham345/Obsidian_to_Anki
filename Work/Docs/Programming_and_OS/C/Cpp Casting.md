---
summary: How to convert expressions of a given type into another type. This can be done implicitly, explicitly, or through various casting methods.
type: note/workflow
functions: ["[[Cpp dynamic_cast]]", "[[Cpp static_cast]]", "[[Cpp std any]]", "[[Cpp stoi]]", "[[Cpp to_string]]", "[[Cpp typeid]]", "[[Cpp.memory.dynamic_pointer_cast]]"]
concept_of: ["[[Cpp]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, July 1st 2025, 3:45:59 pm
tags: [code/cpp/compilerChecks, code/cpp/oop/polymorphism, code/cpp/variables/casting, code/cpp/variables/const, code/cpp/variables/static]
workflow_of: ["[[Cpp Variables and Containers]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

## Usage
- [p] `toType varName ` `=` `static_cast<toType>(dataToConvert)` = Static type conversion (done at compile time) = #code/cpp/variables/casting #code/cpp/compilerChecks #code/cpp/variables/static
<!--ID: 1751434091742-->

- [p] `toType varName ` `=` `dynamic_cast<toType>(dataToConvert)` = Usually used for downcasting (converting a pointer/reference of a base class to a derived class) in polymorphisms and inheritance. Returns a `nullptr` if the conversion isn't possible. = #code/cpp/variables/casting #code/cpp/oop/polymorphism 
<!--ID: 1751434091746-->

- [p] `const_cast<toType>(data)` = Used to modify the const or volatile qualifier of a program, temporarily removing the constancy of an object. USE CAUTION. = #code/cpp/variables/casting #code/cpp/variables/const
<!--ID: 1751434091750-->

 - [p] `implicit_cast<toType>(data)` = Used when the compiler can’t determine which of two types to use as `T` when using a function that takes in only one type. This is only applicable when you have two types that can be implicitly casted to each other. = #code/cpp/variables/casting #code/cpp/variables/implicit_conversion

## Media
[cplusplus.com/doc/oldtutorial/typecasting/](https://cplusplus.com/doc/oldtutorial/typecasting/)
<iframe src="https://cplusplus.com/doc/oldtutorial/typecasting/" style="width: 100%; height: 600px;"></iframe>