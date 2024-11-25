# Напишите программу, в которой создается итератор, генерирующий
# числа Фибоначчи (первые два числа равны единице, а каждое следую-
# щее есть сумма двух предыдущих). Количество генерируемых чисел пе-
# редается в качестве аргумента конструктору при создании итератора.


class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count -= 1
            return result
        else:
            raise StopIteration

iterator = FibonacciIterator(7)

for num in iterator:
    print(num)
