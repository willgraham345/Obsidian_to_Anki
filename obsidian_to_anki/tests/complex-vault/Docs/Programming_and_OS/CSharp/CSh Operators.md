---
summary:
headings:
  - "[[#Usage]]"
type: note/concept
concepts:
  - "[[CSh]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 17th 2025, 10:50:23 am
concept_of:
  - "[[CSh|C Sharp]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
Used to perform operation on variables and values

## Usage


### Arithmetic

| Operator | Name           | Description                            | Example     |
| -------- | -------------- | -------------------------------------- | ----------- |
| `+`        | Addition       | Adds together two values               |  `x + y`    |
| `-`        | Subtraction    | Subtracts one value from another       |  `x - y`    |
| `*`        | Multiplication | Multiplies two values                  |  `x * y`    |
| `/`        | Division       | Divides one value by another           |  `x / y`    |
| `%`        | Modulus        | Returns the division remainder         |  `x % y`    |
| `++`       | Increment      | Increases the value of a variable by 1 |  `x++`      |
| `--`       | Decrement      | Decreases the value of a variable by 1 | `x--`       |

### Assignment
| Operator     | Example | Same As      |
| ------------ | ------- | ------------ |
|  `=`         | `x = 5`   | `x = 5`      |
|  `+=`        | `x += 3`  | `x = x + 3`  |
|  `-=`        | `x -= 3`  | `x = x - 3`  |
|  `*=`        | `x *= 3`  | `x = x * 3`  |
|  `/=`        | `x /= 3`  | `x = x / 3`  |
|  `%=`        | `x %= 3`  | `x = x % 3`  |
|  `&=`        | `x &= 3`  | `x = x & 3`  |
|  `\|=`       | `x \|= 3` | `x = x \| 3` |
|  `^=`        | `x ^= 3`  | `x = x ^ 3`  |
|  `>>=`       | `x >>= 3` | `x = x >> 3` |
| `<<=`        | `x <<= 3` | `x = x << 3` |

### Comparison
| Operator | Name                     | Example     |
| -------- | ------------------------ | ----------- |
| `==`       | Equal to                 |  `x == y`   |
| `!=`       | Not equal                |  `x != y`   |
| `>`        | Greater than             |  `x > y`    |
| `<`        | Less than                |  `x < y`    |
| `>=`       | Greater than or equal to |  `x >= y`   |
| `<=`       | Less than or equal to    | `x <= y`    |

### Logic
| Operator | Name        | Description                                             | Example              |
| -------- | ----------- | ------------------------------------------------------- | -------------------- |
| `&&`     | Logical and | Returns True if both statements are true                | `x < 5 &&  x < 10`   |
| `\|`     | Logical or  | Returns True if one of the statements is true           | `x < 5 \| x < 4`     |
| `!`      | Logical not | Reverse the result, returns False if the result is true | `!(x < 5 && x < 10)` |
