# Напишите программу, в которой есть функция для заполнения вло-
# женного списка. Список заполняется натуральными числами «змей-
# кой»: сначала заполняется первая строка, затем последний столбец
# (сверху вниз), последняя строка (справа налево), первый столбец (сни-
# зу вверх), вторая строка (слева направо), и так далее.

n = 5

mas = [[0] * n for i in range(n)]

def snake(mas):
    index = 1
    y, x = 0, 0
    r = n

    while index <= n * n:
        for i in range(r):
            mas[y][x] = index
            index += 1
            x += 1
        x -= 1
        y += 1
        r -= 1

        for i in range(r):
            mas[y][x] = index
            index += 1
            y += 1
        y -= 1
        x -= 1

        for i in range(r):
            mas[y][x] = index
            index += 1
            x -= 1
        x += 1
        y -= 1
        r -= 1

        for i in range(r):
            mas[y][x] = index
            index += 1
            y -= 1
        y += 1
        x += 1

    for row in mas:
        print(row)

snake(mas)