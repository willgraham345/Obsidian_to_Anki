---
status: stalled
type: project
project_id: 1
company: Varex
project: config
subproject:
---
# Relevant Notes:
- [[Greg Gerber]]

# Updates/Notes:

## Drawings of Config:
General terminology in config

parse calls
![[VD.ConfigCreator.Parse.Calls2024-06-17.16.35.24.excalidraw|321]]
ConfigCreator Imports
![[ConfigCreator UI Diagram 2024-06-19 16.49.33.excalidraw|825]]

## Changes/Progress
### Building/Debugging
1. Navigate to `ConfigCreator` Build with the windows command shell by using the `generate.bat` and `build.bat`. 
2. Open Visual Studio, set ConfigCreator as the startup project, and click debug

### Changes to git
`ConfigCreator.h`
- Added `TAB_NON_MODULAR` static expression in the private section of the `ConfigCreator`

## Debugging
1. Cloned `engineering/ConfigCreator` at `src/config_work/ConfigCreator`
	- Was able to build and launch, didn't find any tests
2. Cloned  `engineering/XConfigure` at `src/config_work/XConfig`
	- Built docs in `/docs/html/index.html`
3. Copied an official build to `src/config_work/Config_official_build`
	- Ran this, didn't really do much
4. Cloned `software/tooele/support/config` at `src/config_work/config`
	- I think this is the actual repo I should be looking into, mostly because it has a test folder. 
5. Cloned `software/configuration` to `src/config_work/configuration`
	- This one holds all the test configurations that I'm supposed to try to open.

### Opening `1313_MJI_32051`
![[Pasted.image.20240617140926.png| 700]]


| Repo          | Project Path                     | Tests | Documentation                                                                                                                                                                                                                                                     |
| ------------- | -------------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| config        | `software/tooele/support/config` | Yes   | Yes, [Online](http://slfpbuildmstr.vic.ad.vareximaging.com/jenkins/static-files/G2Sh0YacxWdudpNekXUQkRxpY213zH38zeoSJilAuW93aTk5NDI2OToxNzE4MTQwMjI5MzM1OnZpZXcvVG9vZWxlL2pvYi9Ub29lbGUtQ29uZmlnL2xhc3RTdWNjZXNzZnVsQnVpbGQvYXJ0aWZhY3Q=/doxygen/html/index.html) |
| XConfig       | `engineering/XConfigure`         | No    | Yes, generated in docs folder                                                                                                                                                                                                                                     |
| ConfigCreator | `engineering/ConfigCreator`      | No    | No, build failed                                                                                                                                                                                                                                                  |
| configuration | `software/configuration`         | No    | No                                                                                                                                                                                                                                                                |

#### Debugging
Ran the debugger while opening `"C:\Users\wi994269\src\config_work\configuration\1313_MJI_32051\32054rA_MianyangJiuli_1313_receptor_config.dat"`

This threw exceptions, and I've been tracing them back. 
`parse` called on 46 in `Config.cpp`
- `NotFoundException at Config.h:45 in Config::checkToken: The token was not found: SAP_MATERIAL_NUMBER_REV`
- Gets through until `token = CONFIG_END_OF_FILE (500)`, then throws an exception.
	- Not 100% sure why it's doing that. 
	- The error is thrown 

Wasn't sure why that was happening. Is this related to the tokens getting messed up?
Made this graph of the errors as well as the output I'm getting in the debugger. 

#### After [[2024-06-18 Greg]]
- This configuration is **not** modular, as `Config::Config::isModular()` returns false
- in `ConfigCreator.cpp`, we need to try and `setText` to something other than the other stuff. 

##### `isModular()` failure
```cpp
try
{
	if(Config::Config::isModular())
	{
		ui->sapMaterial->setText(cfg->getSapMaterialWithRev().c_str());
	}
	else {
		ui->sapMaterial->setText("No SAP Material");
	}
}
```
- The error comes with the `Config::Config::isModular()`
	- This would work if it was a static function 
- `cfg` is a shared pointer towards config.

Tried opening XConfigure on the same file (solution within the folder) to see what the file "Should" look like. 

The `groupBoxModules` looks good. There shouldn't be any modules loaded as `isModular()` fails.

Starting to debug the ConfigCreator.cpp signal call. I think that'll get me headed in the right direction. 

The `loadConfig` method ([[VD.ConfigCreator.Class]]), calls the parse function. It reloads the widget at the end of that function. Based on that, the `QTabWidget` page isn't being loaded correctly. 

Not sure what Greg wants here. The updating to the config module doesn't get called because the configuration is not modular. 

Figured out what I need to add. I need to add a ui tab that covers "standard" and stuff that returns false to `Config::isModular()`
- From there, we also need to get the system stuff reading correctly into the modules tab. 

### Things changed to UI
1. Added `tabNonModular` and `tableNonModular` to the `tabWidget`
2. Set `ui->tabWidget->setTabEnabled()` to be false

### Potential Changes to ConfigCreator.cpp
1. 
Rebuilt repo to reflect changes. 

On line 472 of `ConfigCreator.cpp`

#### Rebuilding Documentation to better understand the UI call graph
- [x] Generate the ConfigCreator docs in Doxygen. 
	- Think I got it by removing the `utils/` and `autoversion/` folders
Things that need to be redefined within the files

### 2024-07-01 11:00
- Restarted on the project, trying to build within Visual Studio and VSCode. 
	- Getting an error on line 365 for ConfigCreator.cpp, where I modified. 
There's a call to the `populateModeTable()` before my comments testing if the configuration returns true to `isModular()`
I moved that below and I'm still getting similar errors.
I added parentheses to the statement, and now I'm seeing unresolved externals on the executable. I googled the problem, and the first [stack overflow thread](https://stackoverflow.com/questions/14069041/unresolved-external-symbols-qt-creator) said that it could be an issue due to not running qmake. I'll recompile and try again. 
- Not sure that there's a good answer here. qmake isn't mentioned directly in any of the files, outside of a VS mention within the project. 
- Recompiling didn't work.
Trying to build from Visual Studio
- I'm having issues with the linker, and it saying that I've broken the one definition rule. 
	- LNK2005
	- LK1120
		- Number of unresolved external symbol errors in the current link
	- LNK2019
		- The compiled code for function makes a reference or call to symbol, but the linker can't find the symbol definition in any of the libraries or files. 
		- Getting this error on the nonModularAdd. 
Went back to the original setup, and still had issues. 

### 2024-07-01 12:00
- Pulled from the repository, and there's been a bunch of changes to the ConfigCreator.cpp. I want to test and see if the thing builds & runs. 
	- I noticed a "linker fail" right at the beginning, but that might not mean anything. 
	- Big errors when building from script
- Really confused as to why the `cfg->` fails when I test modularity, but not when it's called like three lines later
- I'll try to build from VS
	- Nope, still has tons of errors. I'll need to double check with Greg to see if there's a way to get a build without errors. 

### 2024-07-09 10:00
Trying to figure out how to build/compile the ConfigCreator
Got it. 

### 2024-07-09 11:00
Not sure how the modules are loaded in the `onModuleRowChanged()`
- Adde the def