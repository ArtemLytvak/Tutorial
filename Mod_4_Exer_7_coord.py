# [1, 12, 3, 24, 5]
# [1, 12, 3, 24, 5]
# [1, 12, 3, 24, 5]
# calculate_distance([0, 1, 3, 2, 0, 2]) #Повинно бути calculate_distance([0, 1, 3, 2, 0, 2]) == 17.6

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):

    n = 1
    new_list = []
    new_list1 = []

        # створюємо список з парами попереднє значення і поточне значення координати
        # i використовуємо, як саме значення в списку
        # n використовуємо для зміни положення за індексом
    for i in coordinates:
        if n == len(coordinates):
            break
        if i > coordinates[n]:
            new_list += [[coordinates[n], i]]
        else: new_list += [[i, coordinates[n]]]
        n+=1

    print(new_list)
    tuple1 = tuple(map(tuple, new_list))
    print(tuple1)
    result = 0
    for k, v in points.items():
        for k1 in tuple1:
            if k == k1:
                result += v
    print(round(result, 2))




calculate_distance([0, 1, 3, 2, 0, 2])
















