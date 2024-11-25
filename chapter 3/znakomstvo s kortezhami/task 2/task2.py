# Напишите программу, в которой пользователь вводит целое чис-
# ло, а программа формирует кортеж, который состоит из цифр, входя-
# щих в это число. Предложите способы создания кортежа, при котором
# цифры, формирующие число, включаются в кортеж в прямом и обрат-
# ном порядке.

numb = input("Введите целое число: ")


def method_1(k):
    return print(tuple(int(digit) for digit in k))

def method_2(k):
    return print(tuple(int(digit) for digit in reversed(k)))

method_1(numb)
method_2(numb)
