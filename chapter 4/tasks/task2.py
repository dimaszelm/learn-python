# Напишите программу, в которой пользователь вводит два целых чис-
# ла, а программой определяются цифры, которые есть в представлении
# обоих чисел.

nums = input("Введите число: ")
nums_2 = input("Введите число: ")

digit = set()

for num in nums:
    digit.add(num)

for num in nums_2:
    digit.add(num)

print(f"Цифры в числе {nums} и {nums_2}: ", digit)