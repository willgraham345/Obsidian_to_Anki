---
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
concepts:
  - "[[CMake Scope for Target Links]]"
  - "[[CMake Variables Scope]]"
similar:
  - "[[CMake Variables]]"
aliases: [CMake PRIVATE, CMake PUBLIC, CMake scope]
concept_of:
  - "[[CMake target]]"
  - "[[CMake Variables]]"
  - "[[CMake]]"
date created: Monday, March 2nd 2026, 3:38:58 pm
date modified: Monday, March 2nd 2026, 4:40:13 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
implements:
  - "[[CMake target]]"
implementations:
  - "[[CMake target_sources]]"
  - "[[CMake target_link_libraries]]"
  - "[[CMake Libraries]]"
uses:
  - "[[CMake set]]"
---

# Summary
󰙎 CMake Scope ;;; Various aspects of when something is or isn't accessible within CMake.

# Additional Background

## Concepts of Note
### Variable Visibility and Scope
󰙎 CMake variable visibility ;;; A variable in CMake created using `set()` will have scope that is 
- See [[CMake set]] for a good explanation

#### Default variable scope visibility
- Current `CMakeLists` file or function
- Any subdirectory's CMakeLists files
- Functions or macros that are invoked
- Any files that are included with the [[CMake include]] command

When a new subdirectory is processed (or a function is called), a new variable scope is created and initialized wiht the curernt value of all variables in the calling scope. 
- Any new variables created will be within the child scope. Changes to existing variables will not impact parent scope.

### Target Visibility
- This is NOT the types of targets (see [[CMake target#Types of Targets]])
󰙎 `PUBLIC` ;;; Stuff following this is used to build **me** and anyone **linking** me
󰙎 `PRIVATE` ;;; Stuff following this is used to build **me** and only me.

#### When to use each
##### PRIVATE
##### Public

## Examples
### CMake Scope within Target Links
For example, let’s say we have a Project, which is a collection of libraries. This Project is used by some Tool (_so Tool depends on Project_) and also it has a dependency of its own (_so Project depends on Dependency_). In this case that Dependency library will be a _direct_ dependency for our Project and a _transitive_ dependency for the Tool:

![Relations between projects](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/relations.png)

Applying to this example, my understanding of the scopes would be the following:

- **PRIVATE** - the Tool gets `doThingy()` functionality of Dependency through `doTheThing()` function of AnotherLibrary and cannot get `doThingy()` function directly from Dependency:![CMake, PRIVATE linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/private.png)
    
- **INTERFACE** - the Tool gets `doThingy()` function directly from Dependency, while AnotherLibrary does not (_and so it no longer has `doTheThing()` function available_):![CMake, INTERFACE linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/interface.png)
    
- **PUBLIC** - the Tool can do both: get `doThingy()` functionality of Dependency through `doTheThing()` function of AnotherLibrary and get `doThingy()` function directly from Dependency:![CMake, PUBLIC linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/public.png)
    

While `PRIVATE` and `PUBLIC` scopes make sense to me, I cannot think of a real-world example of `INTERFACE` linkage. Why would a library A link to library B only to make B available higher in the dependency chain, so without using B’s functionality itself?

The `INTERFACE` scope would probably make sense for a so-called “header-only” library (_which has no sources of its own, only headers_), when it provides linking to other libraries without using them itself. But I myself never needed to create such a thing, so I’m still puzzled about the actual use of the `INTERFACE` scope.