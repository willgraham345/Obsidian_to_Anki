---
type: note
---
# Background
- New storage class in C++11
- Can be combined with other storage specifiers like [[Cpp.Storage.Classes.static]] and [[Cpp.Storage.Classes.extern]]
- *Memory Location:* RAM
- *Lifetime:* Till the end of its thread
# Usage
## Example Usage
```cpp
// C++ program to illustrate the use of thread_local storage
// sprecifier
#include <iostream>
#include <thread>
using namespace std;

// defining thread local variable
thread_local int var = 10;

// driver code
int main()
{
	// thread 1
	thread th1([]() {
		cout << "Thread 1 var Value: " << (var += 18) << '\n';
	});

	// thread 2
	thread th2([]() {
		cout << "Thread 2 var Value: " << (var += 7) << '\n';
	});

	// thread 3
	thread th3([]() {
		cout << "Thread 3 var Value: " << (var += 13) << '\n';
	});

	th1.join();
	th2.join();
	th3.join();

	return 0;
}
```
### Output
```
Thread 1 var Value: 28  
Thread 2 var Value: 17  
Thread 3 var Value: 23
```