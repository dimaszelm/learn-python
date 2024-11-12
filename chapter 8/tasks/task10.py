# Напишите программу, в которой создается бинарное дерево объек-
# тов: в вершине структуры находится объект, который содержит ссылки
# на два объекта того же класса. Каждый из этих объектов содержит ссыл-
# ки на два объекта, и так далее.

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def show(self):
        print(self.value, end=" ")
        if self.left:
            self.left.show()
        if self.right:
            self.right.show()

    def insert_left(self, value):
        if self.left is None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = self.right
            self.right = new_node


def create_binary_tree():
    root = TreeNode(1)

    root.insert_left(2)
    root.insert_right(3)

    root.left.insert_left(4)
    root.left.insert_right(5)

    root.right.insert_left(6)
    root.right.insert_right(7)


    return root


tree = create_binary_tree()

print("Дерево :")
tree.show()
