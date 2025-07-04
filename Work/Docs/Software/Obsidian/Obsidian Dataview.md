---
type: note/component
date created: Tuesday, June 18th 2024, 12:44:00 pm
date modified: Thursday, December 19th 2024, 10:18:32 am
tags: [note/Obsidian]
---
# Background
Related to [[Obsidian.Kanban]], [[Obsidian.Breadcrumbs]], and [[Obsidian.MetaEdit]]

See [[Obsidian Metadata]] for more info on data types and variables that are implicit

## Data types
- Text (default catch-all)
- Number
- Boolean
- Date
	- `field.year`, `field.month`, `field.weekyear`, `field.week`, `field.weekday`, `field.day`, `field.hour`, `field.minute`, `field.second`, `field.millisecond` 
- Duration
	- `<time> <unit>`
		- i.e. `6 hours`, `4 minutes`, `6hrs`
- Link
- List
	- Multi-value fields.
- Object
	- Map of multiple fields under one parent field. 

### Inline fields
Dataview supports "inline" fields with a `Key::Value` syntax that you can use everywhere. 
- Hide it in reader mode by using something like the key/value examples below
```
longKeyIDontWantToRead:: key //Reads until the end of the line

I would rate this a [rating:: 9]! It was [mood:: acceptable].

Hiding the key while in reader mode can be done with (KeyICantSeeInReaderMode:: parentheses).
```

#### Sanitizing Metadata With Dataview
Spaces or capitalized letters in metadata key name will not be shown by dataview. 

The software can also deal with emojis and non-UTF-8 data. 

#### Things that are indexed automatically
- Bullet points
- Task lists
	- If you'd like to annotate a list item (like a task), with metadata, you have to use the bracket syntax, because there's already other data on the task field. 

## Output Format
`TABLE` = one result per row and one or more columns of field data
`LIST` = A bullet point list of pages which match the query. You can output one field for each page alongside their file links.
`TASK` = interactive task list
`CALENDAR` = Calendar view displaying each hit via a dot on its referred date.

# Usage
## DataviewJS
By far the easier way to work with stuff.
[Codeblock reference]([Codeblock Reference - Dataview (blacksmithgu.github.io)](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvspantext))

### Output all inline fields/properties
Make sure to have the dataviewjs on to p if you want to look into this. 
```
const page = dv.current()

dv.span(Object.entries(page))
```

## DQL Query
Every query has:
- `Query Type` (at least one)
- `FROM` (zero or one of these)
- `data commands` (zero to many)
```
<QUERY-TYPE>
	<fields>
FROM <source>
<DATA-COMMAND> <expression>
<DATA-COMMAND> <expression>
          ...
```

### Fields
```
file.mday as "Modified Date", file.tags as "Tags"
```
See more at [[#Field In-depth]]

### Examples
Lists all pages in your vault as a bullet point list
```
LIST
```

Lists all tasks (completed or not) in your vault
```
TASK
```

Renders a Calendar view where each page is represented as a dot on its creation date.
```
CALENDAR file.cday
```

Shows a table with all pages of your vault, their field value of due, the files' tags and an average of the values of multi-value field working-hours
```
TABLE due, file.tags AS "tags", average(working-hours)
```

Creating new Categories
```
FLATTEN
```
- Essentially creates 

## Data Commands
### `SORT = ASC/DESC`
- Determines order in which things appear
- `DESC` or `ASC`

### Metadata Filters
```
TABLE
	time-played AS "Time Played",
	length AS "Length",
	rating AS "Rating" 
```

## Field In-Depth