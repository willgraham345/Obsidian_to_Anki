---
tags: note/python
type: note
---
## `ascii()`
Returns a string containing a printable representation of an object and escapes non-ASCII in string using `\x` `\u` or `\U` escapes
### Syntax
```python
string_printable_representation_of_object = ascii(object)
```
#### Example
```python3
print(ascii("¥"))
```
- output: `\xa5`
## `callable()`
Checks if an object is callable, and returns a boolean
```python3
# Python program to illustrate 
# callable() a test function
def Geek():
    return 5
 
# an object is created of Geek()
let = Geek
print(callable(let))
 
# a test variable
num = 5 * 5
print(callable(num))
```


