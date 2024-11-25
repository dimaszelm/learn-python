# Напишите программу с классом, объекты которого можно вызывать.
# У объекта класса должно быть поле-список с числовыми значениями,
# а результатом метод возвращает полиномиальную сумму. В частности,
# если в списке содержатся числа a0, a1, …, an и в качестве аргумента объ-
# екту при вызове передается значение x, то в качестве результата должно
# возвращаться значение a0 + a1x + a2x + … + anx .

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

poly = Polynomial([2, 3, 4])

print(poly(0))
print(poly(1))
print(poly(2))
