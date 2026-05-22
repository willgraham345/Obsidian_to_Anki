---
template: "[[base_note_template]]"
template-version: 1.0.0
summary: A standardized protocol invented by Microsoft to provide autocomplete, highlighting, and syntax for languages. Typically operates through a client and server architecture.
type: note/tool
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
- Uses jsonrpc to communicate

[Understanding the Language Server Protocol](https://packagemain.tech/p/understanding-the-language-server-protocol)
## Examples
An example request to an LSP for a current document. 
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/completion",
  "params": {
    "textDocument": {
      "uri": "file:///home/alex/code/test/main.go"
    },
    "position": {
      "line": 35,
      "character": 21
    }
  }
}
```