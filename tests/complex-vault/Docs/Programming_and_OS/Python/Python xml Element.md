---
summary: "The class that defines the `Element` interface, and provides a reference implementation of this interface. "
type: note/class
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Properties]]"]
members: ["[[Python xml Element#attrib]]", "[[Python xml Element#tag]]"]
methods: ["[[Python xml Element#find(match)]]", "[[Python xml Element#iter('tagName') -> `Generator[Element[str, None, None]`]]"]
date created: Wednesday, January 28th 2026, 12:13:22 pm
date modified: Wednesday, January 28th 2026, 12:31:35 pm
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- `tag` is the element name
- `attrib` optional dictionary containing element attributes

## Properties
### Members
##### tag
String identifying what kind of data this represents (element type)

##### attrib
Dict containing element's attributes. 

### Methods
##### find(match)
Finds the first subelement matching `match`. 
- Can be a tag name or a path. Returns an element instance or `None`

##### iter('tagName') -> `Generator[Element[str, None, None]`
- An iterator that will loop over all elements and subelements in document order, returning all documents with a matching tag.

## Examples
Go through an xml for nodes of type
