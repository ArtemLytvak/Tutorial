import sys
from pathlib import Path
import os
import string
import shutil
import re

CATEGORIES = {"image": ['.JPEG', '.PNG', '.JPG', '.SVG'],
            "audio": ['.AVI', '.MP4', '.MOV', '.MKV'],
            "docs": ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'],
            "music": ['.MP3', '.OGG', '.WAV', '.AMR'],
            "archive": ['.ZIP', '.GZ', '.TAR'],
            "torrents": [".TORRENT"],
            "executable": [".EXE"]
              }


def un_zip(path):
    for el in path.glob("**/*"):
        if el.suffix.upper() in CATEGORIES["archive"]:
            # parent_dir = el.parent
            new_dir = el.parent.joinpath(rf"{el.stem}")
            shutil.unpack_archive(el, new_dir)
            os.remove(el)


def normalize(file):
    CYRILLIC_SYMBOLS = r"абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ "
    TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_")
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

        file = Path(file)
        suffix = file.suffix
        file = file.stem
        file = re.sub("[!/#$%&'()*+,-/:;<=>?@[\]^`{|}~]", "", file)
        file = file.translate(TRANS) + suffix
    return file

def move_file(file, category, root_dir):
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    file.replace(target_dir.joinpath(normalize(file)))

def get_categories(file):
    extens = file.suffix.upper()
    for cat, exts in CATEGORIES.items():
        if extens in exts:
            return cat
    return "Unknown"

def sort_folder(path):
    for el in path.glob("**/*"):
        if el.is_file():
            category = get_categories(el)
            move_file(el, category, path)
        if el.is_dir():
            if len(os.listdir(el)) == 0:
                el.rmdir()
    un_zip(path)

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "There is no path to folder to sort"
    if not path.exists():
        return "Folder does not exist"
    sort_folder(path)

    return "Let's get it sorted!"

if __name__ == "__main__":
    print(main())








