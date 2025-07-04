---
tags: note/python
type: note
---
# Background
- Documentation found [here](https://pypdf2.readthedocs.io/en/3.0.0/index.html)
- Helpful for reading/writing/cropping stuff to an existing PDF

# Classes
## `PDFReader` Class
### Methods
#### `get_fields` 
Extracts field data if the PDF contains interactive form fields
- Parameters
	- **fileobj** – A file object (usually a text file) to write a report to on all interactive form fields found.
- Returns
	- A dictionary where each key is a field name, and each value is a [`Field`](https://pypdf2.readthedocs.io/en/3.0.0/modules/Field.html#PyPDF2.generic.Field "PyPDF2.generic.Field") object. By default, the mapping name is used for keys. `None` if form data could not be located.
#### `get_form_text_fields`
Retrieve form fields from the document with textual data.
- The key is the name of the form field, the value is the content of the field.
- If the document contains multiple form fields with the same name, the second and following will get the suffix _2, _3, …
#### `outline`

Read-only property for outline items, basically reads the outlines present

#### `page_mode`

Gets the page mode

|   Valid Mode Values|   |
|---|---|
|UseNone | Do not show outline or thumbnails panels |
|UseOutlines | Show outline (aka bookmarks) panel |
|UseThumbs | Show page thumbnails panel |
|FullScreen | Fullscreen view |
|UseOC | Show Optional Content Group (OCG) panel |
|UseAttachments | Show attachments panel |
