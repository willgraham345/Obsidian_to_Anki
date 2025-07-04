---
type: note
headings:
  - "[[#File Structure]]"
concept_of:
  - "[[Python Package Managers]]"
  - "[[Python Packages]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, February 25th 2025, 4:43:03 pm
tags:
  - note/python
---
# Background
- Package manager that combines dependency management and project packaging. 
	- Used to develop applications and libraries
- Not multi-platform

# Usage
## File Structure
Poetry is organized as such...
`projectName`
- `dist/`
- `src/`
	- `projectName/`
		- `__init__.py`
		- `module1.py` (can also be named `projectName`)
- `tests/`
- `__init__.py`
- `poetry.lock`
- `pyproject.toml`
- `main.py` (optional, I like this way of doing it)


| folder           | explanation                                                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dist`/          | Created by a `poetry build` command, which creates the `.whl` and `.tar` files that would be useful if you wanted to upload this to be installed by others                                |
| `src`/           | Source code                                                                                                                                                                               |
| `module1`        | Where you'd put one component of the project. Likely named after the project itself...                                                                                                    |
| `tests/`         | Tests                                                                                                                                                                                     |
| `__init__.py`    | Used to let python know the folder is a module, doesn't need to be filled                                                                                                                 |
| `pyproject.toml` | Used to manage dependencies and explain more about the project. Use `poetry add` to manage the dependencies here. Needs a couple of fields, but is easiest to manage via the command line |
| `main.py`        | I usually have this set up since I like this structure. Imports are a little bit weird (`from src.projectName.module1`). Still, nice to execute it this way.                              |
