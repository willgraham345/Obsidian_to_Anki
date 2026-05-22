# Updates/Notes:
<%*
/*
Modifies the frontmatter to match the metrics...
*/
let id = await tp.system.prompt("Project ID?", throw_on_cancel=true);
console.log(id)
let ticketNum = await tp.system.prompt("Ticket number?", throw_on_cancel=false);
let newName = await tp.system.prompt("Title?", throw_on_cancel=true);
console.log(newName);
let folderTitle = "p"+id;
let fileName;
if (ticketNum) {
    fileName = "p"+id + " " + ticketNum + " " + newName;
} else {
    fileName = "p"+id + " " + newName;
}
console.log(fileName);
let currentPath = tp.file.path(0);
console.log(currentPath);
await tp.file.move("/Projects/"+folderTitle+"/"+fileName);
-%>
<%*
tp.hooks.on_all_templates_executed(async () => {
	const file = tp.file.find_tfile(tp.file.path(true));
	await app.fileManager.processFrontMatter(file, (frontmatter) => {
		frontmatter["project_id"] = Number(id);
		frontmatter["aliases"] = "p"+id;
		frontmatter["contexts"] = "parent";
		frontmatter["issues"] = "";
		frontmatter["type"] = "project";
		frontmatter["next"] = "";
		frontmatter["summary"] = "";
		frontmatter["status"] = "open";
		frontmatter["tags"] = "project/"+id+", taskNote";
		frontmatter["template"] = "[[project_template]]"
		frontmatter["template-version"] = "1.0.1"
	  });

});
-%>
