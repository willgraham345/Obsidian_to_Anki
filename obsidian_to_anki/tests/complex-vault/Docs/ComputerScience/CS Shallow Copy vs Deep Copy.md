---
type: note
associations:
  - "[[Cpp copying]]"
---
# Background
- Creating a copy usually means to create an exact replica of the object. Depending on the resources held by the object, we may need to perform a shallow copy or a deep copy in order to create an exact replica of the object. 
	- If the variables of an object have been dynamically allocated, it is required to do a deep copy in order to create a copy of the object

|   |   |   |
|---|---|---|
||**Shallow Copy**|**Deep copy**|
|**1.**|When we create a copy of object by copying data of all member variables as it is, then it is called shallow copy|When we create an object by copying data of another object along with the values of memory resources that reside outside the object, then it is called a deep copy|
|**2.**|A shallow copy of an object copies all of the member field values.|Deep copy is performed by implementing our own copy constructor.|
|**3.**|In shallow copy, the two objects are not independent|It copies all fields, and makes copies of dynamically allocated memory pointed to by the fields|
|**4.**|It also creates a copy of the dynamically allocated objects|If we do not create the deep copy in a rightful way then the copy will point to the original, with disastrous consequences.|

## Shallow Copy
An object is created by simply copying the data of all variables in the original object. 
- Works well if none of the variables are defined in the heap section of memory. 
- If variables are dynamically allocated memory from the heap section --> the copied object variable will also reference the same memory location.
	- ![[Pasted image 20240327093820.png]]
### Example in C++
```cpp
// C++ program for the above approach
#include <iostream>
using namespace std;

// Box Class
class box {
private:
	int length;
	int breadth;
	int height;

public:
	// Function that sets the dimensions
	void set_dimensions(int length1, int breadth1,
						int height1)
	{
		length = length1;
		breadth = breadth1;
		height = height1;
	}

	// Function to display the dimensions
	// of the Box object
	void show_data()
	{
		cout << " Length = " << length
			<< "\n Breadth = " << breadth
			<< "\n Height = " << height
			<< endl;
	}
};

// Driver Code
int main()
{
	// Object of class Box
	box B1, B3;

	// Set dimensions of Box B1
	B1.set_dimensions(14, 12, 16);
	B1.show_data();

	// When copying the data of object
	// at the time of initialization
	// then copy is made through
	// COPY CONSTRUCTOR
	box B2 = B1;
	B2.show_data();

	// When copying the data of object
	// after initialization then the
	// copy is done through DEFAULT
	// ASSIGNMENT OPERATOR
	B3 = B1;
	B3.show_data();

	return 0;
}
```


## Deep Copy
In a deep copy, an object is created by copying data of all variables *and* it also allocates similar memory resources with the same value for the object.
- ![[Pasted image 20240327094107.png]]

### Example in C++
```cpp
// C++ program to implement the
// deep copy
#include <iostream>
using namespace std;

// Box Class
class box {
private:
	int length;
	int* breadth;
	int height;

public:
	// Constructor
	box()
	{
		breadth = new int;
	}

	// Function to set the dimensions
	// of the Box
	void set_dimension(int len, int brea,
					int heig)
	{
		length = len;
		*breadth = brea;
		height = heig;
	}

	// Function to show the dimensions
	// of the Box
	void show_data()
	{
		cout << " Length = " << length
			<< "\n Breadth = " << *breadth
			<< "\n Height = " << height
			<< endl;
	}

	// Parameterized Constructors for
	// for implementing deep copy
	box(box& sample)
	{
		length = sample.length;
		breadth = new int;
		*breadth = *(sample.breadth);
		height = sample.height;
	}

	// Destructors
	~box()
	{
		delete breadth;
	}
};

// Driver Code
int main()
{
	// Object of class first
	box first;

	// Set the dimensions
	first.set_dimension(12, 14, 16);

	// Display the dimensions
	first.show_data();

	// When the data will be copied then
	// all the resources will also get
	// allocated to the new object
	box second = first;

	// Display the dimensions
	second.show_data();

	return 0;
}

```