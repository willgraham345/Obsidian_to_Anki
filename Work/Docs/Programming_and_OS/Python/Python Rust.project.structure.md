---
tags: note/python
type: note
---
# Background
Use [[Python maturin]] to create

## Structure
```
my-project
├── Cargo.toml
├── my_project
│   ├── __init__.py
│   └── bar.py
├── pyproject.toml
├── README.md
└── src
    └── lib.rs
```
1. Create a folder with your module name (`lib.name` in `Cargo.toml`) next to Cargo.toml, and add python sources there

### Changing folder directory
Specify different python source directory in `pyproject.toml` by setting `tool.maturin.python-source`
**`pyproject.toml`**
```
[tool.maturin]
python-source = "python"
module-name = "my_project._lib_name"
```
Project structure after:
```
my-project
├── Cargo.toml
├── python
│   └── my_project
│       ├── __init__.py
│       └── bar.py
├── pyproject.toml
├── README.md
└── src
    └── lib.rs
```

# Usage
## Examples
See [Examples section at bottom](https://www.maturin.rs/)