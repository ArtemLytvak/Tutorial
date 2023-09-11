def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    list_num = factorial(n) / ((factorial(n - k)) * factorial(k))
    return int(list_num)


