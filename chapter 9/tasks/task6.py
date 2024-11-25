# Напишите программу, в которой для объектов класса предусмотрен
# специальный режим доступа к полям. В частности, у объекта должно
# быть поле-список, значением которому можно присваивать только
# список. Из присваиваемого списка в поле-список копируются только
# текстовые значения. При считывании значения этого поля возвраща-
# ется текстовая строка, содержащая только начальные буквы текстовых
# значений, которые входят в список.


class CustomList:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return ''.join(s[0] for s in self._values if isinstance(s, str))

    @values.setter
    def values(self, new_list):
        if isinstance(new_list, list):
            self._values = [item for item in new_list if isinstance(item, str)]
        else:
            raise ValueError("Значение должно быть списком строк.")

obj = CustomList()

obj.values = ["apple", "banana", "cherry", 123, 45.67]

print(obj.values)

obj.values = ["orange", "kiwi", "grape"]

print(obj.values)
