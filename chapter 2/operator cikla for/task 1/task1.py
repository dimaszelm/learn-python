# Напишите программу, в которой пользователь вводит целое число,
# а программа определяет, сколько в этом числе цифр 0, 1, 2 и так далее,
# до 9.


numb = input("Введите целое число: ")

counts = [0] * 10

for dig in numb:
    counts[int(dig)] += 1

for i in range(10):
    print(f"Цифр {i} в числе {numb} = {counts[i]}")

