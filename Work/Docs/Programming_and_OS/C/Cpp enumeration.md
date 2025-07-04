---
summary: Data type consisting of int constants casted to names, considered less type-safe than [[Cpp enum (class)]]
headings: ["[[#Usage]]"]
type: note/class
same: ["[[Cpp enum (class)]]"]
similar: ["[[Cpp std variant]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, April 14th 2025, 10:00:54 pm
tags: [code/cpp/variables/enumerations]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- A user-defined data type that consists of int constants. 
	- For example: `enum season { spring, summer, autumn, winter } ;`
- Two enumerations cannot share the same names.
	- No variable can have a name which is already in some enumeration
- The enumeration's underlying type is an integer. 
- Unscoped enumerations are enumerations that aren't tied to a class
- Enumeration can be used in a class (C++ 11) that to make enumerations strongly typed and strongly scoped. 
	- These enumerations don't allow implicit conversions to `int` and will not compare with enumerators from different enumerations.

## Usage
- [p] `enum class enumName {name1, bigName2}` = Declare an enum with two different possible types (not implicitly converted to int) = #code/cpp/variables/enumerations 
<!--ID: 1751434091693-->

- [p] `enum enumName {enum1, enum2}` = Declare an enum with two different possible types (implicitly converted to an int) = #code/cpp/variables/enumerations 
<!--ID: 1751434091697-->


## Basic Use Syntax
### Accessing unscoped enumerations
```cpp
struct X
{
    enum direction { left = 'l', right = 'r' };
};
X x;
X* p = &x;
int a = X::direction::left; // allowed only in C++11 and later
int b = X::left;
int c = x.left;
int d = p->left;
```
	
### Underlying Type
```cpp
enum Foo { a, b, c = 10, d, e = 1, f, g = f + c };
//a = 0, b = 1, c = 10, d = 11, e = 1, f = 2, g = 12
```

## Enum Class
### Syntax
```cpp
// Declaration
enum class EnumName{ Value1, Value2, ... ValueN};

// Initialisation
EnumName ObjectName = EnumName::Value;
```

### Example
```cpp
// C++ program to demonstrate working
// of Enum Classes

#include <iostream>
using namespace std;

int main()
{

	enum class Color { Red,
					Green,
					Blue };
	enum class Color2 { Red,
						Black,
						White };
	enum class People { Good,
						Bad };

	// An enum value can now be used
	// to create variables
	int Green = 10;

	// Instantiating the Enum Class
	Color x = Color::Green;

	// Comparison now is completely type-safe
	if (x == Color::Red)
		cout << "It's Red\n";
	else
		cout << "It's not Red\n";

	People p = People::Good;

	if (p == People::Bad)
		cout << "Bad people\n";
	else
		cout << "Good people\n";

	// gives an error
	// if(x == p)
	// cout<<"red is equal to good";

	// won't work as there is no
	// implicit conversion to int
	// cout<< x;

	cout << int(x);

	return 0;
}

```

```output
It's not Red
Good people
1
```