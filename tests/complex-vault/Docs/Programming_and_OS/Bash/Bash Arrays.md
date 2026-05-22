---
summary: Indexed and associative arrays in Bash — initialization, access, iteration, and manipulation
type: note/concept
ai_generated: true
concept_of:
  - "[[Bash Basics]]"
tags:
  - lang/syntax
date created: Wednesday, April 9th 2026, 12:00:00 pm
date modified: Wednesday, April 9th 2026, 12:00:00 pm
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note

- [I] indexed array ;;; Zero-indexed ordered list; declared with `arr=(...)`
- [I] associative array ;;; Key-value map; requires `declare -A` before use
- [I] array element ;;; Single item accessed by index `${arr[n]}` or key `${arr[key]}`
- [I] array length ;;; Total element count; accessed with `${#arr[@]}`

## Usage

### Indexed Arrays

- [p] `Fruits=(Apple Banana Cherry)` ;;; Declare an indexed array
- [p] `${Fruits[0]}` ;;; Access element at index 0
- [p] `${Fruits[@]}` ;;; All elements (each as a separate word)
- [p] `${#Fruits[@]}` ;;; Array length
- [p] `Fruits+=("Mango")` ;;; Append element
- [p] `unset Fruits[0]` ;;; Delete element at index 0
- [p] `${Fruits[@]:1:2}` ;;; Slice — 2 elements starting at index 1

### Associative Arrays

- [p] `declare -A dict` ;;; Declare an associative array
- [p] `dict[key]=value` ;;; Set a key-value pair
- [p] `${dict[key]}` ;;; Get value by key
- [p] `${!dict[@]}` ;;; All keys
- [p] `${dict[@]}` ;;; All values

## Examples

```bash
# Indexed array
Fruits=(Apple Banana Cherry)
echo "${Fruits[0]}"        # Apple
echo "${Fruits[@]}"        # Apple Banana Cherry
echo "${#Fruits[@]}"       # 3
Fruits+=("Mango")
echo "${Fruits[@]:1:2}"    # Banana Cherry

for f in "${Fruits[@]}"; do
  echo "$f"
done

# Associative array
declare -A capitals
capitals[France]="Paris"
capitals[Japan]="Tokyo"
echo "${capitals[France]}"  # Paris

for key in "${!capitals[@]}"; do
  echo "$key => ${capitals[$key]}"
done
```
