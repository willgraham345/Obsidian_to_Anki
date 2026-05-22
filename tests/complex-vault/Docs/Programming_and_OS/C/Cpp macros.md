---
summary: Macros in cpp are object-like, function-like, and/or conditional. They are typically written in all caps. Commonly used for variables that should remain constant through the execution of the program. They are generally-stored as read-only tokens in the memory segment of the program. Macros are implemented by the preprocessor through direct text substitution.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
  - "[[#Workflows]]"
similar:
  - "[[Cpp templates]]"
concept_of:
  - "[[Cpp Variables and Containers]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, March 9th 2026, 9:21:21 pm
tags:
  - lang/macros/function-like
  - lang/macros/object-like
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Cpp Variables and Containers]]"
  - "[[CS Preprocessor]]"
uses:
  - "[[Cpp const]]"
  - "[[Cpp constexpr]]"
processes:
  - "[[Cpp macros#macro expansion]]"
---

# Summary
󰙎 Cpp macros ;;; Macros in cpp are object-like, function-like, and/or conditional. They are typically written in all caps. Commonly used for variables that should remain constant through the execution of the program. They are generally-stored as read-only tokens in the memory segment of the program. Macros are implemented by the preprocessor through direct text substitution.

# Additional Background

`const` vs `constexpr`
Similar, but `constexpr` are initialized at compiler time.

## Concepts of Note
- macro expansion takes place when macros are *used*, not when they are defined. 
Two kinds of macros
- Function like macros
- Object-like macros

## Usage
Constant using `const` keyword
  `#define MACRO_A val` ;;; Define an object-like macro named `MACRO_A` with value `val`. =

 `#define SQUARE(x) {`
      `(x*x)`
      `}` = Define a function-like macro named `SQUARE` with args `x` as the input. =
 `#ifdef MACRO_A`
      `#define MACRO_B 3.14`
      `#endif` = Conditionally compile a macro `MACRO_B`, which is equal to pi, if the macro `MACRO_A` is defined. =

```cpp
const DATATYPE variable_name = value;
```

Constant using the `constexpr` keyword
```cpp
constexpr DATATYPE variable_name = value;
```

Constant using `#define` preprocessor
- Known as "macro constants"
These will work as an alias for the value which is substituted during the preprocessing. 
```cpp
#define MACRO_NAME replacement_value
```

### Processes

##### macro expansion
 start:
1. “To summarize, the complete process of macro expansion when the function-like macro F(Z, 6) is invoked is
2. F(Z, 6)
3. F(3, 6) (argument expansion)
4. 3 x 6 x K (parameter substitution in the macro body)
5. 3x6x7 (expansion of the result)
 end:
