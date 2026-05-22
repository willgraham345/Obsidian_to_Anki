---
summary:
type: note/class
headings:
  - "[[#Properties]]"
  - "[[#Usage]]"
  - "[[#Workflows]]"
methods:
  - "[[Python List#sort()]]"
similar:
  - "[[Python Array]]"
class_of:
  - "[[Python Data Types]]"
date created: Monday, September 9th 2024, 12:05:33 am
date modified: Friday, February 20th 2026, 8:50:35 am
template: "[[base_note_template]]"
template-version: 1.0.0
used_by:
  - "[[Python builtin functions#filter()]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[List Methods](https://www.w3schools.com/python/python_ref_list.asp)

## Properties

### Methods
##### sort()
󰡱 :
- description: Defaults to alphabetical sorting
- args: `reverse=False`, `key`: `function`. 
	- function can be 
- calls:
󰡱 end:

### Processes
### Filtering Python Lists
1. [[Python builtin functions#filter()]]
2. [[Python for loop]]
3. [[Python List_Comprehension]]

### Sorting Python Lists
##### Sort a list of dicts based on the `year` value of dictionaries
```python
# A function that returns the 'year' value:  
def myFunc(e):  
  return e['year']  
  
cars = [  
  {'car': 'Ford', 'year': 2005},  
  {'car': 'Mitsubishi', 'year': 2000},  
  {'car': 'BMW', 'year': 2019},  
  {'car': 'VW', 'year': 2011}  
]  
  
cars.sort(key=myFunc)
```

##### Sort a list of dicts by the offset value
```python
l.sort(key=lambda p: p["OFFSET"])
```
