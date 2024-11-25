# Напишите программу с функцией, которая аргументами получа-
# ет ссылку на функцию (например, f()) и целое число (например, n).
# Результатом является функция, которая вычисляет результат путем
# n-кратного применения функции f().

def func(f, n):
    def rekurs(x):
        result = x
        for i in range(n):
            result= f(result)
        return result
    return rekurs




def suma (x):
    return x + 1

numb_3 = func(suma,6)
print(numb_3(2))