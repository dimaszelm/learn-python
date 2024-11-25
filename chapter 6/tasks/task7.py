# Напишите программу, в которой методом рекурсии символы из тек-
# ста, переданного аргументом функции, отображаются «через один»:
# то есть отображается первый, третий, пятый и так далее, символы.

k = 0

def rekurs(text):
    global k
    # if k < len(text)-1 or k == len(text)-1 or k == len(text)-2:
    #     print(text[k])
    #     k += 2
    #     return rekurs(text)
    k = text



rekurs("1hello world")
print(k)
rekurs("hello world")
print(k)
