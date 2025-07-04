---
summary: The ways that python handles different exceptions, and how to manage it.
headings: ["[[#Exceptions]]", "[[#Syntax]]"]
type: note/concept
components: ["[[Python raise]]", "[[Python try except else finally]]"]
associations: ["[[Python Control Flow]]"]
concept_of: ["[[Python|#note/python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, April 8th 2025, 12:13:21 pm
tags: [note/python]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
```python
try:  
# Code that might raise an exception  
except SomeException:  
# Code to handle the exception  
else:  
# Code to run if no exception occurs  
finally:  
# Code to run regardless of whether an exception occurs
```

## Exceptions

| Exception             | Description                                                                       |
| --------------------- | --------------------------------------------------------------------------------- |
| ArithmeticError       | Raised when an error occurs in numeric calculations                               |
| AssertionError        | Raised when an assert statement fails                                             |
| AttributeError        | Raised when attribute reference or assignment fails                               |
| Exception             | Base class for all exceptions                                                     |
| EOFError              | Raised when the input() method hits an "end of file" condition (EOF)              |
| FloatingPointError    | Raised when a floating point calculation fails                                    |
| GeneratorExit         | Raised when a generator is closed (with the close() method)                       |
| ImportError           | Raised when an imported module does not exist                                     |
| IndentationError      | Raised when indentation is not correct                                            |
| IndexError            | Raised when an index of a sequence does not exist                                 |
| KeyError              | Raised when a key does not exist in a dictionary                                  |
| KeyboardInterrupt     | Raised when the user presses Ctrl+c, Ctrl+z or Delete                             |
| LookupError           | Raised when errors raised cant be found                                           |
| MemoryError           | Raised when a program runs out of memory                                          |
| NameError             | Raised when a variable does not exist                                             |
| NotImplementedError   | Raised when an abstract method requires an inherited class to override the method |
| OSError               | Raised when a system related operation causes an error                            |
| OverflowError         | Raised when the result of a numeric calculation is too large                      |
| ReferenceError        | Raised when a weak reference object does not exist                                |
| RuntimeError          | Raised when an error occurs that do not belong to any specific exceptions         |
| StopIteration         | Raised when the next() method of an iterator has no further values                |
| SyntaxError           | Raised when a syntax error occurs                                                 |
| TabError              | Raised when indentation consists of tabs or spaces                                |
| SystemError           | Raised when a system error occurs                                                 |
| SystemExit            | Raised when the sys.exit() function is called                                     |
| TypeError             | Raised when two different types are combined                                      |
| UnboundLocalError     | Raised when a local variable is referenced before assignment                      |
| UnicodeError          | Raised when a unicode problem occurs                                              |
| UnicodeEncodeError    | Raised when a unicode encoding problem occurs                                     |
| UnicodeDecodeError    | Raised when a unicode decoding problem occurs                                     |
| UnicodeTranslateError | Raised when a unicode translation problem occurs                                  |
| ValueError            | Raised when there is a wrong value in a specified data type                       |
| ZeroDivisionError     | Raised when the second operator in a division is zero                             |