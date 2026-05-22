---
summary: Filesystem manipulation within rust. Extra platform functionality is in `std::os::$platform`
headings: ["[[#Properties]]"]
type: note/library/module
functions: ["[[Rust std fs#copy]]", "[[Rust std fs#create_dir]]", "[[Rust std fs#metadata]]", "[[Rust std fs#read_link]]", "[[Rust std fs#remove_dir_all]]"]
classes: ["[[Rust DirBuilder]]", "[[Rust File]]", "[[Rust FileType]]", "[[Rust Metadata]]", "[[Rust OpenOptions]]"]
date created: Wednesday, December 3rd 2025, 11:00:24 am
date modified: Wednesday, December 3rd 2025, 11:05:52 am
library_of: ["[[Rust std]]"]
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Properties
### Functions
#### copy
Copies the contents of one file to another

#### create_dir
Creates a new, empty directory at the provided path

#### remove_dir_all
Removes a directory after removing all of its contents. 

#### read_link
Reads a symbolic link

#### metadata
Queries the filesystem to get information about a file, directory, etc.