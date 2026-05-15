---
summary: Same functionality as auto, but this tries to store these variables closer in the register to the microprocessor if a free register is available. A hint to the compiler.
headings: ["[[#Concepts of Note]]"]
type: note/item
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, September 2nd 2025, 11:07:37 am
item_of: ["[[Cpp keywords]]"]
keyword_of: ["[[Cpp Storage Classes and Keywords]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
## Concepts of Note
- Same functionality of [[Cpp auto]], but it tires to store these variables closer in the register to the microprocessor if a free register is available. 
- 
- *Scope:* Local
- *Default Value:* Garbage Value
- *Memory Location:* Register in CPU or RAM
- *Lifetime:* Till the end of its scope

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