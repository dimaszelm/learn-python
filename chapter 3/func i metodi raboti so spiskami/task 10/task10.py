# Напишите программу, в которой создается два списка одинаково-
# го размера. На основе этих списков поочередной вставкой элементов
# из первого и второго списка формируется новый список.

from random import randint

n = int(input("Введите количество элементов в каждом списке: "))

list1 = [randint(0, 100) for _ in range(n)]
list2 = [randint(0, 100) for _ in range(n)]

print("Первый список:", list1)
print("Второй список:", list2)

new_list = []
for i in range(n):
    new_list.append(list1[i])
    new_list.append(list2[i])

print("Новый список с чередующимися элементами:", new_list)
