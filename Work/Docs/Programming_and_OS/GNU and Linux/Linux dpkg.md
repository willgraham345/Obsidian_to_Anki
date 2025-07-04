---
type: note/library
component_of: ["[[Linux Package Management]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Thursday, February 6th 2025, 10:08:01 am
---
# Background
- A tool to install, build, remove, and manage Debian package. 
- Used to interact with packages on the system, controlled fully with the help of the cli parameters, first 

## How it works
See [[Linux apt# How it works]] for more information and a graph explaining the process. 
1. Extracts the package and copies the content to the right location, and check for pre-existing files and modifications on them
2. Run package maintainer scripts `preinst`, `postinst`  (`prerm`, `postrm` if a package is being upgraded)
3. Execute some actions based on triggers

### Maintenance Scripts 
Maintainer scripts are usually located at `/var/lib/dpkg/info/<package-name>.{pre,post}{rm,inst}`
- These are usually shell scripts, but there isn't a hard rule
- 

#### Example Maintenance Scripts
```
$ ls /var/lib/dpkg/info/xml-core.{pre,post}{rm,inst}
/var/lib/dpkg/info/xml-core.postinst
/var/lib/dpkg/info/xml-core.postrm
/var/lib/dpkg/info/xml-core.preinst
/var/lib/dpkg/info/xml-core.prerm
```

### Control files
There are more, but the mot important ones are:
- `control`: A [list](https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-sourcecontrolfiles) of the dependencies, and other useful information to identify the package
- `conffiles`: A [list](https://www.debian.org/doc/manuals/maint-guide/dother.en.html#conffiles) of config files (usually those in `/etc`)
- `debian-binary`: contains the deb-package version, [currently 2.0](http://tldp.org/HOWTO/Debian-Binary-Package-Building-HOWTO/x60.html#AEN66)
- `md5sums`: A list of md5sums of each file in the package for verifying
- `templates`: A file with [error descriptions and dialogs](https://www.debian.org/doc/packaging-manuals/debconf_specification.html#AEN45) during installation

# Basics
`dpkg [options] [.deb package name]`


| Option            | Function                                                                                                                                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _-i OR --install_ | Install a package using the dpkg command. The command will extract all control files for the specified package, remove any previously installed older instance of the package, and install the new package on our system.          |
| _-r OR --remove_  | Remove an installed package from our system. It removes every file belonging to the specific package except the configuration files. This can be seen as the uninstallation option.                                                |
| _-P OR --purge_   | An alternative way to remove an installed package from our system. It completely removes every fie belonging to the specific package, including the configuration files. This can be seen as the ‘complete uninstallation’ option. |
| _--update-avail_  | Uhe information of the dpkg command about available packages in its repositories. If new packages are available, they are synced from the official repositories.                                                                   |
| _--merge-avail_   | Merge the information of the dpkg command about available packages in its repositories with previously available information. It is usually run right after the previous command.                                                  |
| _--help_          | Display the help page for the dpkg command and exit.                                                                                                                                                                               |
