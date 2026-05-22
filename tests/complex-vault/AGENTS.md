---
aliases: []
id: AGENTS
tags: []
---

**AGENTS.md**

---

### Vault Overview
This vault is a mixed‑purpose knowledge base used for personal knowledge management, project tracking, research, and software development.  
Key top‑level folders:

| Folder | Primary Purpose |
|--------|------------------|
| `Docs/` | Technical reference, research notes, hardware/software documentation, career planning, and topic‑specific collections (e.g., `Docs/Programming_and_OS/`). |
| `Projects/` | Active and completed project workspaces (each project gets its own sub‑folder, e.g., `Projects/p020`). |
| `Notes/` | Daily, weekly, fleeting, meeting, and PR notes. |
| `People/` | Individual person pages (often used as “hub” for contacts). |
| `TagPages/` | Auto‑generated tag‑topic pages (used by the *Tag Page* plugin). |
| `zz_Templates/` | All note‑creation templates and supporting scripts. |
| `.obsidian/` | Vault‑wide settings, installed plugins, snippets, and theme configuration. |
| `Archive/` | Historical material, old projects, and deprecated templates. |
| `Vault_Tools/` | Helper queries, Dataview scripts, and other utility notes. |

The vault makes heavy use of the **Dataview**, **Templater**, **Breadcrumbs**, and **Meta‑Bind** plugins to create dynamic links, generate front‑matter, and surface backlinks.

---

### 1. Links Between Notes
| Convention | Example | Description |
|-------------|---------|-------------|
| **Standard Wiki‑link** | `[[Some Note]]` | Creates a bidirectional link; back‑link shows up in the linked note’s *Backlinks* pane. |
| **Breadcrumbs** | `[[Parent]] > [[Child]]` (often placed in a `#Breadcrumbs` block) | Provides a hierarchical navigation trail. The *breadcrumbs* plugin renders the trail as a clickable path. |
| **Tag‑based navigation** | `#math/systems` | Tags are used as a taxonomy. TagPage‑MD generates a page per tag (e.g., `TagPages/systems_Tags.md`). |
| **Dataview queries** | ```dataview table status from "Projects" where type = "project"``` | Pulls data from front‑matter across the vault. Queries live in notes under `Vault_Tools/Queries` and are also reused via the *dataview queries* template. |
| **Template‑generated links** | `template: "[[project_template]]"` in front‑matter | When a new note is created from a template, any placeholder `[[Link]]` inside the template is automatically resolved. |
| **Meta‑bind buttons** | ```meta‑bind‑button``` blocks in `Homepage.md` | Provide quick‑action UI elements (open a note, run a command, etc.) without leaving the note. |

**Best practice for agents**  
- Prefer `[[Note Name]]` for any reference that may require a backlink.  
- Use breadcrumb syntax for hierarchical structures (e.g., a project’s overview → sub‑task → specific discussion).  
- When a tag is the primary classifier, add it to the front‑matter `tags:` list and optionally embed a `#tag` in the body for the *Tag Page* plugin to surface it.  

---

### 2. Templates
All templates reside under `zz_Templates/`.  They are categorized by purpose and are referenced in notes via the `template:` front‑matter key.

| Sub‑folder | Purpose | Representative files |
|-----------|---------|------------------------|
| `template_classes/` | Core note‑type scaffolds (project, research, meeting, fleeting, jira_issue, tag_page, etc.) | `project_template.md`, `research_template.md`, `meeting_template.md` |
| `JournalRelated/` | Daily/Weekly note structures | `Daily Note Template.md`, `Weekly Note Template.md` |
| `apply_properties/` | Scripts that add or modify front‑matter properties after note creation (e.g., `process_apply.md`, `research_apply.md`). |
| `breadcrumbTemplates/` | Pre‑written breadcrumb blocks for easy insertion (`breadcrumbs_down.md`). |
| `dataviewQueries/` | Ready‑to‑use Dataview queries (e.g., `dv backlinks-by-time-with-summary.md`). |
| `dataviewScripts/` | JavaScript snippets for advanced Dataview use (e.g., `projectQueryList.js`, `peopleTableQuery.js`). |
| `Template_scripts/` | Misc. helper scripts (currently empty). |

**How a template is invoked**  
```yaml
---
template: "[[project_template]]"
template-version: 1.0.0
---
```
The *Templater* plugin inserts the content of `project_template.md` and resolves any embedded variables (`{{title}}`, `{{date}}`, etc.).  Template versions are tracked in the front‑matter, allowing agents to detect outdated templates.

