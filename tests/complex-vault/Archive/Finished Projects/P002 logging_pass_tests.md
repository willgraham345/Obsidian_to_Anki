---
status: closed
type: project
project_id: 0
company: Varex
project: logging
subproject: logging_tests
---
# Todo

# People
[[Mike Beister]]

# Updates/Notes:
## Actual + Expected:
- Not sure how to build/execute
	- Are `log/test/build/win64` where I should be executing tests?

### Built Repo
What I Did:
- I'm able to build the repo to the `test/build` directory using the following commands:
```shell
./generate.bat
./build.bat
```
- Debug by opening Visual Studio, and opening the solution file: `log\test\build\win64\LogTests.sln`
	- From there, you can hit `F5` to start the debugging thing. 

### Ran Tests
Set `LogTests` as the Startup Project
- Got this output from the `LogTests` solution
	- ![[Pasted.image.20240529165922.png| 500]]
	- We can replicate this, and write new logs by clicking on the executable `C:\Users\wi994269\src\log\test\build\win64\Debug\LogTests.exe`
		- For whatever reason, the logfiles are REALLY sparse. 
		- Here's what I'm getting when I interact with the `settings` variable within the debugging console:
			- ![[Screenshot.2024-05-30.161626.png| 500]]
				- I don't know where that directory is, but here are the places I've checked
					- `C:\Users\user\AppData/Local/Varex/logs`
					- `C:\Users\wi994269\src\log\test\build\win64\Debug`

### Jim Meeting Notes
- Jim wrote a front to `spdlog`
- Logging HAS to be getting it somewhere otherwise it will fail. 
- It default initializes a `LogSettings.txt` if you don't provide one. 

### Was able to get LogSettings.txt to work
- Put a new LogSettings.txt into the same directory as the solution. I was able to edit things within the solution that caused the repo to fail. 
	- Modified `test/CMakeLists.txt` to make this happen

### Error at 1724
```cpp
ASSERT_EQ(CreateProcess(childApp, NULL, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi), 1) << "Could not create child process " << childApp << "error: " << GetLastError();
```
- The heck is `childApp`?

#### Added this line above that failing line
```cpp
CreateProcess(childApp, NULL, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)
```
- This launches the 
- `CreateProcess` is from a `processthreadsapi.h` file. That file is deep in the Program Kits (I believe for Visual Studio)
	- `childApp` is `"WinChildFlushApp.exe`. Not sure what it does. 
	- Build within the `component.cmake` file. I have no idea what this thing does. 

##### Before/After It hit my line
![[Pasted.image.20240604115312.png| 500]] ![[Pasted.image.20240604115354.png| 500]]

### Rebuild without Changes
- Did it fail at this other place, or no?
- Yes it did, not sure why.
![[Pasted.image.20240604121731.png| 300]]

### Try again, but instead I'll copy this to each of the build folders.
- I need to revisit the diagrams I made of the building process. See [[VD.logging.repo.build.process]] for more info on this. 

The rebuild didn't work. My CMake isn't copying the directory over, and I don't think it is building correctly. 

### May 11
- Another failure. Here's where I'm at. 
1. Remove changes to `component.cmake`, see if I can rebuild the repo and reproduce the same errors that Jenkins saw. 
   
   With no changes from `master`, I see a successful build
2. Adding in the copying of LogSettings.txt within the `custom_test_code()` function. 
	- I have an error within `configure_file`.
		- I had:
```cmake
configure_file(
	${CMAKE_CURRENT_SOURCE_DIR}/test/LogSettings.txt
	${CMAKE_CURRENT_BINARY_DIR}/LogSettings.txt COPYONLY
)
```
- Caused an error as there isn't a `test/test` directory. 
3. Once I fixed error 2, I had a successful build. Failed in tests at the WindowsSignalHandlers again. 
4. Realized I had accidentally deleted this line from the build file, and only Linux builds were failing. 
```cmake
install(FILES LogSettings.txt DESTINATION bin)
```
5. Pushed and am now waiting on Jenkins build. 

### 2024-07-01 09:00
Jim messaged me saying that the project is finished
## System Overview/Notes:
### Diagrams
[[VD logging repo LogTests classDiagram]]

