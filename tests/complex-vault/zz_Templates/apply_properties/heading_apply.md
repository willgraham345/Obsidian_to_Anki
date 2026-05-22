<%*
const choices = [
  "Concepts of Note",
  "Usage",
  "Syntax",
  "Examples",
  "Diagrams",
  "Properties",
  "Formatting",
  "Breadcrumbs",
  "Questions",
  "Flashcards"
];
let heading = await tp.system.suggester(choices, choices, throw_on_cancel=true);
console.log(heading);
const headingLink = `[[#${heading}]]`;
let current_headings_vals = await tp.frontmatter["headings"];
await tp.file.cursor_append("## " + heading);
console.log(current_headings_vals);
let new_heading;
if (current_headings_vals == null) {
	new_heading = [headingLink];
}
else {
	current_headings_vals.push(headingLink);
	new_heading = current_headings_vals;
}
%>

<%*
tp.hooks.on_all_templates_executed(async () => {
  const file = tp.file.find_tfile(tp.file.path(true));
  await tp.app.fileManager.processFrontMatter(file, (frontmatter) => {
    frontmatter["headings"] = new_heading;
 });

});
-%>
