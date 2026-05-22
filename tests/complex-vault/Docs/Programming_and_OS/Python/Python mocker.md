---
type:
headings:
  - "[[#Examples]]"
  - "[[#Properties]]"
methods:
  - "[[Python mocker#mocker.patch.dict]]"
  - "[[Python mocker#mocker.patch.multiple]]"
  - "[[Python mocker#mocker.patch.object]]"
  - "[[Python mocker#mocker.patch.stop]]"
  - "[[Python mocker#mocker.patch.stopall]]"
  - "[[Python mocker#mocker.patch]]"
class_of:
  - "[[Python pytest-mock]]"
date created: Wednesday, March 4th 2026, 3:51:36 pm
date modified: Wednesday, March 4th 2026, 3:58:43 pm
item_of:
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Python mocker ;;; 

# Additional Background
## Properties
##### mocker.patch
󰡱 :
- description: Patch a function or a method
- args:
- calls:
󰡱 end:

##### mocker.patch.object
󰡱 :
- description: Patch a method of an object
- args:
- calls:
󰡱 end:

##### mocker.patch.multiple
󰡱 :
- description: Patch multiple functions or methods of an object
- args:
- calls:
󰡱 end:

##### mocker.patch.dict
󰡱 :
- description: Patch a dictionary
- args:
- calls:
󰡱 end:

##### mocker.patch.stopall
󰡱 :
- description: Stop all patches
- args:
- calls:
󰡱 end:

##### mocker.patch.stop
󰡱 :
- description: Stop a specific patches
- args:
- calls:
󰡱 end:

## Examples
### Mocking a function
```python
# mock_examples/area.py
PI = 3.14159

def area_of_circle(radius: float) -> float:
	"""
	Function to calculate area of a circle
	:param radius: Radius of the circle
	:return: Area of the circle
	"""
	return PI * radius * radius

# In test function
from mock_examples.area import area_of_circle
def test_area_of_circle():  
	"""  
	Function to test area of circle  
	"""  
	assert area_of_circle(5) == 78.53975
def test_area_of_circle_with_mock(mocker):
	"""  
	Function to test area of circle with mocked PI value  
	"""  
	mocker.patch("area.PI", 3.0)  
	assert area_of_circle(5) == 75.0
```

### Mocking a class

```python
# mock_examples/person.py
from typing import Dict

class Person:
    def __init__(self, name: str, age: int = None, address: str = None) -> None:
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def address(self) -> str:
        return self._address

    def get_person_json(self) -> Dict[str, str]:
        return {"name": self._name, "age": self._age, "address": self._address}


# tests/test_person.py
import pytest
from mock_examples.person import Person

@pytest.fixture
def person():
    return Person(name="Eric", age=25, address="123 Farmville Rd")


def test_person_properties(person):
    """
    Test individual properties of the Person class.
    """
    assert person.name == "Eric"
    assert person.age == 25
    assert person.address == "123 Farmville Rd"

def test_person_class_with_mock(mocker):
    """
    Test the Person class using a mock for the 'get_person_json' method 
    """
    person = Person(name="Eric", age=25, address="123 Farmville Rd")
    mock_response = {"name": "FAKE_NAME", "age": "FAKE_AGE", "address": "FAKE_ADDRESS"}

    # Patch the method
    mocker.patch.object(person, "get_person_json", return_value=mock_response)

    assert person.get_person_json() == mock_response

```