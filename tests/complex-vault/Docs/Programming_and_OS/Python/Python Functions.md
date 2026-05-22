---
summary: First class objects (can be passed as arguments). You can store functions in variables, pass functions as parameters to other functions, return functions from other functions, store them in hash tables, lists, and all other data structures.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/concept
functions: ["[[Python dunder functions and methods]]"]
concepts: ["[[Python lambda]]"]
similar: ["[[Cpp functions]]"]
concept_of: ["[[Python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Saturday, December 6th 2025, 4:22:33 pm
tags: [lang/functions, lang/functions/variadic]
template:
template-version:
uses: ["[[Python asterisk]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- Keyword arguments cannot be declared before positional arguments.

### Args (`*`)
- Arbitrary number of arguments (`*args`) is used when you don't know how many arguments will be passed to your function
```python

def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   
```

### Kwargs (`**`)
- Keyword arguments `kwargs` are used when you don't know how many keyword arguments will be passed into your function.
```python
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)
```

### Typing function args
See [[Python typing#Define a generic fn args]] for more info

## Usage
  `def food(**kwargs)` ;;; Define a variable number of args within the `food` function that allows keyword arguments. =
  `def food(*args)` ;;; Define a variable number of args wtihin the `food` argument that does not support keyword naming/args. = 
  `def a(input: str | int | None ;;; None)` = Define fn `a` which takes in an input `input` which is either a `str`, `int`, or `None`. Make it default to `None` if nothing is provided. = 

## Examples
```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)

# HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
# hi, i am created by a function passed as an argument.
```
