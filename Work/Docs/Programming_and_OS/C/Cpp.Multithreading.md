---
type: note/library
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, February 14th 2025, 3:25:02 pm
libraries:
  - "[[Arduino TOC]]"
  - "[[C Arduino Digital Pins]]"
  - "[[C Arduino Serial Communication]]"
  - "[[Cpp atomic]]"
  - "[[Cpp condition_variable]]"
  - "[[Cpp future]]"
  - "[[Cpp Multithreading pthread]]"
  - "[[Cpp std mutex (library)]]"
  - "[[Cpp thread]]"
  - "[[Cpp.RTOS]]"
  - "[[Zephyr TOC]]"
library_of: "[[Cpp]]"
---
# Background
- Multithreading allows concurrent execution of two or more parts of a program to run concurrently to maximize the CPU. Every part of such a program is called a thread. Threads are lightweight processes within a process. 
- Multithreading support introduced in C++11.
	- Before that, POSIX threads and pthreads libraries were used. 
	- POSIX is also functional with C
		- See an example in [[C.Threads]]

# Usage

```cpp
std::thread thread_object (callable);
```

## Launching threads
### Function pointer
```cpp
void foo(param)
{ 
	//Statements; 
}
// The parameters to the function are put after the comma
std::thread thread_obj(foo, params);
```

### Function Object
```cpp
// Define the class of function object
class fn_object_class {
	// Overload () operator
	void operator()(params)
	{ 
		//Statements; 
	}
}
// Create thread object
std::thread thread_object(fn_object_class(), params)
```

### Lambda expression 
```cpp
// Define a lambda expression
auto f = [](params)
{
	//Statements;
};
// Pass f and its parameters to thread
// object constructor as
std::thread thread_object(f, params);
```

### Member Function 
#### Non-static
```cpp
// defining clasc
class Base {
public:
	// non-static member function
	void foo(param) { Statements; }
}
// object of Base Class
Base b;
// first parameter is the reference to the functionn
// and second paramter is reference of the object
// at last we have arguments
std::thread thread_obj(&Base::foo, &b, params);
```

#### Static
```cpp
// defining class
class Base {
public:
	// static member function
	static void foo(param) { Statements; }
}
// object of Base Class
Base b;
// first parameter is the reference to the function
// and rest are arguments
std::thread thread_obj(&Base::foo, params);
```

## Waiting for threads to finish
```cpp
int main()
{
	// Start thread t1
	std::thread t1(callable);
	// Wait for t1 to finish
	t1.join();
	// t1 has finished do other stuff
	Statements;
}
```