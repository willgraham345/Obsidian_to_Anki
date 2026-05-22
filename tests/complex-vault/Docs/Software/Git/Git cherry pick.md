---
summary: Apply changes introduced by some existing commits. Not always best practice, as it duplicates commits.
type: note/tool
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, September 18th 2025, 10:19:15 am
tags: []
tool_of: ["[[Git]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[Cherry pick guide](https://www.atlassian.com/git/tutorials/cherry-pick)
  `git cherry-pick commitSha` ;;; Pulls the changes one commit makes onto your current branch. = #tools/git/commits/cherry-pick
<!--ID: 1758253288111-->

  `git cherry-pick commitSha1^..commitSha2` ;;; Pulls changes from a range of commits onto your current branch. = #tools/git/commits/cherry-pick 
<!--ID: 1758253288115-->
