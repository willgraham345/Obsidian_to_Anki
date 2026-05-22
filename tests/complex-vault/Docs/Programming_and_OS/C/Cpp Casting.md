---
summary: How to convert expressions of a given type into another type. This can be done implicitly, explicitly, or through various casting methods.
type: note/process
headings:
functions:
  - "[[Cpp dynamic_cast]]"
  - "[[Cpp static_cast]]"
  - "[[Cpp std any]]"
  - "[[Cpp stoi]]"
  - "[[Cpp to_string]]"
  - "[[Cpp typeid]]"
  - "[[Cpp.memory.dynamic_pointer_cast]]"
concept_of:
  - "[[Cpp]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, March 20th 2026, 11:08:20 am
implementations:
  - "[[Cpp static_cast]]"
process_of:
  - "[[Cpp Variables and Containers]]"
tags: [lang/build/compiler, lang/data/casting, lang/data/casting/implicit, lang/data/const, lang/data/static, lang/oop/polymorphism]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

## Usage
  `toType varName = static_cast<toType>(dataToConvert)` ;;; Static type conversion (done at compile time) 

  `toType varName = dynamic_cast<toType>(dataToConvert)` ;;; Usually used for downcasting (converting a pointer/reference of a base class to a derived class) in polymorphisms and inheritance. Returns a `nullptr` if the conversion isn't possible. =  

  `const_cast<toType>(data)` ;;; Used to modify the const or volatile qualifier of a program, temporarily removing the constancy of an object. USE CAUTION. = 

 `implicit_cast<toType>(data)` ;;; Used when the compiler can’t determine which of two types to use as `T` when using a function that takes in only one type. This is only applicable when you have two types that can be implicitly casted to each other. 

## Media
[cplusplus.com/doc/oldtutorial/typecasting/](https://cplusplus.com/doc/oldtutorial/typecasting/)
<iframe src="https://cplusplus.com/doc/oldtutorial/typecasting/" style="width: 100%; height: 600px;"></iframe>
