---
summary: Set of compiler and toolchain technologies. Used to transform between programming languages and ISAs for a variety of hardware architectures. Intended to be language-agnostic, and a "universal" compiler backend.
headings:
  - "[[#Concepts of Note]]"
type: note/tool/build/compiler
date created: Wednesday, December 10th 2025, 9:09:58 am
date modified: Wednesday, December 10th 2025, 9:25:13 am
implementations:
  - "[[Clang|Clangd]]"
tags:
  - lang/build/compiler
template: "[[base_note_template]]"
template-version: 1.0.0
tools:
  - "[[LLVM Debugger]]"
aliases: []
id: LLVM
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[LLVM - Wikipedia](https://en.wikipedia.org/wiki/LLVM)

## Concepts of Note
Takes programming languages, and writes it into the processor-specific ISA.
󰙎 LLVM ;; Low level virtual machine 

󰙎 IR ;; Intermediate representation

### How LLVM works
1. **Front‑end**  
   - Parses source code (e.g., C/C++ via Clang) and lowers it to LLVM IR.  
   - Other languages (Rust, Swift, Julia, etc.) provide their own front‑ends that emit the same IR.

2. **Middle‑end (Optimization Passes)**  
   - The IR is passed through a pipeline of transformation passes (e.g., dead‑code elimination, loop unrolling, inlining).  
   - Passes are independent of the source language and target architecture, allowing reuse across projects.

3. **Back‑end (Code Generation)**  
   - Targets are described by *target descriptions* that map IR constructs to machine instructions.  
   - LLVM includes back‑ends for x86, ARM, AArch64, RISC‑V, WebAssembly, and many others.  
   - The back‑end performs instruction selection, register allocation, and final assembly emission.

4. **Tooling**  
   - **llvm‑as / llvm‑dis** – assemble/disassemble textual IR.  
   - **opt** – run optimization passes on IR files.  
   - **llc** – compile IR to native assembly.  
   - **clangd** (listed on line 7) provides IDE features using the same front‑end.  
   - **LLVM Debugger** (line 11) offers a low‑level debugging experience for IR and generated code.


### Why LLVM Is “Universal”

- **Language‑agnostic IR**: All front‑ends emit the same low‑level, typed, SSA‑based representation.  
- **Target‑agnostic back‑ends**: Adding a new ISA only requires a target description; the same optimization pipeline works unchanged.  
- **Pluggable passes**: Projects can insert custom analysis or transformation passes without rewriting the whole compiler.  


### Takeaway

When you need to support a new language or a new hardware platform, you can often reuse LLVM’s existing front‑ends, optimization passes, and back‑ends, focusing only on the parts that are truly language‑ or hardware‑specific.

