---
type:
headings:
date created: Sunday, March 8th 2026, 8:50:22 pm
date modified: Thursday, March 12th 2026, 9:00:04 am
item_of:
  - "[[CS Data Structures]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[CS Preprocessor]]"
  - "[[CS tokenizer]]"
---

# Summary
󰙎 CS Token ;;; “A token is a data structure that, besides the token text (a sequence of characters), also contains information about its nature (for instance, whether the token represents a number, a keyword, or an identifier) and debugging information (the file and line number it was read from). Therefore, a token conveys additional information with respect to the portion of plaintext it corresponds to”

Excerpt From
Real-Time Systems Development with RTEMS and Multicore Processors
Bloom, Gedare
This material may be protected by copyright.

# Additional Background


For LLMs, token means something more abstract. For example, 3 tokens may be "fir" "e" "tr" "uck". Each of these separately means something, which is why the tokenizer splits it as such. 