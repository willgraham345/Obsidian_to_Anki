---
tags: note/python
type: note
---
# Background
Specified file format in [PEP 518](https://peps.python.org/pep-0518/) which specifies how python software packages should specify what build dependencies they have in order to execute their chosen build system. 
- History
	- distutils
	- setuptools
	- Both used the `setup.py` file that project maintainers executed to build distributions of their software.
		- This is an issue, because you can't execute a `setup.py` without knowing its dependencies. 


# Usage
## Running a `pyproject.toml`
```shell
python -m pip install .
```