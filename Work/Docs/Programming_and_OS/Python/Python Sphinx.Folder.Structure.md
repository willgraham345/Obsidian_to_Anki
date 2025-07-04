---
tags: note/python
type: note
---
# Background
A documentation generator tool that converts reStructuredText into HTML, PDF, or man pages. 
- Uses [[Python Sphinx.reStructuredText]] as the language of choice in most documents. 

Arguably the best tutorial on Sphinx is from [ReadTheDocs](https://docs.readthedocs.io/en/stable/index.html)
- TONS of references and examples

Reads a `conf.py` in your source directory (repo root)
## Documentation Layout
```
simpleble-master
├── docs
│ ├── build
│ ├── make.bat
│ ├── Makefile
│ └── source
	└── _static
├── LICENSE
├── README.md
├── requirements.txt
└── package
	└── package.py
```
- `docs/`
	- Directory where our Sphinx documentation will reside
	- `docs/source`
		-  Where all of our `.rst` files will reside
		- `docs/source/conf.py`
			- Where all the Sphinx configuration settings are specified. Project names, release, and some extra config keys.
		- `source/index.rst`
			- Root document of the project, serving as the welcome page and the root of the "table of contents tree" (toctree). Tells Sphinx how to render our `index.html` page. 
				- Serves as the front page of your HTML
			- In general, each `source/*.rst` file is converted to a corresponding `build/html/*.html` page when `make html` is called. 
		- `source/_static`
			- Default directory for static files like images within Sphinx projects. 
	- `docs/build/`
		- Directory where the output of any builder is stored when `make <builder>` or `sphinx-build <builder>` that will hold the rendered documentation.
		- `docs/build/make.bat` and `Makefile`
			- Simplify some common Sphinx operations (like rendering the content)
- `package`
	- Our python package we're documenting 

[Progress on Intro](https://www.sphinx-doc.org/en/master/tutorial)

[Really Good Tutorial on Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html)

[Another really good tutorial](https://biapol.github.io/blog/johannes_mueller/entry_sphinx/Readme.html)
# Usage


## Make sure Build is Working Right
```shell
sphinx-build --version
```
## Create Documentation Layout
```shell
sphinx-quickstart docs
```
- Presents a series of questions required to change basic directory and config layout for your project inside the `docs` folder


## Building Documentation as HTML
```shell
$ sphinx-build -M html docs/source/ docs/build/
```
- See [[Python Sphinx.Builders]] for more info on building alternative builders