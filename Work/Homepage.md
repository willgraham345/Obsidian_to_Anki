---
date created: Tuesday, August 20th 2024, 2:05:31 pm
date modified: Wednesday, June 18th 2025, 3:04:41 pm
---


```meta-bind-button
label: Open QuickSwitcher
icon: compass
style: default
class: ""
cssStyle: ""
tooltip: ""
id: ""
hidden: false
actions:
  - type: command
    command: darlal-switcher-plus:switcher-plus:open

```

```meta-bind-button
label: Manage workspaces
icon: book
style: default
class: ""
cssStyle: ""
backgroundImage: ""
tooltip: ""
id: ""
hidden: false
actions:
  - type: command
    command: workspaces:open-modal

```

```meta-bind-button
label: Open Command DB
icon: file
hidden: false
class: ""
tooltip: ""
id: ""
style: default
actions:
  - type: open
    link: "[[Command DB]]"
    newTab: true

```

## Cheatsheets:
```dataview
TABLE
	type, file.mtime as "Last Modified Time"
WHERE type = "cheatsheet"
```

## Tag Pages:
```dataview
TABLE file.mtime as "Last Modified", type
WHERE type = "tag_page" and file.name != "Template Tag Page"
SORT file.name ASC
```
 