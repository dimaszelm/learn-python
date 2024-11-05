# Напишите программу, в которой создается вложенный список из слу-
# чайных чисел. В матрице, которая реализуется данным вложенным
# списком, удаляется строка и столбец. Номер строки и номер столбца,
# которые нужно удалить, вводятся пользователем.
from random import randint

n = 5

c = int(input("Введите номер столбца для удаления (1-5): ")) - 1
r = int(input("Введите номер строки для удаления (1-5): ")) - 1

mas = [[randint(0, 9) for i in range(n)] for j in range(n)]

print("Исходная матрица:")
for row in mas:
    print(row)

def delete_row_col(matrix, row_to_delete, col_to_delete):
    matrix = [row for i, row in enumerate(matrix) if i != row_to_delete]
    matrix = [[val for j, val in enumerate(row) if j != col_to_delete] for row in matrix]
    return matrix

mas = delete_row_col(mas, r, c)

print("\nМатрица после удаления строки и столбца:")
for row in mas:
    print(row)

