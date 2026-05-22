---
summary: Specifies where the executable target should look for include files
type: note/function
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Flashcards]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
implements:
  - "[[CMake target]]"
aliases: []
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, March 18th 2026, 8:17:48 pm
id: CMake target_include_directories
tags: []
template:
template-version:
used_by:
  - "[[CMake Libraries]]"
  - "[[Cpp include|C include]]"
---

# Summary
󰙎 `target_include_directories` ;;; “Specifies include‑path directories for a CMake target, controlling header search order and visibility (PRIVATE/ PUBLIC/ INTERFACE).”  

# Additional Background  
- [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories")

## Concepts of Note
- **Visibility flags** – [[CMake PRIVATE]], [[CMake PUBLIC]], [[CMake INTERFACE]].  
- **SYSTEM** keyword – suppresses warnings for system headers.  
- **Transitive propagation** – how [[CMake PUBLIC]]/[[CMake INTERFACE]] affect dependent targets.  

## Usage
 `target_include_directories(myLib PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src)` ;;; Private include of all directories in `src/` for `myLib`. 


## Examples

### Specify include directories that are required when linking to a library
```cmake
add_library(foo foo.cxx)
target_include_directories(foo PUBLIC
                           "${CMAKE_CURRENT_BINARY_DIR}"
                           "${CMAKE_CURRENT_SOURCE_DIR}"
                           )
```
- Anything that links to the target will automatically have `foo`'s binary and source as directories
	- The order of the include directories brought in through [[CMake Usage Requirements for a Library]], will match the order of the targets in the [[CMake target_link_libraries]] call. 

## Diagrams
```
@startuml
node "myLib (PRIVATE)" as A
node "myApp (depends on myLib)" as B
node "otherLib (PUBLIC)" as C
A --> B : compile
C --> A : compile
@enduml
```  

## Flashcards
Add flashcards using third‑schema:  

󰠗 What does the [[CMake INTERFACE]] keyword do in `target_include_directories`? ;; It adds the directory only to dependents; the target itself does not use it for compilation.  
󰠗 How does the SYSTEM keyword affect include directories? ;; It marks the directories as system include paths, suppressing compiler warnings.  

