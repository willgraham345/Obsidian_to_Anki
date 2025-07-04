---
type: note/concept
date created: Friday, September 13th 2024, 12:03:47 pm
date modified: Friday, October 11th 2024, 5:48:30 pm
---
summary:: Idiom where class X derives from class template Y, taking template parameter Z, where Y is instantiated with Z = X. Provides a way for base classes to use methods of derived classes during compile time. 

similar:: [[DP Template Method]], [[Cpp Curiously Recurring Template Pattern]]

[The Curiously Recurring Template Pattern (CRTP) - DEV Community](https://dev.to/sandordargo/the-curiously-recurring-template-pattern-crtp-46j7)

A base class exposes an interface, and derived classes implement the interface. 

Base class is designed to be inherited from by its template parameter, and by nothing else. 

- Unrelated in the GoF Design Patterns book. A behavioral algorithm, and a C++ idiom
- A technique for static polymorphism and enabling code reuse in a template-based hierarchy.
- Class X derives from a class template instantiation using X itself as a template argument.

```cpp
// The Curiously Recurring Template Pattern (CRTP)
template<class X>
class Base
{
    // methods within Base can use template to access members of Derived
};

class Derived : public Base<Derived>
{
    // ...
};
```

```cpp
template <typename T>
class Counter
{
    static int _createdObjects;
    static int _aliveObjects;

    Counter()
    {
        ++_createdObjects;
        ++_aliveObjects;
    }

    Counter(const Counter&)
    {
        ++_createdObjects;
        ++_aliveObjects;
    }
protected:
    ~counter() // objects should never be removed through pointers of this type
    {
        --_aliveObjects;
    }
};
template <typename T> int Counter<T>::_createdObjects( 0 );
template <typename T> int Counter<T>::_aliveObjects( 0 );
```