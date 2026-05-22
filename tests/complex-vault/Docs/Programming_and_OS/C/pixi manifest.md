---
summary: pixi.manifest file, holds the configuration for your project.
headings:
type: note/configuration
configuration_of: ["[[pixi]]"]
date created: Thursday, October 23rd 2025, 1:54:02 pm
date modified: Thursday, October 23rd 2025, 1:57:41 pm
template: "[[base_note_template]]"
template-version: 1.0.0
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Pixi Manifest - Pixi by prefix.dev](https://pixi.sh/latest/reference/pixi_manifest/)
  `[workspace]` ;;; Alias for project in pixi. = #tools/pixi 
  `[package]` ;;; Specify properties specific to the package you want to build. = #tools/pixi 
  `[package.build.backend]` ;;; Pixi backends describe how to build a conda pcakage, for a certain language or build tool. = #tools/pixi 
  `[dependencies]` ;;; Specifies dependencies used within the pixi project. = #tools/pixi 
  `[feature]` ;;; Tells about a feature in the project. You can almost treat these as variants of the same build package. = #tools/pixi 
