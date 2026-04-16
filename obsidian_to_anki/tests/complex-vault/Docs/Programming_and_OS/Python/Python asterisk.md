---
summary: "Python prefix operator which is used for packing, unpacking, and widely within functions. "
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/keyword
date created: Tuesday, November 18th 2025, 5:00:59 pm
date modified: Tuesday, November 18th 2025, 5:31:36 pm
template: "[[base_note_template]]"
template-version: 1.0.0
used_by: ["[[Python Functions]]", "[[Python typing]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
args (`*`)
- The `*` operator lets us pack or unpack all items in a particular iterable as separate arguments.
kwargs (`*`)
- The `**` operator lets us take a dictionary of key-value pairs and pack/unpack it into keyword arguments in a function call.
	- Functions in python can't have the same keyword arg specified multiple times, so the keys must be distinct here.

### Unpacking containers
- `*` can also be used to unpack containers. As of 2025-11-18, I think about this as a separate thing than args/kwargs.
- This just pulls out the rest of the iterable

## Examples
### Unpacking *into* a function call
```python
>>> print(fruits[0], fruits[1], fruits[2], fruits[3])
lemon pear watermelon tomato
>>> print(*fruits)
lemon pear watermelon tomato
```

### Unpacking keyword arguments *into* a function call
```python
def myfunc(a, b, c):
	print(a, b, c)

mydict = {'a': 1, 'b': 2, 'c': 3}  
myfunc(**mydict)
```

```python
>>> date_info = {'year': "2020", 'month': "01", 'day': "01"}
>>> filename = "{year}-{month}-{day}.txt".format(**date_info)
>>> filename
'2020-01-01.txt'
```

### Unpacking containers *within* a function call
```python
def product(*numbers):
	# each element is unpacked into store called numbers,
	p = reduce(lambda x, y: x * y, numbers)

primes = [2, 3, 5, 7, 11, 13]
product(*primes)	

```
