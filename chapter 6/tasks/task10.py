# Напишите программу, в которой используется функция-генера-
# тор, создающая итерируемый объект со степенями двойки. Количество
# элементов определяется аргументом функции-генератора.


def level_two(count):
    for i in range(count):
        yield 2**i


for level in level_two(5):
    print(level)