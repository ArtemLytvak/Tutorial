import re
def replace_spam_words(text, spam_words):
    text2 = text
    for i in range(len(spam_words)):
        pattern = rf"{spam_words[i]}"
        text1 = re.sub(pattern, "*" * len(pattern), text2, flags=re.IGNORECASE)
        text2 = text1
    return text2
replace_spam_words("Guido van Rossum began working on Python in the late 1980s,\
as a successor to the ABC programming PYTHOn language,\
 and first released pYthoN it in 1991 as Python 0.9.0.", ["BeGan", "python"])