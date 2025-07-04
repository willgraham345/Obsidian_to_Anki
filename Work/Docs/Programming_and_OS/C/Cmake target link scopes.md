---
summary: There are INTERFACE, PRIVATE, and PUBLIC scopes for linking libraries. The scope determines how libraries access their functionality (through direct or indirect methods/inheritance).
date created: Wednesday, October 16th 2024, 11:38:09 am
date modified: Wednesday, October 16th 2024, 11:39:48 am
type: note/concept
---
`VIEW[**{summary}**][text(renderMarkdown)]`
[CMake target\_link\_libraries() scopes | Declaration of VAR](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/)

# Really good Example
For example, let’s say we have a Project, which is a collection of libraries. This Project is used by some Tool (_so Tool depends on Project_) and also it has a dependency of its own (_so Project depends on Dependency_). In this case that Dependency library will be a _direct_ dependency for our Project and a _transitive_ dependency for the Tool:

![Relations between projects](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/relations.png)

Applying to this example, my understanding of the scopes would be the following:

- **PRIVATE** - the Tool gets `doThingy()` functionality of Dependency through `doTheThing()` function of AnotherLibrary and cannot get `doThingy()` function directly from Dependency:![CMake, PRIVATE linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/private.png)
    
- **INTERFACE** - the Tool gets `doThingy()` function directly from Dependency, while AnotherLibrary does not (_and so it no longer has `doTheThing()` function available_):![CMake, INTERFACE linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/interface.png)
    
- **PUBLIC** - the Tool can do both: get `doThingy()` functionality of Dependency through `doTheThing()` function of AnotherLibrary and get `doThingy()` function directly from Dependency:![CMake, PUBLIC linking](https://decovar.dev/blog/2023/07/22/cmake-target-link-libraries-scopes/images/public.png)
    

While `PRIVATE` and `PUBLIC` scopes make sense to me, I cannot think of a real-world example of `INTERFACE` linkage. Why would a library A link to library B only to make B available higher in the dependency chain, so without using B’s functionality itself?

The `INTERFACE` scope would probably make sense for a so-called “header-only” library (_which has no sources of its own, only headers_), when it provides linking to other libraries without using them itself. But I myself never needed to create such a thing, so I’m still puzzled about the actual use of the `INTERFACE` scope.