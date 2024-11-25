# Напишите программу с функцией, которая создает вложенный спи-
# сок. Размеры списка указываются аргументами функции. Список запол-
# няется случайными буквами.

from random import randint
m = input("Кол-во строк: ")
n = input("Кол-во столбцов: ")

def show(A):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()

def symbs(m, n):
    val='A'
    res=[['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=val
            val=chr(randint(65,90))
    return res

C = symbs(int(m),int(n))
print("вложенный список C:")
show(C)