**Common required front‑matter fields**  
| Field | Typical values | Meaning |
|-------|----------------|--------|
| `type` | `project`, `note/system`, `research`, `meeting`, `fleeting` … | Categorises the note for queries and tag pages. |
| `tags` | `["math/systems"]`, `["project"]` | Enables tag‑based navigation. |
| `date created` / `date modified` | Human‑readable timestamps | Used by the *Meta‑bind* buttons for quick access. |
| `aliases` | List of alternate names | Allows multiple link spellings. |
| `contexts` | Custom list (e.g., `parent, rust, oxi_msg`) | Free‑form classification used by agents. |

---

### 3. Knowledge‑Center (Hub) Notes
These notes act as entry points to large collections and typically contain a **table of contents** built with Dataview or manual links.

| Hub Note | Location | Content Highlights |
|----------|----------|-------------------|
| **Homepage.md** | Root | Buttons to open QuickSwitcher, workspace manager, and the *Command DB*; contains global navigation shortcuts. |
| **Systems.md** 
| **Programming_and_OS Hub.md** | `Docs/Programming_and_OS/` | **New hub** that aggregates language‑specific knowledge bases (Python, Rust, C++). Uses Dataview to pull notes where `tags` contain `programming/<lang>` and `type` is `note/system` or `research`. |
stems/Systems.md` | Front‑matter `type: note/system`; lists system‑related concepts with tags `#math/systems`. |

**Guidance for agents**  
- When creating a new collection, add a corresponding hub note with a Dataview table that filters by `type:` or by a dedicated tag.  
- Keep the hub note’s front‑matter `type: hub` (or a custom value) so future queries can discover it.  

### Systems (high‑level categories)  

| System | Description | Typical folder | Primary tag(s) |
|--------|-------------|----------------|----------------|
| **Language Overview** | General characteristics, history, ecosystem | `Docs/Programming_and_OS/<Lang>/` | `#programming/<lang>` |
| **Syntax & Semantics** | Grammar, language constructs, idioms | `Docs/Programming_and_OS/<Lang> Syntax/` | `#programming/<lang>/syntax` |
| **Standard Library** | Core modules, APIs, examples | `Docs/Programming_and_OS/<Lang>/StdLib/` | `#programming/<lang>/stdlib` |
| **Package Management** | Dependency managers, repos, versioning | `Docs/Programming_and_OS/<Lang>/Packaging/` | `#programming/<lang>/packaging` |
| **Build & Tooling** | Compilers, build systems, CI pipelines | `Docs/Programming_and_OS/<Lang>/Build/` | `#programming/<lang>/build` |
| **Testing** | Unit, integration, property‑based testing frameworks | `Docs/Programming_and_OS/<Lang>/Testing/` | `#programming/<lang>/testing` |
| **Debugging & Profiling** | Debuggers, profilers, tracing tools | `Docs/Programming_and_OS/<Lang>/Debug/` | `#programming/<lang>/debug` |
| **Interoperability** | FFI, bindings, cross‑language bridges | `Docs/Programming_and_OS/<Lang>/Interop/` | `#programming/<lang>/interop` |

> **Example paths**  
> * Python: `Docs/Programming_and_OS/Python/StdLib/AsyncIO.md`  
> * Rust:   `Docs/Programming_and_OS/Rust/Build/Cargo.md`  
> * C++:    `Docs/Programming_and_OS/Cpp/Testing/GoogleTest.md`

#### Note Types Used Within Programming_and_OS  

| `type` value | When to use | Example note |
|--------------|-------------|--------------|
| `note/system` | High‑level overview of a system (e.g., “Python Standard Library”). | `Docs/Programming_and_OS/Python/StdLib/Overview.md` |
| `reference` | Precise API or command reference; often includes code signatures and parameter tables. | `Docs/Programming_and_OS/Rust/StdLib/Vec.md` |
| `example` | Small, self‑contained code snippets illustrating a concept. | `Docs/Programming_and_OS/Cpp/Interop/PythonBinding_Example.md` |
| `tutorial` | Step‑by‑step guide that walks the reader through a workflow. | `Docs/Programming_and_OS/Python/Testing/pytest_Tutorial.md` |
| `research` | Exploratory comparison, performance benchmarks, or design discussions. | `Docs/Programming_and_OS/Rust/Research/MemoryModel_Study.md` |
| `project` | A concrete implementation project that uses the language (e.g., a CLI tool). | `Projects/p020 - Create messaging framework for Rust.md` |

### 4. Note Types (Front‑matter `type:` values)
The vault uses a small but extensible taxonomy.  Below are the most common values and their intended usage.

