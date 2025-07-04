---
summary: Using lazy (not necessarily lazyvim the distro) to manage configuration of different plugins.
headings: ["[[#Concepts of Note]]", "[[#Media]]"]
type: note/concept
concept_of: ["[[Neovim lazy]]"]
date created: Tuesday, April 1st 2025, 10:11:38 am
date modified: Wednesday, May 14th 2025, 12:15:31 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Media
[lazy.nvim](https://lazy.folke.io/)

## Concepts of Note
### Use `opts` instead of `config`. 
> [!success]
> ```lua
> { "folke/todo-comments.nvim", opts = {} },
> ```

You can also do:
```lua
opts = function()
...
end
```
and:
```lua

```
> [!danger]
> ```lua
> {  "folke/todo-comments.nvim",
> config = function()
	> require("todo-comments").setup({})
> end,
> },
> ```

## Media

> [!NOTE] Really good website here...
> [Customizing Plugins \| AstroNvim Documentation](https://docs.astronvim.com/configuration/customizing_plugins/)
