import re

def is_valid_password(password):
    regexAZ = r"[A-Z]+"
    regexaz = r'[a-z]+'
    regex09 = r'[0-9]+'
    a = False
    matchAZ = re.search(regexAZ, password)
    matchaz = re.search(regexaz, password)
    match09 = re.search(regex09, password)
    print(matchAZ, matchaz, match09)
    if matchAZ and matchaz and match09 and len(password) >= 8:
        a = True
    return a





















