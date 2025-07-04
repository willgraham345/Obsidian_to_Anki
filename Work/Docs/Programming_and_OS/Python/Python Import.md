---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, February 24th 2025, 11:34:57 am
function_of: ["[[Python Basics]]", "[[Python folder structure]]", "[[Python Packages]]"]
tags: [note/python]
---
# Modules in Python
Python modules are `.py` that contain python code. Modules are used to group related code together

Packages/modules are defined with a `__init__.py` file.

## Python Module Search Path
Does the following search
1. Current directory
2. Build-in module list
3. Inside `sys.path` directories


|Method|Advantages|Disadvantages|
|---|---|---|
|`sys.path.append()`|Simple and straightforward|Changes are session-specific|
|`os.chdir()`|Changes are permanent for the session|Can have side effects in multithreaded code|
|Relative imports|Useful for complex directory structures|Can be confusing if overused|
|`imp` module|Provides low-level import functions|More complex than other methods|
|`importlib` module|Allows programmatic imports|Requires the module name as a string|

# Usage
## Basic
```python
import [module]
from [module] import [function or value]
```

### Relative Imports
```python
# Suppose you have the following directory structure:
#
# my_project/
# ├── main.py
# └── my_module/
#     └── sub_module.py

# You can use a relative import in main.py to import sub_module.py like this:
from .my_module import sub_module

```

### Another File
```python
from file import classA
from file import functionA
```

### Another Directory
```python
import sys

# print the original sys.path
print('Original sys.path:', sys.path)

# append a new directory to sys.path
sys.path.append('/path/to/directory')

# print the updated sys.path
print('Updated sys.path:', sys.path)

# now you can import your module
import your_module
```

## Aliasing
```python
import [module] as [x]
x.function()
```

## Advanced usage
## Misc
### Dir function
Returns all properties and methods present within a module
```python
import json
json_details = dir(json)
print(json_details)
```


