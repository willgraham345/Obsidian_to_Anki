---
type: note
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, October 8th 2024, 12:51:23 pm
---
# Background
- Constant values that are assigned to constant variables. 
- Contain memory, but do not have references as variables.
String vs Char
- Strings are like characters, but they can store multiple characters and use a double quote to store the same

# Usage

## Integer Literals
### Prefixes
| Integer Literal Type | Syntax                   | Example          |
|----------------------|--------------------------|------------------|
| Decimal              | `int num = 10;`          | `10`             |
| Binary               | `int num = 0b1010;`      | `0b1010`         |
| Octal                | `int num = 012;`         | `012`            |
| Hexadecimal          | `int num = 0xA;`         | `0xA`            |

### Suffixes
| Integer Literal Type | Suffix   | Example         |
|----------------------|----------|-----------------|
| Decimal              | (none)   | `int num = 10;` |
| Binary               | `b`      | `int num = 0b1010;` |
| Octal                | `o` or `O` | `int num = 012;` |
| Hexadecimal          | `x` or `X` | `int num = 0xA;` |

## Floating-Point Literals
```cpp
// VALID
10.125  
1.215-10L  
10.5E-3
// INVALID
123E  
1250f  
0.e879
```

## Character Literals
```cpp
char chr = 'G';
```

## String Literals
```cpp
char stringVal[] = "GeeksforGeeks";
```

# Macros
| Name       | Expresses                                                  |
| ---------- | ---------------------------------------------------------- |
| CHAR_MIN   | The minimum value for an object of type char               |
| CHAR_MAX   | Maximum value for an object of type char                   |
| SCHAR_MIN  | The minimum value for an object of type Signed char        |
| SCHAR_MAX  | Maximum value for an object of type Signed char            |
| UCHAR_MAX  | Maximum value for an object of type Unsigned char          |
| CHAR_BIT   | Number of bits in a char object                            |
| MB_LEN_MAX | Maximum number of bytes in a multi-byte character          |
| SHRT_MIN   | The minimum value for an object of type short int          |
| SHRT_MAX   | Maximum value for an object of type short int              |
| USHRT_MAX  | Maximum value for an object of type Unsigned short int     |
| INT_MIN    | The minimum value for an object of type int                |
| INT_MAX    | Maximum value for an object of type int                    |
| UINT_MAX   | Maximum value for an object of type Unsigned int           |
| LONG_MIN   | The minimum value for an object of type long int           |
| LONG_MAX   | Maximum value for an object of type long int               |
| ULONG_MAX  | Maximum value for an object of type Unsigned long int      |
| LLONG_MIN  | The minimum value for an object of type long long int      |
| LLONG_MAX  | Maximum value for an object of type long long int          |
| ULLONG_MAX | Maximum value for an object of type Unsigned long long int |
