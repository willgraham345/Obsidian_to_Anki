---
summary:
type: note/concept
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
concepts: ["[[Python classmethod]]", "[[Python Decorators]]", "[[Python dunder members]]", "[[Python Method Resolution Order]]", "[[Python OOP Polymorphism]]"]
concept_of: ["[[Python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, December 16th 2025, 12:22:48 pm
items: ["[[Python dunder functions and methods]]", "[[Python dunder members]]"]
tags: [lang/oop, lang/oop/class, lang/oop/class/methods/dunder, todo/refactor]
template: "[[base_note_template]]"
template-version: 1.0.0
uses: ["[[Python Decorators]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Python provides several built-in methods that are always available.
- Specifying types for variables within a class
󰙎  Instance method ;;; Method that refers to an instance of the class, rather than the class as whole. Think of this as the opposite of a classmethod. = 

󰙎  Dunder method ;;; Method in Python that modifies one of the built in functions that Python keeps in global scope. = 

## Examples

```python
class Projectile(Sprite):
	def __init__(self,
		centerx: int,
		y: int,
		direction: str,
		data_dir: str,
		projectile_type: str) -> None:
	def mark_for_deletion(self) -> None:
		"""Mark the laser for deletion"""
		self.is_alive = False
```

## Usage
  `class definition` ;;; Defining a class in python (example in link) =  
ID: 1751997628626


  `c.__call__()` ;;; Built-in method in python that enables programmers to write class `c` where instances behave like functions and can be called like functions. When defined, `(c(arg1, arg2))` automatically triggers this method. = 


  `c.__self__` ;;; Built-in instance method to refer to an instance of class `c`, to which the method is bound. = 
  `c.__func__` ;;; Built-in instance method to refer to the function object of class `c`. = 
  `c.__name__` ;;; Built-in instance method to refer to the name of the method of class `c`. = 
  `c.__module__` ;;; Built-in instance method to refer to the name of the module where `c` was defined in. `None` if this is unavailable. = 

[3. Data model — Python 3.14.0 documentation](https://docs.python.org/3/reference/datamodel.html#method.__self__)  
- Add `__next__()`
- Add `async def()`
- Add `__anext__()`
