---
type: note/function
date created: Wednesday, July 31st 2024, 9:17:54 am
date modified: Thursday, December 19th 2024, 10:18:34 am
---
# Background
- Using flatten for tasks is great, as you can access all of them as one thing rather than all over. 

[Dataview Example Vault](https://s-blu.github.io/obsidian_dataview_example_vault/)

# Usage

## Using Data within current note
```
FLATTEN this.<dv_field> as <name>
```

## Query Backlinks from Current note
```
TABLE cols
FROM [[]]
```

## Filter and Display tasks by status
```
TABLE file.name, T.text AS "Tasks", file.tags
FROM #research/MARS 
flatten file.tasks as T
where T.status = "'"
where T.text
```

## Display accessed properties/tasks
```
TABLE propertyName, T.task_subfield as "task_subfield", file.tags, 
```

## Sourcing
### Multiple Dataview entries in the same file
If you have multiple inline/property entries for the same file, they will be concatenated as a list for a dataview table. This can be extended with the [[obsidian.metabind]] plugin for better interaction between entries. 

### Source
`FROM`
- Takes a source or a combination of sources as an argument
- You can only add one of these

#### Current File
```
WHERE file.path = this.file.path
```

#### Example Sources
List all pages inside folder Books and subfolders
```
LIST FROM "Books"
```
Lists all pages that include the tag `#status/open` or `#status/wip`
```
LIST
FROM #status/open OR #status/wip
```


