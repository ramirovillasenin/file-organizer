# File Organizer

A Python script that automatically sorts files in a folder by extension.

## How it works
- Scans a target folder
- Creates subfolders by file type (.txt, .jpg, .pdf, etc.)
- Moves each file to the correct subfolder

## Usage
```bash
python3 organizer.py /path/to/folder
```

## Example
```bash
python3 organizer.py ~/Downloads
```

## Tech
- Python 3
- os, shutil, pathlib, argparse
