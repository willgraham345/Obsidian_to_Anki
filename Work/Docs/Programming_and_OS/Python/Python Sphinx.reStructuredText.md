---
tags: note/python
type: note
---
# Background
- Default plaintext markup language used by Sphinx.

[Cheatsheet](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-directives)
# Usage
## Paragraphs
- Most basic block. A chunk of text separated by one or more blank lines. Indentation is significant in reST, so all lines of the same paragraph must be left-aligned to the same level of indentation. 

## Inline Markup
- one asterisk: `*text*` for emphasis (italics),
- two asterisks: `**text**` for strong emphasis (boldface), and
- backquotes: ` ``text`` ` for code samples.

Restrictions
- it may not be nested,
- content may not start or end with whitespace: `* text*` is wrong,
- it must be separated from surrounding text by non-word characters. Use a backslash escaped space to work around that: `thisis\ *one*\ word`.

## Lists and Quote-like blocks
Pretty much the same as markdown. See cheatsheet (above) for more info

## Literal Blocks
Introduced by ending a paragraph with a special marker `::`
- Literal block must be indented
```
This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.
```
- NEEDS to have the empty line underneath the `::`. 
## Doctest Blocks
Interactive python sessions cut-and-pasted into docstrings. They do not require the [[Python Sphinx.reStructuredText#Literal Blocks]] syntax. The doctest must end with a blank line nad should NOT end with an unused prompt


## Tables
CSV tables and list tables are also supported. 
- How to implement [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-directives)
### Grid Tables
```
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
```
### Simple Tables
```
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
```

## Sections
Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings. However, this convention is used in [Python Developer’s Guide for documenting](https://devguide.python.org/documentation/markup/#sections) which you may follow:
- `#` with overline, for parts
- `*` with overline, for chapters
- `=` for sections
- `-` for subsections
- `^` for subsubsections
- `"` for paragraphs

## Directives
A generic block of explicit markup. One of the extension mechanisms of reST which Sphinx uses a LOT.
- See more here [[Python Sphinx.reStructuredText.Directives.and.Cross-references]]

Docutils supports:
- Admonitions
- Images
- Additional body elements
- Special tables
- Special directives
- HTML specifics
- Influencing markups


## Images
reST supports an image directive like this:
```
.. image:: gnu.png
   (options)
```