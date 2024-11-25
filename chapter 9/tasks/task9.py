# Напишите программу, в которой создается итератор, генерирующий
# нечетные натуральные числа. Количество генерируемых чисел опреде-
# ляется аргументом конструктора.

class OddNumberIterator:
    def __init__(self, count):
        self.count = count
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            result = self.current
            self.current += 2
            self.count -= 1
            return result
        else:
            raise StopIteration

iterator = OddNumberIterator(5)

for num in iterator:
    print(num)
