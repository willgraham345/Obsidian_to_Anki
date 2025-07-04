---
summary: 
type: note/concept
components: ["[[Python break]]", "[[Python continue]]", "[[Python enumerate]]", "[[Python for loop]]", "[[Python if else]]", "[[Python while loop]]"]
associations: ["[[Python Exception Handling]]"]
concept_of: ["[[Python|#note/python]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, February 24th 2025, 11:59:17 am
tags: [note/python]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Assertions
Description:
-   An assertion is a sanity-check that you can turn on or turn off when
    you have finished testing the program. An expression is tested, and
    if the result comes up false, an [exception]{.underline} is. If a second argument is added, the assertion will have text to it

Syntax:

``` python
 a = 2
 assert 2 + a == 7, "ErrorMessage"

> Output:
>
> 2
>
> AssertionError: ErrorMessage
```