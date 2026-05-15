---
summary:
headings: ["[[#Concepts of Note]]"]
type: note/concept
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Saturday, November 8th 2025, 12:16:40 pm
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
  `namespace a.b.c;` ;;; Declares a namespace `a.b.c` in C# = #lang/scope 
<!--ID: 1759154339879-->

  `{ }` ;;; A block of code in C# = #lang/scope #lang/syntax/statements
<!--ID: 1759154339883-->

󰠗  What does every statement in C# end with? ;; `;` = #lang/syntax
<!--ID: 1759154339874-->

  `member ``=>`` expression` ;;; Define an expression-bodied member. = #lang/syntax/statements #lang/oop/members
<!--ID: 1759154339888-->

󰙎  Expression-bodied member ;;; Member's implementation in one line of code. = #lang/syntax/statements


- `Main`
	- Always appears in a C# program
- `Console`
	- Class of the `System` namespace
	- Has a `WriteLine()` method used for outputting text
	- If you omit the `using System`, you would have to write `System.Console.WriteLine()`
- `;`
	- Every C# statement ends with a `;`
	- The name of the C# file does not have to match the class name, but they often do. When saving files, make sure to add the `.cs` file extension.

### Types of Statements in CSharp
[[CS Statement Types]]

# Usage
## Hello World 
```csharp
using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");    
    }
  }
}
```
