---
tags: note/python
type: note
---
# Background
Napoleon is an extension that lets you write nicer and more appealing Python code like those described in [[Python Docstrings]].
- A preprocessor that parses NumPy and Google style docstrings and converts them to reStructuredText before Sphinx attempts to parse them. 
Napoleon interprets every docstring that `autodoc` can find, including docstrings on `modules`, `classes`, `attributes`, `methods`, `functions`, and `variables`. 

Napoleon will need additional configuration after you've run the `sphinx-apidoc` compilation command. 

## Configuration
Listed below are the settings used by napoleon and their default values. These settings are changed in the `conf.py` file within the Sphinx directory. 

### Basic ones

| Setting                        | Description                                                                                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| napoleon_google_docstring      | True to parse Google style docstrings. False to disable support for Google style docstrings. Defaults to True.                                                                                                           |
| napoleon_numpy_docstring       | True to parse NumPy style docstrings. False to disable support for NumPy style docstrings. Defaults to True.                                                                                                             |
| napoleon_include_init_with_doc | True to list `__init__` docstrings separately from the class docstring. False to fall back to Sphinx’s default behavior, which considers the `__init__` docstring as part of the class documentation. Defaults to False. |

### napoleon_include_init_with_doc
- True to list `__init___` docstrings separately from the class docstring. False to fall back to Sphinx’s default behavior, which considers the `__init___` docstring as part of the class documentation. _Defaults to False._

#### **If True**:
```python
def __init__(self):
    """
    This will be included in the docs because it has a docstring
    """
def __init__(self):
    # This will NOT be included in the docs
```

### napoleon_include_private_with_doc
- True to include private members (like `_membername`) with docstrings in the documentation. False to fall back to Sphinx’s default behavior. _Defaults to False._

#### **If True**:
```python
def _included(self):
    """
    This will be included in the docs because it has a docstring
    """
    pass
def _skipped(self):
    # This will NOT be included in the docs
    pass
```

### napoleon_include_special_with_doc
- True to include special members (like `__membername__`) with docstrings in the documentation. False to fall back to Sphinx’s default behavior. _Defaults to True._

#### **If True**:
```python
def __str__(self):
    """
    This will be included in the docs because it has a docstring
    """
    return unicode(self).encode('utf-8')

def __unicode__(self):
    # This will NOT be included in the docs
    return unicode(self.__class__.__name__)
```

### napoleon_use_admonition_for_examples
- True to use the `.. admonition::` directive for the **Example** and **Examples** sections. False to use the `.. rubric::` directive instead. One may look better than the other depending on what HTML theme is used. _Defaults to False._

#### This [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) snippet will be converted as follows:
```
Example
-------
This is just a quick example
```
**If True**:
```
.. admonition:: Example

   This is just a quick example
```

**If False**:
```
.. rubric:: Example

This is just a quick example
```

### napoleon_use_admonition_for_notes[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_admonition_for_notes "Link to this definition")
- True to use the `.. admonition::` directive for **Notes** sections. False to use the `.. rubric::` directive instead. _Defaults to False._

Note

The singular **Note** section will always be converted to a `.. note::` directive.

- See also
	- [`napoleon_use_admonition_for_examples`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_admonition_for_examples)

### napoleon_use_admonition_for_references[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_admonition_for_references "Link to this definition")

True to use the `.. admonition::` directive for **References** sections. False to use the `.. rubric::` directive instead. _Defaults to False._

See also

### [`napoleon_use_admonition_for_examples`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_admonition_for_examples)

napoleon_use_ivar[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_ivar "Link to this definition")

True to use the `:ivar:` role for instance variables. False to use the `.. attribute::` directive instead. _Defaults to False._

This [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) snippet will be converted as follows:

Attributes
----------
attr1 : int
    Description of `attr1`

**If True**:

:ivar attr1: Description of `attr1`
:vartype attr1: int

**If False**:

.. attribute:: attr1

   Description of `attr1`

   :type: int

napoleon_use_param[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_param "Link to this definition")

True to use a `:param:` role for each function parameter. False to use a single `:parameters:` role for all the parameters. _Defaults to True._

This [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) snippet will be converted as follows:

Parameters
----------
arg1 : str
    Description of `arg1`
