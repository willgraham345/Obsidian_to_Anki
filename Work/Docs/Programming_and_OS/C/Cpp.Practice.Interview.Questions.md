---
type: note
---
## INTERVIEW QUESTIONS
### 1.
Is there a difference between **class** and **struct**?
#### A
Classes can have functions, structs can only have data members

### 2.
What will the line of code below print out and why?

```cpp
#include <iostream>

int main(int argc, char **argv)
{
    std::cout << 25u - 50;
    return 0;
}
```
#### A.
- If two operands differ from one another, then the operand with the "lower type" will be promoted to the type of the "higher type" operand, using the following hierarchy 

### 3.
What is the error in the code below and how should it be corrected?

```cpp
my_struct_t *bar;
/* ... do stuff, including setting bar to point to a defined my_struct_t object ... */
memset(bar, 0, sizeof(bar));
```

#### A:
```cpp
my_struct_t *bar;
/* ... do stuff, including setting bar to point to a defined my_struct_t object ... */
memset(bar, 0, sizeof(bar));
```


### 4.
What will `i` and `j` equal after the code below is executed? Explain your answer.

```cpp
int i = 5;
int j = i++;
```


### 5.
Assuming `buf` is a valid pointer, what is the problem in the code below? What would be an alternate way of implementing this that would avoid the problem?

```cpp
size_t sz = buf->size();
while ( --sz >= 0 )
{
	/* do something */
}
```



### 6.
Consider the two code snippets below for printing a vector. Is there any advantage of one vs. the other? Explain.

Option 1:

```cpp
vector vec;
/* ... .. ... */
for (auto itr = vec.begin(); itr != vec.end(); itr++) {
	itr->print();
}
```

Option 2:

```cpp
vector vec;
/* ... .. ... */
for (auto itr = vec.begin(); itr != vec.end(); ++itr) {
	itr->print();
}
```


### 7.
Implement a template function `IsDerivedFrom()` that takes class C and class P as template parameters. It should return true when class C is derived from class P and false otherwise.



### 8.
Implement a template boolean `IsSameClass()` that takes class A and B as template parameters. It should compare class A and B and return false when they are different classes and true if they are the same class.



### 9.
Is it possible to have a recursive inline function?


### 10.
What is the output of the following code:

```cpp
#include <iostream>

class A {
public:
    A() {}
    ~A() {
        throw 42;
    }
};

int main(int argc, const char * argv[]) {
    try {
        A a;
        throw 32;
    } catch(int a) {
        std::cout << a;
    }
}
```



### 11.
You are given library class Something as follows:

```cpp
class Something {
public:
    Something() {
        topSecretValue = 42;
    }
    bool somePublicBool;
    int somePublicInt;
    std::string somePublicString;
private:
    int topSecretValue;
};
```

Implement a method to get topSecretValue for any given Something* object. The method should be cross-platform compatible and not depend on sizeof (int, bool, string).


### 12.
Implement a void function F that takes pointers to two arrays of integers (`A` and `B`) and a size `N` as parameters. It then populates `B` where `B[i]` is the product of all `A[j]` where `j != i`.

For example: If `A = {2, 1, 5, 9}`, then `B` would be `{45, 90, 18, 10}`.

### 13.
When you should use virtual inheritance?

### 14.
What is the output of the following code:

```cpp
#include <iostream>

int main(int argc, const char * argv[]) {
    int a[] = {1, 2, 3, 4, 5, 6};
    std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
}
```


### 15.
What is the output of the following code:

```cpp
#include <iostream>

class Base {
    virtual void method() {std::cout << "from Base" << std::endl;}
public:
    virtual ~Base() {method();}
    void baseMethod() {method();}
};

class A : public Base {
    void method() {std::cout << "from A" << std::endl;}
public:
    ~A() {method();}
};

int main(void) {
    Base* base = new A;
    base->baseMethod();
    delete base;
    return 0;
}
```

### 16.
How many times will this loop execute? Explain your answer.
```abnf
unsigned char half_limit = 150;

for (unsigned char i = 0; i < 2 * half_limit; ++i)
{
    // do something;
}
```


### 17.
How can you make sure a C++ function can be called as e.g. `void foo(int, int)` but not as any other type like `void foo(long, long)`?

### 18.
What is the problem with the following code?

```cpp
class A
{
public:
A() {}
~A(){}
};

class B: public A
{
public:
B():A(){}
~B(){}
};

int main(void)
{
  A* a = new B();
  delete a;
}
```


### 19.
What is a storage class?

### 20.
How can a C function be called in a C++ program?

### 21.
What will be the output of the following program?

```cpp
#include <iostream>

struct A
{
    int data[2];

    A(int x, int y) : data{x, y} {}
    virtual void f() {}
};

int main(int argc, char **argv)
{
    A a(22, 33);

    int *arr = (int *) &a;
    std::cout << arr[2] << std::endl;

    return 0;
}
```


### 22.
Are you allowed to have a `static const` member function? Explain your answer.

### 23.
Explain the `volatile` and `mutable` keywords.

### 24.
C++ supports multiple inheritance. What is the “diamond problem” that can occur with multiple inheritance? Give an example.