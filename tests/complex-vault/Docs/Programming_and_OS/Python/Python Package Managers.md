---
summary: Dependency manager, works really well with docker if you get it set up.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/item
date created: Thursday, February 6th 2025, 11:29:14 am
date modified: Tuesday, November 11th 2025, 2:29:57 pm
function_of:
  - "[[Docker]]"
template:
template-version:
tools:
  - "[[Python conda]]"
  - "[[Python pip]]"
  - "[[Python pipx]]"
  - "[[Python poetry]]"
  - "[[Python uv]]"
  - "[[Python venv]]"
used_by:
  - "[[Docker]]"
  - "[[Python Scoping Rules]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
- [What does the structure of a modern Python project look like? - YouTube](https://www.youtube.com/watch?v=Lr1koR-YkMw)
- [Docker python poetry](https://www.baeldung.com/ops/docker-python-poetry)

## Usage
### pip

  `pip freeze > requirements.txt` ;;; Writes a requirements file for pip to read from later = #lang/scope/packages  #tools/python/pip
  `pip install -r requirements.txt` ;;; Installs requirements from a requirements file in pip = #lang/scope/packages #tools/python/pip

### poetry
See [[Python poetry]]

### uv
See [[Python uv]]
  `source .venv/bin/activate` ;;; Activate a uv environment. = #tools/python/uv
  `deactivate` ;;; Deactivate a uv environment. = #tools/python/uv
  `uv venv` ;;; Creates a uv virtual environment. = #tools/python/uv
  `uv venv` ;;; Creates and initializes a uv virtual project. = #tools/python/uv
