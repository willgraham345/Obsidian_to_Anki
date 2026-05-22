---
type: note
---
# Background
Types of C++ exceptions
1. Synchronous 
	- when something goes wrong because of a mistake in the input data or when the program is not equipped to handle the current type of date it's working with, such as dividing a number by zero
2. Asynchronous
	- Exceptions beyond the program's control, such as disc failure, keyboard interrupts, etc.

Limitations of exception handling in C++
- Exceptions may break the structure or flow of the code as multiple invisible exit points are created in the code which makes the code hard to read and debug.
- If exception handling is not done properly can lead to resource leaks as well.
- It’s hard to learn how to write Exception code that is safe.
- There is no C++ standard on how to use exception handling, hence many variations in exception-handling practices exist.
# Usage
## Syntax
```cpp
try {           
     // Code that might throw an exception__  
   throw SomeExceptionType("Error message");  
 }   
catch ( ExceptionName e1 )  {     
     // catch block catches the exception that is thrown from try block__  
 }
```


## Examples
More examples of this can be found [here](https://www.geeksforgeeks.org/exception-handling-c/)
```cpp
// C++ program to demonstate the use of try,catch and throw
// in exception handling.

#include <iostream>
#include <stdexcept>
using namespace std;

int main()
{

	// try block
	try {
		int numerator = 10;
		int denominator = 0;
		int res;

		// check if denominator is 0 then throw runtime
		// error.
		if (denominator == 0) {
			throw runtime_error(
				"Division by zero not allowed!");
		}

		// calculate result if no exception occurs
		res = numerator / denominator;
		//[printing result after division
		cout << "Result after division: " << res << endl;
	}
	// catch block to catch the thrown exception
	catch (const exception& e) {
		// print the exception
		cerr << "Exception " << e.what() << endl;
	}

	return 0;
}

```