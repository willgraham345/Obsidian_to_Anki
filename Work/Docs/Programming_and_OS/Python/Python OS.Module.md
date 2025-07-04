---
tags: note/python
type: note
---
# Background
The Python OS module provides functions for interacting with the operating system. This comes under Python's standard utility modules. 

## `os.environ`
- A Python mapping object that represents the user's environment variables. 
- Returns a dictionary having the user's environmental variable as a key, and values as values
	- Behaves like a python dictionary, so common dictionary operations like `.get()` and `.set()` can be performed. 
	- We can modi

### Example usage of `os.environ` object
```python
# Python program to explain os.environ object  
  
# importing os module  
import os 
import pprint 
  
# Get the list of user's 
# environment variables 
env_var = os.environ 
  
# Print the list of user's 
# environment variables 
print("User's Environment variable:") 
pprint.pprint(dict(env_var), width = 1) 
```

```
```