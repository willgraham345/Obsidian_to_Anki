---
tags: note/python
type: note
---
# Background
The configuration directory (directory with the `conf.py` file, default as the source directory) has the `conf.py` file. 
- This build configuration file contains nearly all the configuration needed to customize Sphinx input and output behavior. 

Extensions should also be defined within `conf.py`. See [[Python Sphinx.Extensions]] for more information

Remember, the front page of the output will be defined in the `index.rst`, see [[Python Sphinx.reStructuredText]] for more information on how to write a good starting page. 

# Config
## Theme Configuration
- Find variable `html_theme`
	- There are tons of lots themes, so you can pick one of a ton. 
	- `sphinx_rtd_theme` is a good one. 
[Sphinx Theme Gallery](https://www.google.com/search?q=sphinx+themes&oq=sphinx+themes&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhAuGEDSAQgxMjg1ajBqMagCALACAA&sourceid=chrome&ie=UTF-8)
## Autodoc Config
If we want Sphinx to autogenerate documentation from the comments of our code, we need to point Sphinx to the directory where Python source code resides. 

Usually you need to uncomment lines at the top of the `conf.py`
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../<source_dir>/'))
```
- update `source_dir` with wherever your source code is
	- Absolute path must be specified in relation to where `conf.py` resides
## requirements.txt
Create a `requirements.txt` file in the root directory of the repository, which lists the dependencies in our package. 
- If we don't have this in our file, then ReadTheDocs will fail

## Project Information
`project` = project's name
`author` = author's name
copyright
`project_copyright`
`version` = major project version. Something like `2.6`
`release` = full project version. Something like `2.6.0rc1`

``