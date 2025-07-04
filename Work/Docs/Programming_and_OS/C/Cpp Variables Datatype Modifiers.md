---
type: note/concept
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, October 8th 2024, 12:52:05 pm
component_of:
  - "[[Cpp Primitive Data Types]]"
---
# Background
To get the range of data types with the following chart...
****Note: syntax<limits.h>**** header file is defined to find the range of fundamental data-types. Unsigned modifiers have minimum value is zero. So, no macro constants are defined for the unsigned minimum value.


|Data Type|Size (in bytes)|Range|
|---|---|---|
|short int|2|-32,768 to 32,767|
|unsigned short int|2|0 to 65,535|
|unsigned int|4|0 to 4,294,967,295|
|int|4|-2,147,483,648 to 2,147,483,647|
|long int|4|-2,147,483,648 to 2,147,483,647|
|unsigned long int|4|0 to 4,294,967,295|
|long long int|8|-(2^63) to (2^63)-1|
|unsigned long long int|8|0 to 18,446,744,073,709,551,615|
|signed char|1|-128 to 127|
|unsigned char|1|0 to 255|
|float|4|-3.4×10^38 to 3.4×10^38|
|double|8|-1.7×10^308 to1.7×10^308|
|long double|12|-1.1×10^4932 to1.1×10^4932|
|wchar_t|2 or 4|1 wide character|