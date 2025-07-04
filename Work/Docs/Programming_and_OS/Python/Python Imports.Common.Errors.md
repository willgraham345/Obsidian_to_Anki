---
tags: note/python
type: note
---
## Relative Imports


## `imp` Module
```python
import imp

# load a source module from a file
file, pathname, description = imp.find_module('my_module', ['/path/to/directory'])
my_module = imp.load_module('my_module', file, pathname, description)

```

# Common Issues
### ‘ModuleNotFoundError’

The most common issue you might run into is the ‘ModuleNotFoundError’. This error occurs when Python can’t find the module you’re trying to import. Here’s an example:

```python
# trying to import a non-existent module
import non_existent_module
```

Python

Running this code would result in the following output:

```python
# Output
ModuleNotFoundError: No module named 'non_existent_module'
```

Python

This error typically means that Python can’t find your module in the directories listed in `sys.path`. To fix this, you can add the directory containing your module to `sys.path` using `sys.path.append()` as we discussed earlier.

### Dealing with Relative Import Issues
```python
# Output
ImportError: attempted relative import with no known parent package
```

Python

This error means that Python doesn’t know what the parent package of your current module is. To fix this, make sure that your script is part of a package (i.e., it’s inside a directory that contains an `__init__.py` file), and that you’re running your script using the `-m` option.

For example, if your script is named `main.py`, you should run it like this: `python -m main`