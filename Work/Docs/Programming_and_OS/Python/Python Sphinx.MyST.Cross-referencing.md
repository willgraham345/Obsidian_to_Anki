---
tags: note/python
type: note
---
# Background
Everywhere you see a `\`, I added that so this markdown interpreter wouldn't see it. 

[Using cross-references with Sphinx](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)

## Directives in MyST
```mst
\```{directivename} <directive arguments>
:optionname: <valuename>

<directive content>
\```
```

### Example Admonition
```
# My nifty title

Some **text**!

\```{admonition} Here's my title
:class: warning

Here's my admonition content
\```
```
- What it looks like
	- ![[Pasted.image.20240418110009.png]]

## Toctree
```myst
\```{toctree}
My page name <page1>
page2
examples/content_child2.md
\```
```


### Toctree options
| Option        | Description                                  | Control how toctree appears in doc? |
| ------------- | -------------------------------------------- | ----------------------------------- |
| caption       | A title for this toctree                     | Y                                   |
| hidden        | Do not show within the document              | <br>Y                               |
| includehidden | Included child hidden toctree entries        | <br>Y                               |
| maxdepth      | The depth of document sub-headings shown     | <br>Y                               |
| titlesonly    | Only show the first top-level heading        | <br>Y                               |
| reversed      | Reverse the order of the entries in the list | <br>Y                               |
| name          | Allow the toctree to be referenced           | N                                   |
| numbered      | Number all headings in children              | N                                   |
d


## Automatically created targets for section headers
Add this to your `conf.py`
```python
extensions = [
    'sphinx.ext.autosectionlabel',
]

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True
```
### Using automatically created section header targets
```
{ref}`path/to/file_1:My Subtitle`
{ref}`Custom Text <target_to_paragraph>`
{doc}`Custom title </guides/intersphinx>`
```


## Inserting other documents directly into the current document
```MyST
\```{literalinclude} example.txt
\```

\```{include} example.txt
\```
```