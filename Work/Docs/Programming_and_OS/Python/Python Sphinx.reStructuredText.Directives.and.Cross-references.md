---
tags: note/python
type: note
---
# Background
When using `:ref:`, `:doc:` and `:def:`, they need to be stored in the `docs/source` directory.

| Description                      | Syntax                                                | Example                                             |
| -------------------------------- | ----------------------------------------------------- | --------------------------------------------------- |
| Link using the `:ref:` role      | `:ref:`target`                                      ` | :ref:`Sphinx Introduction <intro>`                  |
| Link to a document using `:doc:` | `:doc:`document`                                  `   | :doc:`Installation Guide <installation>`            |
| Link using `:def:` to a term     | `:def:`term`                                      `   | :def:`Sphinx <sphinx>`                              |
| Link to a specific heading       | `[Link Text](path/to/document.rst#specific-heading)`  | [Installation Guide](installation.rst#installation) |
| Image from an external URL       | `![Alt Text](https://example.com/image.jpg)`          | ![OpenAI Logo](https://openai.com/assets/logo.png)  |
| Image from local directory       | `![Alt Text](path/to/image.jpg)`                      | ![Sphinx Logo](_static/sphinx_logo.jpg)             |


## Cross-references
### Automatically Labeling Sections
Manually adding explicit target to each section is a lot, use the `autosectionlabel` extension with sphinx. Add the following to your `conf.py` file
```python
# Add the extension
extensions = [
    "sphinx.ext.autosectionlabel",
]

# Make sure the target is unique
autosectionlabel_prefix_document = True
```

#### Using the target
```rst
{path/to/page}:{title-of-section}
```

### Components in Cross-references
#### References
- References = pointers in your documentation to other documentation
#### Targets
- Targets = where the references point to
##### Example Targets for a Section

```rst
.. _My target:

Explicit targets
~~~~~~~~~~~~~~~~

Reference `My target`_.
```
- Explicit targets can be added to paragraphs (or any other part of a page)

```rst
.. _target to paragraph:

An easy way is just to use the final link of the page/section.
This works, but it has :ref:`some disadvantages <target to paragraph>`:
```

```rst
You can also create _`in-line targets` within an element on your page,
allowing you to, for example, reference text *within* a paragraph.
```


##### Implicit Targets
You may reference some objects by name without explicitly giving them one by using implicit targets
When you create a section, footnote, or citation, Sphinx will create a target with the title as the name. 

##### Explicit Targets
###### `ref`
The `ref` role can be used to reference explicit targets
```rst
- :ref:`my target`.
- :ref:`Target to paragraph <target to paragraph>`.
- :ref:`Target inside a paragraph <in-line targets>`.
```

Can be used for code blocks as well. 
Use 
```rst
:ref\`code <target to code>`
```
##### `doc`
- Allows us to link to a page instead of just a section. The target name can be relative to the page where the role exists, or relative to your documentation's root folder (in both cases, you should omit the extension)

```rst
- :doc:`intersphinx`
- :doc:`/guides/intersphinx`
- :doc:`Custom title </guides/intersphinx>`
```

### Invalid targets debugging
You can use the `-W` option to make Sphinx fail the build if there are invalid references.
#### Finding Reference name
List all targets for built documentation
```shell
python -m sphinx.ext.intersphinx <link>
```
- `<link>` is either a URL or a local path that points to your inventory file (usually in `_build/html/objects.inv`)
