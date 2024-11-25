# Напишите программу, в которой создается цепочка объектов. Для со-
# здания цепочки объектов предложите функцию, при вызове которой
# в качестве аргумента передается целое число, определяющее количество
# объектов в цепочке. Результатом функция должна возвращать ссылку
# на первый объект в цепочке.

class MyClass:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def show(self):
        print(self.value)
        if self.next:
            self.next.show()


def create_chain(num):
    head = MyClass(1)
    current = head

    for i in range(2, num + 1):
        new_object = MyClass(i)
        current.next = new_object
        current = new_object

    return head



num_objects = 5
chain = create_chain(num_objects)

chain.show()
