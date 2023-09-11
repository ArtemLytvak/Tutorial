import os
from pathlib import Path
import sys
import shutil
# path = sys.argv[1]
CATEGORIES = {"image": ['.JPEG', '.PNG', '.JPG', '.SVG'],
            "audio": ['.AVI', '.MP4', '.MOV', '.MKV'],
            "docs": ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'],
            "music": ['.MP3', '.OGG', '.WAV', '.AMR'],
            "archive": ['.ZIP', '.GZ', '.TAR'],
            "torrents": [".TORRENT"],
            "executable": [".EXE"]
              }
def un_zip(path):
    path = Path(path)
    for el in path.glob("**/*"):
        if el.suffix.upper() in CATEGORIES["archive"]:
            parent_dir = el.parent
            new_dir = parent_dir.joinpath(rf"{el.stem}")

            shutil.unpack_archive(el, new_dir)
un_zip(r"C:\Users\user\Documents\GitHub\Tutorial\SORT")
