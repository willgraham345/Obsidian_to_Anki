---
summary: Yaml ain't markup language. A popular serialization language used for configuration files.
headings: ["[[#Concepts of Note]]", "[[#Questions]]", "[[#Usage]]"]
type: note/system
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, November 5th 2025, 11:25:12 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.0
uses: ["[[YAML Schemas]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Title Unavailable \| Site Unreachable](https://spacelift.io/blog/yaml)

## Concepts of Note
- YAML dictates nesting through indentation. Similar to python indentation.
󰙎  YAML Sequence ;;; Yaml's version of a list. = #lang/config/yml  
󰙎  YAML Maps ;;; Yaml's version of a map/dictionary. = #lang/config/yml 

| YAML Node type                    | Indent          | Desired Structure |
| --------------------------------- | --------------- | ----------------- |
| Maps (map/dict)                   | Indent          | `dict`            |
| Sequences (array/list)            | Indent with `-` | `list`            |
| Literals (String/number/bool/etc) | N/A             | `literals`        |
| New document                      | `---`           | New doc           |

### Schemas
Typically defined through JSON schema.
[Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step)

## Usage


  `  a: val` ;;; Define a dict/map with key `a` with value `b`. = 
- [p] `  a: `
      `- b`
      `- c` = Define a list `a` with values `b` and `c` = 
- [p] `message: >`
      `looks `
      `like `
      `a multiline message` = Write "looks like a multiline message" but concatenates to a normal message in YAML. = #lang/config/yml 
- [p] `message: >+`
      `looks`
      `like`
      `a multline message` = Preserve "chomp" characters in yml, making a string "looks like a multiline message" in YAML. = #lang/config/yml 
- [p] `message: >+`
      `looks`
      `like`
      `a multiline message` = Erase "chomp" characters in yml, making a string "lookslikeamultilinemessage" in YAML. = #lang/config/yml 
  `scalars: !!str true` ;;; Tag a map `scalars` to parse a literal `true` as a string, not as a bool. = #lang/config/yml 
  `rank: !!int 1` ;;; Tag a map `rank` to parse a literal `1` as an int, not as a string. = #lang/config/yml 
- [p] 

## Example
```yaml
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

```python
{
  "doe": "a deer, a female deer",
  "ray": "a drop of golden sun",
  "pi": 3.14159,
  "xmas": true,
  "french-hens": 3,
  "calling-birds": [
     "huey",
     "dewey",
     "louie",
     "fred"
  ],
  "xmas-fifth-day": {
  "calling-birds": "four",
  "french-hens": 3,
  "golden-rings": 5,
  "partridges": {
    "count": 1,
    "location": "a pear tree"
  },
  "turtle-doves": "two"
  }
}
```

## Questions

󰠗  Can tab characters be used for indentation in YAML? ;; No, only spaces can be used for indentation. = #lang/config/yml
󰠗  What is the difference between a string in yaml that is quoted, and unquoted (`" "` vs ` `) ;; Nothing. They're only important to quote when they contain a value that can be mistaken for a special character. = #lang/config/yml 
󰠗  What two features in yaml let us rewrite snippets without any configuration? ;; Anchors and aliases = #lang/config/yml 