arg2 : int, optional
    Description of `arg2`, defaults to 0

**If True**:

:param arg1: Description of `arg1`
:type arg1: str
:param arg2: Description of `arg2`, defaults to 0
:type arg2: :class:`int`, *optional*

**If False**:

:parameters: * **arg1** (*str*) --
               Description of `arg1`
             * **arg2** (*int, optional*) --
               Description of `arg2`, defaults to 0

napoleon_use_keyword[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_keyword "Link to this definition")

True to use a `:keyword:` role for each function keyword argument. False to use a single `:keyword arguments:` role for all the keywords. _Defaults to True._

This behaves similarly to [`napoleon_use_param`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_param). Note unlike docutils, `:keyword:` and `:param:` will not be treated the same way - there will be a separate “Keyword Arguments” section, rendered in the same fashion as “Parameters” section (type links created if possible)

See also

[`napoleon_use_param`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_param)

napoleon_use_rtype[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_use_rtype "Link to this definition")

True to use the `:rtype:` role for the return type. False to output the return type inline with the description. _Defaults to True._

This [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) snippet will be converted as follows:

Returns
-------
bool
    True if successful, False otherwise

**If True**:

:returns: True if successful, False otherwise
:rtype: bool

**If False**:

:returns: *bool* -- True if successful, False otherwise

napoleon_preprocess_types[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_preprocess_types "Link to this definition")

True to convert the type definitions in the docstrings as references. Defaults to _False_.

Added in version 3.2.1.

Changed in version 3.5: Do preprocess the Google style docstrings also.

napoleon_type_aliases[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_type_aliases "Link to this definition")

A mapping to translate type names to other names or references. Works only when `napoleon_use_param = True`. _Defaults to None._

With:

napoleon_type_aliases = {
    "CustomType": "mypackage.CustomType",
    "dict-like": ":term:`dict-like <mapping>`",
}

This [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) snippet:

Parameters
----------
arg1 : CustomType
    Description of `arg1`
arg2 : dict-like
    Description of `arg2`

becomes:

:param arg1: Description of `arg1`
:type arg1: mypackage.CustomType
:param arg2: Description of `arg2`
:type arg2: :term:`dict-like <mapping>`

Added in version 3.2.

napoleon_attr_annotations[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_attr_annotations "Link to this definition")

True to allow using [**PEP 526**](https://peps.python.org/pep-0526/) attributes annotations in classes. If an attribute is documented in the docstring without a type and has an annotation in the class body, that type is used.

Added in version 3.4.

napoleon_custom_sections[](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#confval-napoleon_custom_sections "Link to this definition")

Add a list of custom sections to include, expanding the list of parsed sections. _Defaults to None._

The entries can either be strings or tuples, depending on the intention:

- To create a custom “generic” section, just pass a string.
    
- To create an alias for an existing section, pass a tuple containing the alias name and the original, in that order.
    
- To create a custom section that displays like the parameters or returns section, pass a tuple containing the custom section name and a string value, “params_style” or “returns_style”.
    

If an entry is just a string, it is interpreted as a header for a generic section. If the entry is a tuple/list/indexed container, the first entry is the name of the section, the second is the section key to emulate. If the second entry value is “params_style” or “returns_style”, the custom section will be displayed like the parameters section or returns section.

Added in version 1.8.

Changed in version 3.5: Support `params_style` and `returns_style`

## Docstring Sections
All the following section headers are supported:
- `Args` _(alias of Parameters)_
- `Arguments` _(alias of Parameters)_
- `Attention`
- `Attributes`
- `Caution`
- `Danger`
- `Error`
- `Example`
- `Examples`
- `Hint`
- `Important`
- `Keyword Args` _(alias of Keyword Arguments)_
- `Keyword Arguments`
- `Methods`
- `Note`
- `Notes`
- `Other Parameters`
- `Parameters`
- `Return` _(alias of Returns)_
- `Returns`
- `Raise` _(alias of Raises)_
- `Raises`
- `References`
- `See Also`
- `Tip`
- `Todo`
- `Warning`
- `Warnings` _(alias of Warning)_
- `Warn` _(alias of Warns)_
- `Warns`
- `Yield` _(alias of Yields)_
- `Yields`