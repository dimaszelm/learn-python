# Напишите программу, в которой описывается функция, предназна-
# ченная для создания объекта. Объект создается на основе уже суще-
# ствующего объекта, который передается функции в качестве аргумента.
# В создаваемый объект добавляются только те неслужебные поля из ис-
# ходного объекта, которые имеют целочисленное значение.

class Human:
    def __init__(self, name=None, age=None, height=None, work=None):
        self.name = name
        self.age = age
        self.height = height
        self.work = work

    def show(self):
        attributes = [str(value) for value in self.__dict__.values() if value is not None]
        print(", ".join(attributes))


def create_new_human(obj):
    new_human = Human()
    for attr, value in obj.__dict__.items():
        if isinstance(value, int):
            new_human.__dict__[attr] = value
    return new_human


human_1 = Human("Nik", 32, 176, "Engineer")
human_1.show()

new_human = create_new_human(human_1)
new_human.show()
