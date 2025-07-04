---
tags: note/python
type: note
---
# Background
A way to keep track of our python modules and packages 

# Usage
## How to Create
```
pip freeze > requirements.txt
```
- Outputs a list of all installed Python modules with their versions

## Installing Packages from a Requirements File
```
pip install -r requirements.txt
```

## Maintenance
```
pip list --outdated
```
- Outputs a list of outdated packages