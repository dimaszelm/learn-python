# Напишите программу, в которой описывается функция с произволь-
# ным количеством числовых аргументов, а результатом возвращается
# список из трех элементов: среднее значение аргументов, максимальное
# значение среди аргументов и минимальное значение среди аргументов.


def  avg_max_min(*n):
    list_result =[]
    list_result.append(sum(n) / len(n))
    list_result.append(max(n))
    list_result.append(min(n))
    return list_result

mass = []
mass.append(1)
mass.append(1)
print(mass)


print(avg_max_min(1,5,1,9,9))
