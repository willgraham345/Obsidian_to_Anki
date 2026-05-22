---
summary: Copy cstrings back and forth.
headings:
  - "[[#Usage]]"
type: note/function
up:
  - "[[Cpp std string]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, May 14th 2025, 10:34:13 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[More examples](https://www.geeksforgeeks.org/different-ways-to-copy-a-string-in-c-c/)

## Usage

- IMPORTANT: only for C strings
- From `<string.h>`
- Accepts a pointer to destination array, and source array as parameter
```cpp
char* **strcpy**(char* _dest_, const char* _src_);
```

### Example
```cpp
// CPP program to copy the string using
// strcpy function
#include <bits/stdc++.h>
using namespace std;

// Function to copy the string
char* copyString(char s[])
{
	char* s2;
	s2 = (char*)malloc(20);

	strcpy(s2, s);
	return (char*)s2;
}

// Driver Code
int main()
{
	char s1[20] = "GeeksforGeeks";
	char* s2;

	// Function Call
	s2 = copyString(s1);
	cout << s2 << endl;
	return 0;
}

// This code is contributed by Susobhan Akhuli
```

## Loops
### Example
```cpp
// CPP program to copy string using loops
#include <iostream>
#include <string.h>
using namespace std;

// Function to copy the string
char* copyString(char s[])
{
	int i;
	char* s2;
	s2 = (char*)malloc(20);

	// Executing till null character
	// is found
	for (i = 0; s[i] != '\0'; i++) {

		// Copy the character one
		// by one from s1 to s2
		s2[i] = s[i];
	}

	// Return the pointer of newly
	// created string
	return (char*)s2;
}

// Driver Code
int main()
{
	char s1[20] = "GeeksforGeeks";
	char* s2;

	// Function Call
	s2 = copyString(s1);
	cout << s2 << endl;
	return 0;
}

// This code is contributed by Susobhan Akhuli
```