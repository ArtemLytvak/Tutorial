grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
def formatted_grades(students):

    list_students = []
    n = 1
    for k, v in students.items():
        list_students.append("{:>4}|{:<10}|{:^5}|{:^5}".format(n, k, v, grades[v]))
        n += 1
    print(list_students)
    return list_students



        # for el in formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})
formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})
