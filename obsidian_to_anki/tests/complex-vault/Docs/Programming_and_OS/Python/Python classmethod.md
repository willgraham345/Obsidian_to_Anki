---
summary: Applies to ALL instances of the class (similar to Cpp static), with the passing of instance hidden as a first parameter.
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/concept
implements: ["[[DP Decorator]]", "[[Python Decorators]]"]
similar: ["[[Cpp static]]"]
concept_of: ["[[Python OOP]]"]
date created: Tuesday, November 11th 2025, 1:54:39 pm
date modified: Tuesday, November 11th 2025, 1:58:28 pm
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

## Examples


- In the example below, we're only passing a class to the method, so no instance is involved. We can call the class method as if it was a static function.
```python
class Cls:
    @classmethod
    def introduce(cls):
        print("Hello, I am %s!" %cls)
```

```python
 Cls.introduce() # same as Cls.introduce(Cls)
 # outputs: Hello, I am <class 'Cls'>
```

```python
class SubCls(Cls):
    pass

SubCls.introduce()
# outputs: Hello, I am <class 'SubCls'>
```