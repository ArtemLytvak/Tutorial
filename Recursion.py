def fnc(n):
    if n <= 1:
        return 1
    else:
        return n + fnc(n-1)


print(fnc(5))
