---
type: note/component
components:
  - "[[Mermaid Flowchart Shapes]]"
---

# Background
[Flowchart Syntax Site](https://mermaid.js.org/syntax/flowchart.html)
# Usage
## Syntax
### Graph Direction
```
flowchart LR
```
- `TD` = Top to down
- `LR` = Left to right
- `TB` = Bottom to up
### Elements
```
element_1
```
- [[Mermaid General Stuff#Mermaid formatting]]
#### Element Shapes
```
node["square"]
node("rounded edges")
node(["stadium-shaped"])
node((Circle))
```
##### Subroutine
```
node[[in_subroutine]]
```
##### Cylindrical
```
node[(Database)] %data
```
##### 
### Subgraph
```
flowchart LR
  subgraph TOP
    direction TB
    subgraph B1
        direction RL
        i1 -->f1
    end
    subgraph B2
        direction BT
        i2 -->f2
    end
  end
  A --> TOP --> B
  B1 --> B2
```

### Relationships
| Length                          | 1      | 2       | 3        |
| ------------------------------- | ------ | ------- | -------- |
| Normal                          | `---`  | `----`  | `-----`  |
| Normal with arrow               | `-->`  | `--->`  | `---->`  |
| Thick                           | `===`  | `====`  | `=====`  |
| Thick with arrow                | `==>`  | `===>`  | `====>`  |
| Dotted                          | `-.-`  | `-..-`  | `-...-`  |
| Dotted with arrow               | `-.->` | `-..->` | `-...->` |
| Invisible (good for formatting) | `~~~`  | `~~~~`  | `~~~~~`  |
# Examples
