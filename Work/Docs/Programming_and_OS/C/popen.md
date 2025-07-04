---
summary: Will open a process by creating a pipe, forking, and invoking the shell. See the linux man page for more information.
headings:
  - "[[#Examples]]"
type: note/function
date created: Wednesday, June 25th 2025, 3:50:46 pm
date modified: Wednesday, June 25th 2025, 3:56:47 pm
function_of:
  - "[[C Standard Libraries]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[popen(3) - Linux manual page](https://man7.org/linux/man-pages/man3/popen.3.html)

## Examples

```c
#include <stdio.h>

FILE *popen(const char *command, const char *type);
int pclose(FILE *stream); 
```
