# Напишите программу, создающую список из чисел, которые при де-
# лении на 5 дают в остатке 3 (такие числа вычисляются по формуле 5k + 3,
# где k = 0,1,2…). Отобразить этот список в прямом и обратном порядке.

n = input("Введите кол-во чисел в списке: ")

nums = [(5 * k + 3) for k in range(int(n)) ]
print("прямой список:",nums)
print("список в обратном порядке:", list(reversed(nums)))