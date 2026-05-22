---
summary: "Highlight groups are either editor interface or syntax highlighting. "
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/item
date created: Tuesday, November 11th 2025, 9:20:41 am
date modified: Tuesday, November 11th 2025, 9:23:00 am
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Syntax - Neovim docs](https://neovim.io/doc/user/syntax.html#%3Ahighlight)

## Concepts of Note
- Highlight groups can be linked to one another.
## Usage

  `:hi` ;;; List all the current highlight groups that have attributes set. = #tools/nvim
  `:hi {group-name}` ;;; List one highlight group. = #tools/nvim 
