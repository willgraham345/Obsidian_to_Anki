---
type: note/concept
concept_of: ["[[Cpp Basics]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 10:45:57 am
---

|C|C++|
|---|---|
|C was developed by Dennis Ritchie between the year 1969 and 1973 at AT&T Bell Labs.|C++ was developed by Bjarne Stroustrup in 1979.|
|C does no support polymorphism, encapsulation, and inheritance which means that C does not support object oriented programming.|C++ supports [polymorphism](https://www.geeksforgeeks.org/polymorphism-in-c/), [encapsulation](https://www.geeksforgeeks.org/encapsulation-in-c/), and [inheritance](https://www.geeksforgeeks.org/inheritance-in-c/) because it is an object oriented programming language.|
|C is (mostly) a subset of C++.|C++ is (mostly) a superset of C.|
|Number of [keywords](https://www.geeksforgeeks.org/variables-and-keywords-in-c/) in C:  <br>* C90: 32  <br>* C99: 37  <br>* C11: 44  <br>* C23: 59|Number of [keywords](https://www.geeksforgeeks.org/cc-tokens/) in C++:  <br>* C++98: 63  <br>* C++11: 73  <br>* C++17: 73  <br>* C++20: 81|
|For the development of code, C supports [procedural programming](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/).|C++ is known as hybrid language because C++ supports both [procedural](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/) and [object oriented programming paradigms](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/).|
|Data and functions are separated in C because it is a procedural programming language.|Data and functions are encapsulated together in form of an object in C++.|
|C does not support information hiding.|Data is hidden by the Encapsulation to ensure that data structures and operators are used as intended.|
|Built-in data types is supported in C.|Built-in & user-defined data types is supported in C++.|
|C is a function driven language because C is a procedural programming language.|C++ is an object driven language because it is an object oriented programming.|
|Function and operator overloading is not supported in C.|Function and operator overloading is supported by C++.|
|C is a function-driven language.|C++ is an object-driven language|
|Functions in C are not defined inside structures.|Functions can be used inside a structure in C++.|
|Namespace features are not present inside the C.|[Namespace](https://www.geeksforgeeks.org/namespace-in-c/) is used by C++, which avoid name collisions.|
|Standard IO header is [stdio.h](https://www.geeksforgeeks.org/whats-difference-between-and/).|Standard IO header is [iostream.h](https://www.geeksforgeeks.org/basic-input-output-c/).|
|Reference variables are not supported by C.|Reference variables are supported by C++.|
|Virtual and friend functions are not supported by C.|[Virtual](https://www.geeksforgeeks.org/virtual-function-cpp/) and [friend functions](https://www.geeksforgeeks.org/friend-class-function-cpp/) are supported by C++.|
|C does not support inheritance.|C++ supports inheritance.|
|Instead of focusing on data, C focuses on method or process.|C++ focuses on data instead of focusing on method or procedure.|
|C provides [malloc()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/) and [calloc()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/) functions for [dynamic memory allocation](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/), and [free()](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/) for memory de-allocation.|C++ provides [new operator](https://www.geeksforgeeks.org/new-and-delete-operators-in-cpp-for-dynamic-memory/) for memory allocation and [delete operator](https://www.geeksforgeeks.org/new-and-delete-operators-in-cpp-for-dynamic-memory/) for memory de-allocation.|
|Direct support for exception handling is not supported by C.|[Exception handling](https://www.geeksforgeeks.org/exception-handling-c/) is supported by C++.|
|[scanf()](https://www.geeksforgeeks.org/scanf-and-fscanf-in-c-simple-yet-poweful/) and printf() functions are used for input/output in C.|[cin and cout](https://www.geeksforgeeks.org/basic-input-output-c/) are used for [input/output in C++](https://www.geeksforgeeks.org/basic-input-output-c/).|
|C structures don’t have access modifiers.|C ++ structures have access modifiers.|
|C follows the top-down approach|C++ follows the Bottom-up approach|
|There is no strict type checking in C programming language.|Strict type checking in done in C++.  So many programs that run well in C compiler will result in many warnings and errors under C++ compiler.|
|C does not support overloading|C++ does support overloading|
|Type punning with unions is allows (C99 and later)|Type punning with unions is undefined behavior (except in very specific circumstances)|
|Named initializers may appear out of order|Named initializers must match the data layout of the struct|
|File extension is “.c”|File extension is “.cpp” or “.c++” or “.cc” or “.cxx”|
|Meta-programming: macros + _Generic()|Meta-programming: templates (macros are still supported but discouraged)|
|There are 32 keywords in the C|There are 97 keywords in the C++|