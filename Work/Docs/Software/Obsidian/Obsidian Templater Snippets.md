---
type: note/function
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, December 19th 2024, 10:20:03 am
---
# Background
- 

# Usage
## Running templater scripts
Use add template modal, with only the frontmatter sections

### Example appending to an already existing file within a folder
```
<%*
const folder = "Will/QuoteSources";
const items = app.vault.getMarkdownFiles().filter(x => x.path.startsWith(folder));
const selectedItem = (await tp.system.suggester((item) => item.basename, items));
console.log(selectedItem);
const quote = await tp.system.prompt("quote?");
console.log(quote);
const quote_formatted_as_task = "\n"+ "- [Q] " + quote;
await app.vault.adapter.append(selectedItem.path, quote_formatted_as_task);
_%>
```

## Get Dataview to access tags and inline fields
```
<%*
const dv = this.app.plugins.plugins["dataview"].api;
const folder = "research_citations";
const items = app.vault.getMarkdownFiles().filter(x => x.path.startsWith(folder));
const citation_file = (await tp.system.suggester((item) => item.basename, items));
const citation_file_dv = dv.page(citation_file.basename);
const today = tp.date.now("YYYY-MM-DD");
console.log(citation_file);
//const tags_to_add = tp.file.tags
const citation_note_str = "citation_note";
await tp.file.rename("note_"+citation_file.basename);
console.log(citation_file_dv.file.tags);
const tags = citation_file_dv.file.tags;
const filtered_tags = tags.
map(x => x.replace("#", ""));
-%>
```

## At end of templater script
```
<%*
/*
Modifies the frontmatter to match the metrics...
*/
tp.hooks.on_all_templates_executed(async () => {
	const file = tp.file.find_tfile(tp.file.path(true));
	await app.fileManager.processFrontMatter(file, (frontmatter) => {
		frontmatter["field1"] = field1;
		frontmatter["field2"] = field2;
		if (field3!=""){
		frontmatter["field3"] = field3;
		}
  });
});
-%>
```

## Add to another note
```
<%*
const files = app.vault.getMarkdownFiles().map(file => {
  const fileCache = app.metadataCache.getFileCache(file);
  if (fileCache?.frontmatter?.aliases) {
    file.display = `${file.basename}\n${fileCache.frontmatter.aliases.join(", ")}`;
  } else {
    file.display = file.basename;
  }
  return file;
});
const selectedItem = (await tp.system.suggester(item => item.display, files)).basename;

const note = tp.file.find_tfile(`${selectedItem}.md`);

const insertedContent = `\n\n%%\n\`\`\`query\nfile: /^${selectedItem}.md/ /\\b[a-záàäæãééíóöőüű]+\\s*=\\s+[^\`]*?(?=\\s|\\z)|(?:(?:German|English|Greek|Hebrew|Arabic|Slavic|Turkic|Turkish|Ossetian|Alanian|Avestan|Sanskrit|Persian|Egyptian|Sumerian|Accadian|Akkadian|Assyrian|Assyr-Babilonian|Hittite[^\`]*?))\\s([^\`]+?)\\s/\n\`\`\`\n\`\`\`query\nfile: /^${selectedItem}.md/ /(Evernote|otherstuffiwanttocommentout)(?!.*\\%\\%)/\n\`\`\`\n%%`;

const fileContent = await app.vault.read(note);
const separator = '---';

const firstSeparatorPos = fileContent.indexOf(separator);
const secondSeparatorPos = fileContent.indexOf(separator, firstSeparatorPos + 1);

if (secondSeparatorPos !== -1) {
  const updatedContent = fileContent.slice(0, secondSeparatorPos + separator.length) +
    `${insertedContent}` +
    fileContent.slice(secondSeparatorPos + separator.length);
  
  await app.vault.modify(note, updatedContent);
}

await new Promise(resolve => setTimeout(resolve, 250));
app.workspace.getLeaf(true).openFile(note);
_%>
```

## Selecting from a list
```
<%*
const workout_groups = [
"Abs-Core",
"Arms-Chest",
"Cardio",
"Legs",
"Pull",
"Push",
"Shoulders",
"Stretch"
]
const workout_type = await tp.system.suggester(workout_groups, workout_groups);
-%>
```

### On the fly value
```
<%*
const items = ["item 1", "item 2"];
let selectedItem = await tp.system.suggester(item => item, items);
// No selected option, user hit `Escape` key
if (!selectedItem) {
  selectedItem = await tp.system.prompt("Type custom option");
}
-%>
<% selectedItem %>
```

```
<%*
const customOption = "--CREATE CUSTOM OPTION--"
const items = ["item 1", "item 2", customOption];
let selectedItem = await tp.system.suggester(item => item, items);
if (selectedItem === customOption) {
  selectedItem = await tp.system.prompt("Type custom option");
}
-%>
```