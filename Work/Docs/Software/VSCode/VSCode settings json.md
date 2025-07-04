---
type: note
---
# Background
- File where the settings for nearly everything is written. 
	- Shouldn't be confused with the user settings file, which configures system-level configurations. 
- These settings are shared by all users of the project, unless you .gitignore them.

## Settings Precedence (later scope overrides earlier)
- Default settings - This scope represents the default unconfigured setting values.
- User settings - Apply globally to all VS Code instances.
- Remote settings - Apply to a remote machine opened by a user.
- Workspace settings - Apply to the open folder or workspace.
- Workspace Folder settings - Apply to a specific folder of a [multi-root workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces).
- Language-specific default settings - These are language-specific default values that can be contributed by extensions.
- Language-specific user settings - Same as User settings, but specific to a language.
- Language-specific remote settings - Same as Remote settings, but specific to a language.
- Language-specific workspace settings - Same as Workspace settings, but specific to a language.
- Language-specific workspace folder settings - Same as Workspace Folder settings, but specific to a language.
- Policy settings - Set by the system administrator, these values always override other setting values.

# Usage

## Default Settings
There is a command to open default settings with preferences and command palatte. 

## What are the settings value types?
- String - `"files.autoSave": "afterDelay"`
- Boolean - `"editor.minimap.enabled": true`
- Number - `"files.autoSaveDelay": 1000`
- Array - `"editor.rulers": []`
- Object - `"search.exclude": { "**/node_modules": true, "**/bower_components": true }`js

## Where is the user settings located?
- **Windows** `%APPDATA%\Code\User\settings.json`
- **macOS** `$HOME/Library/Application\ Support/Code/User/settings.json`
- **Linux** `$HOME/.config/Code/User/settings.json`
- Can also be accessed through the command window with `Open User Data Folder`