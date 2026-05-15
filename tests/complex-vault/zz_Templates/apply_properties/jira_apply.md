<%*
let name = await tp.system.prompt("Jira Type?");
let issueTypes = [
"",
"Bug",
"Document",
"Epic",
"Improvement",
"Requirement",
"New Feature",
"Story",
"Task",
"Test",
]
let sum = await tp.system.prompt("Summary");
let type = await tp.system.suggester(issueTypes, issueTypes, throw_on_cancel=true);
%>

<%*
tp.hooks.on_all_templates_executed(async () => {
  const file = tp.file.find_tfile(tp.file.path(true));
  await tp.app.fileManager.processFrontMatter(file, (frontmatter) => {
    frontmatter["summary"] = sum;
    frontmatter["jira-type"] = type;
 });

});
-%>