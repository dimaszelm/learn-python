# Напишите программу, в которой создается и отображается список, со-
# держащий степени двойки (числа 2^0, 2^1, 2^2, 2^3 и так далее). Размер списка
# (количество чисел в списке) вводится пользователем с клавиатуры.

n = input("Введите кол-во чисел в списке: ")
nums =[2**i for i in range(int(n))]
print(nums)