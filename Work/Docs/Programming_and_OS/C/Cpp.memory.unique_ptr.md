---
summary: A smart pointer that owns and manages another object through a pointer. The owned object is disposed of when the unique_ptr goes out of scope.<br><br>The managing of the unique_ptr can aslo be assigned to another pointer once operator `=` is called.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note
similar: ["[[Cpp.memory.shared_ptr]]"]
class_of: ["[[Cpp std memory]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, July 3rd 2025, 11:35:57 am
implementations: ["[[Cpp memory make_unique]]"]
tags: []
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[cplusplus.com/reference/memory/unique\_ptr/](https://cplusplus.com/reference/memory/unique_ptr/)

## Concepts of Note
- [p] `uniquePtrName.reset()`

## Usage

## Examples
```cpp
// C++ program to demonstrate the working of unique_ptr
// Here we are showing the unique_pointer is pointing to P1.
// But, then we remove P1 and assign P2 so the pointer now
// points to P2.

#include <iostream>
using namespace std;
// Dynamic Memory management library
#include <memory>

class Rectangle {
	int length;
	int breadth;

public:
	Rectangle(int l, int b)
	{
		length = l;
		breadth = b;
	}

	int area() { return length * breadth; }
};

int main()
{
// --\/ Smart Pointer
	unique_ptr<Rectangle> P1(new Rectangle(10, 5));
	cout << P1->area() << endl; // This'll print 50

	// unique_ptr<Rectangle> P2(P1);
	unique_ptr<Rectangle> P2;
	P2 = move(P1);

	// This'll print 50
	cout << P2->area() << endl;

	// cout<<P1->area()<<endl;
	return 0;
}
```