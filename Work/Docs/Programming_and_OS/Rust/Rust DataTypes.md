---
summary: Every value in rust is a certain data type, and Rust is statically typed.
type: note/concept
concepts:
  - "[[Rust Array]]"
  - "[[Rust Integer Overflow]]"
  - "[[Rust Tuples]]"
associations:
  - "[[Rust Variables]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, April 4th 2025, 1:19:16 pm
workflows:
  - "[[Rust type conversion (casting)]]"
classes:
  - "[[Rust std String]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Every value in Rust is a certain data type.
- Rust is statically typed, meaning that we must know the types of all variables at compile time. The compiler can typically infer what type we want to use based on the value and how we use it. 

## Scalar types
Scalar = a single value

| Length  | Signed  | Unsigned |
| ------- | ------- | -------- |
| 8-bit   | `i8`    | `u8`     |
| 16-bit  | `i16`   | `u16`    |
| 32-bit  | `i32`   | `u32`    |
| 64-bit  | `i64`   | `u64`    |
| 128-bit | `i128`  | `u128`   |
| arch    | `isize` | `usize`  |

|Number literals|Example|
|---|---|
|Decimal|`98_222`|
|Hex|`0xff`|
|Octal|`0o77`|
|Binary|`0b1111_0000`|
|Byte (`u8` only)|`b'A'`|


| Floating Point Types | Size    |
| -------------------- | ------- |
| `f32`                | 32 bits |
| `f64`                | 64 bits |

#### Booleans
`true`
`false`

#### Characters
`char`
- Char has single quotes `'`, and strings have double quotes `"` 
- Unicode scalar values from `U+0000` to `U+E000` to `U+10FFFF` inclusive

## Compound Types
- Group multiple values into one type
- Rust has two primitive types: tuples and arrays