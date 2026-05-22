---
template: "[[base_note_template]]"
template-version: 1.0.2
type:
aliases: []
id: Linux jq
tags: []
---

# Summary
󰙎 jq ;;; lightweight command‑line JSON processor for DevOps pipelines
# Additional Background
[jq manual](https://jqlang.org/manual/)

## Usage
### Extracting fields
```bash
# Single field
echo '{"name":"Alice","age":30}' | jq '.name'
# → "Alice"

# Nested field
echo '{"user":{"city":"NYC"}}' | jq '.user.city'
# → "NYC"
```
### Arrays
```bash
# Get array element by index
echo '[10, 20, 30]' | jq '.[1]'
# → 20

# Get all elements
echo '[{"name":"Alice"},{"name":"Bob"}]' | jq '.[]'

# Map over array
echo '[1,2,3]' | jq '[.[] | . * 2]'
# → [2, 4, 6]
```
### Filtering Arrays
```bash
# Select where condition is true
echo '[{"name":"Alice","age":30},{"name":"Bob","age":17}]' | jq '[.[] | select(.age >= 18)]'
# → [{"name":"Alice","age":30}]
```
### Builtins
```bash
# Length
echo '[1,2,3]' | jq 'length'              # → 3

# Keys of an object
echo '{"a":1,"b":2}' | jq 'keys'          # → ["a", "b"]

# Sort array
echo '[3,1,2]' | jq 'sort'                # → [1, 2, 3]

# Sort array of objects by field
jq 'sort_by(.age)' data.json

# Unique values
echo '[1,2,2,3,1]' | jq 'unique'          # → [1, 2, 3]

# Sum
echo '[1,2,3,4]' | jq 'add'               # → 10
```
