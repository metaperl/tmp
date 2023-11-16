
"""
Python script to look for all zip files and list their contents.

Very useful when you have downloaded all your content via GOOGLE TAKEOUT and need to see
which zipfile contains what because you cannot afford to unzip them all at once because
it would be space-prohibitive.

"""

from pathlib import Path
from loguru import logger
from zipfile import ZipFile


def print_all_files(d):
    for root, dirs, files in Path(d).walk(on_error=print):
        logger.info(f"Files in {root} = {files}")
        for _ in dirs:
            print_all_files(_)

# print_all_files(".")

def print_zip_file_contents(f):
    with ZipFile(f, 'r') as zipObj:
        for entry in zipObj.infolist():
            print(f"- {entry.filename}")

    print("")


def search_and_list_zips(d):
    """Print contents of all zip files in current and child directories, recursively."""
    for root, dirs, files in Path(d).walk(on_error=None):
        for file in files:
            if file.endswith(".zip"):
                print(f"# Files in {root} = {file}")
                try:
                    print_zip_file_contents(file)
                except Exception as e:
                    print(f"{e}")

search_and_list_zips(".")
