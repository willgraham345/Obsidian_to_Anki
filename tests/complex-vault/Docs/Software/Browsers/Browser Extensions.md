---
summary: A group of HTML, CSS, and JavaScript files that work together. Usually runs in its own domain, the domain labeled by the extensions ID. There is also a manifest.json file which lists identification of the extension, permissions required, and accessibility of the extension.
date created: Friday, November 1st 2024, 10:05:11 am
date modified: Friday, November 1st 2024, 10:22:19 am
type: 
---
`VIEW[**{summary}**][text(renderMarkdown)]`
[Attacking browser extensions - The GitHub Blog](https://github.blog/security/vulnerability-research/attacking-browser-extensions/?utm_source=tldrnewsletter)

# Extension URLs
- Typically follow the pattern
- `browser_specific_extension_scheme://extension_id/actual_resource_name`

# Manifest.json
There are v2 and v3 permissions requirements. 
`content_scripts`, `background` and `action`.

## background
Most powerful of the three contexts with the ability to access most of the browser extension APIs/WebExtensions API. 