---
type: note
---
# Background
Tokenizing a string denotes splitting a string with respect to some delimeter
[More info here](https://www.geeksforgeeks.org/tokenizing-a-string-cpp/)

# Usage
## stringstream
- **Time Complexity:** O(n ) where n is the length of string.  
- **Auxiliary Space:** O(n-d) where n is the length of string and d is the number of delimiters.
```cpp
// Tokenizing a string using stringstream
#include <bits/stdc++.h>
using namespace std;
int main()
{
	
	string line = "GeeksForGeeks is a must try";
	// Vector of string to save tokens
	vector <string> tokens;
	// stringstream class check1
	stringstream check1(line);
	string intermediate;
	// Tokenizing w.r.t. space ' '
	while(getline(check1, intermediate, ' '))
	{
		tokens.push_back(intermediate);
	}
	// Printing the token vector
	for(int i = 0; i < tokens.size(); i++)
		cout << tokens[i] << '\n';
}
```
Output
```
GeeksForGeeks
is
a
must
try
```

## strtok
Splits strings according to given delimiters and returns the next token
```cpp
// C/C++ program for splitting a string
// using strtok()
#include <stdio.h>
#include <string.h>
int main()
{
	char str[] = "Geeks-for-Geeks";
	// Returns first token 
	char *token = strtok(str, "-");
	// Keep printing tokens while one of the
	// delimiters present in str[].
	while (token != NULL)
	{
		printf("%s\n", token);
		token = strtok(NULL, "-");
	}
	return 0;
}
```
Output
```
Geeks
for
Geeks
```

- **Time Complexity:** O(n ) where n is the length of string.  
- **Auxiliary Space:** O(1).