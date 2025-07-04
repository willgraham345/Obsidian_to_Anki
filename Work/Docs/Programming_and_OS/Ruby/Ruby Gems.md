---
summary: A ruby gem is a package with a name, version, and platform. There is code, documentation, and a gemspec inside of each gem.
type: note/component
workflows: ["[[Ruby Gems with JFrog Artifactory Workflow]]"]
date created: Wednesday, October 2nd 2024, 5:32:25 pm
date modified: Wednesday, March 26th 2025, 8:52:17 am
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

### Installing Gems
```
gem install <gem_name>
```

### List Gems
```
gem list
```