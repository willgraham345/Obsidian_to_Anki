---
tags: note/python
type: note
---
## Instance Method
- An instance method is a function defined inside of a class. It varies with the different instances of the class.
```python
class Dog:
    def __init__(self, sound):
        self.sound = sound
    def bark(self):
        return f"The dog makes the sound: {self.sound}"
```

## Class Method
- A class method applies to ALL instances of the class, with the passing of instance hidden as a first parameter
	- In the example below, we're only passing a class to the method, so no instance is involved. We can call the class method as if it was a static function.
```python
class Cls:
    @classmethod
    def introduce(cls):
        print("Hello, I am %s!" %cls)
```

```python
 Cls.introduce() # same as Cls.introduce(Cls)
 # outputs: Hello, I am <class 'Cls'>
```

```python
class SubCls(Cls):
    pass

SubCls.introduce()
# outputs: Hello, I am <class 'SubCls'>
```