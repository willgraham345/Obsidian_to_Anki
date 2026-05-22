---
type: note
---
# Type Casting
Type Casting: when you assign a value of one primitive data type to another


## Widening Casting
- Done automatically
- Converts a smaller type to a larger type size
- `byte` -> `short` -> `char` -> `int` -> `long` -> `float` -> `double`

## Narrowing Casting
- Done manually, by placing the type in parentheses in front of the value
- Converting a larger type to a smaller size type
- `double` -> `float` -> `long` -> `int` -> `char` -> `short` ->`byte`
- `double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int`