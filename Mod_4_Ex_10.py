from random import randint


def get_random_password():
    string_pass = str()

    for char in range(8):
        string_pass += chr(randint(40, 126))

    return string_pass























