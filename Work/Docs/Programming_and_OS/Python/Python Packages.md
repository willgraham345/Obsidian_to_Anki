---
type: note
concepts: ["[[Python Package Managers]]", "[[Python venv]]"]
functions: ["[[Python Import]]"]
associations: ["[[Python folder structure]]"]
concept_of: ["[[Python|#note/python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, February 24th 2025, 11:34:39 am
tags: [note/python]
---
# Background
- There is a centralized catalogue of Python packages at [PyPI](pypi.org). 
- Python packages come in two formats:

## Basics
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

# Usage