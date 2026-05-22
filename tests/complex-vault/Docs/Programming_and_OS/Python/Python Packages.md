---
summary: A type of python module--Python packages come in two formats, (source distributions/wheels). Both are archive files.
headings:
  - "[[#Usage]]"
type: note/library
associations:
  - "[[Python folder structure]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, November 12th 2025, 5:58:31 pm
item_of:
  - "[[Python Scoping Rules]]"
keywords:
  - "[[Python import]]"
tags: []
template:
template-version:
uses:
  - "[[Python Package Managers]]"
  - "[[Python importlib]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[5. The import system — Python 3.14.0 documentation](https://docs.python.org/3/reference/import.html#package-path-rules)

## Concepts of Note
Two formats:
1. A built form (wheel)
2. Source distributions (sdist)
- Both are archives

### Wheel
- Compatible with any python version, interpreter (cpython and pypy), OS, and hardware architecture. Can be limited to a specific platform/architecture or a specific platform
	- [[Python pip]] `install` tries to find a matching wheel and install that. If it doesn't find one, it downloads source distribution and builds a wheel for the current platform which requires the right compilers to be installed. 

### Source distribution 
- A distribution that still needs to be “built” to be used. 
- Available as `*.tar.gz` files (tarballs)
- This is not the default option, as pip likes to install built distributions. 
	- Can be specified with the `—-no-binary` option
	- Takes more time
- When installing from source, it first builds the built distribution (wheels) before installing. 

### Virtual Environment Structure
- bin/ — contains scripts (activate, custom scripts etc) and commands (python, pip etc)
- lib/ —mainly contains the installed python packages and information about them
- pyvenv.cfg — some configurations
Also see [[Python Rust.project.structure]]

### Typical Package structure
```
README.rst
LICENSE
setup.py
requirements.txt
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

## Usage

See [[Python Package Managers#Usage]] and [[Python poetry]]

### Installing Packages from a Requirements File
```
pip install -r requirements.txt
```

### Maintenance
```
pip list --outdated
```
- Outputs a list of outdated packages
