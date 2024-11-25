# Напишите программу, в которой описана функция, возвращающая
# результатом сумму нечетных чисел. Количество чисел передается аргу-
# ментом функции.

n = int(input("Введите кол-во чисел :"))

def sumnumb(k):

    sumnechet = 0

    for i in range(k+1):
        if i % 2 != 0:
            sumnechet += i
    return sumnechet

print(sumnumb(n))


