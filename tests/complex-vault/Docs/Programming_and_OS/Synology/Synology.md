---
summary:
type: note/system
headings: ["[[#Concepts of Note]]"]
date created: Monday, January 19th 2026, 4:01:19 pm
date modified: Monday, January 19th 2026, 4:04:43 pm
template: "[[base_note_template]]"
template-version: 1.0.1
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
### File structure
- `homes/`
	- Visible only to administrator users
	- Within the folder, the real location of each user's 'home' folder. Shared permissions are configured to allow admin users to have access to all of its contents but any standard user only has access to their own `homes/<user_name>` folder
- `home/`
	- Managed by DSM and different for each user, admin and standard. 

| User account | DSM account type | "Home" linked to | Can access "Homes" |
| ------------ | ---------------- | ---------------- | ------------------ |
| admin        | administrator    | /homes/<admin>   | Yes                |
| user1        | standard         | /homes/<user1>   | No                 |
| user2        | standard         | /homes/<user2>   | No                 |

### Using Git