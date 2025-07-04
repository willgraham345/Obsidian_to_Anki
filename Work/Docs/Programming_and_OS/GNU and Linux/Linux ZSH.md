---
summary: 
type: note/component
component_of: ["[[Linux CLI]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:03:23 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

https://thevaluable.dev/zsh-install-configure-mouseless/


1. `.zshenv` - Should only contain user’s environment variables.
2. `.zprofile` - Can be used to execute commands just after logging in.
3. `.zshrc` - Should be used for the shell configuration and for executing commands.
4. `.zlogin` - Same purpose than `.zprofile`, but read just after `.zshrc`.
5. `.zlogout` - Can be used to execute commands when a shell exit.