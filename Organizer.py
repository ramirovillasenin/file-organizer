import os
import shutil
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to the folder to organize")
args = parser.parse_args()

test_folder = Path(args.folder)



# test_folder =  Path("test_files")
# test_folder.mkdir(exist_ok=True)

# files = [
#     "Document1.txt", "Document2.txt", "Document3.txt",
#     "Photo.jpg", "Photo2.jpg", "file.pdf"
#     "file1.pdf", "data.csv", "image1.png",
#     "notes.txt"
# ]

# for filenames in files:
#     (test_folder / filenames).touch()

counts = {}
for file in test_folder.iterdir():
    ext = file.suffix  # .txt, .jpg, etc
    counts[ext] = counts.get(ext, 0) + 1

for ext, count in counts.items():
    print(f"{ext}: {count} file(s)")


#move each file to its own subfolder

for file in test_folder.iterdir():
    if file.is_file():
        ext = file.suffix[1:] #remove the dot jpg, txt
        dest_folder = test_folder / ext
        dest_folder.mkdir(exist_ok=True)
        shutil.move(str(file), dest_folder / file.name)

print("Files moved successfully!")


