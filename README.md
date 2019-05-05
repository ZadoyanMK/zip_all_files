# Zip all files
Script for groupping all text in all folder and subfolder in zip_result.txt

Files are writing for next rule:

```
path/to/first/filename ~
First file content

path/to/second/filename ~
Second file content

...
```

All filenames displayed with index and "~" at the end.

This script has tested only on windows!

## Requirements

Need python3

## Usage:

```
zip_all.py [-h] [--path PATH] [--symb SYMB] [--index]
```

Optional arguments:

```
  -h, --help            show this help message and exit
  --path PATH, -p PATH  Base path
  --symb SYMB, -s SYMB  Symbol after filename at file
  --index, -i           Need index to each file?
```
