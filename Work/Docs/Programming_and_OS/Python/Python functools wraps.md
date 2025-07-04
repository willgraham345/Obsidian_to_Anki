---
summary: Wraps is a decorateor applied to the wrapper function of a decorator. Updates the wrapper to look like a wrapped function by copying attributes.
headings: 
type: 
date created: Wednesday, April 23rd 2025, 1:01:33 pm
date modified: Wednesday, April 23rd 2025, 1:03:53 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Examples
```python
def a_decorator(func):
	def wrapper(*args, **kwargs):
		"""A wrapper function"""
		# Extend some capabilities of func
		func()
	wrapper.__name__ = func.__name__
	wrapper.__doc__ = func.__doc__
	return wrapper

@a_decorator
def first_function():
	"""This is docstring for first function"""
	print("first function")

@a_decorator
def second_function(a):
	"""This is docstring for second function"""
	print("second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

"""
Prints:
first_function
This is docstring for first function
second_function
This is docstring for second function
"""
```
