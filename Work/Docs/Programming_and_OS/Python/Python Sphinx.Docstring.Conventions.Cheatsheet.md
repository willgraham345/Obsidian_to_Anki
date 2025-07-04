---
tags: note/python
type: note
---
# Background
How Sphinx uses docstring conventions in reStructuredText


# Google
[Google Style Guide](https://google.github.io/styleguide/pyguide.html)

| Directive  | Description                                          | Example                                                     |
| ---------- | ---------------------------------------------------- | ----------------------------------------------------------- |
| Args       | Describes function parameters or method arguments.   | `Args: a (int): The first parameter.`                         |
| Returns    | Describes the return value of a function or method.  | `Returns: int - The sum of a and b.`                          |
| Raises     | Lists exceptions that may be raised by a function.   | `Raises: ValueError - If a is not an integer.`                |
| Note       | Provides additional information about the function.  | `Note: This function assumes that the input is non-negative.` |
| Examples   | Demonstrates how to use the function or class.       | `Examples:`                                                   |
|            |                                                      | `print(add(1, 2))`                                            |
| See Also   | References related functions, modules, or resources. | `See Also:`                                                   |
|            |                                                      | `OtherMathFunctions.add()`                                    |
|            |                                                      | `https://example.com/doc`                                     |
| Attributes | Describes attributes of a class.                     | `Attributes:`                                                 |
|            |                                                      | `name (str): The name of the person.`                         |
|            |                                                      | `age (int): The age of the person.`                           |
| Module     | Describes the purpose and usage of a module.         | `Module: math_utils`                                          |
|            |                                                      | `This module provides utility functions for mathematical`     |
|            |                                                      | `calculations.`                                               |
| Class      | Describes the purpose and usage of a class.          | `Class: MyClass`                                              |
|            |                                                      | `This class represents a simple example of a Python class.`   |
|            |                                                      | `It has methods for performing basic operations.`             |

## Example
```python
def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        ValueError: If a or b is not an integer.

    Examples:
        print(add(1, 2))  # Output: 3
        print(add(5, 7))  # Output: 12
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a + b


class Person:
    """
    Represents a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Examples:
        person = Person("Alice", 30)
        print(person.name)  # Output: Alice
        print(person.age)   # Output: 30
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """
        Greets the person.

        Returns:
            str: A greeting message.

        Examples:
            person = Person("Bob", 25)
            print(person.greet())  # Output: "Hello, I'm Bob!"
        """
        return f"Hello, I'm {self.name}!"


if __name__ == "__main__":
    """
    Example usage of the add function and Person class.
    """

    # Add two numbers
    print(add(3, 4))  # Output: 7

    # Create a Person object
    person = Person("Charlie", 35)
    print(person.greet())  # Output: "Hello, I'm Charlie!"

```

# Numpy
| Directive            | Description                                                  | Example                                           |
|----------------------|--------------------------------------------------------------|---------------------------------------------------|
| `Parameters`         | Function parameter description                               | `Parameters` <br> `- param_name : int, optional` <br> `    Description, defaults to default_value` |
| `Type`               | Type of function parameter                                   | `Type` <br> `- param_name : int`                 |
| `Raises`             | Exception raised by function                                 | `Raises` <br> `- ValueError` <br> `    Description`                 |
| `Returns`            | Description of what the function returns                     | `Returns` <br> `    Description`                           |
| `Return type`        | Type of the return value                                     | `Return type` <br> `    int`                                    |

# Sphinx

| Directive            | Description                                                  | Example                                           |
|----------------------|--------------------------------------------------------------|---------------------------------------------------|
| `:param:`            | Indicates a function parameter                               | `:param param_name: Description, defaults to default_value` |
| `:type:`             | Indicates the type of a parameter                           | `:type param_name: int, optional`                 |
| `:raises:`           | Indicates that an exception is raised                        | `:raises ValueError: Description`                 |
| `:return:`           | Indicates what is returned by the function                   | `:return: Description`                           |
| `:rtype:`            | Indicates the type of the return value                       | `:rtype: str`                                    |

