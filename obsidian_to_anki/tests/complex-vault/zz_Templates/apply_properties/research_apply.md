<%*
let summary = await tp.system.prompt("Summary", throw_on_cancel=true);
const ratings = ["","1", "2", "3", "4", "5"];
let rating = await tp.system.suggester(ratings, ratings, throw_on_cancel=true);
const reading_status_choices = ["almost-finished", "might-read", "not-worth-reading", "skimmed", "to-read", "done"];
let reading_status = await tp.system.suggester(reading_status_choices, reading_status_choices, throw_on_cancel=true);
const types = ["idea/method", "idea/framework", "idea/connection", "system/new", "system/version", "review", "survey"];
let type_research = await tp.system.suggester(types, types, throw_on_cancel=true);
%>

<%*
tp.hooks.on_all_templates_executed(async () => {
	const file = tp.file.find_tfile(tp.file.path(true));
	await app.fileManager.processFrontMatter(file, (frontmatter) => {
		frontmatter["summary"] = summary
		frontmatter["rating"] = rating
		frontmatter["reading"] = reading_status
		frontmatter["type-research"] = type_research
		frontmatter["template"] = "[[research_template]]"
		frontmatter["template-version"] = "1.0.1"
	  });

});
-%>
