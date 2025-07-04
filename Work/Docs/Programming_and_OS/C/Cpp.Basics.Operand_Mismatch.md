---
type: note
up: ["[[Cpp Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 22nd 2024, 4:07:29 pm
---
# Background
If two operands (inputs to the operator) don't match, then the operand with a "lower type" will be upgrade to match the operand of a "higher type"

# Order
`long double`
`double`
`float`
`unsigned long int`
`long int`
`unsigned int`
`int` 

```cpp
cout << 25u - 50;

// OUTPUTS:
4294967271
```
- `int` 50 is "promoted" to `unsigned int` -> `50u`
	- `25u-50u` will be an unsigned integer, --> 4204067271 when promoted to unsigned integer
