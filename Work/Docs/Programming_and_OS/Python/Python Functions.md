---
summary: First class objects (can be passed as arguments). You can store functions in variables, pass functions as parameters to other functions, return functions from other functions, store them in hash tables, lists, and all other data structures.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
similar: ["[[Cpp Functions]]"]
concept_of: ["[[Python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, April 28th 2025, 10:23:04 am
tags: [note/python]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
### Args and Kwargs
- Arbitrary number of arguments (`*args`) is used when you don't know how many arguments will be passed to your function
- Keyword arguments `kwargs` are used when you don't know how many keyword arguments will be passed into your function.

```python
def my_function(*kids):  
  print("The youngest child is " + kids[2])  
my_function("Emil", "Tobias", "Linus")

def my_function(**kids): # Could also be written my_function(**kwargs):
	print("His name is " + kid["lname"])
my_function(fname="Tobias", lname="Refsnes")
```

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

```
HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
hi, i am created by a function passed as an argument.