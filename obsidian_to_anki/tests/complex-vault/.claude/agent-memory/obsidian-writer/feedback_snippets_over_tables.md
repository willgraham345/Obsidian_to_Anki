---
name: use snippet inline patterns instead of tables for method/property listings
description: In library/API notes, use `- [p] \`ClassName.method()\` ;;; description` snippet pattern over markdown tables for method listings
type: feedback
---

Use the snippet inline pattern (`- [p] \`ClassName.method(args)\` ;;; description`) instead of markdown tables when documenting methods, properties, or API surface in library notes. The `- [p]` prefix is required — it is the Obsidian task marker that renders as the snippet icon.

**Why:** User explicitly rejected table-formatted and bare-icon-formatted sections. The correct form requires `- [p]` before the backtick code. Matches vault's concise inline style.

**How to apply:** In `## Properties` sections for library notes, list each method or attribute as `- [p] \`code\` ;;; description`. Include the class name in the snippet when context is needed (e.g., `ContainerCollection.run()` not just `.run()`). Term definitions in `## Concepts of Note` use `- [I] term ;;; description`.
