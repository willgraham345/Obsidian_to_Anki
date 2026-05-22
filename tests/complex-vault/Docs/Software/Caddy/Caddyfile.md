---
type:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Syntax]]"
  - "[[#Usage]]"
date created: Thursday, April 2nd 2026, 8:56:11 am
date modified: Thursday, April 2nd 2026, 8:59:55 am
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Caddyfile ;;; 

# Additional Background
## Concepts of Note
󰙎 Addresses ;;; 
󰙎 Directives ;;; Fucntional keywords which customize how the site is served

## Usage
### Caddyfile environment variables
 `{$DOMAIN:localhost}` ;;; Caddyfile environment variables

## Syntax
### Addresses
|Address|Effect|
|---|---|
|`example.com`|HTTPS with managed [publicly-trusted certificate](https://caddyserver.com/docs/automatic-https#hostname-requirements)|
|`*.example.com`|HTTPS with managed [wildcard publicly-trusted certificate](https://caddyserver.com/docs/caddyfile/patterns#wildcard-certificates)|
|`localhost`|HTTPS with managed [locally-trusted certificate](https://caddyserver.com/docs/automatic-https#local-https)|
|`http://`|HTTP catch-all, affected by [`http_port`](https://caddyserver.com/docs/caddyfile/options#http-port)|
|`https://`|HTTPS catch-all, affected by [`https_port`](https://caddyserver.com/docs/caddyfile/options#http-port)|
|`http://example.com`|HTTP explicitly, with a `Host` matcher|
|`example.com:443`|HTTPS due to matching the [`https_port`](https://caddyserver.com/docs/caddyfile/options#http-port) default|
|`:443`|HTTPS catch-all due to matching the [`https_port`](https://caddyserver.com/docs/caddyfile/options#http-port) default|
|`:8080`|HTTP on non-standard port, no `Host` matcher|
|`localhost:8080`|HTTPS on non-standard port, due to having a valid domain|
|`https://example.com:443`|HTTPS, but having both `https://` and `:443` is redundant|
|`127.0.0.1`|HTTPS, with a locally-trusted IP certificate|
|`http://127.0.0.1`|HTTP, with an IP address `Host` matcher (rejects `localhost`)|

## Diagrams

 
![[Caddyfile.png]]