# "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"
import re
def find_word(text, word):

    pattern = rf"{word}"
    result = re.search(pattern, text)

    dict = {'result': True if result else False,
            'first_index': result.start() if result else None,
            'last_index': result.end() if result else None,
            'search_string': word,
            'string': text}
    return dict
find_word(text="Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.\", 'Python'", word="python")
