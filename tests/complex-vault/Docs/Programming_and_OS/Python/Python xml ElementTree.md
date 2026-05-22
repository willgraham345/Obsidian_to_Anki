---
summary: Module of Python's xml which has an API for parsing/creating XML data. Also refers to the API regarding ElementTrees. ElementTrees are basically a wrapper around an Element.
type: note/library/module
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
  - "[[#Workflows]]"
members:
  - "[[Python xml ElementTree#getroot()]]"
functions:
  - "[[Python xml ElementTree#fromstring()]]"
methods:
  - "[[Python xml ElementTree#find()]]"
processes:
  - "[[Python xml ElementTree#Modify an xml item]]"
  - "[[Python xml ElementTree#Reading an xml from a file]]"
date created: Friday, January 23rd 2026, 3:59:32 pm
date modified: Wednesday, January 28th 2026, 12:38:41 pm
library_of:
  - "[[Python xml]]"
template: "[[base_note_template]]"
template-version: 1.0.1
uses:
  - "[[Python xml Element]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- XML is a hierarchical data format. There are two different classes which can be used to represent the data.

[[Python xml Element]]: Usually represents a single node in the tree. Interactions with a single XML element **AND** its sub-elements are done on the `Element` level.

## Properties
### Methods
##### getroot()
Gets the root `Element`

##### find()
Same as [[Python xml Element#find()]] starting at the root of the tree.

### Functions
##### fromstring()
Parses XML from a string directly into either an [[Python xml Element]] or [[Python xml ElementTree]]

### Processes
##### Reading an xml from a file
 start:
1. `import xml.etree.ElementTree as ET`
2. `tree = ET.parse('data_path.xml')`
3. `root = tree.getroot()`

 end:

##### Modify an xml item
 start:
1. Usually, read the xml file using [[#fromstring()]]
2. 
 end:
