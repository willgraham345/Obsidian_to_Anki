---
tags: note/python
type: note
---
# Background
- This section covers how to write "main" pages and other stuff. 

## Index.rst and Other Stuff
The `index.rst` created by `sphinx-quickstart` is the root document, whose main function is to serve as a welcome page. 
- Also the table of contents tree (toctree)
	- Sphinx allows you to assemble a project from different files, which is helpful when the project grows.


# Usage
## Example
Create a `docs/source/usage.rst` (next to the `index.rst`) with these contents
`usage.rst`
```rst
Usage
=====

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache
```
- This file has two section headers, normal paragraph text, and a code-block that renders a block of content as source code.
	- Structure of the document is determined by succession of heading styles (installation is a subsection of usage in the above codeblock)
- To complete the process, add a `toctree` directive at the end of `index.rst` including the document you just created 
`index.rst`
```rst
Contents
--------

.. toctree::

   usage
```

Gap inserts the document in the root of the toctree
```
index
└── usage
```
If you build the HTML documentation by running `make html`, you will see that the `toctree` gets rendered as a list of hyperlinks, and this allows you to navigate to the new page you just created.


## Adding Cross-references
You can add cross-references to specific parts of the documentation.

`index.rst`
```rst
Check out the :doc:`usage` section for further information.
```

To reference the "Installation" subsection, add a label right before the heading, as follows:
`docs/source/usage.rst`
```rst
=====

.. _installation:
Installation
------------

...
```

`docs/source/index.rst`
```rst
Check out the :doc:`usage` section for further information, including how to
:ref:`install <installation>` the project.
```
- `install` specifies how the link will look like (we want it to be a specific word, so the sentence makes sense). Whereas the `<installation>` part refers to the actual label we want to add a cross-reference to.
	- If you don't use an explicit title, i.e. (see below), the section title will be used
```
:ref:`installation`
```
- Both `:doc:` and `:ref:` roles will be rendered as hyperlinks in the HTML documentation. 