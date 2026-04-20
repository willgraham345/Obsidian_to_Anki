---
summary: A ruby gem is a package with a name, version, and platform. There is code, documentation, and a gemspec inside of each gem.
type: note/item
headings:
processes:
  - "[[Ruby Gems with JFrog Artifactory Workflow]]"
date created: Wednesday, October 2nd 2024, 5:32:25 pm
date modified: Monday, February 9th 2026, 11:40:52 am
template:
template-version:
item_of:
  - "[[Ruby]]"
prev:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

Gem Structure
```
% tree freewill
freewill/
├── bin/
│   └── freewill
├── lib/
│   └── freewill.rb
├── test/
│   └── test_freewill.rb
├── README
├── Rakefile
└── freewill.gemspec
```

## Usage
```
gem
```

 `gem install gemmy` ;;; Install a gem named `gemmy` in ruby.
 
