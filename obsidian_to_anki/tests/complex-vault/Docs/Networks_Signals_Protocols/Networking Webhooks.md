---
type:
headings:
  - "[[#Concepts of Note]]"
date created: Friday, March 6th 2026, 4:54:25 pm
date modified: Friday, March 6th 2026, 4:55:36 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Networking Webhooks ;;; A way for one app to automatically notify another app when something happens. Data is pushed through a URL to your application at the moment an event happens.

# Additional Background
## Concepts of Note

Polling is like repeatedly calling a restaurant to ask "is my table ready?" A webhook is like the restaurant texting _you_ when it is.

### Things to know (according to Claude):
- Your endpoint must be publicly accessible (the external service needs to reach it)
- You should verify incoming requests (e.g., using a secret signature) to ensure they're legitimate
- Your endpoint should respond quickly with a `200 OK` — do heavy processing asynchronously