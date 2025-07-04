---
tags: note/python
type: note
---
# Background
We can auto-generate documentation from docstrings using `sphinx-apidoc` command.
- You'll need to uncomment the following lines at the top of the `conf.py`

## Things to do before invoking the build command
1. Make sure these commands are uncommented
```python
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
```
2. You can use `numpy` style documentation with the `sphinx.ext.napoleon`
```python
extensions = [
			 ...
			 'sphinx.ext.napoleon',
]
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar
```
- Those napoleon options disable the parsing of Google-style docstrings
- For more information on Napoleon configuration, see [[Python Sphinx.Extensions.Napoleon]]


# Usage
## Example Invocation
```shell
sphinx-apidoc -o ./source ../pkg_name
```
- Should be executed from the `docs/` folder
## Simple Example
```shell
youruser@yourpc:~yourWorkspacePath/simpleble-master/docs$ sphinx-apidoc -o ./source ../simpleble
Creating file ./source/simpleble.rst.
Creating file ./source/modules.rst.
```

