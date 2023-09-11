import re
# Молох бог ужасен.
# ['лох']
def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if not space_around:
            template = rf"{word}"
            result = re.findall(template, text.lower(), flags=re.IGNORECASE)
            if result:
                return True
            else:
                return False
        else:
            template = rf"\b{word}\s?"
            result = re.findall(template, text.lower(), flags=re.IGNORECASE)
            if result:
                return True
            else:
                return False


is_spam_words("Сполох ходит далеко", "лох", space_around=True)
