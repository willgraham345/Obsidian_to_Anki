---
type: daily_log
date: <% tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD") %>
week: <% tp.date.now("YYYY-[W]W", 0, tp.file.title, "YYYY-MM-DD") %>
year: <% tp.date.now("YYYY", 0, tp.file.title, "YYYY-MM-DD") %>
tags:
  - logs/daily
---
Navigation: [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %> | <-]] [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>| ->]]
# Log
- [ ] Journal
- [ ] Add meetings to calendar
- [ ] Plan through sprint
- [ ] Emails?
- [ ] Todo list?
- [ ] Text Kate when I'll be home
# Goals

# Queries
> [!ABSTRACT]- Notes Created Today
> ```dataview
> TABLE file.tags as "Tags", file.mday as "Last Modified"
> FROM ""
> WHERE file.cday = date("<%tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD")%>")
> SORT file.ctime asc
> ```

> [!ABSTRACT]- Notes Last Modified Today
> ```dataview
> TABLE file.folder as "Folder", file.tags as "Tags"
> FROM ""
> WHERE file.mday = date("<%tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD")%>")
> SORT file.folder asc
> ```
