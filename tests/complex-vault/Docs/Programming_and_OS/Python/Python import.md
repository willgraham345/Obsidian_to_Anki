---
summary:
headings:
  - "[[#Usage]]"
  - "[[#Workflows]]"
type: note/keyword
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, November 12th 2025, 5:58:35 pm
function_of:
  - "[[Python Basics]]"
keyword_of:
  - "[[Python Basics]]"
  - "[[Python folder structure]]"
  - "[[Python Packages]]"
  - "[[Python importlib]]"
  - "[[Python Modules]]"
template: "[[base_note_template]]"
template-version: 1.0.0
uses:
  - "[[Python glob]]"
  - "[[Python sys#modules]]"
used_by:
  - "[[Python Modules]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[5. The import system — Python 3.14.0 documentation](https://docs.python.org/3/reference/import.html#package-path-rules)

## Concepts of Note

### Processes
##### Import search
 process_start:
1. Starts search in the [[Python sys#modules]] path.
2. If none found, Python's import protocol is invoked to find/load the module. This has bot ha finder and a loader.
 process_end:

## Usage

See [[Python Scoping Rules#Usage]]


