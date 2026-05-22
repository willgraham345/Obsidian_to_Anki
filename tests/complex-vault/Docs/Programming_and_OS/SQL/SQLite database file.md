---
summary:
headings: ["[[#Concepts of Note]]"]
type: note/concept
date created: Friday, October 17th 2025, 10:47:02 am
date modified: Friday, October 17th 2025, 10:58:17 am
item_of: ["[[SQLite]]"]
items: ["[[SQLite database file header]]"]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎  Pages ;;; Main file consisting of one or more pages. The size of a page is a power of 2 between 512 and 65536 inclusive. All pages in the database are the same size. = #tools/databases/sqlite/database_file
^035de5
󰙎  Database header ;;; First 100 bytes of database file, formatted in big-endian. = #tools/databases/sqlite/database_file 

󰙎  Lock-byte page ;;; Lock-byte page set aside for use by operating system VFS implementation in implementing the database file locking primitives. = #tools/databases/sqlite/pages
󰙎  Freelist page ;;;  List of pages that are not in active use. = #tools/databases/sqlite/pages 
󰙎  B-tree pages ;;; Key/data storage with unique and ordered keys on page-oriented storage devices. = #tools/databases/sqlite/pages 

Types of pages
- b-tree pages
	- table b-tree interior
	- table b-tree leaf
	- index b-tree interior
	- index b-tree leaf
- freelist
	- freelist trunk
	- freelist leaf
- payload overflow
- pointer map
- lock-byte
