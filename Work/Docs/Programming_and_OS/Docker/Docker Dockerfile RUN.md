---
summary: Enables you to execute commands within a Dockerfile.
type: note/function
date created: Monday, December 2nd 2024, 11:59:32 am
date modified: Monday, June 30th 2025, 3:15:52 pm
function_of: ["[[Docker Dockerfile|Dockerfile]]"]
tags: [command/dockerfile]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

<iframe src="https://docs.docker.com/reference/dockerfile/#run" style="width: 100%; height: 600px;background-color:white;"></iframe>


- [p] `RUN` = Execute build commands to create a new layer on top of the current image. Has both shell and exec forms (shell most common), which can be used to break up longer instructions into multiple lines = #command/dockerfile 
<!--ID: 1751434091250-->

- [p] `RUN --mount=[type=<TYPE>][,option=<value>[,option=<value>]...]` = Docker command that lets you determine what type of filesystem that the build is able to access. Can be used to access build secrets or ssh-agent sockets, and use a persistent management cache to speed up your build. = #command/dockerfile = `bind` bind-mount context directories
<!--ID: 1751434091255-->

- [p] `RUN --mount=type=cache` = Mount temp directory to cache directory for compilers and package managers. Additional options available... = #command/dockerfile/run
<!--ID: 1751434091261-->

- [p] `RUN --mount=type=ssh` = Allows the build container to access SSH keys via SSH agents, with support for passphrases. Additional options available... = #command/dockerfile/run
<!--ID: 1751434091266-->

- [p] `RUN --mount=type=tmpfs` = Mount a `tmpfs` in the build container. Additional options available... = #command/dockerfile/run
<!--ID: 1751434091271-->

- [p] `RUN --mount=type=secret` = Allow the build container to access secure files such as private keys without baking them into the image/build cache. Additional options available... = #command/dockerfile/run
<!--ID: 1751434091277-->
