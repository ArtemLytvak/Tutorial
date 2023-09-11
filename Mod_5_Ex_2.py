articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_list = list()
    if letter_case:
        for i in articles_dict:
            if i['title'].find(key) != -1 or i['author'].find(key) != -1:
                new_list.append(i)

    else:
        for i in articles_dict:
            if i['title'].lower().find(key.lower()) != -1 or i['author'].lower().find(key.lower()) != -1:
                new_list.append(i)

    return new_list


find_articles('Ocean')

