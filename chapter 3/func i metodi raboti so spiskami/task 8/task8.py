# Напишите программу, в которой создается числовой список. Список
# заполняется случайными числами. Затем элементы с четными индекса-
# ми сортируются в порядке возрастания, а элементы с нечетными индек-
# сами сортируются в порядке убывания.
from random import randint

n = int(input("Введите количество чисел в списке: "))

chet = []
nechet = []
num_list = [randint(0, 100) for _ in range(n)]
print("Исходный список:", num_list)

for num in num_list:
    if num % 2 == 0:
        chet.append(num)
    else:
        nechet.append(num)

chet.sort()
nechet.sort(reverse = True)

print("Четные числа: ",chet)
print("Нечетные числа: ",nechet)

