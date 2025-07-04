---
summary: When it comes to creating backups, packaging software source code for distribution, and managing files in Linux, the tar command is no doubt one of the widely used archiving utilities. Tar command which is abbreviated as tape archive is used to group files into archives called tarballs and also compress files using popular compression algorithms such as gzip, bzip2, and xz.
type: note/concept
concept_of: ["[[Linux File System Types]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:11:32 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

# Options

|Options|A brief description|
|---|---|
|-A|Append the archive to the end of another archive.|
|-c|Create a new archive. Directories are archived recursively, unless the --no-recursion option is given.|
|-d|Find differences between the archive and the file system.|
|--delete|This option has no short form, it deletes specified members from an archive.|
|-r|Same as the -A options. It appends files to the end of an archive.|
|-t|List the contents of an archive.|
|-u|Append files that are newer than the corresponding copy in the archive.|
|-x|Extract files from an archive.|
|-? or --help|Display a short option summary and exit.|
|-k|Don't replace existing files when extracting.|
|-O|Extract files to standard output.|
|-f|the filename of the archive.|
|-v|Verbosely list files processed.|
|-z|Compress files with gzip.|
|-j|Compress files with bzip2.|
|-J|Compress files with xz.|
|-Z|Compress files with compress.|
|-a|Use the archive suffix/extension to determine the compression program.|
|-l|Used to check for symbolic links when creating archives.|
|-C|Change to the specified directory before permitting any operations|
|-W|Used with -c option to verify any data errors.|
|--exclude=FILE|Exclude the FILE when adding to the tar archive or extracting from a tar archive.|
|-P|Preserves leading slashes from file names when creating archives.|
|-p|Preserve archived file permissions during extraction.|
|--wildcards|Enables the tar command to interpret wildcards.|
|-m|Instructs tar to update the modification time of the extracted files to the current time.|
|-N|Only archive files newer than the specified date.|
|--remove-files|This deletes the original files from the disk after archiving them.|
|--strip-components|Strips the specified number of leading components from file names during extraction.|
|--to-command|Pipe extracted files to a command for further processing.|
|--listed-incremental|Used to handle new GNU-format incremental backups.|
|--ignore-zeros|Ignore zeroed blocks in the archive, which are normally treated as end-of-file (EOF) markers. Tar will stop reading after encountering 2 consecutive EOF (512-blocks filled with zeroes).|
|--no-recursion|Avoid descending automatically in directories.|
|--one-file-system|Instructs tar to stay in local file system when creating archive.|

# `tar` Command Operations


## **Create an archive**

The -c option can be used to combine multiple files into an archive called a tarball. The -f option is used to specify the archive file name.

Here is an example of creating archives using the tar command:

```
$ tar -cf archive.tar file1 file2
```

## **Compress an archive**

Compressing is different from creating an archive in the sense that archiving uses the same amount of disk space as all the individual files and directories combined, whilst compression reduces the size. The option for compressing files depends on the type of algorithm you want to use. To create and compress an archive using gzip use the -z option:

```
$ tar -czf archive.tar.gz file1 file2
```

Tar offers a good option, -a, that intelligently determines the compression algorithm from the specified archive suffix or extension. Compressing an archive using the xz compression algorithm, for example, you would use:

```
$ tar -caf archive.tar.xz file1 file2
```

## **Extract from an archive**

The -x option can be used for extracting or uncompressing archives. Here is an example of extracting an archive in the current working directory:

```
$ tar -xf archive.tar
```

If you want to extract an archive to a specific directory use the -C option followed by the directory where you want the files to be extracted:

```
$ tar -xf archive.tar -C directory-path
```

## **Concatenate multiple archives**

If you have two or more archives you can concatenate or combine them using the -A option:

```
$ tar -Af archive.tar archive2.tar
```

## **Append files to archive**

Tar command gives you the ability to add more files to an already existing archive without having to extract and archive the files again. To append files to an archive use the -a option or -r option:

```
$ tar -rf archive.tar file_to_append
$ tar -af archive.tar file_to_append
```

## **List archive contents**

The -t option can be used to list the contents of an archive. This option is very handy if you just want to have a peek at a large archive without extracting it:

```
$ tar -tf archive.tar
```