---
type: note/component
summary: Same functionality as auto, but this tries to store these variables closer in the register to the microprocessor if a free register is available.
---
# Background
- Same functionality of [[Cpp.Storage.Classes.auto]], but it tires to store these variables closer in the register to the microprocessor if a free register is available. 
- 
- *Scope:* Local
- *Default Value:* Garbage Value
- *Memory Location:* Register in CPU or RAM
- *Lifetime:* Till the end of its scope

# Usage
## Example
```cpp
// C++ Program to illustrate the use of register variables
#include <iostream>
using namespace std;

void registerStorageClass()
{

	cout << "Demonstrating register class\n";

	// declaring a register variable
	register char b = 'G';

	// printing the register variable 'b'
	cout << "Value of the variable 'b'"
		<< " declared as register: " << b;
}
int main()
{

	// To demonstrate register Storage Class
	registerStorageClass();
	return 0;
}

```