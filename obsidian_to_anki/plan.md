---
type:
headings:
date created: Tuesday, May 12th 2026, 7:17:19 pm
date modified: Wednesday, May 13th 2026, 12:28:53 pm
tags: []
template:
template-version:
---

"Atomics" = A regular expresssion "type". These are distinguished by each "Custom Regexps" in the `obsidian_to_anki.ini`.
"States" = The snapshot of how an atomic is being treated at this moment in time by the database, and other targets (Anki). States are explained more thoroughly below in `### State Changes`
"Actions" = Actions are the scripts that are run from this tool. Writing, diffing, and scanning are actions.
"Target" = Not a source of truth for an atomic, but a place we want to migrate or move the atomic towards.

### State changes
“States” to implement:
- sync (the file is up to date in the database, the vault, and in other targets)
- add (new to obsidian, not present in database, not present in other targets)
- stale (this note is in the database, but not in obsidian or other targets)
	- recommended actions: Add a flag in the write script to remove stale atomics
- orphan (in Anki/other targets, but not in obsidian or the database)
	- recommended actions: Output this in the diff. Add a flag to diff to "show orphans". This should then present a CLI interface where orphans are output to the terminal. Add another flag to remove orphans, which will prompt the user if they want to remove the orphans from the source
- fieldModification (vault scan returned an atomic that matched the first or second field of an existing database entry, but not the entire entry. A modification has taken place)
	- recommended actions: In diff, there should be a flag to resolve matches. Users should be prompted for two options (1. Modify database entry to match vault and add this card to "toModify" state; 2. Remove database entry, move this atomic to an "add" state) 
- modifyDeck (the vault scan matches the database entry for field 1 and field 2, but does *not* match the deck type)
	- recommended actions: This should be a simple "modifying deck" category in the diff. This should execute a simple write command to anki to in-place modify a card.
- modifyType (the vault scan matches the database entry for field 1 and field 2s, but has a different type)
	- recommended actions: This should be a simple "modifying deck" category in the diff. This should execute a simple write command to anki to in-place modify a card. Move this to "toModify"
- toModify (Database now has the correct entry which matches the vault, this should be written to anki and other targets) 
	- recommended actions: In-place modify the target

Some states can act as specifications of other states. 

### Process modification
The scanning process should follow this process:
1. Scan file hashes. If no change has happened, no change has happened. Go to next file. Title this as method: `find_vault_modifications()` 
	- If this is the first time being run (no database present), skip this method. 
2. `add_atomic_id()` This method will add a frontmatter property to each file in the vault. This uuid will be used by the database to "match" atomics in the vault, to atomics in the database. Additionally, it will be used to determine if a file's hash has changed.
3. `parse_files()` Parse new files, and scan modified files. Add these to a “staged” or “state unknown” table in the database. 
4. `compare_vault_modifications()`. Compare the files output from “staged” against the atomics already within the database. Do they line up with the states mentioned in “states”? Create a table for each within the database. 

The diff should follow this process:
1. Determine what is the 
2. Specify what changes would be made to bring the database (Anki) in line with the vault. Determine a way to clearly and repeatably output this information. I *don't* like Markdown tables. Markdown subheadings, or a markdown format is fine.
	1. Ideally, 


There should be a staging table for each “state”. This will improve the diff process. 

# TODO
- [ ] Change the configuration name of "Custom Regexps" to "Atomics". That configuration entry should be changed to `Atomics`
- [ ] Make process modification changes as notated in the `### Process Modifications` subheading
- [ ] Implement the `### State changes` subheading