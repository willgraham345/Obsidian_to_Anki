---
type: note/item
headings:
  - "[[#Usage]]"
  - "[[#Examples]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, March 4th 2026, 3:11:43 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
item_of:
  - "[[Python pytest]]"
---

# Summary
󰙎 Python pytest markernames ;;; Decoratorr used to help group tests within a file.

# Additional Background
- To use markers, we have to import pytest module in the testfile. We can define our own marker names to run the tests having those marker names

## Usage
 `@pytest.mark.<markername>` ;;; Marks a pytest python method as `<markername>`

 `pytest -m marky -v` ;;; Run pytest markername `marky` from cli

## Examples

```python
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

