---
summary: Windows open-source platform that can be used for a variety of applications. See [[dotnet Platform Overview]]
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
type: note/system
down:
  - "[[dotnet Delegates]]"
  - "[[dotnet Enumerations]]"
  - "[[dotnet Executables]]"
  - "[[dotnet Interfaces]]"
  - "[[dotnet Standard Streams]]"
  - "[[dotnet Structures]]"
  - "[[dotnet Type System]]"
concepts:
  - "[[dotnet Classes]]"
processes:
  - "[[dotnet SDK Install and Start]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, November 4th 2025, 9:26:50 am
items: "[[dotnet Platform Components]]"
more_info:
  - "[[dotnet Platform Overview]]"
  - "[[dotnet SDK Install and Start]]"
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
Writes Windows applications, web applications, web services
- Can use any of the following languages:
	- Visual basic
	- C#
	- C++
	- Jscript
	- COBOL
- The idea is you can use .NET to use anything within the above languages.
- All of these languages can access the framework as well as communicate with each other. 
	- .NET consists of an enormous library of codes used by the client languages. These languages use OO methodology.
- Some components of the .NET framework
	- Common language Runtime (CLR)
	- .NET framework Class library
	- Common Language Specification
	- Common Type System
	- Metadata and Assemblies
	- Windows Forms
	- ASP.NET and ASP.NET AJAX
	- ADO.NET
	- Windows Workflow Foundation (WF)
	- Windows Presentation Foundation
	- Windows Communication Foundation (WCF)
	- LINQ


C# --> CIL --> CLR (common language runtime, something that is run on linux, windows, and macOS stuff)
- C

## Usage

  `dotnet restore` ;;; Similar to `pip install -r requirements.txt` = #tools/dotnet
<!--ID: 1758253289511-->

  `dotnet test` ;;; Runs test within a dotnet project = #lang/test/cli_running
<!--ID: 1758253289518-->
