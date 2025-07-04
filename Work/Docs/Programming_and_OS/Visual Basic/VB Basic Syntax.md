---
type: note
---
# Background
A VB.NET program can be defined as a collection of objects that communicate via invoking each other's methods


# Usage
## Rectangle Example
```vb
Imports System
Public Class Rectangle
   Private length As Double
   Private width As Double

   'Public methods
   Public Sub AcceptDetails()
      length = 4.5
      width = 3.5
   End Sub

   Public Function GetArea() As Double
      GetArea = length * width
   End Function
   Public Sub Display()
      Console.WriteLine("Length: {0}", length)
      Console.WriteLine("Width: {0}", width)
      Console.WriteLine("Area: {0}", GetArea())

   End Sub

   Shared Sub Main()
      Dim r As New Rectangle()
      r.Acceptdetails()
      r.Display()
      Console.ReadLine()
   End Sub
End Class
```