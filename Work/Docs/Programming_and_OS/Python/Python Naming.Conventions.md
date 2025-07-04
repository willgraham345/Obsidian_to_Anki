---
tags: note/python
type: note
---
# Coding Convention Standards
## In General
- Don't
	- Use names that are general or too wordy (i.e. `data_structure`, `my_list`, `info_map`)
## Class Names
- Class names should follow the `PascalCase` 
- This is separate for builtin names
```python
class ClassName():
	def __init__(self,):
```
## Variable Names
- Variable names should normally use `camelCase` convention. Start with a lowercase, end with uppercase
```python
variableName = "variable"
```
## Function Names
- Function names should be `lower_case`, with words separated by underscores as necessary
	- mixedCase is only allowed in contexts that's already the prevailing style
```python
def function_name():
	return
```
### Function and Method Arguments
- Always use cls for first argument to class methods (this is just a convention)
```python
class MyClass:
	classVariable = 10
	#A class method
	@classmethod
	def myMethod(cls):
		return cls.classVariable
```
- If a function argument's name clashes with a reserved keyword, its better to append a single trailing underscore to rather than use an abbreviation or spelling corruption.
## Constants
- Usually defined on a module level written in `CAPITAL`, and are written in all capital letters with underscores
```python
CONSTANT_NAME = "constant"
```

## Strings
Using single quotes for string literals 

```python
'my-identifier'
```

Use double-quotes for strings that are more likely to contain single-quote characters as part of the string itself
- Error messages, strings with natural language 
```python
"You've got an error!"
```

Rationale
- Single quotes are easier to read/type. 
- Use triple single quotes for docstrings


## Docstrings
### Numpy Dostrings
Based on google format, usable by Sphinx
```python
"""
My numpydoc description of a kind
of very exhautive numpydoc format docstring.

Parameters
----------
first : array_like
    the 1st param name `first`
second :
    the 2nd param
third : {'value', 'other'}, optional
    the 3rd param, by default 'value'

Returns
-------
string
    a value in a string

Raises
------
KeyError
    when a key error
OtherError
    when an other error
"""
```