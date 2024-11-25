# Напишите программу с классом, объекты которого можно индекси-
# ровать. В частности, у объекта должно быть два поля-списка с числами.
# При индексировании объекта возвращается сумма элементов из списков
# с соответствующим индексом. Если в каком-то списке нет такого эле-
# мента, он заменяется нулевым значением.

class IndexObject:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __getitem__(self, index):
        val1 = self.list1[index] if index < len(self.list1) else 0
        val2 = self.list2[index] if index < len(self.list2) else 0
        return val1 + val2

obj = IndexObject([1, 2, 3], [4, 5])


print(obj[0])
print(obj[1])
print(obj[2])
print(obj[3])
