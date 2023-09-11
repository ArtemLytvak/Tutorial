import string
from pathlib import Path
import os
import re
def normalize(file):
    CYRILLIC_SYMBOLS = r"абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ "
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
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
    print(file)


normalize(r"C:\Users\user\Downloads\audio\1. # Введение в курс Python.mp4")

# def normalize(sort()):
#     for file in path.glob("**/*"):
#         if file.is_file():
#             for let in file.stem:



# TRANS = {}
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
# def translate(name):
#     return name.translate(TRANS)



# def remove_empty_dir()
    # path = Path(r"C:\Users\user\Downloads")
    # for el in path.glob("*"):
    #     dir = os.listdir(el)
    #     if not dir:
    #         print("Empty")
    #     else:
    #         print("Not empty")