---
summary:
headings:
type: note/item
associations:
  - "[[CSh console output]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 17th 2025, 10:48:26 am
item_of:
  - "[[Csh System]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

The console can also be used to read data.
  `ReadLine()` ;;; Prompt for console input = #lang/io
<!--ID: 1758253289537-->


```csharp
Console.WriteLine("Enter your age:");
int age = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Your age is: " + age);
```
