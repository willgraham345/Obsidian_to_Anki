---
tags: note/python
type: note
---
# Background
Helpful feature that lets us set up and tear down resources or test data. 
- Can provide modularity and a common way to setup and tear-down logic across multiple tests
- Used when we want to run code before every test method. 
	- Usually used to initialize database connections, base the base, etc

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
