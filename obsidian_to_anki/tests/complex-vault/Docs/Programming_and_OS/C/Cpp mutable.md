---
summary: Determines how instance variables are modified after creation. Uses const and mutable as keywords
type: note/concept
implements: []
associations: ["[[Cpp const]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, February 7th 2025, 10:41:12 am
---
# Background
- Sometimes there is a requirement to modify one or more data members of the class/struct through the `const` function even though you don't want the function to update other members of the class/struct
- Used to allow a particular data member of a const object to be modified

# Usage
## Example
```cpp
// C++ program to illustrate the use of mutalbe storage
// class specifiers
#include <iostream>
using std::cout;

class Test {
public:
	int x;

	// defining mutable variable y
	// now this can be modified
	mutable int y;

	Test()
	{
		x = 4;
		y = 10;
	}
};

int main()
{
	// t1 is set to constant
	const Test t1;

	// trying to change the value
	t1.y = 20;
	cout << t1.y;

	// Uncommenting below lines
	// will throw error
	// t1.x = 8;
	// cout << t1.x;
	return 0;
}

```