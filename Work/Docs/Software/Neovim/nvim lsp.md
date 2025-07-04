---
summary: Meant to standardize the protocol for a language server (thing that analyzes your code) interacts with development tools.
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
type: note/component
date created: Friday, June 27th 2025, 10:56:21 am
date modified: Friday, June 27th 2025, 11:34:38 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- The neovim lsp client is usually configured through `nvim-lspconfig`
- The language server is what's made by a 3rd party, typically made for each language.
- The framework for working with LSPs is `vim.lsp`

## Usage

### Absolute basics
```lua
vim.lsp.start({
	name = 'my-server-name',
	cmd = {'name-of language-server-executable'},
	root_dir = vim.fs.dirname(vim.fs.find({'setup.py', 'pyproject.toml'}, {upward = true})[1]),
})
```
- You can then hook this to an autocommand that would attach when the language is detected... 

### Managing language servers
- The preferred way to deal with this is to use mason. Configure this right from neovim.