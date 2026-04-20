---
summary: 
headings: ["[[#Concepts of Note]]", "[[#Examples]]"]
type: note/keyword
associations: ["[[Cpp default]]"]
concept_of: ["[[Cpp Control Flow]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Tuesday, July 8th 2025, 12:27:24 pm
uses: ["[[Cpp attributes#^4207c2]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note

󰠗  Which is faster, a `switch` or an `if` statement in cpp? ;; A switch statement = #lang/control_flow/switch  
<!--ID: 1751999251022-->

󰠗  Does a cpp statement implicitly exit after executing a case block? ;; No, it requires `break` to exit. If letting multiple case statements execute a shared set of instructions, then a `[[fallthrough]]` statement is required = #lang/control_flow/switch 
<!--ID: 1751999251028-->



  `switch (varToLookAt)`<br>`case varVal1:`<br>`{`<br>`//statements`<br>`}`<br>`default:`<br>`{`<br>`//statements`<br>`}` ;;; How to define a switch statement in cpp. = #lang/control_flow/switch 
<!--ID: 1751999148574-->

## Examples
```cpp
switch (grade) {
  case 9:
    std::cout << "Freshman\n";
    break;
  case 10:
    std::cout << "Sophomore\n";
    break;
  case 11:
    std::cout << "Junior\n";
    break;
  case 12:
    std::cout << "Senior\n";
    break;
  default:
    std::cout << "Invalid\n";
    break;
}
```

## Keywords
### default
Signals compiled to jumpy to this case if no other cases evaluate as true

### break
Signals the compiler to jump out of a case statement 
