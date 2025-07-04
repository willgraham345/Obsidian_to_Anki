---
tags: note/python
type: note
---
# Background


# Usage
## Edit conf.py
```python
sys.path.append(os.path.abspath("./_ext"))
extensions = [
	  'extname',
	  'sphinx.ext.todo',
]
todo_include_todos = True #if false, it defaults to removing all todo and todolist nodes
extensions = ['todo']
```

## Usage in rst
Built on top of [[Python Sphinx autodoc]], so won't work if that isn't enabled. 
Syntax is indent sensitive

```rst
.. todo:: This comment will appear
.. todo::
This comment is ignored because of bad indentation and you get a warning
.. todo::
   This is the correct indentation and this todo will appear.
```

## Commenting in Docstrings
Supported by [[Python Sphinx.Extensions.Napoleon#Docstring Sections]]