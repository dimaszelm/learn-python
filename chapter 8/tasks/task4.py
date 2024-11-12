# Напишите программу, в которой описана функция, предназначен-
# ная для создания объектов. Функции при вызове передается список
# и текстовый аргумент. Текстовый аргумент определяет название клас-
# са, на основе которого создается объект. Текстовые элементы из списка
# определяют названия полей объекта (нетекстовые аргументы игнориру-
# ются). Значениями полей объекта являются натуральные числа.


def create_obj(fields, class_name):
    if not isinstance(class_name, str) or not isinstance(fields, list):
        return print("Вы передали неверные значения")

    class MyClass:
        def __init__(self):
            k = 1
            for item in fields:
                if isinstance(item, str):
                    self.__dict__[item] = k
                    k += 1

        def show(self):
            print(f"Объект с полями ({self.__class__.__name__}):")
            for attr, value in self.__dict__.items():
                print(f"{attr} = {value}")

    MyClass.__name__ = class_name
    return MyClass()

A = create_obj(["Hello", "world", "field", 1, 2, 34], "TestClass")

A.show()




