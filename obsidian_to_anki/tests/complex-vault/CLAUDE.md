# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

This is an Obsidian vault — a markdown-based personal knowledge base. There is no build system, package manager, or test runner. The "code" here is primarily YAML front-matter, Dataview queries (SQL-like), and Templater scripts (JavaScript).

For full vault conventions, read **AGENTS.md** at the root. It covers link styles, template usage, note type taxonomy, and guidance for creating/modifying notes.

## Architecture

The vault is organized into these primary domains:

- **`Docs/`** — Technical reference library. Language-specific knowledge lives under `Docs/Programming_and_OS/<Lang>/` with sub-folders per concern (Syntax, StdLib, Build, Testing, Debug, Interop).
- **`Projects/`** — One sub-folder per project (e.g., `Projects/p020`). Project notes use `type: project`.
- **`Notes/`** — Temporal notes: `Daily/`, `Weekly/`, `Fleeting/`, `Meetings/`, `PRs/`.
- **`zz_Templates/`** — All templates. `template_classes/` has core scaffolds; `dataviewScripts/` has JS snippets; `apply_properties/` has front-matter automation scripts.
- **`Vault_Tools/`** — Dataview queries and utility notes.
- **`Archive/`** — Deprecated/historical material; don't add new content here.

## Front-Matter Requirements

Every note needs these YAML front-matter fields:

```yaml
---
type: <project|note/system|research|meeting|fleeting|hub|tag_page|todo|reference|example|tutorial>
tags: []
date created: <timestamp>
date modified: <timestamp>
---
```

## Key Plugin Interactions

- **Dataview** — SQL-like queries embedded in notes. Reuse existing queries from `Vault_Tools/Queries` before writing new ones.
- **Templater** — JavaScript-based templating. Templates in `zz_Templates/template_classes/` are invoked via the `template:` front-matter key.
- **Breadcrumbs** — Hierarchical navigation. Use `[[Parent]] > [[Child]]` syntax in a `#Breadcrumbs` block. Update breadcrumb blocks when moving notes.
- **Meta-Bind** — Button widgets in notes (used in `Homepage.md`). Syntax: ` ```meta-bind-button``` ` blocks.

## Conventions

- Use `[[Exact Note Title]]` for wiki-links. Tags use `/` as hierarchy delimiter (e.g., `#programming/rust`).
- New projects go in `Projects/<folderTitle>/` using `project_template.md`.
- New research topics go in `Docs_Research_Industry/Topics/<Topic>/` with `type: research`.
- When adding a top-level tag, create a corresponding `TagPages/<tag>_Tags.md` using `tag_page.md` template.
- Check `template-version` in a note's front-matter against the source template when updating stale notes.
