---
type: note
---
# Background
| Build Method         | Benefits                                                                                                                                                                                                                                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IDE                  | - Create builds immediately and test them in a debugger.  <br>- Run multi-processor builds for C++ and C# projects.  <br>- Customize different aspects of the build system.                                                                                                                                                  |
| CMake                | - Build C++ projects using the CMake tool  <br>- Use the same build system across Linux and Windows platforms.                                                                                                                                                                                                               |
| MSBuild command line | - Build projects without installing Visual Studio.  <br>- Run multi-processor builds for all project types.  <br>- Customize most areas of the build system.                                                                                                                                                                 |
| Azure Pipelines      | - Automate your build process as part of a continuous integration/continuous delivery pipeline.  <br>- Apply automated tests with every build.  <br>- Employ virtually unlimited cloud-based resources for build processes.  <br>- Modify the build workflow and create build activities to perform deeply customized tasks. |
# Usage
## IDE Build Walkthrough
When you create a project, VS creates a default build config for project and the solution that contains the project. 
- These configs define how the solutions and projects are built and deployed
Typically open a project by the solution file rather than by the folder view. 