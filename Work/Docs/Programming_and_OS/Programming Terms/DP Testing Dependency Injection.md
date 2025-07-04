---
summary: An object or function receives other objects/functions it requires rather than creating them internally. Tight coupling between code is bad and inflexible. We want to avoid hard-coded dependencies.
concepts:
  - "[[DP Testing Constructor Injection]]"
  - "[[DP Testing Interface Injection]]"
  - "[[DP Testing Property Injection]]"
date created: Wednesday, November 6th 2024, 9:29:18 am
date modified: Wednesday, November 6th 2024, 9:35:57 am
type: note/concept
---

`VIEW[**{summary}**][text(renderMarkdown)]`

```breadcrumbs
title: Breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

How can a class be independent of the creation of the objects it depends on?
How can an application, and the objects it uses support different configurations?

<iframe src="https://builtin.com/articles/dependency-injection#:~:text=The%20three%20types%20of%20dependency,property%20injection%20and%20method%20injection." style="width: 100%; height: 800px;"></iframe>
