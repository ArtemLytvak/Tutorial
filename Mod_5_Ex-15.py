import re


def find_all_links(text):
    print(text)
    result = []
    iterator = re.finditer(r"[A-z]{4,5}\:\/\/\w*\.\w+\.*\w{0,3}", text)
    for match in iterator:
        result.append(match.group())

    return result