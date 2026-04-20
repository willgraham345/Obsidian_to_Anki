---
summary: A file in C#, essentially a workspace container. Holds references to one or more projects (.csproj, .vbproj, etc.). Doesn't directly control compilation, just a metadata for Visual Studio or `dotnet build` to know. The SDK iterates through all projects inside the solution and builds them in dependency order.
headings: ["[[#Concepts of Note]]"]
type: note/item
date created: Friday, September 19th 2025, 4:37:11 pm
date modified: Friday, September 19th 2025, 4:39:24 pm
item_of: ["[[CSh Architecture]]"]
uses: ["[[CSh csproj]]", "[[VB vbproj]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### Items included
.NET core target
```cs
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>
</Project>
```
Include directives
```cs
<Compile Include="Program.cs" />
<Compile Include="Models\MyClass.cs" />
```