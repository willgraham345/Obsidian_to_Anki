---
summary: The build context is the set of files that your build can access. The positional argument that you pass to the build command specifies the context you want to use for the system.
date created: Friday, November 1st 2024, 2:44:51 pm
date modified: Friday, November 1st 2024, 2:49:20 pm
type: note/concept
---
`VIEW[**{summary}**][text(renderMarkdown)]`

# Contexts
- Filesystem context 
	- When your build context is a local directory, a remote, or a tar file, that then becomes the set of files that the builder can access during the build. Build instructions can then use `ADD` and `COPY`
	- Processed recursively, and repositories include all submodules.
- Text file contexts
	- Interprets the file as a dockerfile. The build doesn't use a filesystem context.zz