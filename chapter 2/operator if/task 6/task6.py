# Напишите программу, в которой пользователь вводит три числа,
# а программа определяет, может ли существовать треугольник со сторо-
# нами, длина которых равняется введенным значениям. Условие суще-
# ствования треугольника такое: сумма двух любых (из трех введенных)
# чисел должна быть больше третьего числа.


a = input("Введите сторону a треугольника: ")
b = input("Введите сторону b треугольника: ")
c = input("Введите сторону c треугольника: ")
print("Вы ввели стороны:", a, b,c)


if a + b > c and a + c > b and b + c > a :
    print("такой треугольник существует")
else:
    print("такого треугольника не существует")