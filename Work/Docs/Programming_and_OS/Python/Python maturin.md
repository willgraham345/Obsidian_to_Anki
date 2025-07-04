---
tags: note/python
type: note
---
# Background
- Builds and publishes crates with pyo3, cffi, and uniffi bindings
	- Also does rust binaries as python packages with minimal configuration

# Usage
4 main commands
1. `maturin new`: Creates new cargo project with maturin configured
2. `maturin publish`: Builds the crate into python packages and publishes them to pypi
3. `maturin build`: Builds wheels and stores them in a folder (`target/wheels` default) without uploading them. 
4. `maturin develop`: Builds the crate and installs it as a python module directly in the current virtual environment

`pyo3` bindings are automatically detected