---
type:
date created: Friday, October 11th 2024, 5:45:39 pm
date modified: Friday, October 11th 2024, 5:47:36 pm
---
[summary::]

# Object Counter
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

# Static Polymorphism
```cpp
template <typename T>
class Vehicle
{
public:
    double getNumberOfWheels() const
    {
        return static_cast<T const&>(*this).getNumberOfWheels();
    }
};
```
Derived classes
```cpp
class Bus : public Vehicle<Bus>
{
public:
    explicit Bus(int value) : value_(value) {}
    double getNumberOfWheels() const {return value_;}
private:
    int value_;
};
```

```cpp
class Scooter : public Vehicle<Scooter>
{
public:
    double getNumberOfWheels() const {return 2;}
};
```