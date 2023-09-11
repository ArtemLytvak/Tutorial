import re

def find_all_words(text, word):

    pattern = rf"{word}"
    result = re.findall(pattern, text, flags=re.IGNORECASE)
    return result
find_all_words("Guido van Rossum began working on Python in the late 1980s,\
               as a successor to the ABC programming PYTHOn language,\
               and first released pYthoN it in 1991 as Python 0.9.0.", "python")

