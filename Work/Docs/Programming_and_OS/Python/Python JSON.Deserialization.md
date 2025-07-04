---
tags: note/python
type: note
---
# Usage
`json.load()`
- For files and objects
`json.loads()`
- For strings

## Example

```python
import json  
  
# some JSON:  
x =  '{ "name":"John", "age":30, "city":"New York"}'  
  
# parse x:  
y = json.loads(x)  
  
# the result is a Python dictionary:  
print(y["age"])
```


[More Examples](https://stackoverflow.com/questions/7771011/how-can-i-parse-read-and-use-json-in-python)