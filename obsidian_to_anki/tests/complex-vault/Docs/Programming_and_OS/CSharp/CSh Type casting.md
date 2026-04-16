---
summary:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/concept
concept_of:
  - "[[CSh Data Types]]"
  - "[[CSh|C Sharp]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, September 17th 2025, 10:44:50 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
Type casting is when you assign a value of one data type to another data type
- **Implicit Casting** (automatically) - converting a smaller type to a larger type size  
    `char` -> `int` -> `long` -> `float` -> `double`  
- **Explicit Casting** (manually) - converting a larger type to a smaller size type  
    `double` -> `float` -> `long` -> `int` -> `char`

## Usage
  `Convert.ToBoolean(myVar)` ;;; Converts a var `myVar` explicitly using a built-in method to a `bool` = #lang/data/casting
<!--ID: 1758253289544-->

It is also possible to convert data types explicitly by using built-in methods, such as `Convert.ToBoolean`, `Convert.ToDouble`, `Convert.ToString`, `Convert.ToInt32` (`int`) and `Convert.ToInt64` (`long`):

### Example
```csharp
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));    // convert int to string
Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
Console.WriteLine(Convert.ToString(myBool));   // convert bool to string
```
