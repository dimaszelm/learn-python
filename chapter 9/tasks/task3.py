# Напишите программу, в которой для объектов класса определена опе-
# рация сложения. У каждого объекта есть поле-список, и при сложении
# объектов получается новый объект того же класса. Его поле-список по-
# лучается объединением полей-списков исходных объектов.

class CustomList:
    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Поле items должно быть списком.")
        self.items = items

    def __add__(self, other):
        if not isinstance(other, CustomList):
            raise TypeError("Можно складывать только объекты класса CustomList.")
        return CustomList(self.items + other.items)

    def __repr__(self):
        return f"CustomList({self.items})"


obj1 = CustomList([1, 2, 3])
obj2 = CustomList([4, 5, 6])

result = obj1 + obj2

print("Объект 1:", obj1)
print("Объект 2:", obj2)
print("Результат сложения:", result)
