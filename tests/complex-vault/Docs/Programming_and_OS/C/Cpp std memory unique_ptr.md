---
summary: "Smart pointer with exclusive ownership. The owned object is destroyed when the unique_ptr goes out of scope. Ownership can be transferred (moved) but not copied."
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
up: "[[Cpp std memory]]"
similar:
  - "[[Cpp pointers]]"
  - "[[Cpp std memory shared_ptr]]"
  - "[[Cpp std memory weak_ptr]]"
aliases: [Cpp unique_ptr]
class_of:
  - "[[Cpp std memory]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, April 2nd 2026, 3:55:54 pm
implementations:
  - "[[Cpp std memory make_unique]]"
tags: []
template:
template-version:
uses:
  - "[[Cpp std memory make_unique]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[cplusplus.com/reference/memory/unique\_ptr/](https://cplusplus.com/reference/memory/unique_ptr/)

## Concepts of Note
󰙎 exclusive ownership ;;; only one `unique_ptr` may own a given object at a time — no copy constructor or copy assignment
󰙎 move semantics ;;; ownership transferred via `std::move(p)` — source pointer becomes null after transfer
󰙎 custom deleter ;;; `unique_ptr<T, Deleter>` — second template param specifies cleanup callable; useful for C handles (e.g. `FILE*`)
󰙎 make_unique ;;; preferred factory (C++14); exception-safe, no raw `new` → [[Cpp std memory make_unique]]
󰠗 Why can't you copy a unique_ptr? ;; Copying would create two owners for the same object, violating exclusive ownership. Transfer ownership with `std::move()`.
󰠗 What happens when a unique_ptr goes out of scope? ;; Its destructor calls `delete` (or the custom deleter) on the managed pointer automatically.

## Usage
### Create
 `auto p = std::make_unique<MyType>(args...);` ;;; preferred construction of a pointer, which should only be accessed by one unit of translation (C++14 and up)

### Transfer Ownership
 `auto q = std::move(p);` ;;; p becomes null; q takes ownership
 `fn(std::move(p));` ;;; pass ownership into a function

### Access and Release
 `p->method()` ;;; member access
 `p.get()` ;;; raw pointer — does not affect ownership; never delete this
 `p.reset();` ;;; destroy managed object and set pointer to null
 `p.reset(new MyType());` ;;; destroy old object, take ownership of new one
 `T* raw = p.release();` ;;; relinquish ownership without destroying — caller must delete

### Custom Deleter
 `std::unique_ptr<FILE, decltype(&fclose)> f(fopen("x","r"), fclose);` ;;; manage a C FILE* with automatic fclose on scope exit

See also [[Cpp std memory make_unique]]

## Examples %% fold %% 
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