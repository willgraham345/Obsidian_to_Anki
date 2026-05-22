---
summary:
type: note/library
headings:
  - "[[#Usage]]"
concepts:
  - "[[Python pytest parameterizing]]"
  - "[[Python pytest monkeypatch]]"
processes:
  - "[[Python pytest Running Tests Cheatsheet]]"
  - "[[Python pytest running tests]]"
prev:
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, March 4th 2026, 3:15:17 pm
items:
  - "[[Python pytest assertions]]"
  - "[[Python pytest fixtures]]"
  - "[[Python pytest markernames]]"
  - "[[Python pytest monkeypatch]]"
library_of:
  - "[[Python]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.1
associations:
  - "[[Python unittest]]"
libraries:
  - "[[Python pytest-mock]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- Pytest is a framework that makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. 
	- Requires Python 3.7+ or PyPy3
- Capabilities
	- Parallel running of multiple tests
	- Own way of detecting the test file and testing functions automatically
	- Allows us to skip a subset of the tests during execution
	- Allows us to run a subset of the entire test suite
	- Automatically captures standard output and prints to terminal.
	- Easy syntax

## Less Boilerplate
- Most tests follow the Arrange-Act-Assert model:
1. Arrange: set up the conditions for the test
2. Act: call some function or method
3. Assert: some end condition is true

## Naming Files
All files will have a format of `test_*.py` or `*_test.py`
- We can also have other files if we specifically mention them.. 

## Usage


### Different invocations
### `python -m pytest`
- Explicitly specifying which python interpreter to use for running your test. 
- Can be useful in complex environments or when working with multiple Python versions.

### `pytest`
- Most straightforward way, direct call to the pytest test runner
- Usually works, but requires the pytest package being installed on your Python environment's PATH

### Everything in a Directory
To run all the tests fro all the folders in the folder and subfolders, we need to run the command:
```bash
py.test
```
- This will run all filenames starting with `test_` and all the filenames ending with `_test` in that folder and subfolders under that folder

### Subset of an Entire Test with Pytest
We can run specific tests either by:
- Grouping test names by substring matching
- Grouping of tests by [[Python pytest markernames]]

#### Substring Matching
```bash
py.test -k <substring_matching_keyword> -v
```
- k flag is substring, v flag is verbosity
