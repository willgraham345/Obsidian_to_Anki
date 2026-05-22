---
summary: A general-purpose polymorphic function wrapper. Instances can store, copy, and invoke any target. The target is the stored callable object of the std::function. If a std::function contains no target it is considered empty.
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Concepts of Note]]"
  - "[[#Members]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
implements:
  - "[[DP Type Erasure]]"
similar:
  - "[[Cpp Lambda Capture|Lambda Functions]]"
associations:
  - "[[Cpp std move]]"
class_of:
  - "[[Cpp std functional (library)]]"
date created: Friday, October 11th 2024, 2:17:19 pm
date modified: Monday, March 23rd 2026, 3:10:36 pm
tags: []
template:
template-version:
used_by:
  - "[[Cpp std reference_wrapper]]"
  - "[[DP Type Erasure]]"
uses:
  - "[[Cpp Lambda Capture]]"
---

# Summary
󰙎 std function ;;; A general-purpose polymorphic function wrapper. Instances can store, copy, and invoke any target. The target is the stored callable object of the std::function. If a std::function contains no target it is considered empty. Used heavily for type erasure in test injections.

# Additional Background
## Concepts of Note
![[DP Type Erasure#^c4e56e]]

## Usage
󰙎 `std::function<R(Args...)>` ;;; canonical C++ type-erasure wrapper — stores any callable (lambda, free function, functor, bound member) matching the signature.

 `std::function<int(float)> func` ;;; Empty constructor for a std function `func` which returns an `int` and takes a `float` as a parameter. 

 `std::function<void(int)> printFunc{print_func}` ;;; Create a standard function `printFunc` which will use previously defined function `void print_num(int i) { std::cout << i; }`. `printFunc(55)` is how it is called.

 `std::function<void(int)> printFunc([](int i) {std::cout << i;});` ;;; Create a standard function `printFunc` using a lambda function. The `printFunc(55)` should print "55" to the console with `cout`. The lambda does not need any additional context.

 `Car(getThing getter): m_getter(std::move(getter))` ;;; Define a constructor for `Car`, which instantiates a std function aliased (`using std::function<rType(args)> getThing`)

## Syntax
### Basic
```cpp
// ReturnType: what the callable returns
// ArgType1, ArgType2: parameter types the callable accepts
std::function<ReturnType(ArgType1, ArgType2)> name;

// Assign any matching callable — lambda, free function, functor, or bound member
name = [](ArgType1 a, ArgType2 b) -> ReturnType {
    return ...;
};

// Invoke like a normal function
ReturnType result = name(arg1, arg2);
```

### Type Erasure — Dependency Injection
```cpp
// Define erased signatures as named aliases
// int()  — callable returns int, takes no args
// void() — callable returns void, takes no args
using SpeedFn = std::function<int()>;
using StopFn  = std::function<void()>;

class Car {
    SpeedFn mGetSpeed;  // concrete type of the stored callable is hidden here
    StopFn  mStop;
public:
    // Constructor accepts any callable matching each signature
    // std::move transfers ownership without copying captured state
    Car(SpeedFn getSpeed, StopFn stop)
        : mGetSpeed{std::move(getSpeed)}, mStop{std::move(stop)} {}

    void controlSpeed() {
        if (mGetSpeed() > 50)  // invokes stored callable — no vtable or override needed
            mStop();
    }
};

// Production: wrap the real object in lambdas at the composition root
// [&] captures motor by reference so the lambda delegates to the real object
DcMotor motor;
Car car{[&] { return motor.getSpeed(); },
        [&] { motor.stop(); }};

// Test: inject plain lambdas — no mock class or interface required
// stopped is captured by reference so the lambda can set it when invoked
bool stopped = false;
Car testCar{[] { return 100; },       // always reports speed > 50
            [&] { stopped = true; }}; // records that stop was called
testCar.controlSpeed();
assert(stopped);
```

## Concepts of Note
### Lambda Captures
See [[Cpp Lambda Capture]] for more information

## Members
| Function              | Description                                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **swap()**            | Swaps the wrapped callable of two std::function objects.                                                                                                                |
| **operator bool**     | Checks if the `std::function` contains a callable.                                                                                                                      |
| **operator ()**       | Invoke the callable with the given arguments.                                                                                                                           |
| **target()**          | Returns a pointer to the stored callable. If there is no callable stored, returns nullptr.                                                                              |
| **target_type()**<br> | Returns the [`**typeid**`](https://www.geeksforgeeks.org/typeid-operator-in-c-with-examples/) of the callable. If no callable is stored, it returns `**typeid(void)**`. |

## Media
[std function - cppreference.com](https://en.cppreference.com/w/cpp/utility/functional/function)