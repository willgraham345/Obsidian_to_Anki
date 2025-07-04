---
type: note
---
# Background
This file explains how to create C# files with the "Hello World" printed to the screen

## Basics
- C# ignores white space
- `namespace` is a way to organize your code
	- `using System` means that we can use classes from the `System` namespace
- `{}` mark beginning and end of a code block
- `class`
	- Container for data and methods, bringing functionality to the program. 
- `Main`
	- Always appears in a C# program
- `Console`
	- Class of the `System` namespace
	- Has a `WriteLine()` method used for outputting text
	- If you omit the `using System`, you would have to write `System.Console.WriteLine()`
- `;`
	- Every C# statement ends with a `;`
	- The name of the C# file does not have to match the class name, but they often do. When saving files, make sure to add the `.cs` file extension.
- `//`
	- Comments
- `/*` and `*/`
	- Multi-line comments

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
