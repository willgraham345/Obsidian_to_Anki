<%*
types = [
	"career",
	"career/cv-resume",
	"career/ideas",
	"cheatsheet",
	"citation_note",
	"daily_log",
	"fleeting",
	"jira-issue",
	"meeting",
	"note",
	"note/class",
	"note/class/enum",
	"note/concept",
	"note/configuration",
	"note/diagram",
	"note/example",
	"note/function",
	"note/interface",
	"note/item",
	"note/item/variable",
	"note/keyword",
	"note/library",
	"note/library/module",
	"note/standard",
	"note/system",
	"note/tool",
	"note/tool/build",
	"note/tool/build/compiler",
	"note/workflow",
	"paper-conference",
	"person",
	"presentation",
	"project",
	"report",
	"tag_page",
	"tag_research_page",
	"update_log",
	"vault_tool",
	"webpage",
	"weekly_log",
];
let sum = await tp.system.prompt("Summary");
let type = await tp.system.suggester(types, types, throw_on_cancel=true);
-%>
<%*
tp.hooks.on_all_templates_executed(async () => {
	const file = tp.file.find_tfile(tp.file.path(true));
	await app.fileManager.processFrontMatter(file, (frontmatter) => {
		frontmatter["template"] = "[[base_note_template]]"
		frontmatter["template-version"] = "1.0.1"
		frontmatter["summary"] = sum
		frontmatter["type"] = type
	  });

});
-%>
