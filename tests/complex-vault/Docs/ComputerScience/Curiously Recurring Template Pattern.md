---
summary: Idiom where class X derives from class template Y, taking template parameter Z, where Y is instantiated with Z = X. Provides a way for base classes to use methods of derived classes during compile time.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
similar:
  - "[[Template Method]]"
aliases: [Crtp]
concept_of:
  - "[[Behavioral Patterns]]"
  - "[[DP Creational Patterns]]"
date created: Friday, September 13th 2024, 12:03:47 pm
date modified: Thursday, February 26th 2026, 10:34:12 am
diagrams:
  - "[[crtp.puml]]"
images:
  - "[[crtp.svg]]"
implementations:
  - "[[Cpp Curiously Recurring Template Pattern]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
󰙎 Curiously Recurring Template Pattern ;; Idiom where class X derives from class template Y, taking template parameter Z, where Y is instantiated with Z = X. Provides a way for base classes to use methods of derived classes during compile time, and add functionality *through* the base class. 

# Additional Background
## Concepts of Note
Derived classes are template specializations for the base class. 

### Pros/Cons
- Pros:
	- The base class has access to the derived class's members
- Cons:
	- Odd
	- Hard to implement


[The Curiously Recurring Template Pattern (CRTP) - DEV Community](https://dev.to/sandordargo/the-curiously-recurring-template-pattern-crtp-46j7)

A base class exposes an interface, and derived classes implement the interface. 

## Usage

## Examples
```cpp
template<class X>
class Base {
	void foo() {
		X& underlying = static_cast<X&>(*this);
	}
};
```
- You can now access the derived class (`X`) with a static cast. 

### C++ static polymorphism
Base class
```cpp
// Base class
template <typename T>
class Vehicle
{
	public:
		double getNumberOfWheels() const
		{
			return static_cast<T const&>(*this).getNumberOfWheels();
		}
};

//Derived classes
class Bus : public Vehicle<Bus>
{
	public:
		explicit Bus(int value) : value_(value) {}
		double getNumberOfWheels() const {return value_;}
	private:
		value_;
};
class Scooter : public Vehicle<Scooter>

```

## Diagrams
![[crtp.svg]]
