# Ми розробляємо кулінарний блог. І в рецептах, при
# написанні списку інгредієнтів, ми розділяємо їх комами,
# а перед останнім ставимо союз "and", як у прикладі нижче:
# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
# Напишіть функцію format_ingredients, яка прийматиме на вхід список
# з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# та повертатиме рядок зібраний з його елементів в описаний вище спосіб.
# Ваша функція має вміти обробляти списки будь-якої довжини.
def format_ingredients(*items):
    # items = list()
    string: str = f""
    for i in items:
        string += i + ", "
        if len((items)) - items.index(i) == 2:
            string += "and "
    return string


print(format_ingredients(("2 eggs", "1 liter sugar", "1 tsp salt", "vinegar")))