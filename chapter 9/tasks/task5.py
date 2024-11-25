# Напишите программу, в которой для объектов класса предусмотрены
# операции сравнения. У каждого объекта есть поле-список с числовыми
# значениями. Операции сравнения выполняются так: объекты на пред-
# мет равенства проверяются по первому элементу в списках, на предмет
# «не равно» — по второму элементу в списках, «меньше» — по третье-
# му элементу в списках, и так далее. Если соответствующего элемента
# в списке нет, используется нулевое значение.


#lesson38 в OOP

from dataclasses import dataclass

@dataclass
class CustomList:
    values: list

    def _get_value(self, index):
        return self.values[index] if index < len(self.values) else 0

    def __eq__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(0) == other._get_value(0)

    def __ne__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(1) != other._get_value(1)

    def __lt__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(2) < other._get_value(2)

    def __le__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(2) <= other._get_value(2)

    def __gt__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(2) > other._get_value(2)

    def __ge__(self, other):
        if not isinstance(other, CustomList):
            return NotImplemented
        return self._get_value(2) >= other._get_value(2)


obj1 = CustomList([1, 2, 3])
obj2 = CustomList([1, 3, 2])
obj3 = CustomList([0, 2])

print(obj1 == obj2)
print(obj1 != obj2)

print(obj1 < obj2)
print(obj1 > obj2)

print(obj1 < obj3)
print(obj3 > obj1)
