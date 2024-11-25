# Напишите программу, в которой генерируется 15 случайных целых
# чисел: 5 чисел попадают в диапазон значений от 1 до 10 и 10 чисел по-
# падают в диапазон от 10 до 30.


from random import randint


num_5 = set()
num_10 = set()

while len(num_5) < 5:
    num_5.add(randint(1,10))

while len(num_10) < 10:
    num_10.add(randint(10,30))

print (num_5)
print (num_10)
num = num_5 | num_10

print(num)