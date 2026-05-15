---
summary:
type: note/item
headings:
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, March 5th 2026, 11:18:25 am
items:
  - "[[Python pytest.Conftest.py]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python pytest fixtures ;;; Provides a modular way to setup and tear-down test data across multiple tests.

# Additional Background

When pytest runs a test, it looks at the parameters in that function's signatures, then searches for fixtures that have the same names as the signatures. 
- Once pytest finds the fixtures, it runs those fixtures and pass those objects into the test function as arguments. 

## Fixture Properties
- They can request other fixtures

# Usage
## Defining Fixtures
```python
import pytest

@pytest.fixture
def setup_example():
    # Setup code
    yield "some setup data"
    # Teardown code (optional)

```

## Using Fixtures in Test Functions
```python
def test_example(setup_example):
    # Use the fixture value in the test
    assert setup_example == "some setup data"
```

## Fixture Scope
```python
@pytest.fixture(scope="module")
def setup_example_module():
    # Setup code
    yield "some setup data"
    # Teardown code (executed once per module)

```

## Fixture finalizaton
```python
@pytest.fixture
def setup_teardown_example():
    # Setup code
    yield "some setup data"
    # Teardown code

```

## Fixture Dependencies 
```python
@pytest.fixture
def dependency_fixture():
    return "dependency data"

@pytest.fixture
def setup_example_with_dependency(setup_example, dependency_fixture):
    # Use the values from both fixtures
    return f"{setup_example} - {dependency_fixture}"

```
