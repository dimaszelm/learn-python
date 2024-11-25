# Напишите программу, в которой создается цепочка наследования
# из трех классов. У объекта исходного класса имеется поле, и у каждого
# следующего класса добавляется по одному полю. Опишите методы, пе-
# реопределяемые в производных классах, которые позволяют присваи-
# вать значения полям и отображать значения полей.

class BaseClass:
    def __init__(self, field):
        self.field = field

    def show(self):
        print(self.field)

class ChildClass(BaseClass):
    def __init__(self, field, field2):
        super().__init__(field)
        self.field2 =field2

    def show(self):
        super().show()
        print(self.field2)


class ChildClass2(ChildClass):
    def __init__(self, field, field2, field3):
        super().__init__(field, field2)
        self.field3 = field3

    def show(self):
        super().show()
        print(self.field3)

obj = ChildClass2("name", "weight", "height")
print(obj.__dict__)