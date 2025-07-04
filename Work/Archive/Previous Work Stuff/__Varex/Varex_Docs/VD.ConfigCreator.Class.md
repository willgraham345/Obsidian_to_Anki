---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
---
# `ConfigCreator`
- Description:
	- Manages the GUI for the [[VD.config.Module]] repo

## `public`
### onModuleRowChanged(int rowIndex)
Overview:
- ❓What does this do? 
- ❓How could I integrate my new tab into this workflow? 
Operations:
1. 

### keyPressEvent(QKeyEvent \*event)
Overview:
- ❓I think this only matters if I'm trying to edit stuff in my table through buttons. Might be a good idea to implement for the standard key:values.
Operations:
1. 

## `private`
### loadConfig(QString filename)
Overview:
- 
Operations:
1. Loads the file, checks for bugs all over
	1. Does the path exist? Can it be opened in binary?
2. Opens the file and begins parsing
3. Checks `isOldStyle`
	1. Handles conversion if true
4. Gets modules
5. Reloads all widgets

There's an `OldStyle` variable in here that doesn't make much sense to me. 

### reloadAllWidgets()
Overview:
- Responsible for reloading all widgets in UI. 
Operations:
1. Clears everything in the UI (sets rows to zero, which clears data)
2. `populateModeTable()` (middle of the UI table)
3. Populate modules list
	1. Within this, there's a call to get the modules and it updates the `listWidgetModules` based on the modules. 
	2. Declares `moduleName :: std::string`, and assigns value of `m.first.string()` to that. 
	3. Creates `QListConfigModule` object with arguments:
		- `m.second`
		- `txt`
		- `ui->listWidgetModules`
4. Populate system tokens
Variables
- `tabWidget`
	- Thing that isn't loading in our config


### onModuleRowChanged()
Overview:
- Sets tabs to be enabled or disabled with macros defined in ConfigCreator.h
Operations:
1. Initializes `listConfigModule` which grabs a pointer from `listWidgetModules->currentItem()`. 
	1. Based on that answer, you enable/disable different tabs on the thing