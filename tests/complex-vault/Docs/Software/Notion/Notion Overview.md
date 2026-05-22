---
type: note
---
# Background
Everything in notion is stored within blocks. 
- There are over 90 blocks. You can create just about anything with these blocks. 
```mermaid
---
title: Notion class Diagram
---
classDiagram
	class block
	class page{
		title
		icon
		cover
		comments
		backlinks
	}
	class todo
	class paragraph
	todo --|> block
	paragraph --|> block
	synced_blocks --|> block
	page *-- todo: Composed of
	page *-- paragraph: Composed of
	page *-- synced_blocks : Composed of
```
Pages can be nested within one another, and exist inside of databases

Blocks can be edited and turned into different types of blocks on the fly.
- Pages are essentially blocks, and you can use them to use other stuff. 
[Types of Blocks](https://thomasfrank.notion.site/Notion-Block-Reference-All-of-Notion-s-Blocks-8b40147600284c60b6f708e38f16ee68)

# Usage
