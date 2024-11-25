# Напишите программу, в которой создается числовой список. Список запол-
# няется случайными числами. Затем между каждой парой элементов этого спис-
# ка вставляется новый элемент, равный сумме значений соседних элементов.
from random import randint

n = int(input("Введите количество чисел в списке: "))

num_list = [randint(0, 100) for _ in range(n)]
print("Исходный список:", num_list)

result_list = []

for i in range(len(num_list) - 1):
    result_list.append(num_list[i])
    result_list.append(num_list[i] + num_list[i + 1])
result_list.append(num_list[-1])

print("Список с вставленными суммами:", result_list)
