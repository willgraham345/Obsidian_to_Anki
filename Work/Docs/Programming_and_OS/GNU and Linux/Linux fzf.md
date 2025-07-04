---
type: note/function
date created: Wednesday, September 25th 2024, 9:16:50 am
date modified: Thursday, February 6th 2025, 10:08:37 am
function_of: ["[[Linux CLI]]"]
---
# Background
- Command line fuzzy finder, really really good tool.

# Usage
- `CTRL-T` runs `$FZF_CTRL_T_COMMAND` to get a list of files and directories
- `ALT-C` runs `$FZF_ALT_C_COMMAND` to get a list of directories
- `vim ~/**<tab>` runs `fzf_compgen_path()` with the prefix (`~/`) as the first argument
- `cd foo**<tab>` runs `fzf_compgen_dir()` with the prefix (`foo`) as the first argument
- `CTRL-R` reloads the candidate list