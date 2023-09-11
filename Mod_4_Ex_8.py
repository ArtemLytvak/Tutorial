# [[1, 1, 5, 10], [10, 2], [1, 1, 1]] = 6

def game(terra, power):
    n = 0
    res = power
    for x in terra:
        for i in x:

            if i > res:
                break
            if i <= res:
                res += i
    print(res)

game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1)



















