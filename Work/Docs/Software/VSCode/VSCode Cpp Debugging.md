---
summary: 
type: note/component
component_of: ["[[gdb]]", "[[VSCode Debugging]]"]
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, February 13th 2025, 12:35:12 pm
sections: ["[[#Using Debug Console]]"]
tags: [note/VSCode]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

`launch.json` is used to configure the debugger in VSCode. 
- You need to fill in the `program` field with the path to the executable you plan to debug. 
	- Must be specified for launch and attach (if you plan to attach)
- 
Most common errors are:
- `undefined _main`, `attempting to link with file built for unknown-unsupported file format` 
	- occurs when `helloworld.cpp` is not the active file when you start a build or start debugging
	- The compiler is trying to compile something that isn't source code, like your `launch.json` `tasks.json`, or `c_cpp_properties.json` file. 

# Usage
## Using Debug Console
You can execute commands for your debugger using the `-exec <command>` within the console. 
[Debug C++ in Visual Studio Code](https://code.visualstudio.com/docs/cpp/cpp-debug)
<iframe src="https://code.visualstudio.com/docs/cpp/cpp-debug" style="width: 100%; height: 600px;"></iframe>

## Configure VSCode's debugging behavior
### program (required)
- Specifies the full path to the executable the debugger will launch or attach to. The debugger requires this location in order to load debug symbols.

### `symbolSearchPath`
- Tells the Visual Studio Windows Debugger what paths to search for symbol (.pdb) files. Separate multiple paths with a semicolon. For example: `"C:\\Symbols;C:\\SymbolDir2"`.

### `requireExactSource`
- An optional flag that tells the Visual Studio Windows Debugger to require current source code to match the pdb.

### `additionalSOLibSearchPath`
- Tells GDB or LLDB what paths to search for .so files. Separate multiple paths with a semicolon. For example: `"/Users/user/dir1;/Users/user/dir2"`.

### `externalConsole`
- Used only when launching the debugger. For `attach`, this parameter does not change the debugger's behavior.
- **Windows**: When set to true, it will spawn an external console. When set to false, it will use VS Code's integratedTerminal.
- **Linux**: When set to true, it will notify VS Code to spawn an external console. When set to false, it will use VS Code's integratedTerminal.
- **macOS**: When set to true, it will spawn an external console through `lldb-mi`. When set to false, the output can be seen in VS Code's debugConsole. Due to limitations within `lldb-mi`, integratedTerminal support is not available.

### `avoidWindowsConsoleRedirection`
- In order to support VS Code's Integrated Terminal with gdb on Windows, the extension adds console redirection commands to the debugger's arguments to have console input and output show up in the integrated terminal. Setting this option to `true` will disable it.

### `logging`
- Optional flags to determine what types of messages should be logged to the Debug Console.
- **exceptions**: Optional flag to determine whether exception messages should be logged to the Debug Console. Defaults to true.
- **moduleLoad**: Optional flag to determine whether module load events should be logged to the Debug Console. Defaults to true.
- **programOutput**: Optional flag to determine whether program output should be logged to the Debug Console. Defaults to true.
- **engineLogging**: Optional flag to determine whether diagnostic engine logs should be logged to the Debug Console. Defaults to false.
- **trace**: Optional flag to determine whether diagnostic adapter command tracing should be logged to the Debug Console. Defaults to false.
- **traceResponse**: Optional flag to determine whether diagnostic adapter command and response tracing should be logged to the Debug Console. Defaults to false.

### `visualizerFile`
- `.natvis` file to be used when debugging. See [Create custom views of native objects](https://learn.microsoft.com/visualstudio/debugger/create-custom-views-of-native-objects) for information on how to create Natvis files.

### `showDisplayString`
- When a `visualizerFile` is specified, `showDisplayString` will enable the display string. Turning on this option can cause slower performance during debugging.

## Configure Target Application
### `args`
- JSON array of command-line arguments to pass to the program when it is launched. Example `["arg1", "arg2"]`. If you are escaping characters, you will need to double escape them. For example, `["{\\\"arg1\\\": true}"]` will send `{"arg1": true}` to your application.

### `cwd`
- Sets working directory of the application launched by debugger

### `environment`
- Environment variables to add to environment for the program. 

## Customizing GDB or LLDB
See [here](https://code.visualstudio.com/docs/cpp/launch-json-reference#_customizing-gdb-or-lldb)