---
summary: Helpful string container for functions and input/output. Takes multiple strings as input at once.
type: note/class
examples: ["[[#Parse csv]]", "[[#Reading a line of data with unknown amount of numbers]]", "[[#Stringstream Functions Parameters]]"]
class_of: ["[[Cpp Input Output]]", "[[Cpp std]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 3rd 2025, 10:28:19 am
headings: ["[[#Examples]]", "[[#Usage]]"]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
### Instantiation
```cpp
stringstream stringstream_object(string_name);
```
[std  basic_stringstream - cppreference.com](https://en.cppreference.com/w/cpp/io/basic_stringstream)

| Function  | Description                                                                                                                                                                                                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear()` | Clears error bits in the stringstream object so you can use it again. You'll need to call this each time you start passing a new string with the stringstream object. If you don't, the object could still be in a bad state and you may not be able to read anything from the stringstream (even if you change its associated string). |
| `str()`   | Returns the string associated with the stringstream object                                                                                                                                                                                                                                                                              |
| `str (s)` | Associates the string `s` to the stringstream object                                                                                                                                                                                                                                                                                    |
| `<<`      | Add a string to the stringstream object                                                                                                                                                                                                                                                                                                 |
| `>>`      | Read something from the stringstream object                                                                                                                                                                                                                                                                                             |

## Examples
### Stringstream Functions Parameters
```cpp
// C++ Program to print string using function
#include <iostream>

void print_string(std::string s)
{
	std::cout << "Passed String is: " << s << std::endl;
	return;
}

int main()
{
	std::string s = "GeeksforGeeks";
	print_string(s);
	return 0;
}
```
Output:
```
Passed String is: GeeksforGeeks
```

### Pointers/Strings
```cpp
// C++ Program to print string using pointers
#include <iostream>
using namespace std;

int main()
{

	string s = "Geeksforgeeks";

	// pointer variable declared to store the starting
	// address of the string
	char* p = &s[0];

	// this loop will execute and print the character till
	// the character value is null this loop will execute and
	// print the characters

	while (*p != '\0') {
		cout << *p;
		p++;
	}
	cout << endl;

	return 0;
}

```
Output:
```
Geeksforgeeks
```

#### Output a String onto Separate Lines
```cpp
// C++ Program to demonstrate use of stringstream object
#include <iostream>
#include <sstream>
#include<string>

using namespace std;

int main()
{

	string s = " GeeksforGeeks to the Moon ";
	stringstream obj(s);
	// string to store words individually
	string temp;
	// >> operator will read from the stringstream object
	while (obj >> temp) {
		cout << temp << endl;
	}
	return 0;
}
```
Output:
```
GeeksforGeeks
to
the
Moon
```

### Extraction
#### Reading a line of data with unknown amount of numbers
- This could also be done by calling `getline()`, looking for spaces, and calling `substr` to get substring for each number converting it to a C string. That's way harder than this:
```cpp
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main (void)
{
	stringstream ss;
	int foo;
	string inp;

	while (getline (cin, inp)) {
		ss.clear ();
		ss.str ("");
		ss << inp;

		while (ss >> foo) {
			cout << foo << endl;
		}
	}

	return 0;
}
```

#### Space Separated Integer to Vector
```cpp
#include <iostream>
#include <sstream>
#include <vector>

int main ( int, char ** )
{
    std::istringstream reader("31 #00 532 53 803 33 534 23 37");
    std::vector<int> numbers;
    do
    {
        // read as many numbers as possible.
        for (int number; reader >> number;) {
            numbers.push_back(number);
        }
        // consume and discard token from stream.
        if (reader.fail())
        {
            reader.clear();
            std::string token;
            reader >> token;
        }
    }
    while (!reader.eof());

    for (std::size_t i=0; i < numbers.size(); ++i) {
        std::cout << numbers[i] << std::endl;
    }
}
```

### Parse csv
```cpp
stringstream ss("23,4,56");
char ch;
int a, b, c;
ss >> a >> ch >> b >> ch >> c;  // a = 23, b = 4, c = 56
```
- `ch` is for discarded commas
- If `>>` fails to return a value, that is a value for a conditional. Failure to return a value is false.

#### Count number of words in a string
```cpp
// C++ program to demonstrate the
// use of a stringstream to
// convert int to string
#include <iostream>
#include <sstream>
using namespace std;

// Driver code
int main()
{
	int val=123;

	// object from the class stringstream
	stringstream geek;

	// inserting integer val in geek stream
	geek << val;

	// The object has the value 123
	// and stream it to the string x
	string x;
	geek >> x;

	// Now the string x holds the
	// value 123
	cout<<x+"4"<<endl;
	return 0;
}
```

```
 Number of words are: 6
```

#### Print frequencies of individual words in a string


#### Convert integer to a string
```cpp
// C++ program to demonstrate the
// use of a stringstream to
// convert int to string
#include <iostream>
#include <sstream>
using namespace std;

// Driver code
int main()
{
	int val=123;

	// object from the class stringstream
	stringstream geek;

	// inserting integer val in geek stream
	geek << val;

	// The object has the value 123
	// and stream it to the string x
	string x;
	geek >> x;

	// Now the string x holds the
	// value 123
	cout<<x+"4"<<endl;
	return 0;
}
```
Output
```
1234
```
