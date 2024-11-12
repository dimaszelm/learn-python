# Напишите программу, в которой описана функция. В качестве ар-
# гументов функции передаются два объекта одного и того же класса.
# У каждого объекта есть поле, представляющее собой список из целых
# чисел. В результате функция возвращает объект того же класса. Поле-
# список этого объекта получается суммированием соответствующих эле-
# ментов из полей-списков объектов, переданных аргументами функции.
# Если в этих объектах списки разной длины, то недостающие элементы
# в списке заменяются нулями.

class MyClass:
    def __init__(self, list_numb):
        self.list_numb = list_numb

    def show(self):
        print(self.list_numb)


def create_new_obj(object_1, object_2):
    list_new_obj = []
    for i in range(max(len(object_1.list_numb),len(object_2.list_numb))):
        value_1 = object_1.list_numb[i] if i < len(object_1.list_numb) else 0
        value_2 = object_2.list_numb[i] if i < len(object_2.list_numb) else 0
        list_new_obj.append(value_1 + value_2)
    new_obj = MyClass(list_new_obj)
    return new_obj


list_obj_1 = [1,23,31,4,52,6,7,85,9]
obj_1 = MyClass(list_obj_1)

list_obj_2 = [2,38,57,92,132]
obj_2 = MyClass(list_obj_2)

obj_1.show()
obj_2.show()

new_object = create_new_obj(obj_1, obj_2)
new_object.show()