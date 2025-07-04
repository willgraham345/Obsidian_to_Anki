---
summary: 
type: note/component
date created: Wednesday, June 19th 2024, 2:46:43 pm
date modified: Thursday, December 19th 2024, 10:19:32 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Background
Metadata = key and value pair. 
- You can add any number of fields to a **note**, a **list item**, or a **task**
[[Person Template]]

# Implicit Fields for Pages

| Field Name         | Data Type      | Description                                                                                                                                                                      |
| ------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file.name`        | Text           | The file name as seen in Obsidians sidebar.                                                                                                                                      |
| `file.folder`      | Text           | The path of the folder this file belongs to.                                                                                                                                     |
| `file.path`        | Text           | The full file path, including the files name.                                                                                                                                    |
| `file.ext`         | Text           | The extension of the file type; generally `md`.                                                                                                                                  |
| `file.link`        | Link           | A link to the file.                                                                                                                                                              |
| `file.size`        | Number         | The size (in bytes) of the file.                                                                                                                                                 |
| `file.ctime`       | Date with Time | The date that the file was created.                                                                                                                                              |
| `file.cday`        | Date           | The date that the file was created.                                                                                                                                              |
| `file.mtime`       | Date with Time | The date that the file was last modified.                                                                                                                                        |
| `file.mday`        | Date           | The date that the file was last modified.                                                                                                                                        |
| `file.tags`        | List           | A list of all unique tags in the note. Subtags are broken down by each level, so `#Tag/1/A` will be stored in the list as `[#Tag, #Tag/1, #Tag/1/A]`.                            |
| `file.etags`       | List           | A list of all explicit tags in the note; unlike `file.tags`, does not break subtags down, i.e. `[#Tag/1/A]`                                                                      |
| `file.inlinks`     | List           | A list of all incoming links to this file, meaning all files that contain a link to this file.                                                                                   |
| `file.outlinks`    | List           | A list of all outgoing links from this file, meaning all links the file contains.                                                                                                |
| `file.aliases`     | List           | A list of all aliases for the note as defined via the [YAML frontmatter](https://help.obsidian.md/How+to/Add+aliases+to+note).                                                   |
| `file.tasks`       | List           | A list of all tasks (I.e., `\| [ ] some task`) in this file.                                                                                                                     |
| `file.tasks.text`  |                | Text for the tasks                                                                                                                                                               |
| `file.lists`       | List           | A list of all list elements in the file (including tasks); these elements are effectively tasks and can be rendered in task views.                                               |
| `file.frontmatter` | List           | Contains the raw values of all frontmatter in form of `key \| value` text values; mainly useful for checking raw frontmatter values or for dynamically listing frontmatter keys. |
| `file.day`         | Date           | Only available if the file has a date inside its file name (of form `yyyy-mm-dd` or `yyyymmdd`), or has a `Date` field/inline field.                                             |
| `file.starred`     | Boolean        | If this file has been bookmarked via the Obsidian Core Plugin "Bookmarks".                                                                                                       |

# Task Implicit Fields

| Field Name       | Data Type | Description                                                                                                                                                                                                                                                                                                             |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`         | Text      | The completion status of this task, as determined by the character inside the `[ ]` brackets. Generally a space `" "` for incomplete tasks and an `"x"` for completed tasks, but allows for plugins which support alternative task statuses.                                                                            |
| `checked`        | Boolean   | Whether or not this task's status is **not** empty, meaning it has some `status` character (which may or may not be `"x"`) instead of a space in its `[ ]` brackets.                                                                                                                                                    |
| `completed`      | Boolean   | Whether or not this _specific_ task has been completed; this does not consider the completion or non-completion of any child tasks. A task is explicitly considered "completed" if it has been marked with an `"x"`. If you use a custom status, e.g. `[-]`, `checked` will be true, whereas `completed` will be false. |
| `fullyCompleted` | Boolean   | Whether or not this task and **all** of its subtasks are completed.                                                                                                                                                                                                                                                     |
| `text`           | Text      | The plain text of this task, including any metadata field annotations.                                                                                                                                                                                                                                                  |
| `visual`         | Text      | The text of this task, which is rendered by Dataview. This field can be overriden in DataviewJS to allow for different task text to be rendered than the regular task text, while still allowing the task to be checked (since Dataview validation logic normally checks the text against the text in-file).            |
| `line`           | Number    | The line of the file this task shows up on.                                                                                                                                                                                                                                                                             |
| `lineCount`      | Number    | The number of Markdown lines that this task takes up.                                                                                                                                                                                                                                                                   |
| `path`           | Text      | The full path of the file this task is in. Equals to `file.path` for [pages](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/).                                                                                                                                                              |
| `section`        | Link      | Link to the section this task is contained in.                                                                                                                                                                                                                                                                          |
| `tags`           | List      | Any tags inside the task text.                                                                                                                                                                                                                                                                                          |
| `outlinks`       | List      | Any links defined in this task.                                                                                                                                                                                                                                                                                         |
| `link`           | Link      | Link to the closest linkable block near this task; useful for making links which go to the task.                                                                                                                                                                                                                        |
| `children`       | List      | Any subtasks or sublists of this task.                                                                                                                                                                                                                                                                                  |
| `task`           | Boolean   | If true, this is a task; otherwise, it is a regular list element.                                                                                                                                                                                                                                                       |
| `annotated`      | Boolean   | True if the task text contains any metadata fields, false otherwise.                                                                                                                                                                                                                                                    |
| `parent`         | Number    | The line number of the task above this task, if present; will be null if this is a root-level task.                                                                                                                                                                                                                     |
| `blockId`        | Text      | The block ID of this task / list element, if one has been defined with the                                                                                                                                                                                                                                              |

# Usage
## Other useful stuff

| Field Name        | Data Type | Description                                        |
| ----------------- | --------- | -------------------------------------------------- |
| `date(today)`     |           | A way to have today always within the query        |
| `dur(1 week)`     |           | Another way to work with dates on a dynamic query. |
| `[[]]`            |           | Files that link to the current file                |
| `!outgoing([[]])` |           | Files that do not have al ink in the file          |
