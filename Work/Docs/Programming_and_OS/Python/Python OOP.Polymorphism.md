---
tags: note/python
type: note
---
# Background
[[PT OOP Polymorphism]]

# Usage
## Class Method
```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
```
## Method Overloading
### Inheritance with Method Overriding
```python
class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Creating instances of different classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method on different objects
animal.speak()  # Output: This animal makes a sound
dog.speak()     # Output: Woof!
cat.speak()     # Output: Meow!
```

### Default Parameter Values
```python
class Calculator:
    def add(self, a, b=0):
        return a + b

# Creating an instance of the Calculator class
calc = Calculator()

# Calling the add method with different numbers of arguments
print(calc.add(5, 3))   # Output: 8
print(calc.add(5))      # Output: 5 (default value of b is used)

```
### Keyword Arguments
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the print_info function with different keyword arguments
print_info(name="Alice", age=30)                 # Output: name: Alice \n age: 30
print_info(name="Bob", age=25, city="New York")  # Output: name: Bob \n age: 25 \n city: New York
```
### Variable Arguments
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the sum_numbers function with different numbers of arguments
print(sum_numbers(1, 2, 3))          # Output: 6
print(sum_numbers(1, 2, 3, 4, 5))    # Output: 15
```