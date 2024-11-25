# Напишите программу, в которой создается цепочка объектов. Пред-
# ложите метод или функцию, которые позволяют вставить новый объ-
# ект в уже существующую цепочку, а также метод или функцию, которые
# позволяют удалить объект из цепочки (так, чтобы оставшиеся объекты
# образовали цепочку).

class MyClass:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def show(self):
        print(self.value)
        if self.next:
            self.next.show()

    def instert_new_object(self, new_object):
        new_object.next = self.next
        self.next = new_object

    def delete_new_object(self):
        if self.next:
            self.next = self.next.next



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

print("начальная цепочка: ")
chain.show()

object_to_insert = chain
while object_to_insert.value != 3:
    object_to_insert = object_to_insert.next

new_object = MyClass(99)
object_to_insert.instert_new_object(new_object)

print("Цепочка после вставки объекта со значением 99 после объекта с значением 3:")
chain.show()

object_to_delete = chain
while object_to_delete.value != 3:

    object_to_delete = object_to_delete.next
object_to_delete.delete_new_object()

print("Цепочка после удаления объекта с значением 4:")
chain.show()

