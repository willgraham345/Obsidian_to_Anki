---
name: prefer breadcrumb front-matter over inline term defs for artifact/relationship links
description: When note relationships (uses, used_by, outputs, etc.) can be expressed as front-matter breadcrumb fields, do so instead of writing inline term definition entries for them
type: feedback
---

Use front-matter breadcrumb fields (`uses`, `used_by`, `tool_of`, `similar`, `associations`, etc.) to express relationships between notes rather than defining them as inline `󰙎 term ;;; description` entries in body sections like `### Output Artifacts`.

**Why:** Inline term defs are for concepts/API items that need explanation. Relationships between notes are better expressed as breadcrumb links — they power the Breadcrumbs plugin navigation and keep note bodies lean.

**How to apply:** When drafting a section that would just enumerate related notes (e.g. "Output Artifacts: toolchain, kernel, rootfs, bootloader"), move those links to front-matter breadcrumb fields instead. Only keep an inline section if the items require non-obvious explanation beyond a link.
