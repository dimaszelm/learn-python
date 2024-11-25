# Напишите программу, в которой описан класс и функция, предназначен-
# ная для создания списка из объектов. У объектов класса должно быть поле
# (предназначенное для записи целочисленных значений). При вызове функ-
# ции аргументом ей передается целое число, определяющее количество объ-
# ектов в списке. Поля объектов заполняются целыми нечетными числами.

class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

def create_objects(num):
    objects_list = []
    uneven_number = 1

    for i in range(num):
        obj = MyClass(uneven_number)
        objects_list.append(obj)

        uneven_number += 2

    return objects_list


num_objects = 5
objects = create_objects(num_objects)

for obj in objects:
    obj.show()
