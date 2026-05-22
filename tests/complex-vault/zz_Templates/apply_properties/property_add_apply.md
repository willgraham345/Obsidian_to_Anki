
<%*
let name = await tp.system.prompt("New message/method/function name?");
const choices = [
	"processes",
  "members",
  "methods",
  "messages",
  "functions",
	"variables",
	"configurations",
];
let type = await tp.system.suggester(choices, choices, throw_on_cancel=true);
await console.log(type);
let file = tp.file.title;
const fieldLink = `[[${file}#${name}]]`;


let current_fields_vals = await tp.frontmatter[type];
let templateContent = "";
if (["members","variables","configurations"].includes(type)) {
  const templateFile = tp.file.find_tfile("zz_Templates/template_classes/variable_config_template");
  templateContent = await app.vault.read(templateFile);
}
if (["processes"].includes(type)) {
  const templateFile = tp.file.find_tfile("zz_Templates/template_classes/process_template");
  templateContent = await app.vault.read(templateFile);
}
if (["functions", "methods"].includes(type)) {
  const templateFile = tp.file.find_tfile("zz_Templates/template_classes/function_method_template");
  templateContent = await app.vault.read(templateFile);
}
console.log(current_fields_vals);
let new_field;
if (current_fields_vals == null) {
	new_field = [fieldLink];
}
else {
	current_fields_vals.push(fieldLink);
	new_field = current_fields_vals;
}
await tp.file.cursor_append("### " + type + "\n");
await tp.file.cursor_append("##### " + name + "\n");
await tp.file.cursor_append(templateContent);
%>

<%*
tp.hooks.on_all_templates_executed(async () => {
  const file = tp.file.find_tfile(tp.file.path(true));
  await tp.app.fileManager.processFrontMatter(file, (frontmatter) => {
    frontmatter[type] = new_field;
 });

});
-%>
