---
tags: note/python
type: note
---
# Background
reST does not have facilities to interconnect several documents, or split documents into multiple files. The `toctree` directive is the central element.
IMPORTANT: you need to have the blank space between the title and its contents
- All documents in the source directory (or subdirectoires) must occur in some `toctree` directive. 
	- Sphinx will emit a warning if it finds a file that is not included, because that means that this file will not be reachable through standard navigation. 
- `master_doc` is the "root" of the TOC tree hierarchy. It can be used as the documentation's main page, or as a "full table of contents" if you don't give a `maxdepth` option. 

## Example
```rst
.. toctree::
   :maxdepth: 2

   intro
   strings
   datatypes
   numeric
   (many more documents listed here)
```
- This accomplishs two things:
	- Table of contents from all those documents are inserted, with a maximum depth of two, meaning one nested heading.
	- Sphinx knows that the relative order of the documents `intro`, `strings`, and so forth, and it knows that they are children of the shown document, the library index. 

# Usage
## Basics
- Make sure there's a space between the `.. toctree::` directive and the contents
- `max_depth` will change how many links are shown, adn how many headings are shown
## Entries
Document titles in the `toctree` will automatically read from the title of the referenced documetn. If that isn't what you want, you can specify an explicit title and target
```rst
.. toctree::

   intro
   All about strings <strings>
   datatypes
```

### Section Numbering
```rst
.. toctree::
   :numbered:

   foo
   bar
```
### Additional Options
#### `titlesonly`
```rst
.. toctree::
   :titlesonly:

   foo
   bar
```

#### globbing
```rst
.. toctree::
   :glob:

   intro*
   recipe/*
   *
```
- This includes all first documents whose names start with `intro`, then all documents in the `recipe` folder, then all remaining documents.
- `self` stands for the document containing the `toctree` directive. This is useful if you want to generate a "sitemap" from the toctree

#### hidden
```rst
.. toctree::
   :hidden:

   doc_1
   doc_2
```
- Will notify Sphinx of the document hierarchy, but not insert links into the document at the location of the directive. 

## Special Names
`genindex`
- General index, populated with entries from modules, all index-generating object descriptions and from `index` directives
`modindex`
- Python module index contains one entry per `py:module` directive
`search`
- Contains a form that uses the generated JSON search index and JavaScript to full-text search the generated documents for search words
- Every name beginning with `_`
	- You should not create documents or document-containing directories with these names. 