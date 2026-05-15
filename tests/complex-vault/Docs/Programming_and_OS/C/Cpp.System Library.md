---
type: note
---
# Background
[Docs](https://cplusplus.com/reference/cstdlib/system/)
- Invokes command processor to execute a command. Returns 0 if successfully executed, and a nonzero value if it fails. 

# Usage
```cpp
int system (const char* command);
```

## Clearing the terminal
```cpp
# include <iostream>
using namespace std;
int main()
{
	cout << "Hello world!" << endl;
	system("cls");
	return 0;
}
```

## Checking if you can run a command in an OS
```cpp
// C++ program to check if we can run commands using
// system()
# include <cstdlib>
# include <iostream>
using namespace std;
int main()
{
	if (system(NULL))
		cout << "Command processor exists";
	else
		cout << "Command processor doesn't exists";

	return 0;
}

```