---
summary: Dotfiles manager, helpful for making sure you have things installed correctly.
headings:
  - "[[#Concepts of Note]]"
type: note/system
down:
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
# Additional Background
## Concepts of Note
Scripts are run on every `chezmoi apply`

### Source state attributes
|Prefix|Effect|
|---|---|
|`after_`|Run script after updating the destination|
|`before_`|Run script before updating the destination|
|`create_`|Ensure that the file exists, and create it with contents if it does not|
|`dot_`|Rename to use a leading dot, e.g. `dot_foo` becomes `.foo`|
|`empty_`|Ensure the file exists, even if is empty. By default, empty files are removed|
|`encrypted_`|Encrypt the file in the source state|
|`external_`|Ignore attributes in child entries|
|`exact_`|Remove anything not managed by chezmoi|
|`executable_`|Add executable permissions to the target file|
|`literal_`|Stop parsing prefix attributes|
|`modify_`|Treat the contents as a script that modifies an existing file|
|`once_`|Only run the script if its contents have not been run before|
|`onchange_`|Only run the script if its contents have not been run before with the same filename|
|`private_`|Remove all group and world permissions from the target file or directory|
|`readonly_`|Remove all write permissions from the target file or directory|
|`remove_`|Remove the file or symlink if it exists or the directory if it is empty|
|`run_`|Treat the contents as a script to run|
|`symlink_`|Create a symlink instead of a regular file|
