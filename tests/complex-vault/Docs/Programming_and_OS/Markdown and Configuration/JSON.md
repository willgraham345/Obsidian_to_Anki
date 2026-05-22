---
summary: Javascript object notation, which supports defining primitive types as well as nested lists and objects. Similar to other markup langauges. Can also be used as a serialization framework to define how your data is encoded into bytes.
headings:
  - "[[#Examples]]"
  - "[[#Concepts of Note]]"
type: note/system
processes:
  - "[[Python JSON.Deserialization]]"
  - "[[Python JSON.Serialization]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, November 5th 2025, 11:25:56 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
items:
  - "[[JSON Schema]]"
implements:
  - "[[CS Document Object Model]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note


## Examples


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
