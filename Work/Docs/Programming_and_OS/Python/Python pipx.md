---
tags: note/python
type: note
---
# Background
- Specialized package installer, that can *only* be used to install packages with cli entrypoints
- Relies on [[Python pip]] and [[Python venv]]
- Used solely for application consumption
	
[Docs](https://pipx.pypa.io/stable/)

# Usage
## Install pipx
```shell
pip install --user pipx
```

## Install a CLI tool with pipx
```shell
pipx install <package-name>
pipx uninstall <package-name>
```

## View installed Packages
```shell
pipx list
```