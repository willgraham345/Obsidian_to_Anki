---
summary: Way to enhance behavior of functions/methods without changing code. Essentially a wrapper for a function. Used for logging, access control, code instrumentation, and other stuff.
type: note/concept
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Flashcards]]", "[[#Media]]", "[[#Usage]]"]
functions: ["[[#@abstractmethod]]", "[[#@classmethod]]", "[[#@property]]", "[[#@setter_name.setter]]", "[[#@staticmethod]]", "[[Python Decorators#@abstractmethod]]"]
aliases: []
concept_of: ["[[Python OOP]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, January 22nd 2026, 2:45:39 pm
id: Python Decorators
implementations: ["[[Python classmethod]]", "[[Python dataclass]]"]
libraries: ["[[Python contextlib]]", "[[Python dataclass]]", "[[Python functools]]"]
tags: [lang/functions/decorators, lang/scope]
template: "[[base_note_template]]"
template-verison: 1.0.0
template-version:
used_by: ["[[Python OOP]]"]
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Instead of wrapping as `wrapper(func)` you write this as:
```python
def decorator(func):
	def wrapper(*args, **kwargs):
		#do something
		func(*args, **kwargs)
	return wraooer

@decorator 
def wrapee():
	# does something
```
- You typically want to have wrappers use `*args` and `**kwargs`. The wrapper must pass in all the arguments it would originally take into the function itself.

## Usage

  `@staticmethod` ;;; Add a decorator which does not receive implicit first argument of `self`, has no access to instance/class data, and is typically used for utility functions.
  `@property` ;;; Used to define a getter for a class attribute
  `@classmethod` ;;; Add a decorator which receives the class itself as the first argument, can access class data, and is often used for factory methods and class-level behavior (behavior belonging to the class, not the instance).

## Media

[Top 10 Python Built-In Decorators That Optimize Python Code Significantly \| GeeksforGeeks](https://www.geeksforgeeks.org/top-python-built-in-decorators-that-optimize-python-code-significantly/)

## Examples

### Methods
#### @staticmethod

- Used to define a static method in a class. Static methods are associated with the class rather than instances of the class. They can be called on the class itself without creating an instance.

```python
class MyClass:
    @staticmethod
    def my_static_method():
        # Static method code
```

#### @classmethod

- Used to define a class method. Class methods take the class itself as the first argument and are often used for alternative constructors or for modifying class-level attributes.

```python
class MyClass:
    class_variable = 10

    @classmethod
    def modify_class_variable(cls, value):
        cls.class_variable = value

```

#### @property

- Used to define a method as a "getter" for a class attribute. It allows you to access the method like an attribute, providing a more controlled way to access and possibly compute values based on attributes.

```python
class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value
```

#### @setter_name.setter

- Used in conjunction with @property, defines a method as a "setter" for a class attribute. It allows you to modify the attribute value using the assignment operator.

```python
class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

```

#### @abstractmethod

- Used in abstract base classes (ABCs) to declare abstract methods. Abstract methods must be implemented by subclasses. To use @abstractmethod, you need to import it from the abc module.

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

```

## Flashcards
󰠗  Does decorating a class decorate it's methods as well? ;; No, it does not.
