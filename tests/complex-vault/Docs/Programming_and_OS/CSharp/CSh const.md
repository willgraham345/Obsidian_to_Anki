---
summary: Declares variables as unchangeable and read-only. You can't declare a const variable without assigning the value.
headings:
type: note/keyword
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 17th 2025, 10:40:36 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

- Declares a variable as unchangeable and read-only
- You cannot declare a constant variable without assigning the value. 

```csharp
const int myNum = 15;
myNum = 20; // error
```