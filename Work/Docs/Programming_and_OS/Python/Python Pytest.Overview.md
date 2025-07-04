---
tags: note/python
type: note
---
# Background
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

# Running Pytest
## Different invocations
### `python -m pytest`
- Explicitly specifying which python interpreter to use for running your test. 
- Can be useful in complex environments or when working with multiple Python versions.

### `pytest`
- Most straightforward way, direct call to the pytest test runner
- Usually works, but requires the pytest package being installed on your Python environment's PATH

## Everything in a Directory
To run all the tests fro all the folders in the folder and subfolders, we need to run the command:
```bash
py.test
```
- This will run all filenames starting with `test_` and all the filenames ending with `_test` in that folder and subfolders under that folder

## Subset of an Entire Test with Pytest
We can run specific tests either by:
- Grouping test names by substring matching
- Grouping of tests by markers
### Substring Matching
```bash
py.test -k <substring_matching_keyword> -v
```
- k flag is substring, v flag is verbosity
### Markers
Pytest lets us set various attributes for the test methods using pytest markers `@pytest.mark`. This means we'll need to import pytest on the test files
```python3
@pytest.mark.<name>
```
#### Marker Example
```python3
import pytest
@pytest.mark.set1
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"
```

