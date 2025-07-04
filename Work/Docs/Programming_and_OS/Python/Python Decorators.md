---
summary: Way to enhance behavior of functions/methods without changing code. Essentially a wrapper for a function. Used for logging, access control, code instrumentation, and other stuff.
headings:
  - "[[#Media]]"
  - "[[#Usage]]"
  - "[[#Examples]]"
type: note/concept
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, April 23rd 2025, 12:56:55 pm
tags:
  - code/python/functions/decorators
  - note/python
libraries:
  - "[[Python functools]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Usage
- [p] `@staticmethod` = Define a static method of a class (method is part of class, not instance). = #code/python/functions/decorators
<!--ID: 1751434090724-->

- [p] `@property` = Used to define a getter for a class attribute = #code/python/functions/decorators 
<!--ID: 1751434090727-->

- [p] `@classmethod` = Used to define a class method (which takes the first argument as a class), used often for alternative constructors or modifying class-level attributes = #code/python/functions/decorators 
<!--ID: 1751434090731-->


## Media
[Top 10 Python Built-In Decorators That Optimize Python Code Significantly \| GeeksforGeeks](https://www.geeksforgeeks.org/top-python-built-in-decorators-that-optimize-python-code-significantly/)

## Examples
### @staticmethod
- Used to define a static method in a class. Static methods are associated with the class rather than instances of the class. They can be called on the class itself without creating an instance.
```python
class MyClass:
    @staticmethod
    def my_static_method():
        # Static method code
```
    

### @classmethod
- Used to define a class method. Class methods take the class itself as the first argument and are often used for alternative constructors or for modifying class-level attributes.
```python
class MyClass:
    class_variable = 10

    @classmethod
    def modify_class_variable(cls, value):
        cls.class_variable = value

```

### @property
- Used to define a method as a "getter" for a class attribute. It allows you to access the method like an attribute, providing a more controlled way to access and possibly compute values based on attributes.
```python
class MyClass:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value
```
    

### @setter_name.setter
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

### @abstractmethod
- Used in abstract base classes (ABCs) to declare abstract methods. Abstract methods must be implemented by subclasses. To use @abstractmethod, you need to import it from the abc module.
```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

```