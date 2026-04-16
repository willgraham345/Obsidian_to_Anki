---
summary: Native OS threads, each have their own stack and local slate.
headings: ["[[#Concepts of Note]]", "[[#Diagrams]]"]
type: note/item
similar: ["[[Cpp Multithreading pthread]]", "[[Cpp thread]]"]
date created: Monday, August 4th 2025, 7:05:20 pm
date modified: Monday, August 11th 2025, 2:21:38 pm
item_of: ["[[Rust std]]"]
uses: ["[[Rust closures]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Using Rust scoped threads to improve efficiency and safety - LogRocket Blog](https://blog.logrocket.com/using-rust-scoped-threads-improve-efficiency-safety/)

## Concepts of Note
󰙎  Detached thread ;;; A thread with no way to alert/inform the program to learn when the spawned thread completes or otherwise terminates. = #lang/memory/threading/thread 
<!--ID: 1758253288420-->

󰙎  Scope ;;; A regulated environment that lets you manage numerous threads in your code.
󰙎  JoinHandle ;;; Has a `.join()` method which blocks. We use the `handle.join()` to wait for the thread to finish and have 
- [p] `thread::spawn(move ||`
      `// stuff`
      `});` = Create a new detached thread with `// stuff` as it's executed statements = #lang/memory/threading/thread 
- [p] `thread::scope(|scope| {`
      `s.spawn(|| { // statements });`
      `s.spawn(|| { // statements});`
      `});` = Crates a scope for spawning scoped threads. A `Scope` object, which can borrow non-`'static` data and guarantee that all threads will be joined at the end of the scope. Panics if any of the joined threads panicked. = #lang/memory/threading/thread/scope
  `let res ``= a.join();` ;;; Wait until a thread `a` is completed, and return the result of that thread as `res`. = #lang/memory/threading/thread 
<!--ID: 1758253288406-->

  `let handle ``= std::thread::current()` ;;; Creates a handle `handle` to the current thread that invokes it. = #lang/memory/threading/thread  
<!--ID: 1758253288413-->

󰠗  What function from `thread` creates a new thread? What does it return? ;; `std::thread::spawn()->JoinHandle` = #lang/memory/threading/thread  
<!--ID: 1758253288373-->

󰠗  What function waits for all threads to finish? ;; `std::thread::join()` = #lang/memory/threading/thread  
<!--ID: 1758253288379-->

󰠗  What struct controls the thread creation in `std thread`? What configurations are available? ;; `std::thread::Builder`, the `name`, and the `stack_size`  = #lang/memory/threading/thread  
<!--ID: 1758253288386-->


󰠗  What lifetimes are involved with scoped threads in `std::thread`? ;; `'scope` and `'env`. `'scope` is the lifetime of the scope, and the `'env` represents whatever was borrowed. Everything in `'env` must outlive the `'scope`. = #lang/memory/threading/thread  
<!--ID: 1758253288393-->


  ### Plain threads vs Scoped threads
󰠗  Why would you want to use a `std::thread::scope` instead of a simple `std::thread::spawn`? ;; When the `thread::scope` function completes, all the threads are guaranteed to be joined, so they can return borrowed data. = #lang/memory/threading/thread  
<!--ID: 1758253288400-->

  
## Diagrams %% fold %% 
![[Diagram-program-three-threads.avif | 600]]
