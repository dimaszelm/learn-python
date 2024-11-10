# Напишите программу, которая выполняется следующим образом.
# Пользователь вводит целое неотрицательное число. На основе этого
# числа создается список из натуральных чисел от 1 до этого числа. За-
# тем на основе этого списка создается словарь. Элементы списка служат
# ключами для элементов словаря. Значения элементов словаря опре-
# деляются на основе значений элементов списка, но взятых в обратном
# порядке. Например, если пользователь вводит число 3, то создается спи-
# сок [1,2,3] и на его основе создается словарь из трех элементов. У эле-
# мента с ключом 1 значение 3, у элемента с ключом 2 значение 2, а у эле-
# мента с ключом 3 значение 1.


n = int(input("Введите целое неотрицательное число: "))

if n < 0:
    print("Пожалуйста, введите неотрицательное число.")
else:
    numbers_list = list(range(1, n + 1))

    numbers_dict = {key: numbers_list[-key] for key in numbers_list}

    print("Список:", numbers_list)
    print("Словарь:", numbers_dict)