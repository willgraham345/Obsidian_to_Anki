---
tags: note/python
type: note
---
# Background
Easier and more intuitive (my favorite). Can be used for the shorter form of documentatiton. A configuration of python file needs to be done to get started, so you need to add either `sphinx.ext.napolion` or `sphinxcontrib.napoleon` to the extensions list in `conf.py`

# Usage
## Headers 
### Supported in Sphinx:
 - `Args` _(alias of Parameters)_
 - `Arguments` _(alias of Parameters)_
 - `Attributes`
 - `Example`
 - `Examples`
 - `Keyword Args` _(alias of Keyword Arguments)_
 - `Keyword Arguments`
 - `Methods`
 - `Note`
 - `Notes`
 - `Other Parameters`
 - `Parameters`
 - `Return` _(alias of Returns)_
 - `Returns`
 - `Raises`
 - `References`
 - `See Also`
 - `Todo`
 - `Warning`
 - `Warnings` _(alias of Warning)_
 - `Warns`
 - `Yield` _(alias of Yields)_
 - `Yields`
## Example
```python
class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, param1, param2, param3):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: Doc comment *inline* with attribute

        #: list of str: Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""
    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

		Usage:
			>>> Shell_command

        Returns:
            True if successful, False otherwise.

        """
        return True
    def my_function():
    """
    This function calls another function.

    Returns:
        str: The result of calling :func:`other_module.other_function`.
    """
    return other_module.other_function()

```