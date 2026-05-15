<%*
const projects = [
"FSW",
"Other",
];
let selectedProject = await tp.system.suggester(projects, projects, throw_on_cancel=true);
console.log(selectedProject);
let shortVersion = "";
if (selectedProject=== projects[0]){
	shortVersion = "fsw";
}
if (selectedProject=== projects[1]) {
	selectedProject = await tp.system.prompt("Type other project");
	shortVersion = await tp.system.prompt("Type short version of project name");
}
let issueNumber = await tp.system.prompt("Enter the issue number:");
let summaryTitle = await tp.system.prompt("Enter Jira title name/summary:");
let jiraIssues = [
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

let baseUrl = "https://jira.sdl.usu.edu/browse/";
let url = baseUrl+selectedProject+"-"+issueNumber;
console.log(url);
let fullUrl = baseUrl + issueNumber;
let newTitle = selectedProject+"-"+issueNumber;
await tp.file.rename(newTitle);
%>
# Notes
- 
# Breadcrumbs + Mentions
```breadcrumbs
type: mermaid
field-groups: [downs, sames, ups, prevs, nexts]
depth: [0, 3]
merge-fields: true
sort: field asc
show-attributes: [field]
```
```dataviewjs
dv.view("/zz_Templates/dataviewScripts/JiraIssueDV")
```

<%*
/*
Modifies the frontmatter to match the metrics...
*/
tp.hooks.on_all_templates_executed(async () => {
	const file = tp.file.find_tfile(tp.file.path(true));
	await app.fileManager.processFrontMatter(file, (frontmatter) => {
		frontmatter["summary"] = "";
		frontmatter["type"] = "jira-issue";
		frontmatter["aliases"] = shortVersion+issueNumber;
		frontmatter["url"] = url;
		frontmatter["jira-type"] = "";
		frontmatter["template"] = "[[jira_issue]]"
		frontmatter["template-version"] = "1.0.1"
  });

});
-%>
