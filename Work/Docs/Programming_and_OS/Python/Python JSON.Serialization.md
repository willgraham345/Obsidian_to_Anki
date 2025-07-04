---
tags: note/python
type: note
---
# Usage
```python
json.dumps(data, file_pointer, indent=4)
```
- data = name of dictionary which should be converted to a JSON object
- File pointer = pointer of the file opened in write or append mode

## Example
- Can be used for writing to a JSON file. Write data to a file-like object in json format
```python
import json

# data to be written
data = {
	“user”: {
		“name”: “satya kumar”,
		“age”: 21,
		“Place”: “Patna”,
		“Blood group”: “O+”
	}
}

# Serializinig json and writing JSON filE
with open(“datafile.json”, “w”) as write:
	json.dump(data, write)
```

### OUTPUT
```
{“user”: {“name”: “satyam kumar”, “age”: 21, “Place”: “Patna”, “Blood group”: “O+”}}
```