---
summary: How to add collaboration/function call graphs to a doxygen thing. Scroll down to see where each function is called, and where it calls other functions.
type: note/workflow
date created: Friday, March 7th 2025, 12:01:05 pm
date modified: Friday, March 7th 2025, 12:02:00 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
Make sure these settings are set on the doxyfile....

```doxyfile
HAVE_DOT               = YES
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_STATIC         = YES
CALL_GRAPH             = YES
CALLER_GRAPH           = YES
DISABLE_INDEX          = YES 
GENERATE_TREEVIEW      = YES
RECURSIVE              = YES
```