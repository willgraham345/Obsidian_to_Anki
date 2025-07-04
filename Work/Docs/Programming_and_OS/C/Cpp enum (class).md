---
type: note
aliases: [scoped_enumeration]
concept_of: ["[[Cpp Variables and Containers]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 10:47:19 am
---
# Background
- Introduced in C++ 11 (also called scoped enumerations) which makes enumerations strongly typed and strongly scoped. 
- Underlying type
	- The values of the underlying enumeration. 
- Doesn't allow implicit conversion to int, and doesn't compare enumerators from different enumerations. 

Each enumerator becomes a named constant of the enumeration's type (typically `int`) which can be accessed using `::`. There are no implicit conversions from the values of a scoped enumerator to integral types.

# Usage
```cpp
// Declaration
enum class EnumName{ Value1, Value2, ... ValueN};

// Initialisation
EnumName ObjectName = EnumName::Value;
```