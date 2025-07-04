---
tags: note/python
type: note
---
# Background
Builder's "name" must be given to the `-M` or `-b` command line options of `sphinx-build` to select a builder. `sphinx-build -M <builder_name>`

## Builders
- `html` = Build HTML pages. This is the default builder.
- `dirhtml` = Build HTML pages, but with a single directory per document. Makes for prettier URLs (no `.html`) if served from a webserver.
- `singlehtml` = Build a single HTML with the whole content.
- `htmlhelp**, **qthelp**, **devhelp**, **epub` = Build HTML files with additional information for building a documentation collection in one of these formats.
- `applehelp` = Build an Apple Help Book. Requires **hiutil** and **codesign**, which are not Open Source and presently only available on Mac OS X 10.6 and higher.
- `latex` = Build LaTeX sources that can be compiled to a PDF document using **pdflatex**.
- `man` = Build manual pages in groff format for UNIX systems.
- `texinfo` = Build Texinfo files that can be processed into Info files using **makeinfo**.
- `text` = Build plain text files.
- `gettext` = Build gettext-style message catalogs (`.pot` files).
- `doctest` = Run all doctests in the documentation, if the [`doctest`](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html#module-sphinx.ext.doctest "sphinx.ext.doctest: Test snippets in the documentation.") extension is enabled.
- `linkcheck` = Check the integrity of all external links.
- `xml` = Build Docutils-native XML files.
- `pseudoxml` = Build compact pretty-printed “pseudo-XML” files displaying the internal structure of the intermediate document trees.