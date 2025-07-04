---
tags: note/python
type: note
---
# Background
MyST is Markdown, and Sphinx was written when rST was more popular. We can migrate to MyST using a [CLI tool](https://rst-to-myst.readthedocs.io/en/stable/index.html) 

Add this to conf.py to make sphinx parse MyST
```python
extensions = [
    # Your existing extensions
    ...,
    "myst_parser",
]
```
[Install the MyST extension](https://myst-parser.readthedocs.io/en/stable/intro.html#installation)