---
summary: The order in which bytes within a word of digital data are transmitted or addressed in computer memory.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Media]]"
concept_of:
  - "[[CS Messaging and Serialization]]"
date created: Monday, June 2nd 2025, 10:23:20 am
date modified: Wednesday, March 4th 2026, 3:03:32 pm
tags: [cs/networking]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[Fetching Title#ngrl](https://betterexplained.com/articles/understanding-big-and-little-endian-byte-order/)

󰙎  Endianness ;;; The order in which bytes within a word of digital data are transmitted/addressed. =  

󰙎  Big endian ;;; The MSB (most significant byte), which carries the highest order bits of the data, is stored at the lowest memory address. Read left to right, where the highest value is on the left. =  

󰙎  Little endian ;;; The LSB (least significant byte), which carries the lowest order bits of the data, is stored at the lowest memory address. Read right to left, where the highest value is on the right. =  

󰠗  What is the base unit for an endian? ;; A "word" data type. This is the processor design's natural unit of data handled by the instruction set. The number of "bits" is the word size. = 

## Media

![[CS Endianness.png]]
