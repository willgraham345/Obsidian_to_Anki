---
summary: Unix-based system to download files from the web.
type: note/function
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:13:17 am
function_of: ["[[Linux CLI]]"]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Installing on various distros
Install wget on Debian / Ubuntu:

```
sudo apt install wget
```

Install wget on Fedora / Rocky Linux / AlmaLinux:

```
sudo dnf install wget
```

Install wget on Arch Linux:

```
sudo pacman -Sy wget
```

Install wget on SUSE Linux:

```
sudo zypper install wget
```

# Basics
The basic syntax of wget command:

```
wget [OPTIONS] [URL
```

Where,

- \[OPTIONS\] : This changes the behavior of wget such as changing the directory to save the file, mirroring, recursion, etc.
- \[URL\] : This is the URL of the file or page to download.

The wget configuration file, which is typically located at /etc/wgetrc or ~/.wgetrc. One useful situation is when the server is behind a proxy, you can add proxy details in the config file.

# Flags
|Options|Description|
|---|---|
|`-O` (Uppercase)|Downloads a file using a different file name|
|`-b` or `--background`|Downloads a file in the background and frees up the terminal|
|`-i`, `--input-file`|Allows to specify a list of URLs in a file to download.|
|`-c` ( Lowercase )|Resumes download of a partially downloaded file|
|`-P`|Specifies the directory that a file will be downloaded|
|`-r` or `--recursive`|Tell wget to follow links and download recursively.|
|`-N` or `--timestamping`|Only download files that are newer than existing files.|
|`-m` or `--mirror`|Downloads a mirror copy of a website including all website files. Equal to It's equivalent to `-r -N -l inf --no-remove-listing`.|
|`-np` or `--no-parent`|Don't ascend to the parent directory when retrieving recursively.|
|`-k` or `--convert-links`|Make links in downloaded HTML or CSS point to local files.|
|`-p` or `--page-requisites`|Get all images, etc. needed to display HTML page|
|`--limit-rate`|Limits download speed when downloading a file|
|`--ftp-user=USER`|Set FTP user to USER|
|`--ftp-password=PASS`|Set FTP password to PASS|
|`--no-check-certificate`|Skips SSL certificate checking|
|`--user-agent`|Changes browser UserAgent|
|`-o` or `--output-file`|Log output of wget to a file, use -a option to append.|
|`-V`, `--version`|Displays the version of wget|
|`-h`, `--help`|Displays all the wget command options and usage|
