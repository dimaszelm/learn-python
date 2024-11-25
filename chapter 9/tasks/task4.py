# Напишите программу, в которой для объектов предусмотрены опера-
# ции сложения с числом, вычитания числа и вычитания из числа, а также
# умножения на число и деления на число. У объекта должно быть поле
# с числовым значением, и при выполнении указанных операций они дол-
# жны выполняться с полем объекта.

class Math:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("value должно быть int либо float")
        self.value = value

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("value должно быть int либо float")
        return Math(self.value + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("value должно быть int либо float")
        return Math(self.value - other)

    def __rsub__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("value должно быть int либо float")
        return Math(other - self.value)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("value должно быть int либо float")
        return Math(self.value * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Число должено быть не 0.")
        if other == 0:
            raise ZeroDivisionError
        return Math(self.value / other)

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Число должено быть не 0.")
        if self.value == 0:
            raise ZeroDivisionError
        return Math(other / self.value)

    def __repr__(self):
        return f"Math({self.value})"

obj = Math(10)

print(obj + 5)
print(5 + obj)

print(obj - 3)
print(3 - obj)

print(obj * 4)
print(4 * obj)

print(obj / 2)
print(2 / obj)
