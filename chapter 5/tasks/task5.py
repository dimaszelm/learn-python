# Напишите программу, в которой пользователь вводит два текстовых
# значения, и на их основе создается новый текст. В этот новый текст по-
# очередно включаются буквы из текстов, введенных пользователем. Ко-
# гда один из текстов заканчивается, в качестве символов из этого текста
# используется «звездочка» *.

txt_1 = input("Введите текст: ")
txt_2 = input("Введите второй текст: ")

list_1 = list(txt_1)
list_2 = list(txt_2)
list_result = []

max_size = max(len(list_1), len(list_2))

for i in range(max_size):
    if i < len(list_1):
        list_result.append(list_1[i])
    else:
        list_result.append('*')

    if i < len(list_2):
        list_result.append(list_2[i])
    else:
        list_result.append('*')

result = ''.join(list_result)
print("Результат:", result)

