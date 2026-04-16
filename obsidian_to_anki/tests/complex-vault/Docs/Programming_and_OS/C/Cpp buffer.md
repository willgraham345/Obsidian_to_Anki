---
summary: A block of memory that we use to move data around. Often a `uint8_t` as that represents one byte or `char*`. A buffer can also mean a temporary placeholder for moving into another datatype.<br><br>There are usually functions on either end that are reponsible to "marshall"/serialize/format the data into and out of buffers.
headings: 
type: note/concept
associations:
  - "[[Cpp cache]]"
concept_of:
  - "[[Cpp Input Output]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, June 24th 2025, 8:31:22 am
class_of:
  - "[[Cpp Input Output]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- A buffer is just a block of memory. We use the word buffer when moving data around, because the data will be placed in the buffer, then placed in its final destination. 
- Cache is a smaller and a fast memory component between the CPU and the main memory. Acts as a buffer, but this data is expected to be read multiple times which reduces the need to access slower storages. 
