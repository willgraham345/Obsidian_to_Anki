---
summary: Efficient implementations for "collection"-type data.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/library
date created: Thursday, July 17th 2025, 2:48:32 pm
date modified: Thursday, July 17th 2025, 2:55:42 pm
items: ["[[Rust BinaryHeap]]", "[[Rust BTreeMap]]", "[[Rust hashmap]]", "[[Rust HashSet]]", "[[Rust LinkedList]]", "[[Rust Vec]]", "[[Rust VecDeque]]"]
uses: ["[[Rust std Iterator|Iterator]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[std::collections - Rust](https://doc.rust-lang.org/std/collections/index.html)

## Concepts of Note

󰠗  What collection is best used for arbitrary keys/values, a cache, and a map with no extra functionality? ;; `HashMap` = #lang/data/collections/HashMap  
<!--ID: 1758253288577-->

󰠗  What collection is best used for a map sorted by its keys, able to get a range of entries on demand, able to compare smallest/largest key-value pair, and key comparisons? ;; `BTreeMap` = #lang/data/collections/BTreeMap 
<!--ID: 1758253288584-->

󰠗  What collection is best when you want to remember which keys you've seen, there's no meaningful value to associated with your keys? ;; `Set` = #lang/data/collections/set  
<!--ID: 1758253288593-->


## Usage
![[Rust std Iterator#^c78910]]
