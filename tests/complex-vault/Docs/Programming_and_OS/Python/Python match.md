---
summary: As of v3.10, python can officially support match statements similar to other languages.
headings: ["[[#Syntax]]"]
type: note/item
date created: Monday, December 1st 2025, 10:17:08 am
date modified: Monday, December 1st 2025, 10:19:52 am
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Syntax
- [p] `match x:`
      `case 10:`
      `print("nice")`
      `case _:`
      `print("bummer")` = Create a match statement for variable `x` that prints `nice` if `x=10`, and `bummer` if `x` is anything else. = #lang/control_flow/match 