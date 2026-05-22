---
summary: Similar to a for loop, but will iterate over an object. Keeps track of iterations, and is a built-in function adding a counter to an iterable. Will return in the form of an enumerating object.
headings: ["[[#Syntax]]"]
type: note/keyword
similar: ["[[Python for loop]]"]
date created: Monday, February 24th 2025, 11:59:22 am
date modified: Wednesday, November 19th 2025, 11:21:07 am
item_of: ["[[Python Control Flow]]"]
template:
template-version:
uses: ["[[Python Iterable]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
- Keeps track of the iterations. This is a built-in function that adds a counter to an interable and returns it in the form of an enumerating object. 
	- This enumerating object can be used directly for loops or converted into a list of tuples using the `list()` function. 
```python
enumerate(interable, start = 0)
# or
for count, element in enumerate(<iterable>):
	<action>
```
- `iterable` = any object that supports iteration
- `start` = index value from which the is to be started. 

### Example
```python
l1 = ["eat", "sleep", "repeat"]
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')
```
```python
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)
```
