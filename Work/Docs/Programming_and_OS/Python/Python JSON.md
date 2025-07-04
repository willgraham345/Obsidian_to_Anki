---
tags: note/python
type: note
---
JSON = JavaScript object notation
```json
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
```

JSON supports primitive types like strings and numbers, as well as nested lists and objects
- Really similar to a python dictionary
- Python supports JSON natively 

Serialization = Encoding JSON through the transformation of data into a series of bytes to be stored or transmitted across a network. 
- Marshaling is also a term for this process
Deserialization = Decoding JSON into usable data


[[Python JSON.Serialization]]
[[Python JSON.Deserialization]]