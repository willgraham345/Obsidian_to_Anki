---
summary:
type: note/process
headings:
  - "[[#Concepts of Note]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, February 11th 2026, 1:23:22 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

invoke using the above command in the right directory. 
- Executes all tests in all files whose names follow the form `test_*.py` or `\*_test.py` in the current directory and its subdirectories

### Discovery Rules
If no arguments are specified, then the collection starts from [testpaths](https://docs.pytest.org/en/7.2.x/reference/reference.html#confval-testpaths) (if it is configured), or the current directory. 
- CLI arguments can be used in any combination of directories, file names or node ids.
- Recurse into directories, unless they match [norecursedirs](https://docs.pytest.org/en/7.2.x/reference/reference.html#confval-norecursedirs)

In those directories, search for `test_*.py` or `*_test.py` files imported by their test package name

From those files, collect test items:
- `test` prefixed test functions or methods outside of class
- `tst` prefixed test functions or methods inside `Test` prefixed test classes (without an `__init__` method)

### Test Layouts
#### Layout 1
Putting tests outside actually application code
```
pyproject.toml
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
    ...
```
- Your tests can run against an installed version after executing `pip install ..`
- Your tests can run against the local copy with an editable install after executing `pip install --editable ..`