| `type` value | Typical folder | Example notes | Usage |
|--------------|----------------|---------------|-------|
| `project` | `Projects/` | `p020 - Create messaging framework for Rust.md` | Tracks an active project; used by project‑specific Dataview queries. |
| `note/system` | `Docs/Systems/` | `Systems.md` | Represents a system‑level concept; often tagged `#math/systems`. |
| `research` | `Docs_Research_Industry/Topics/…` | `Space.md` (research topic) | Marks research‑oriented notes, usually linked from a *Research TOC*. |
| `meeting` | `Notes/Meetings/` | `2024-08-20 Radiant.md` | Meeting minutes; template provides a standard agenda and action‑item sections. |
| `fleeting` | `Notes/Fleeting/` | `2026-02-07 IRAD process.md` | Capture quick ideas; life‑cycle is short. |
| `hub` (custom) | Root or `Docs/` | `Homepage.md`, `Web of People TOC.md` | Central navigation pages; agents can locate them via `type: hub`. |
| `tag_page` | `TagPages/` | `systems_Tags.md` | Generated by the *Tag Page* plugin; front‑matter includes a `tag-page-query`. |
| `todo` | Various | `TODO.md` | Simple task lists, often paired with the *Tasks* plugin. |

Agents should read the `type` field to decide how to handle a note (e.g., include it in a project report, surface it on a knowledge‑center page, or skip it when generating a research bibliography).

---

### 5. Conventions & Constraints
1. **Front‑matter format** – YAML block delimited by `---`.  All mandatory keys (`type`, `tags`, `date created`) must be present.  
2. **Tag taxonomy** – Tags are hierarchical, using `/` as a delimiter (e.g., `#math/systems`).  The *Tag Page* plugin creates a page per top‑level tag (`#math/*`).  
3. **Backlink hygiene** – When a note is renamed, the *Obsidian‑auto‑link‑title* and *Metadata‑Menu* plugins automatically update backlinks, but agents should still verify that no orphan links remain.  
4. **Template versioning** – The `template-version` key is used to signal when a note should be refreshed.  Agents can compare the note’s version to the template’s current version in `zz_Templates`.  
5. **Folder hierarchy** –  
   - `Docs/` mirrors subject domains (`Programming_and_OS`, `Hardware`, `Software`, `Math and Physics`).  
   - `Projects/` holds one folder per project (`p020`, `VivaPro`, …).  
   - `Notes/` is split into temporal categories (`Daily`, `Weekly`, `Fleeting`, `Meetings`).  
   - `Archive/` stores any deprecated or historical material.  
6. **Link style** – Use *exact* note titles inside double brackets.  For dynamic linking (e.g., to a tag page) use the `#tag` syntax.  
7. **Dataview usage** – Queries are stored in `Vault_Tools/Queries` and referenced with `dataview: source="..."`.  Agents should prefer re‑using existing queries rather than writing new ones, unless a new data shape is required.  

---

### 6. How Future Agents Should Interact with the Vault
| Task | Recommended Approach |
|------|----------------------|
| **Create a new project note** | Use the `project_template.md` (via Templater) which fills `type: project`, sets `tags: ["project"]`, and adds a breadcrumb block. |
| **Add a research topic** | Place the note under `Docs_Research_Industry/Topics/<Topic>/`, set `type: research`, add appropriate hierarchical tags (e.g., `#research/ai`). |
| **Update a hub/knowledge‑center** | Open the hub note, add a Dataview query that selects notes by `type` or tag, and ensure the front‑matter includes `type: hub`. |
| **Find all notes of a given type** | Run a Dataview query: `table file.link as "Note" from "" where type = "project"` – this works across the whole vault. |
| **Maintain template consistency** | Compare a note’s `template-version` to the current version in its source template; if mismatched, run the *Templater* command “Apply Template Changes” (provided by the *templater‑obsidian* plugin). |
| **Navigate via breadcrumbs** | Insert the `breadcrumbs_down.md` snippet (via *QuickAdd* or manual paste) to any note that is part of a hierarchy; agents should update the breadcrumb block when moving notes. |
| **Add a new tag** | Add the tag to the note’s `tags:` list in front‑matter; optionally create a `TagPages/<tag>_Tags.md` file using the `tag_page.md` template if the tag is top‑level. |

---

**End of AGENTS.md**  

*This document is intended for automated agents that need to read, create, or modify notes in the vault.  It provides the essential conventions, template locations, and navigation patterns to ensure consistency throughout the knowledge base.*
