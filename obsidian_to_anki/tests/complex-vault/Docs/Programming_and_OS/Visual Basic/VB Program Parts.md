---
type: note
---
# Background
A VB.NET program usually consists of the following parts.
- Namespace declaration
- Class or module
- One or more procedures
- Variablers
- the Main procedure
- Statements and Expressions
- Comments


```vb
Imports System
Module Module1
   'This program will display Hello World 
   Sub Main()
      Console.WriteLine("Hello World")
      Console.ReadKey()
   End Sub
End Module
```

`Imports System`
- Used to include the `System` namespace in the program

`Module`
- Declares the module `Module1`
- VB.NET is completely object oriented, so every program must contain a module of a class that contains the data and procedures that your program uses.

Classes or modules would contain more than one procedure
- Procedures contain the executable code (define the behavior of a class)
- A procedure could be any of the following
	- Function
	- Sub
	- Operator
	- Get
	- Set
	- AddHandler
	- RemoveHandler
	- RaiseEvent

`Sub Main()`
- Declares the main procedure, which is the entry point for all VB.NET programs. The Main procedure states what the module or class will do when executed.
`Console.WriteLine("Hello World")`
- Method of the Console class defined in the System namespace. Statement causes the message "Hello World!" to be displayed to the screen
`Console.ReadKey()`
- For the VS.NET Users. This will prevent the screen from running and closing quickly when the program is launched from Visual Studio .NET.