---
template: "[[base_note_template]]"
template-version: 1.0.2
type: note/concept
next:
  - "[[CS Compiler]]"
uses:
  - "[[CS Token]]"
  - "[[Cpp macros]]"
  - "[[Cpp ifdef]]"
  - "[[C error]]"
implementations:
  - "[[gcc and gpp]]"
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
prev:
  - "[[CS Compiler Driver]]"
---

# Summary
󰙎 CS Preprocessor ;;; “The preprocessor, called cpp in a GNU-based toolchain, performs three main activities that, at least conceptually, take place before the source code is passed to the compiler proper. They are: File inclusion, invoked by the include directive. Macro definition, by means of the define directive, and expansion.Conditional inclusion/exclusion of part

Excerpt From
Real-Time Systems Development with RTEMS and Multicore Processors
Bloom, Gedare
This material may be protected by copyright.
# Additional Background
- [I] Plaintext substitution ;;; Code is translated into tokens for the compiler. 
## Concepts of Note
If the input token is a Preprocessor keyword ([[C define]] and [[Cpp include]]), then the Preprocessor analyzes the tokens and follows the statement. 
## Diagrams
![[CS Preprocessor.png]]
